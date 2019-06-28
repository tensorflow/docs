# Docker

[Docker](https://docs.docker.com/install/){:.external}は、*コンテナ*を使用して、
TensorFlowのインストールをシステムのほかの部分から分離した仮想環境を作成します。
TensorFlowのプログラムは、この*仮想環境内*で実行され、ホストマシンとリソースを共有できます。
（ディレクトリへのアクセス、GPUの使用、インターネットへの接続など）
[TensorFlowのDockerイメージ](https://hub.docker.com/r/tensorflow/tensorflow/){:.external}
は各リリースでテストされています。

Dockerは、LinuxでTensorFlowの[GPUサポート](./gpu.md)を有効にするもっとも簡単な方法です。
*ホスト*マシンに必要なのは
[NVIDIA® GPドライバー](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver){:.external}だけです。
(*NVIDIA® CUDA® Toolk*をインストールする必要はありません)


## TensorFlow Dockerの必要条件

1. [Dockerのインストール](https://docs.docker.com/install/){:.external}をローカル*ホスト*マシンで実行してください
2. LinuxでGPUサポートするには、[nvidia-dockerのインストール](https://github.com/NVIDIA/nvidia-docker){:.external}を実行してください

注: `sudo`なしで`docker`コマンドを実行するには、`docker`グループを作成してあなたのユーザーを追加してください。
詳しくは
[Linux用のインストール後の手順](https://docs.docker.com/install/linux/linux-postinstall/){:.external}を参照してください。


## TensorFlowのDockerイメージをダウンロードする

公式のTensorFlowのDockerイメージは、
[tensorflow/tensorflow](https://hub.docker.com/r/tensorflow/tensorflow/){:.external}
Docker Hubリポジトリにあります。
イメージリリースは、次の形式で[タグ付け](https://hub.docker.com/r/tensorflow/tensorflow/tags/){:.external}されています:

| タグ        | 説明                                                                                              |
| ---         | ---                                                                                               |
| `latest`    | 最新リリースのTensorFlowのCPUバイナリイメージ。デフォルト。                                       |
| `nightly`   | TensorFlowのnightlyビルドのイメージ。(不安定)                                                     |
| *`version`* | TensorFlowのバイナリイメージの*version*を指定する。例: *1.14.0*                                   |
| `devel`     | TensorFlowのnightlyビルドの`master`開発環境。TensorFlowのソースコードを含む。                     |

各ベース*タグ*は、機能を追加または変更する亜種があります:

| タグ亜種          | 説明                                                                              |
| ---               | ---                                                                               |
| *`tag`*`-gpu`     | GPUサポートの指定された*tag*リリース。 ([以下参照](#gpu_support))                 |
| *`tag`*`-py3`     | Python3サポートの指定された*tag*リリース。                                        |
| *`tag`*`-jupyter` | Jupyter付きの指定された*tag*リリース (TensorFlowのチュートリアルnotebooks含む)    |

一度に複数の亜種を使用できます。たとえば、
以下はTensorFlowリリースイメージをご使用のマシンにダウンロードします:

<pre class="devsite-click-to-copy prettyprint lang-bsh">
<code class="devsite-terminal">docker pull tensorflow/tensorflow                     # 最新の安定版リリース</code>
<code class="devsite-terminal">docker pull tensorflow/tensorflow:devel-gpu           # GPUサポート付きのnightly開発リリース</code>
<code class="devsite-terminal">docker pull tensorflow/tensorflow:latest-gpu-jupyter  # GPUサポートとJupyter付きの最新版リリース</code>
</pre>


## TensorFlowのDockerコンテナを起動する

TensorFlowの設定コンテナを起動するには、次のコマンド形式を使用します:

<pre class="devsite-terminal devsite-click-to-copy">
docker run [-it] [--rm] [-p <em>hostPort</em>:<em>containerPort</em>] tensorflow/tensorflow[:<em>tag</em>] [<em>command</em>]
</pre>

詳細については、[docker run reference](https://docs.docker.com/engine/reference/run/){:.external}を参照してください。

### CPUのみのイメージを使った例

`latest`タグ付きイメージを使ってTensorFlowのインストールを確認しましょう。
Dockerは、はじめて実行する際に新しいTensorFlowのイメージをダウンロードします:

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
docker run -it --rm tensorflow/tensorflow \
   python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
</pre>

成功: TensorFlowがインストールできました。[チュートリアル](../tutorials)を読んで始めましょう。

もう少しTensorFlowのDockerの使い方を見てみましょう。
TensorFlowで設定されたコンテナ内で `bash`シェルセッションを開始します:

<pre class="devsite-terminal devsite-click-to-copy">
docker run -it tensorflow/tensorflow bash
</pre>

コンテナ内で、`python`セッションを開始してTensorFlowをインポートすることができます。

コンテナ内の*ホスト*マシン上で開発されたTensorFlowプログラムを実行するには、
ホストディレクトリをマウントしてコンテナの作業ディレクトリを変更します。
(`-v hostDir:containerDir -w workDir`):

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
docker run -it --rm -v $PWD:/tmp -w /tmp tensorflow/tensorflow python ./script.py
</pre>

コンテナ内で作成されたファイルがホストに公開されると、アクセス権限の問題が発生する可能性があります。
通常はホストシステム上でファイルを編集するのがベストです。

Python3サポート付きのTensorFlowのnightlyビルドを使用した
[Jupyter Notebook](https://jupyter.org/){:.external}サーバーを起動してください:

<pre class="devsite-terminal devsite-click-to-copy">
docker run -it -p 8888:8888 tensorflow/tensorflow:nightly-py3-jupyter
</pre>

手順に従い、ご使用のホストのWebブラウザ内で以下のURLを開きます:
`http://127.0.0.1:8888/?token=...`


## GPUサポート

Dockerは、GPUでTensorFlowを実行するもっとも簡単な方法です。
*ホスト*マシンに必要なのは
[NVIDIA® GPUドライバー](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver){:.external}だけです。
(*NVIDIA® CUDA® Toolk*をインストールする必要はありません)

NVIDIA® GPUをサポートするDockerコンテナを起動するには、
[nvidia-docker](https://github.com/NVIDIA/nvidia-docker){:.external}をインストールしてください。
`nvidia-docker`はLinuxでのみ利用可能です。詳細は、
[プラットフォームサポートFAQ](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#platform-support){:.external}
を参照してください。

GPUが利用可能か確認します:

<pre class="devsite-terminal devsite-click-to-copy">
lspci | grep -i nvidia
</pre>

`nvidia-docker`がインストールされたことを確認してください:

<pre class="devsite-terminal devsite-click-to-copy">
docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi
</pre>

注: `nvidia-docker` v1は`nvidia-docker`エイリアスを使います。v2は `docker --runtime=nvidia`を使用します。

### GPUが有効なイメージを使った例

GPU対応のTensorFlowのイメージをダウンロードして実行します（数分かかる場合があります）。

<pre class="devsite-terminal devsite-click-to-copy prettyprint lang-bsh">
docker run --runtime=nvidia -it --rm tensorflow/tensorflow:latest-gpu \
   python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
</pre>

GPU対応のイメージの設定にはしばらく時間がかかる場合があります。
GPUベースのスクリプトを繰り返し実行する場合は、`docker exec`を使ってコンテナを再利用できます。

コンテナ内で`bash`シェルセッションを開始するために、最新のTensorFlowのGPUイメージを使用してください:

<pre class="devsite-terminal devsite-click-to-copy">
docker run --runtime=nvidia -it tensorflow/tensorflow:latest-gpu bash
</pre>

成功: TensorFlowがインストールできました。[チュートリアル](../tutorials)を読んで始めましょう。
