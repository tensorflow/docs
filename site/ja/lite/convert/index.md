# TensorFlow Lite コンバータ

TensorFlow Lite コンバータは、 TensorFlow モデルを入力として TensorFlow Lite [`FlatBuffer`](https://google.github.io/flatbuffers/) ファイルを生成します。

コンバータは [SavedModel ディレクトリ](https://www.tensorflow.org/guide/saved_model)、
[`tf.keras` モデル](https://www.tensorflow.org/guide/keras/overview)、
[具象関数](https://tensorflow.org/guide/concrete_function) をサポートしています。

Note: このページは TensorFlow 2.0 のコンバータ API に関するドキュメントです。TensorFlow 1.X の API については [こちら](https://www.tensorflow.org/lite/convert/) をご覧ください。

## デバイスへのデプロイ

TensorFlow Lite `FlatBuffer` ファイルは、クライアントデバイス（モバイルデバイスや組み込みデバイス）にデプロイし、TensorFlow Lite インタープリタを使ってローカルで実行できます。この変換プロセスは下図のとおりです。

![TFLite converter workflow](../images/convert/workflow.svg)

## モデルを変換する

TensorFlow Lite コンバータは [Python API](python_api.md) を使うべきです。
Python API を使うことで、モデルの変換をデプロイパイプラインの中に組み込むことが簡単になり、[互換性](../../guide/ops_compatibility.md) の問題に早い段階で対処しやすくなります。

代わりの方法として [コマンドラインツール](cmdline.md) を使って基本的なモデルを変換することもできます。
