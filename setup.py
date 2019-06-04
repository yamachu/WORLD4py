'''Install world4py and download pre-built WORLD library
'''

import re
import sys
import json

from setuptools import setup, find_packages
from setuptools.command.install import install

# http://python-future.org/compatible_idioms.html
try:
    from urllib.request import urlretrieve, urlopen, Request
except ImportError:
    from urllib import urlretrieve
    from urllib2 import urlopen, Request


class LibraryDownloader(install):
    '''Hook base install task and download pre-build WORLD library after install
    '''

    _DOWNLOAD_BASE_URL = 'https://github.com/yamachu/World/releases/download'
    _LIBRARY_NAME = {
        'mac_32': ('libworld.dylib', 'libworld.dylib'),
        'mac_64': ('libworld.dylib', 'libworld.dylib'),
        'linux_32': ('Linux_libworld.so', 'libworld.so'),
        'linux_64': ('Linux_libworld.so', 'libworld.so'),
        'win_32': ('x86_world.dll', 'world_32.dll'),
        'win_64': ('x64_world.dll', 'world_64.dll'),
    }


    def _get_base_install_path(self):
        # Path separator Unix is '/', Win is '\'
        pathre = re.compile('world4py.__init__\.py')
        install_base_dir = ''
        for path in install.get_outputs(self):
            if pathre.search(path):
                install_base_dir = path.replace('__init__.py', '')
                break

        return install_base_dir


    def _get_platform(self):
        '''Get current platform

        Returns:
            str: current platform (win, mac, linux) and (32, 64) or ""
        '''

        platform = ''
        if sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
            platform = 'win'
        elif sys.platform.startswith('darwin'):
            platform = 'mac'
        elif sys.platform.startswith('linux'):
            platform = 'linux'
        return "{}_{}".format(platform, 64 if sys.maxsize > 2**32 else 32)


    def _get_library(self, platform):
        '''Get native WORLD library name

        Args:
            platform (str): current platform

        Returns:
            str: Library file name

        Raises:
            Exception: When current platform not win, mac or linux, throw
        '''
        if platform == 'win_32':
            return 'world_32.dll'
        elif platform == 'win_64':
            return 'world_64.dll'
        elif platform.startswith('mac'):
            return 'libworld.dylib'
        elif platform.startswith('linux'):
            return 'libworld.so'
        else:
            raise Exception('This architecture is not supported')


    def _get_install_full_path(self, base_path, library_name):
        return '{}{}'.format(base_path, library_name)


    def run(self):
        install.run(self)

        platform = self._get_platform()
        library_full_path = self._get_install_full_path(
            self._get_base_install_path(),
            self._LIBRARY_NAME[platform][1])

        get_latest_request = Request('https://github.com/yamachu/World/releases/latest',
                                     headers={'Accept': 'application/json'})
        get_latest_response = urlopen(get_latest_request)
        response_str = get_latest_response.read().decode('utf-8')
        response_json = json.loads(response_str)
        latest_version = response_json['tag_name']

        urlretrieve("{}/{}/{}".format(
            self._DOWNLOAD_BASE_URL,
            latest_version,
            self._LIBRARY_NAME[platform][0]), library_full_path)


    def get_outputs(self):
        return install.get_outputs(self) + [self._get_install_full_path(
            self._get_base_install_path(),
            self._get_library(self._get_platform())),]


setup(
    name="world4py",
    version="0.1",
    packages=find_packages(),
    description='Python wrapper for WORLD',
    url='https://github.com/yamachu/WORLD4py',
    author='yamachu',
    license='MIT',
    cmdclass={'install': LibraryDownloader},
    keywords='world, world4py',
    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
    ]
)
