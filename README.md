# WORLD4py
Yet another WORLD Python wrpper library

## WORLD4py とは

M.Morise により開発されている分析合成ライブラリ[WORLD](https://github.com/mmorise/World) の非公式Pythonラッパーライブラリです．

オリジナルの WORLD のインタフェースを一部改変した [WORLD](https://github.com/yamachu/World/tree/type/for_cswrapper) をラップしています．
変更の差分は[こちら](https://github.com/yamachu/World/compare/master...type/for_cswrapper)で確認することが出来ます．

詳細はオリジナルの WORLD のリポジトリ及び文献を参照してください．

## 特徴

本ライブラリではWORLDでの主要な分析手法である _Dio_, _CheapTrick_, _D4C_ などを抽象化し API として提供しています．
その他一括して特徴量を抽出する _extract_all_from_waveform_ といったメソッドを提供しています．

本ライブラリは Python の標準モジュールである _ctypes_ を使用した _world4py.native_ と _NumPy_ を使用した _world4py.np_ の2種類が選択可能で _world4py.native_ は環境を制限することなく利用することが可能です．

また本ライブラリはユーザが独自にビルドした WORLD の Cライブラリ を容易に使うことが出来る薄いラッパーとなっています．
これは現在動作確認済みの環境以外のプラットフォーム，および CPUアーキテクチャ においても，その環境にあったライブラリをビルドしこのラッパーに読ませれば利用が可能になるかもしれないということです．


## インストール

### 動作確認済みの環境

依存ライブラリが NumPy版のみ NumPy に依存しているだけなので，基本的にはどの環境の Python でも動作すると思います．

実際に確認したプラットフォームは
* Linux(Ubuntu)
* macOSX
* Windows

Python のバージョンは
* Python 2.7
* Python 3.5

で確認しています．


### インストール方法

今後 pip でのインストールを可能にしますが，現在は _setup.py_ を使用してインストールします．

```
git clone https://github.com/yamachu/WORLD4py.git
cd WORLD4py
python setup.py install
```

このインストール中に使用しているプラットフォームを判別し，あらかじめビルドしてあるネイティブライブラリをダウンロードし展開します．

使用が可能になったかは

```
cd demo
python main.py
```

などで確認してみてください．


## 使い方

### 特徴量抽出および合成

ctypes版

```python
from world4py.native import apis, tools

# get waveform from file
x, fs, nbit = tools.get_wave_parameters('./sample.wav')
# can use Python wave module

# extract F0
f0, time_axis = apis.dio(x, fs)
# extract Spectral envelope
sp, sp_fft_size = apis.cheap_trick(x, fs, time_axis, f0)
# extract Aperiodicity
ap, ap_fft_size = apis.d4c(x, fs, time_axis, f0)
# synthesis
y, y_length = apis.synthesis(f0, sp, ap, fs, fft_size=sp_fft_size)
```

これらの関数により抽出される _f0_, _sp_, _ap_ は ctypes 特有の型になっているため，操作する場合は Python での list のような型に変換する必要があります．

これを実現するのが以下のコードになります．

```python
from world4py.native import utils

# 1d-Pointer cast to 1d-List
f0_list = utils.cast_1d_pointer_to_1d_list(f0)

# 2d-Pointer cast to 2d-List
sp_list = utils.cast_2d_pointer_to_2d_list(sp, len(f0_list), sp_fft_size // 2 + 1)

# do something...

# 2d-List cast to 2d-Pointer
sp_mod = utils.cast_2d_list_to_2d_pointer(sp_list)
```

上記のように Python の list型 のような変数を使用する際は，
utils に定義されるヘルパーメソッドを経由する必要があります．

しかしわざわざ経由させるのは面倒なので，NumPy が使える環境であれば，以下の NumPy 版を使用することを推奨します．

numpy版

```python
from world4py.np import apis, tools

# get waveform from file
x, fs, nbit = tools.get_wave_parameters('./sample.wav')
# can use Python wave module

# extract F0
f0, time_axis = apis.dio(x, fs)
# extract Spectral envelope
sp = apis.cheap_trick(x, fs, time_axis, f0)
# extract Aperiodicity
ap = apis.d4c(x, fs, time_axis, f0)
# synthesis
y  = apis.synthesis(f0, sp, ap, fs)
```

抽出に関しては基本的には ctypes版 と変わりません．
戻り値が一部減っていますが，これは ctypes版の戻り値の情報が戻り値の ndarray から取得可能であるために省略しています．

戻り値が ndarray であるため，ctypes版で必要だった utils のヘルパーメソッドがなくても配列をそのまま扱うことが出来ます．

分析時に様々なパラメータを与えることが可能となっています．
詳細はオリジナルの WORLD や docstring などで確認してください．

この分析パラメータを一括で設定して，特徴量を上記のように一つずつ求めるのではなく，一括で求めることも出来ます．
分析パラメータは辞書型で定義するため，JSON形式などへ変換しやすく，分析条件などを管理しやすい形式となっています．

以下のように抽出条件を設定します．

```python
ana_param = {
    'threshold': 0.3,
    'frame_period': 5.0,
    'f0_ceil': 500.0,
}

# ctypes版での定義
f0, sp, ap, fft_size, array_size = apis.extract_all_from_waveform(x, fs, param)
```

パラメータの定義は各分析手法の docstring に記載してあります．


### 非公開 API の使用

抽象化されていない WORLD のそのままの API を使用することも可能です．

ここでは ctypes を例にとって説明します．
本ライブラリでは RealtimeSynthesis については API を現在提供していません．

それを使用する場合は以下のように行います．

```python
# WORLD の test.cpp の Synthesis2 を参照
from world4py.native import structures, apidefinitions

synthesizer = structures.WorldSynthesizer()
buffer_size = 64
apidefinitions._InitializeSynthesizer(fs, 5.0, sp_fft_size, buffer_size, 1, synthesizer)
f0_length = len(list(f0))
apidefinitions._AddParameters(f0, f0_length, sp, ap, synthesizer)
index = 0
y_length = int(f0_length * 5.0 * fs // 1000) + 1
y = (c_double * y_length)()
i = 0
while apidefinitions._Synthesis2(synthesizer) != 0:
    index = i * buffer_size
    for j in range(buffer_size):
        y[j + index] = synthesizer.buffer[j]
        
    i += 1
    
apidefinitions._DestroySynthesizer(synthesizer)
```

このように _apidefinitions_ というモジュール内に各 WORLD の API が先頭にアンダースコアを付与して実装されています．

使いたいけれど抽象化された API が無いという場合はこのような形式で API にアクセスしてください．


### 研究用途での使用

研究に使用する場合バージョンの固定などが必要になる場面があると思います．
本ラッパーはインストール時に [WORLDのリリースページ](https://github.com/yamachu/World/releases) から対象プラットフォームのライブラリをダウンロードしています．
そのため，Python のラッパーのバージョンが同じでも，内部で使用しているライブラリのバージョンが一致しないといったことが起こることがあります．
独自拡張のラッパーのバージョンは

```
import world4py

world4py.get_native_library_version()
```

で取得することが出来ます．

このバージョンは独自拡張の [WORLDのリリースページ](https://github.com/yamachu/World/releases) のバージョン，
またベースとなっているオリジナルの WORLD のコミットハッシュを示しています．

以前のバージョンに戻したい，また自分で少し動作を変えたライブラリを試したいと言った場合は，

```
import world4py

world4py.get_native_library_path()
```

以上の手順でネイティブライブラリのインストールパスを取得することが出来ます．
そのパスに存在するライブラリファイルを置き換えることで，バージョンのピンニングなどが行なえます．

今後バージョンを指定し差し替えが可能なインタフェースなども検討しています．


#### 他の手段

ラッパー側でネイティブライブラリが読み込まれる前に読み込みパスを変更することで対応することも可能です．
ファイルの書き換えなどが必要なく，また User 権限でも可能であるなどのメリットが有ります．

```
import world4py

world4py._WORLD_LIBRARY_PATH = 'HERE IS MY LIBRARY PATH'

from world4py.native import apis, tools

# do something
```

このように _world4py_ の他のモジュールを呼ぶ以前に _world4py.\_WORLD\_LIBRARY\_PATH_ を書き換えることで読み込み先を変更できます．

---

demo/sample.wav は [©効果音ラボ](http://soundeffect-lab.info) 様の音声を使用しています．
