# ソースからビルドする

ソースからTensorFlowの*pip*パッケージをビルドし、それをUbuntu LinuxとmacOSにインストールします。
この手順はほかのシステムでも機能するかもしれませんが、UbuntuとmacOSでのみテスト・サポートされています。

注: LinuxおよびmacOSシステム用に、十分にテストされたビルド済みの[TensorFlowパッケージ](./pip.md)をすでに提供しています。


## LinuxとmacOS用にセットアップする

以下のビルドツールをインストールして開発環境を設定してください。

### PythonとTensorFlowの依存パッケージをインストールする

<div class="ds-selector-tabs">
<section>
<h3>Ubuntu</h3>
<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">sudo apt install python-dev python-pip  # もしくは python3-dev python3-pip</code>
</pre>
</section>
<section>
<h3>mac OS</h3>
<p>Xcode 9.2以降が必要です</p>
<p><a href="https://brew.sh/" class="external">Homebrew</a>パッケージマネージャーを使用してインストールします:</p>
<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"</code>
<code class="devsite-terminal">export PATH="/usr/local/bin:/usr/local/sbin:$PATH"</code>
<code class="devsite-terminal">brew install python@2  # もしくは python (Python 3)</code>
</pre>
</section>
</div><!--/ds-selector-tabs-->

TensorFlowの*pip*依存パッケージをインストールします。
(仮想環境を使用している場合、`--user`引数は省いてください)

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install -U --user pip six numpy wheel setuptools mock</code>
<code class="devsite-terminal">pip install -U --user keras_applications==1.0.6 --no-deps</code>
<code class="devsite-terminal">pip install -U --user keras_preprocessing==1.0.5 --no-deps</code>
</pre>

依存パッケージは
<a href="https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/pip_package/setup.py" class="external"><code>setup.py</code></a>
の`REQUIRED_PACKAGES`の下に一覧があります。

### Bazelをインストールする

[Bazelのインストール](https://docs.bazel.build/versions/master/install.html){:.external},
TensorFlowをコンパイルするのに使用するビルドツールです。

Bazel実行ファイルの場所を`PATH`環境変数に追加してください。

### GPUサポートをインストールします (オプション、Linuxnのみ)

macOSには*GPUサポートがありません*。

[GPUサポート](./gpu.md)ガイドを読み、GPU上でTensorFlowを実行するために必要なドライバーと追加ソフトウェアをインストールしてください。

注: TensorFlowのGPU対応の[Dockerイメージ](#docker_linux_builds)をセットアップする方が簡単です。

### TensorFlowのソースコードをダウンロードする

[Git](https://git-scm.com/){:.external}を使って
[TensorFlowリポジトリ](https://github.com/tensorflow/tensorflow){:.external}をcloneしてください:

<pre class="devsite-click-to-copy">
<code class="devsite-terminal">git clone https://github.com/tensorflow/tensorflow.git</code>
<code class="devsite-terminal">cd tensorflow</code>
</pre>

リポジトリのデフォルトは`master`開発ブランチです。
[releaseブランチ](https://github.com/tensorflow/tensorflow/releases){:.external}をcheckoutしてビルドすることもできます:

<pre class="devsite-terminal prettyprint lang-bsh">
git checkout <em>branch_name</em>  # r1.9、r1.10 など。
</pre>


## ビルドを設定する

TensorFlowソースツリーのルートディレクトリで次のコマンドを実行してシステムビルドを設定します:

<pre class="devsite-terminal devsite-click-to-copy">
./configure
</pre>

このスクリプトは、TensorFlow依存関係の場所をたずねるプロンプトを出し、
追加のビルド設定オプション（たとえば、コンパイラーフラグ）を求めます。
以下は`./configure`の実行例です (セッションは異なるかもしれません):

<section class="expandable">
<h4 class="showalways">サンプルの構成セッションを表示する</h4>
<pre class="devsite-terminal">
./configure
You have bazel 0.15.0 installed.
Please specify the location of python. [Default is /usr/bin/python]: <b>/usr/bin/python2.7</b>

Found possible Python library paths:
  /usr/local/lib/python2.7/dist-packages
  /usr/lib/python2.7/dist-packages
Please input the desired Python library path to use.  Default is [/usr/lib/python2.7/dist-packages]

Do you wish to build TensorFlow with jemalloc as malloc support? [Y/n]:
jemalloc as malloc support will be enabled for TensorFlow.

Do you wish to build TensorFlow with Google Cloud Platform support? [Y/n]:
Google Cloud Platform support will be enabled for TensorFlow.

Do you wish to build TensorFlow with Hadoop File System support? [Y/n]:
Hadoop File System support will be enabled for TensorFlow.

Do you wish to build TensorFlow with Amazon AWS Platform support? [Y/n]:
Amazon AWS Platform support will be enabled for TensorFlow.

Do you wish to build TensorFlow with Apache Kafka Platform support? [Y/n]:
Apache Kafka Platform support will be enabled for TensorFlow.

Do you wish to build TensorFlow with XLA JIT support? [y/N]:
No XLA JIT support will be enabled for TensorFlow.

Do you wish to build TensorFlow with GDR support? [y/N]:
No GDR support will be enabled for TensorFlow.

Do you wish to build TensorFlow with VERBS support? [y/N]:
No VERBS support will be enabled for TensorFlow.

Do you wish to build TensorFlow with OpenCL SYCL support? [y/N]:
No OpenCL SYCL support will be enabled for TensorFlow.

Do you wish to build TensorFlow with CUDA support? [y/N]: <b>Y</b>
CUDA support will be enabled for TensorFlow.

Please specify the CUDA SDK version you want to use. [Leave empty to default to CUDA 9.0]: <b>9.0</b>

Please specify the location where CUDA 9.0 toolkit is installed. Refer to README.md for more details. [Default is /usr/local/cuda]:

Please specify the cuDNN version you want to use. [Leave empty to default to cuDNN 7.0]: <b>7.0</b>

Please specify the location where cuDNN 7 library is installed. Refer to README.md for more details. [Default is /usr/local/cuda]:

Do you wish to build TensorFlow with TensorRT support? [y/N]:
No TensorRT support will be enabled for TensorFlow.

Please specify the NCCL version you want to use. If NCLL 2.2 is not installed, then you can use version 1.3 that can be fetched automatically but it may have worse performance with multiple GPUs. [Default is 2.2]: 1.3

Please specify a list of comma-separated Cuda compute capabilities you want to build with.
You can find the compute capability of your device at: https://developer.nvidia.com/cuda-gpus.
Please note that each additional compute capability significantly increases your
build time and binary size. [Default is: 3.5,7.0] <b>6.1</b>

Do you want to use clang as CUDA compiler? [y/N]:
nvcc will be used as CUDA compiler.

Please specify which gcc should be used by nvcc as the host compiler. [Default is /usr/bin/gcc]:

Do you wish to build TensorFlow with MPI support? [y/N]:
No MPI support will be enabled for TensorFlow.

Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is -march=native]:

Would you like to interactively configure ./WORKSPACE for Android builds? [y/N]:
Not configuring the WORKSPACE for Android builds.

Preconfigured Bazel build configs. You can use any of the below by adding "--config=<>" to your build command. See tools/bazel.rc for more details.
    --config=mkl            # MKLサポート付きのビルド用の設定。
    --config=monolithic     # ほぼ静的なモノリシックビルド用の設定。
Configuration finished
</pre>
</section>

### 設定オプション

[GPUサポート](./gpu.md)用に、CUDAとcuDNNのバージョンを指定してください。
ご使用のシステムに複数バージョンのCUDAもしくはcuDNNがインストールされている場合、
デフォルトバージョンに頼らず明示的にバージョンを設定してください。
`./configure` はシステムのCUDAのライブラリにシンボリックリンクを作成しますので、
CUDAのライブラリのパスを更新する場合、この設定ステップはビルドの前に再び実行する必要があります。

コンパイル最適化フラグの場合、デフォルト (`-march=native`) はご使用のマシンのCPUタイプ用の生成コードに最適化します。
ただし、異なるCPUタイプ用にTensorFlowをビルドする場合は、より具体的な最適化フラグを検討してください。
例については
[GCCマニュアル](https://gcc.gnu.org/onlinedocs/gcc-4.5.3/gcc/i386-and-x86_002d64-Options.html){:.external}
を参照してください。

`bazel build`コマンドに追加できるいくつかの設定済みのビルド設定が利用可能です。
たとえば:

* `--config=mkl` —[Intel® MKL-DNN](https://github.com/intel/mkl-dnn){:.external}用のサポート
* `--config=monolithic` —ほとんど静的でモノリシックなビルド設定

注: TensorFlow 1.6以降、バイナリは古いCPUでは動作しない可能性があるAVX命令を使用しています。


## pipパッケージをビルドする

### Bazelでのビルド

#### CPUのみ

TensorFlowパッケージビルダーをCPUのみサポートするようにするには`bazel`を使います:

<pre class="devsite-terminal devsite-click-to-copy">
bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package
</pre>

#### GPUサポート

TensorFlowパッケージビルダーをGPUサポート付きにするには:

<pre class="devsite-terminal devsite-click-to-copy">
bazel build --config=opt --config=cuda //tensorflow/tools/pip_package:build_pip_package
</pre>

#### Bazelのビルドオプション

ソースからTensorFlowをビルドすると、大量のRAMを使用する可能性があります。
ご使用のシステムのメモリが制限されている場合は、BazelのRAM使用量を制限してください: `--local_ram_resources=2048`

[公式TensorFlowパッケージ](./pip.md)はGCC 4で構築されており、古いABIを使用しています。
GCC 5以降では、ビルドを古いABIと互換してください: `--cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0"`
ABI互換性により、公式のTensorFlowパッケージに対してビルドされたカスタムオペレーションは、
引き続きGCC 5ビルドパッケージとともに機能します。


### パッケージをビルドする


`bazel build`コマンドは`build_pip_package`という名前の実行ファイルを作成します。
これは`pip`パッケージをビルドするプログラムです。
下記のように実行ファイルを実行して`/tmp/tensorflow_pkg`ディレクトリに`.whl`パッケージをビルドしてください。

releaseブランチからビルドするには:

<pre class="devsite-terminal devsite-click-to-copy">
./bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
</pre>

masterからビルドするには、`--nightly_flag`を使用して正しい依存関係を取得してください:

<pre class="devsite-terminal devsite-click-to-copy">
./bazel-bin/tensorflow/tools/pip_package/build_pip_package --nightly_flag /tmp/tensorflow_pkg
</pre>

おなじソースツリーの下でCUDAと非CUDAの両方の設定をビルドすることは可能ですが、
おなじソースツリー内でこれら2つの設定を切り替えるときは`bazel clean`を実行することを推奨します。

### パッケージをインストールする

生成された`.whl`ファイルのファイル名はTensorFlowのバージョンとプラットフォームに依存します。
パッケージをインストールするには`pip install`を使います。たとえば:

<pre class="devsite-terminal prettyprint lang-bsh">
pip install /tmp/tensorflow_pkg/tensorflow-<var>version</var>-<var>tags</var>.whl
</pre>

成功: TensorFlowがインストールできました。


## DockerのLinuxビルド

ソースからLinuxパッケージをビルドするには、TensorFlowのDocker開発イメージを使うのが簡単です。
これらのイメージは、TensorFlowをビルドするために必要なソースコードと必要な依存関係をすでに含んでいます。
インストールのためのTensorFlowの
[Dockerガイド](./docker.md)と
[利用可能なイメージタグの一覧](https://hub.docker.com/r/tensorflow/tensorflow/tags/){:.external}を参照してください。


### CPUのみ

以下の例は、`:nightly-devel`イメージを使用して
最新のTensorFlowソースコードからCPUのみのPython&nbps;2パッケージをビルドします。
使用可能なTensorFlowの`-devel`タグは、[Dockerガイド](./docker.md)を参照してください。

最新の開発用イメージをダウンロードして、*pip*パッケージをビルドするために使用するDockerコンテナを起動します:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">docker pull tensorflow/tensorflow<var>:nightly-devel</var></code>
<code class="devsite-terminal">docker run -it -w /tensorflow -v $PWD:/mnt -e HOST_PERMS="$(id -u):$(id -g)" \
    tensorflow/tensorflow<var>:nightly-devel</var> bash</code>

<code class="devsite-terminal tfo-terminal-root">git pull  # コンテナ内で、最新のソースコードをダウンロードします</code>
</pre>

上記の`docker run`コマンドは`/tensorflow`ディレクトリ、つまりソースツリーのルートでシェルを起動します。
ホストの現在のディレクトリをコンテナの`/mnt`ディレクトリにマウントし、
環境変数を通してコンテナにホストユーザーの情報を渡します。
(この環境変数はアクセス権を設定するために使用されます。Dockerはこれらを巧妙に行うことができます)

あるいは、コンテナ内にTensorFlowのホストコピーを構築するには、
ホストのソースツリーをコンテナの`/tensorflow`ディレクトリにマウントします:

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
docker run -it -w /tensorflow -v <var>/path/to/tensorflow</var>:/tensorflow -v $PWD:/mnt \
    -e HOST_PERMS="$(id -u):$(id -g)" tensorflow/tensorflow:<var>nightly-devel</var> bash
</pre>

ソースツリーを設定したら、コンテナの仮想環境内にTensorFlowパッケージをビルドします:

1. ビルドを設定する-ビルド設定の質問に答えるようにユーザーに促します。
2. *pip*パッケージを作成するために使用されるツールをビルドします。
3. ツールを実行して*pip*パッケージを作成します。
4. ファイルの所有権をコンテナの外で調整します。

<pre class="devsite-disable-click-to-copy prettyprint lang-bsh">
<code class="devsite-terminal tfo-terminal-root">./configure  # プロンプトに答えるか、デフォルト設定を使用します</code>

<code class="devsite-terminal tfo-terminal-root">bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package</code>

<code class="devsite-terminal tfo-terminal-root">./bazel-bin/tensorflow/tools/pip_package/build_pip_package /mnt  # パッケージを作成します</code>

<code class="devsite-terminal tfo-terminal-root">chown $HOST_PERMS /mnt/tensorflow-<var>version</var>-<var>tags</var>.whl</code>
</pre>

コンテナ内にパッケージをインストールして確認します:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal tfo-terminal-root">pip uninstall tensorflow  # 現在のバージョンを削除します</code>

<code class="devsite-terminal tfo-terminal-root">pip install /mnt/tensorflow-<var>version</var>-<var>tags</var>.whl</code>
<code class="devsite-terminal tfo-terminal-root">cd /tmp  # ソースディレクトリからインポートしません</code>
<code class="devsite-terminal tfo-terminal-root">python -c "import tensorflow as tf; print(tf.__version__)"</code>
</pre>

成功: TensorFlowがインストールできました。

ご使用のホストマシンでは、TensorFlowの*pip*パッケージは(ホストユーザー権限をもつ)
現在のディレクトリにあります: <code>./tensorflow-<var>version</var>-<var>tags</var>.whl</code>

### GPUサポート

*ホスト*マシンは
[NVIDIA®&nbspドライバー](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver){:.external}しか必要としないので、DockerはTensorFlowのGPUサポートをビルドするもっとも簡単な方法です。
(*NVIDIA® CUDA ツールキット*はインストールする必要はありません)
[nvidia-docker](https://github.com/NVIDIA/nvidia-docker){:.external} (Linuxのみ)をセットアップするには、
[GPU supportガイド](./gpu.md)とTensorFlowの[Dockerガイド](./docker.md)を参照してください。

以下の例ではTensorFlowの`:nightly-devel-gpu-py3`イメージをダウンロードし、
`nvidia-docker`を使ってGPU対応のコンテナを実行します。
この開発用イメージは、GPUをサポートするPython 3 *pip*パッケージをビルドするように設定されています:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">docker pull tensorflow/tensorflow<var>:nightly-devel-gpu-py3</var></code>
<code class="devsite-terminal">docker run --runtime=nvidia -it -w /tensorflow -v $PWD:/mnt -e HOST_PERMS="$(id -u):$(id -g)" \
    tensorflow/tensorflow<var>:nightly-devel-gpu-py3</var> bash</code>
</pre>

次に、コンテナの仮想環境内で、GPUサポート付きのTensorFlowパッケージをビルドします:

<pre class="devsite-disable-click-to-copy prettyprint lang-bsh">
<code class="devsite-terminal tfo-terminal-root">./configure  # プロンプトに答えるか、デフォルト設定を使用します</code>

<code class="devsite-terminal tfo-terminal-root">bazel build --config=opt --config=cuda //tensorflow/tools/pip_package:build_pip_package</code>

<code class="devsite-terminal tfo-terminal-root">./bazel-bin/tensorflow/tools/pip_package/build_pip_package /mnt  # パッケージを作成します</code>

<code class="devsite-terminal tfo-terminal-root">chown $HOST_PERMS /mnt/tensorflow-<var>version</var>-<var>tags</var>.whl</code>
</pre>

パッケージをコンテナ内にインストールして検証し、GPUを確認します。

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal tfo-terminal-root">pip uninstall tensorflow  # 現在のバージョンを削除します</code>

<code class="devsite-terminal tfo-terminal-root">pip install /mnt/tensorflow-<var>version</var>-<var>tags</var>.whl</code>
<code class="devsite-terminal tfo-terminal-root">cd /tmp  # ソースディレクトリからインポートしません</code>
<code class="devsite-terminal tfo-terminal-root">python -c "import tensorflow as tf; print(tf.contrib.eager.num_gpus())"</code>
</pre>

成功: TensorFlowがインストールできました。


## テスト済みのビルド設定

### Linux

<table>
<tr><th>バージョン</th><th>Pythonバージョン</th><th>コンパイラー</th><th>ビルドツール</th></tr>
<tr><td>tensorflow-1.13.1</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.19.2</td></tr>
<tr><td>tensorflow-1.12.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.11.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.10.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.9.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.11.0</td></tr>
<tr><td>tensorflow-1.8.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.10.0</td></tr>
<tr><td>tensorflow-1.7.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.10.0</td></tr>
<tr><td>tensorflow-1.6.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.9.0</td></tr>
<tr><td>tensorflow-1.5.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.8.0</td></tr>
<tr><td>tensorflow-1.4.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.5.4</td></tr>
<tr><td>tensorflow-1.3.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.5</td></tr>
<tr><td>tensorflow-1.2.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.5</td></tr>
<tr><td>tensorflow-1.1.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.2</td></tr>
<tr><td>tensorflow-1.0.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.2</td></tr>
</table>

<table>
<tr><th>バージョン</th><th>Pythonバージョン</th><th>コンパイラー</th><th>ビルドツール</th><th>cuDNN</th><th>CUDA</th></tr>
<tr><td>tensorflow_gpu-1.13.1</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.19.2</td><td>7.4</td><td>10.0</td></tr>
<tr><td>tensorflow_gpu-1.12.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.15.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.11.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.15.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.10.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.15.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.9.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.11.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.8.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.10.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.7.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.9.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.6.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.9.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.5.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.8.0</td><td>7</td><td>9</td></tr>
<tr><td>tensorflow_gpu-1.4.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.5.4</td><td>6</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.3.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.5</td><td>6</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.2.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.5</td><td>5.1</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.1.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.2</td><td>5.1</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.0.0</td><td>2.7, 3.3-3.6</td><td>GCC 4.8</td><td>Bazel 0.4.2</td><td>5.1</td><td>8</td></tr>
</table>

### macOS

#### CPU

<table>
<tr><th>バージョン</th><th>Pythonバージョン</th><th>コンパイラー</th><th>ビルドツール</th></tr>
<tr><td>tensorflow-1.13.1</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.19.2</td></tr>
<tr><td>tensorflow-1.12.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.11.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.10.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.15.0</td></tr>
<tr><td>tensorflow-1.9.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.11.0</td></tr>
<tr><td>tensorflow-1.8.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.10.1</td></tr>
<tr><td>tensorflow-1.7.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.10.1</td></tr>
<tr><td>tensorflow-1.6.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.8.1</td>
<tr><td>tensorflow-1.5.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.8.1</td>
<tr><td>tensorflow-1.4.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.5.4</td></tr>
<tr><td>tensorflow-1.3.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.5</td></tr>
<tr><td>tensorflow-1.2.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.5</td></tr>
<tr><td>tensorflow-1.1.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.2</td></tr>
<tr><td>tensorflow-1.0.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.2</td></tr>
</table>

#### GPU

<table>
<tr><th>バージョン</th><th>Pythonバージョン</th><th>コンパイラー</th><th>ビルドツール</th><th>cuDNN</th><th>CUDA</th></tr>
<tr><td>tensorflow_gpu-1.1.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.2</td><td>5.1</td><td>8</td></tr>
<tr><td>tensorflow_gpu-1.0.0</td><td>2.7, 3.3-3.6</td><td>Clang from xcode</td><td>Bazel 0.4.2</td><td>5.1</td><td>8</td></tr>
</table>
