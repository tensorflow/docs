# GPUサポート

TensorFlowのGPUサポートには、さまざまなドライバーとライブラリが必要です。
インストールを簡単にし、ライブラリの競合を避けるために、
[GPUサポート付きのTensorFlowのDockerイメージ](./docker.md)を使用することをおすすめします（Linuxのみ）。
このセットアップには[NVIDIA® GPU drivers](https://www.nvidia.com/drivers){:.external}のみが必要です。

これらのインストール手順はTensorFlowの最新リリース用です。
古いTensorFlowリリースで使用する場合、CUDAおよびcuDNNバージョン用の
[テスト済みビルド設定](./source.md#linux)を参照してください。

## pipパッケージ

利用可能なパッケージ、システム要件、および手順については、
[pipインストールガイド](./pip)を参照してください。
GPUサポート付きTensorFlowパッケージを`pip`インストールするには、安定版または開発版パッケージを選択してください:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install tensorflow-gpu  # stable</code>

<code class="devsite-terminal">pip install tf-nightly-gpu  # preview</code>
</pre>

### TensorFlow 2.0 Beta

GPUサポートのテスト用に[TensorFlow 2.0 Beta](https://www.tensorflow.org/beta)が利用可能です。
インストールするには:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install tensorflow-gpu==2.0.0-beta0</code>
</pre>

## ハードウェア要件

以下のGPU対応デバイスがサポートされています:

* NVIDIA® GPU card with CUDA® Compute Capability 3.以降
  [CUDA対応のGPUカード](https://developer.nvidia.com/cuda-gpus){:.external}を参照してください。


## ソフトウェア要件

以下のNVIDIA®ソフトウェアがお使いのシステムにインストールされている必要があります:

* [NVIDIA® GPドライバー](https://www.nvidia.com/drivers){:.external} —CUDA 10は 410.x 以降を必要とします
* [CUDA® Toolkit](https://developer.nvidia.com/cuda-toolkit-archive){:.external} —TensorFlowはCUDA 10.0をサポートしています (TensorFlow >= 1.13.0)
* [CUPTI](http://docs.nvidia.com/cuda/cupti/){:.external}にはCUDA Toolkitが付属しています
* [cuDNN SDK](https://developer.nvidia.com/cudnn){:.external} (>= 7.4.1)
* *(オプション)* [TensorRT 5.0](https://docs.nvidia.com/deeplearning/sdk/tensorrt-install-guide/index.html){:.external}
  はモデルによって推論のレイテンシーとスループットを改善します


## Linuxセットアップ

以下の`apt`の手順は、必要なNVIDIAソフトウェアをUbuntuにインストールする最も簡単な方法です。
しかし、[ソースからTensorFlowをビルド](./source.md)する場合は、
上記のソフトウェア要件一覧を手動でインストールし、ベースとして
`-devel` [TensorFlowのDockerイメージ](./docker.md)の使用を検討してください。

CUDA® Toolki付属の[CUPTI](http://docs.nvidia.com/cuda/cupti/){:.external}をインストールしてください。
インストールしたディレクトリーを
環境変数`$LD_LIBRARY_PATH`に追加してください:

<pre class="devsite-click-to-copy">
<code class="devsite-terminal">export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64</code>
</pre>

CUDA Compute Capability 3.0を搭載したGPU、またはさまざまなバージョンのNVIDIAライブラリについては、
[ソースからのLinuxビルド](./source.md)ガイドを参照してください。

### aptでCUDAをインストールする

このセクションでは、Ubuntu 16.04および18.04にCUDA 10（TensorFlow >= 13.0）およびCUDA 9をインストールする方法を説明します。
これらの手順は、他のDebianベースのディストリビューションでも動作するでしょう。

注意: [Secure Boot](https://wiki.ubuntu.com/UEFI/SecureBoot){:.external}
はNVIDIAドライバーのインストールを複雑にし、これらの手順で想定する範囲を超えています。


#### Ubuntu 18.04 (CUDA 10)

<pre class="prettyprint lang-bsh">
# NVIDIAパッケージリポジトリを追加する
<code class="devsite-terminal">wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.0.130-1_amd64.deb</code>
<code class="devsite-terminal">sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub</code>
<code class="devsite-terminal">sudo apt-get update</code>
<code class="devsite-terminal">wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt-get update</code>

# NVIDIAドライバーをインストールする
<code class="devsite-terminal">sudo apt-get install --no-install-recommends nvidia-driver-410</code>
# 再起動。コマンドを使用してGPUが表示されていることを確認します: nvidia-smi

# 開発ライブラリと実行時ライブラリをインストールする(~4GB)
<code class="devsite-terminal">sudo apt-get install --no-install-recommends \
    cuda-10-0 \
    libcudnn7=7.4.1.5-1+cuda10.0  \
    libcudnn7-dev=7.4.1.5-1+cuda10.0
</code>

# TensorRTをインストールする。上記でlibcudnn7がインストールされている必要があります。
<code class="devsite-terminal">sudo apt-get update && \
        sudo apt-get install nvinfer-runtime-trt-repo-ubuntu1804-5.0.2-ga-cuda10.0 \
        && sudo apt-get update \
        && sudo apt-get install -y --no-install-recommends libnvinfer-dev=5.0.2-1+cuda10.0
</code>
</pre>


#### Ubuntu 16.04 (CUDA 10)

<pre class="prettyprint lang-bsh">
# NVIDIAパッケージリポジトリを追加する
# apt-key用にHTTPサポートを追加する
<code class="devsite-terminal">sudo apt-get install gnupg-curl</code>
<code class="devsite-terminal">wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_10.0.130-1_amd64.deb</code>
<code class="devsite-terminal">sudo dpkg -i cuda-repo-ubuntu1604_10.0.130-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub</code>
<code class="devsite-terminal">sudo apt-get update</code>
<code class="devsite-terminal">wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt install ./nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt-get update</code>

# NVIDIAドライバーをインストールする
# ドライバーのインストールに関する問題は /usr/lib/nvidia の作成を必要とします
<code class="devsite-terminal">sudo mkdir /usr/lib/nvidia</code>
<code class="devsite-terminal">sudo apt-get install --no-install-recommends nvidia-410</code>
# 再起動。コマンドを使用してGPUが表示されていることを確認します: nvidia-smi

# 開発・実行時ライブラリをインストールする(~4GB)
<code class="devsite-terminal">sudo apt-get install --no-install-recommends \
    cuda-10-0 \
    libcudnn7=7.4.1.5-1+cuda10.0  \
    libcudnn7-dev=7.4.1.5-1+cuda10.0
</code>

# TensorRTをインストールする。上記でlibcudnn7がインストールされている必要があります。
<code class="devsite-terminal">sudo apt-get update && \
        sudo apt-get install nvinfer-runtime-trt-repo-ubuntu1604-5.0.2-ga-cuda10.0 \
        && sudo apt-get update \
        && sudo apt-get install -y --no-install-recommends libnvinfer-dev=5.0.2-1+cuda10.0
</code>
</pre>


#### Ubuntu 16.04 (CUDA 9.0 for TensorFlow < 1.13.0)

<pre class="prettyprint lang-bsh">
# NVIDIAパッケージリポジトリを追加する
<code class="devsite-terminal">sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub</code>
<code class="devsite-terminal">wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.1.85-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt install ./cuda-repo-ubuntu1604_9.1.85-1_amd64.deb</code>
<code class="devsite-terminal">wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt install ./nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb</code>
<code class="devsite-terminal">sudo apt update</code>

# NVIDIAドライバーをインストールする
# ドライバーのインストールに関する問題は /usr/lib/nvidia の作成を必要とします
<code class="devsite-terminal">sudo mkdir /usr/lib/nvidia</code>
<code class="devsite-terminal">sudo apt-get install --no-install-recommends nvidia-410</code>
# 再起動。コマンドを使用してGPUが表示されていることを確認します: nvidia-smi

# CUDAとツールをインストールする。オプションのNCCL 2.xを含みます。
<code class="devsite-terminal">sudo apt install cuda9.0 cuda-cublas-9-0 cuda-cufft-9-0 cuda-curand-9-0 \
    cuda-cusolver-9-0 cuda-cusparse-9-0 libcudnn7=7.2.1.38-1+cuda9.0 \
    libnccl2=2.2.13-1+cuda9.0 cuda-command-line-tools-9-0</code>

# オプション: TensorRTランタイムをインストールします (CUDAのインストール後にする必要があります)
<code class="devsite-terminal">sudo apt update</code>
<code class="devsite-terminal">sudo apt install libnvinfer4=4.1.2-1+cuda9.0</code>
</pre>


## Windowsセットアップ

[ハードウェア要件](#hardware_requirements)と上記の
[ソフトウェア要件](#software_requirements)の一覧を参照してください。
[Windows用のCUDA®インストールガイド](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/){:.external}を読んでください。

インストールされたNVIDIAソフトウェアパッケージが上記のバージョンと一致することを確認してください。
特に、TensorFlowは`cuDNN64_7.dll`ファイルがないとロードされません。
別のバージョンを使用するには、[ソースからのWindows用のビルド](./source_windows.md)ガイドを参照してください。

CUDA、CUPTI、およびcuDNNがインストールされたディレクトリーを`％PATH％`環境変数に追加します。
例えば、CUDA Toolkitが`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0`に、
cuDNNが`C:\tools\cuda`にインストールされている場合、
以下のように`％PATH％`を更新してください:

<pre class="devsite-click-to-copy">
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin;%PATH%</code>
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\extras\CUPTI\libx64;%PATH%</code>
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\include;%PATH%</code>
<code class="devsite-terminal tfo-terminal-windows">SET PATH=C:\tools\cuda\bin;%PATH%</code>
</pre>
