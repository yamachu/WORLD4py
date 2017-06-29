from logging import getLogger, StreamHandler, DEBUG


_logger = getLogger('world4py')
_st_handler = StreamHandler()
_logger.addHandler(_st_handler)


def _get_logger():
    return _logger
