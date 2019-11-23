# TensorFlow LiteをARM64基板用にビルドする

このページではTensorFlow Liteの静的ライブラリを
ARM64ベースのコンピュータ用にビルドする方法を説明します。
あなたが単にTensorFlow Liteを使ってあなたのモデルを実行したいのでしたら、
一番早いのはTensorFlow Lite実行時パッケージを
[Python quickstart](python.md)に
示したようにインストールすることです。

付記: このページで示すのは、TensorFlow Lite用のC++静的ライブラリの
コンパイル方法のみです。
代わりのインストールの選択肢としては:
(推論のためだけに)[PythonインタープリタAPIのみをインストールする](python.md);
[pipからフルのTensorFlowパッケージをインストールする](https://www.tensorflow.org/install/pip);
または[フルのTensorFlowパッケージをビルドする](
https://www.tensorflow.org/install/source)などです。

## ARM64用にクロスコンパイルする

ビルド環境が適切であることを確かめるために、私たちのTensorFlowの
Dockerイメージのうちのどれか、例えば[tensorflow/tensorflow:nightly-devel](
https://hub.docker.com/r/tensorflow/tensorflow/tags/)をお勧めします。

始めるためには、ツールチェインとライブラリ群をインストールします:

```bash
sudo apt-get update
sudo apt-get install crossbuild-essential-arm64
```

Dockerを使っている場合は、`sudo`は使えません。

そしてthe TensorFlowリポジトリ
(`https://github.com/tensorflow/tensorflow`)をgit-cloneしてください
—あなたがTensorFlowの
Dockerイメージを使っているときは、リポジトリはすでに`/tensorflow_src/`に提供されています—
そして、このスクリプトをTensorFlowリポジトリのルートで実行して
ビルドが依存するものをすべてダウンロードしてください:

```bash
./tensorflow/lite/tools/make/download_dependencies.sh
```

これは一回だけ行えばいいことに注意してください。

そしてコンパイルします:

```bash
./tensorflow/lite/tools/make/build_aarch64_lib.sh
```

これにより次にある静的ライブラリがコンパイルされます:
`tensorflow/lite/tools/make/gen/aarch64_armv8-a/lib/libtensorflow-lite.a`.

## ARM64上でネイティブコンパイルをする

これらのステップはHardKernelのOdroid C2上で、gcc version 5.4.0で確認しました。

基板にログインしてツールチェインをインストールします:

```bash
sudo apt-get install build-essential
```

そしてTensorFlowのリポジトリ
(`https://github.com/tensorflow/tensorflow`)をgit-cloneして次を
リポジトリのルートで走らせます:

```bash
./tensorflow/lite/tools/make/download_dependencies.sh
```

これは一回だけ行えばいいことに注意してください。

そしてコンパイルします:

```bash
./tensorflow/lite/tools/make/build_aarch64_lib.sh
```

これにより次にある静的ライブラリがコンパイルされます:
`tensorflow/lite/tools/make/gen/aarch64_armv8-a/lib/libtensorflow-lite.a`.
