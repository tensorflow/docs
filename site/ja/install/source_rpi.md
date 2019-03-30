# Raspberry Pi用にソースからビルドする

このガイドは
[Raspbian 9.0](https://www.raspberrypi.org/downloads/raspbian/){:.external}を実行する
[Raspberry Pi](https://www.raspberrypi.org/){:.external}デバイスにTensorFlowパッケージをビルドします。

この手順は他のRaspberry Piの亜種でも機能するかもしれませんが、
この構成でのみテストおよびサポートされています。

TensorFlow Raspbianパッケージの*クロスコンパイル*をおすすめします。
クロスコンパイルは、パッケージのビルドにデプロイとは異なるプラットフォームを使用しています。
Raspberry Piの限られたRAMと比較的遅いプロセッサーを使用する代わりに、
Linux、macOS、またはWindowsを実行している、より強力なホストマシン上でTensorFlowをビルドする方が簡単です。

注: Raspbianシステム用に、十分にテストされたビルド済みの[TensorFlow packages](./pip.md)をすでに提供しています。


## ホスト用にセットアップする

### Dockerをインストールする

依存関係の管理を簡単にするために、ビルドスクリプトは
[Docker](https://docs.docker.com/install/){:.external}を使ってコンパイル用の仮想Linux開発環境を作成します。
以下を実行してDockerがインストールされていることを確認します:
`docker run --rm hello-world`

### TensorFlowのソースコードをダウンロードする

[Git](https://git-scm.com/){:.external}を使って
[TensorFlow repository](https://github.com/tensorflow/tensorflow){:.external}をcloneしてください:

<pre class="devsite-click-to-copy">
<code class="devsite-terminal">git clone https://github.com/tensorflow/tensorflow.git</code>
<code class="devsite-terminal">cd tensorflow</code>
</pre>

レポジトリのデフォルトは `master` 開発ブランチです。
[release branch](https://github.com/tensorflow/tensorflow/releases){:.external}をcheckoutしてビルドすることもできます:

<pre class="devsite-terminal prettyprint lang-bsh">
git checkout <em>branch_name</em>  # r1.9, r1.10, etc.
</pre>

ポイント: 最新の開発ブランチでビルドの問題が発生している場合は、
動作が確認されているreleaseブランチを試してください。


## ソースからビルドする

Raspberry 2と3のデバイス上で動作する
ARMv7 [NEON instructions](https://developer.arm.com/technologies/neon){:.external}
とともにPythonの*pip*パッケージをビルドするため、TensorFlowのソースコードをクロスコンパイルします。
ビルドスクリプトはコンパイルのためにDockerコンテナを起動します。
ターゲットパッケージとしてPython 3とPython 2.7のどちらかを選択してください:

<div class="ds-selector-tabs">
  <section>
    <h3>Python 3</h3>
<pre class="devsite-terminal prettyprint lang-bsh">
CI_DOCKER_EXTRA_PARAMS="-e CI_BUILD_PYTHON=python3 -e CROSSTOOL_PYTHON_INCLUDE_PATH=/usr/include/python3.4" \\
    tensorflow/tools/ci_build/ci_build.sh PI-PYTHON3 \\
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh
</pre>
  </section>
  <section>
    <h3>Python 2.7</h3>
<pre class="devsite-terminal prettyprint lang-bsh">
tensorflow/tools/ci_build/ci_build.sh PI \\
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh
</pre>
  </section>
</div><!--/ds-selector-tabs-->

Pi 1とZeroを含むすべてのRaspberry Piデバイスをサポートするパッケージをビルドするには、
`PI_ONE`引数を渡します。例えば:

<pre class="devsite-terminal prettyprint lang-bsh">
tensorflow/tools/ci_build/ci_build.sh PI \
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh PI_ONE
</pre>

ビルドが完了すると(〜30分)、`.whl`パッケージファイルがホストのソースツリーの
output-artifactsディレクトリーに作成されます。
wheelファイルをRaspberry Piにコピーして、`pip`を使ってインストールします:

<pre class="devsite-terminal devsite-click-to-copy">
pip install tensorflow-<var>version</var>-cp34-none-linux_armv7l.whl
</pre>

成功: TensorFlowをRaspian上にインストールできました。
