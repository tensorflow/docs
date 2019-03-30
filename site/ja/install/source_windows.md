# Windows向けにソースからビルドする

ソースからTensorFlow *pip* パッケージをビルドし、それをWindowsにインストールします。

注: Windowsシステム用に、十分にテストされたビルド済みの[TensorFlow packages](./pip.md)をすでに提供しています。

## Windwos用にセットアップする

以下のビルドツールをインストールしてWindows用開発環境を設定します。

### PythonとTensorFlowの依存パッケージをインストールする

[Python 3.5.x or Python 3.6.x 64-bit release for Windows](https://www.python.org/downloads/windows/){:.external}をインストールしてください。
オプション機能として*pip*を選択し、それをあなたの`％PATH％`環境変数に追加してください。

TensorFlowの*pip*依存パッケージをインストールします:

<pre class="devsite-click-to-copy">
<code class="devsite-terminal tfo-terminal-windows">pip3 install six numpy wheel</code>
<code class="devsite-terminal tfo-terminal-windows">pip3 install keras_applications==1.0.6 --no-deps</code>
<code class="devsite-terminal tfo-terminal-windows">pip3 install keras_preprocessing==1.0.5 --no-deps</code>
</pre>

依存パッケージは
<a href="https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/pip_package/setup.py" class="external"><code>setup.py</code></a>
の`REQUIRED_PACKAGES`の下に一覧があります。

### Bazelをインストールする

[Install Bazel](https://docs.bazel.build/versions/master/install-windows.html){:.external},
TensorFlowをコンパイルするのに使用するビルドツールです。
[build C++](https://docs.bazel.build/versions/master/windows.html#build-c){:.external}でBazelをセットアップしてください。

Bazel実行可能ファイルの場所を`PATH`環境変数に追加してください。

### MSYS2をインストールする

TensorFlowをビルドするのに必要なbinツールのため、[Install MSYS2](https://www.msys2.org/){:.external}を行ってください。
`C:\msys64`にMSYS2がインストールされている場合、`C:\msys64\usr\bin`を`%PATH%`環境変数に追加してください。
次に`cmd.exe`を使用して実行してください:

<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">
pacman -S git patch unzip
</pre>

### Visual C++ Build Tools 2015をインストールする

*Visual C++ build tools 2015*をインストールしてください。
これは*Visual Studio 2015*に付属していますが、別々にインストールすることができます:

1. [Visual Studio downloads](https://visualstudio.microsoft.com/vs/older-downloads/){:.external}に移動します
2. *Redistributables and Build Tools*を選択します
3. ダウンロード・インストールします:
   - *Microsoft Visual C++ 2015 Redistributable Update 3*
   - *Microsoft Build Tools 2015 Update 3*

注: TensorFlowは*Visual Studio 2015 Update 3*に対してテスト済みです。

### GPUサポートをインストールする (オプション)

Windows用の[GPUサポート](./gpu.md)ガイドを読み、
GPU上でTensorFlowを実行するために必要なドライバーと追加ソフトウェアをインストールしてください。


### TensorFlowのソースコードをダウンロードする


[Git](https://git-scm.com/){:.external}を使って
[TensorFlow repository](https://github.com/tensorflow/tensorflow){:.external}をcloneしてください (`git`はMSYS2と一緒にインストールされています):

<pre class="devsite-click-to-copy">
<code class="devsite-terminal tfo-terminal-windows">git clone https://github.com/tensorflow/tensorflow.git</code>
<code class="devsite-terminal tfo-terminal-windows">cd tensorflow</code>
</pre>

レポジトリのデフォルトは `master` 開発ブランチです。
[release branch](https://github.com/tensorflow/tensorflow/releases){:.external}をcheckoutしてビルドすることもできます:

<pre class="devsite-terminal tfo-terminal-windows prettyprint lang-bsh">
git checkout <em>branch_name</em>  # r1.9, r1.10, etc.
</pre>

ポイント: 最新の開発ブランチでビルドの問題が発生している場合は、
動作が確認されているreleaseブランチを試してください。


## ビルドを設定する

TensorFlowソースツリーのルートディレクトリーで次のコマンドを実行してシステムビルドを設定します:

<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">
python ./configure.py
</pre>

このスクリプトは、TensorFlow依存関係の場所をたずねるプロンプトを出し、
追加のビルド設定オプション（例えば、コンパイラーフラグ）を求めます。
以下は `python ./configure.py` の実行例です (セッションは異なるかもしれません):

<section class="expandable">
<h4 class="showalways">View sample configuration session</h4>
<pre class="devsite-terminal tfo-terminal-windows">
python ./configure.py
Starting local Bazel server and connecting to it...
................
You have bazel 0.15.0 installed.
Please specify the location of python. [Default is C:\python36\python.exe]: 

Found possible Python library paths:
  C:\python36\lib\site-packages
Please input the desired Python library path to use.  Default is [C:\python36\lib\site-packages]

Do you wish to build TensorFlow with CUDA support? [y/N]: <b>Y</b>
CUDA support will be enabled for TensorFlow.

Please specify the CUDA SDK version you want to use. [Leave empty to default to CUDA 9.0]:

Please specify the location where CUDA 9.0 toolkit is installed. Refer to README.md for more details. [Default is C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v9.0]:

Please specify the cuDNN version you want to use. [Leave empty to default to cuDNN 7.0]: <b>7.0</b>

Please specify the location where cuDNN 7 library is installed. Refer to README.md for more details. [Default is C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v9.0]: <b>C:\tools\cuda</b>

Please specify a list of comma-separated Cuda compute capabilities you want to build with.
You can find the compute capability of your device at: https://developer.nvidia.com/cuda-gpus.
Please note that each additional compute capability significantly increases your build time and binary size. [Default is: 3.5,7.0]: <b>3.7</b>

Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is /arch:AVX]: 

Would you like to override eigen strong inline for some C++ compilation to reduce the compilation time? [Y/n]:
Eigen strong inline overridden.

Configuration finished
</pre>
</section>

### 設定オプション

[GPUサポート](./gpu.md)用に、CUDAとcuDNNのバージョンを指定してください。
ご自身のシステムに複数バージョンのCUDAもしくはcuDNNがインストールされている場合、
デフォルトバージョンに頼らず明示的にバージョンを設定してください。
`./configure.py` はシステムのCUDAのライブラリにシンボリックリンクを作成しますので、
CUDAのライブラリのパスを更新する場合、この設定ステップはビルドの前に再び実行する必要があります。

注: TensorFlow 1.6以降、バイナリは古いCPUでは動作しない可能性があるAVX命令を使用しています。


## pipパッケージをビルドする

### Bazelでのビルド

#### CPUのみ

TensorFlowパッケージビルダーをCPUのみサポートするようにするには `bazel` を使います:

<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">
bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package
</pre>

#### GPUサポート

TensorFlowパッケージビルダーをGPUサポート付きにするには:

<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">
bazel build --config=opt --config=cuda --define=no_tensorflow_py_deps=true //tensorflow/tools/pip_package:build_pip_package
</pre>

#### Bazelのビルドオプション

ビルド時にこのオプションを使用して、パッケージ作成に関する問題を回避します。
https://github.com/tensorflow/tensorflow/issues/22390

<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">
--define=no_tensorflow_py_deps=true
</pre>

ソースからTensorFlowをビルドすると、大量のRAMを使用する可能性があります。
ご自身のシステムのメモリが制限されている場合は、BazelのRAM使用量を制限してください: `--local_resources 2048,.5,1.0`

GPUサポート付きでビルドしている場合、nvccの警告メッセージを抑制するために
`--copt=-nvcc_options=disable-warnings`を追加してください。

### パッケージをビルドする


`bazel build`コマンドは`build_pip_package`という名前の実行ファイルを作成します。
これは`pip`パッケージをビルドするプログラムです。
例えば、以下は`C:/tmp/tensorflow_pkg`ディレクトリーに`.whl`パッケージをビルドします:

<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">
bazel-bin\tensorflow\tools\pip_package\build_pip_package C:/tmp/tensorflow_pkg
</pre>

同じソースツリーの下でCUDAと非CUDAの両方の設定をビルドすることは可能ですが、
同じソースツリー内でこれら2つの設定を切り替えるときは`bazel clean`を実行することを推奨します。

### パッケージをインストールする

生成された`.whl`ファイルのファイル名はTensorFlowのバージョンとプラットフォームに依存します。
パッケージをインストールするには `pip3 install`を使います。例えば:

<pre class="devsite-terminal tfo-terminal-windows prettyprint lang-bsh">
pip3 install C:/tmp/tensorflow_pkg/tensorflow-<var>version</var>-cp36-cp36m-win_amd64.whl
</pre>

成功: TensorFlowがインストールできました。


## MSYSシェルを使用してビルドする

TensorFlowはMSYSシェルを使ってビルドすることもできます。以下の項目に変更を加え、
Windowsのネイティブコマンドライン(`cmd.exe`)の前の指示に従ってください。

### MSYSパス変換を無効にする {:.hide-from-toc}

MSYSは自動的にUnixパスのように見える引数をWindowsパスに変換します。
そしてこれは `bazel`では動作しません。
(ラベル`//foo/bar:bin`はスラッシュで始まるのでUnixの絶対パスと見なされます)

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">export MSYS_NO_PATHCONV=1</code>
<code class="devsite-terminal">export MSYS2_ARG_CONV_EXCL="*"</code>
</pre>

### PATHをセットします {:.hide-from-toc}

BazelとPythonのインストールディレクトリーを`$PATH`環境変数に追加してください。
Bazelが`C:\tools\bazel.exe`に、そしてPythonが`C:\Python36\python.exe`にインストールされている場合、
`PATH`を以下のように設定してください:

<pre class="prettyprint lang-bsh">
# 区切り文字としてUnixスタイルの':'を使用します
<code class="devsite-terminal">export PATH="/c/tools:$PATH"</code>
<code class="devsite-terminal">export PATH="/c/Python36:$PATH"</code>
</pre>

GPUサポート用に、CUDAとcuDNNのbinディレクトリー`$PATH`に追加します:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">export PATH="/c/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v9.0/bin:$PATH"</code>
<code class="devsite-terminal">export PATH="/c/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v9.0/extras/CUPTI/libx64:$PATH"</code>
<code class="devsite-terminal">export PATH="/c/tools/cuda/bin:$PATH"</code>
</pre>


## テスト済みのビルド設定

### CPU

<table>
<tr><th>Version</th><th>Python version</th><th>Compiler</th><th>Build tools</th></tr>
<tr><td>tensorflow-1.12.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.11.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.10.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.9.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.8.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.7.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.6.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.5.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.4.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.3.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.2.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.1.0</td><td>3.5</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
<tr><td>tensorflow-1.0.0</td><td>3.5</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td></tr>
</table>

### GPU

<table>
<tr><th>Version</th><th>Python version</th><th>Compiler</th><th>Build tools</th><th>cuDNN</th><th>CUDA</th></tr>
<tr><td>tensorflow_gpu-1.12.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Bazel 0.15.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.11.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Bazel 0.15.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.10.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.9.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.8.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.7.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.6.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.5.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.4.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>6</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.3.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>6</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.2.0</td><td>3.5-3.6</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>5.1</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.1.0</td><td>3.5</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>5.1</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.0.0</td><td>3.5</td><td>MSVC 2015 update 3</td><td>Cmake v3.6.3</td><td>5.1</td><td>8</td></tr>
</table>
