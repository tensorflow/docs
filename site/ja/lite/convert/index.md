# TensorFlow Lite コンバーター

TensorFlow Lite コンバーターは TensorFlow モデルを入力として、TensorFlow Lite [`FlatBuffer`](https://google.github.io/flatbuffers/) ファイルを生成します.

コンバーターは [SavedModel directories](https://www.tensorflow.org/alpha/guide/saved_model)、 [`tf.keras` models](https://www.tensorflow.org/alpha/guide/keras/overview)、 [concrete functions](concrete_function.md) をサポートしています.

Note: このページは TensorFlow 2.0 のコンバータAPIに関するドキュメントです。TensorFlow 1.X のAPIについては [こちら](https://www.tensorflow.org/lite/convert/) をご覧ください.

## デバイスへのデプロイ

TensorFlow Lite `FlatBuffer` ファイルは、クライアントデバイス(モバイルデバイスや組み込みデバイス)にデプロイし、TensorFlow Lite インタープリターを利用してローカルで実行できます. この変換プロセスは下図のとおりです.

![TFLite converter workflow](../images/convert/workflow.svg)

## モデルを変換する

TensorFlow Lite コンバーターは [Python API](python_api.md) を使うべきです. Python API を使うことで、モデルの変換をデプロイパイプラインの中に組み込むことが簡単になり、[互換性](../../guide/ops_compatibility.md) の問題に早い段階で対処しやすくなります.

代わりの方法として [コマンドラインツール](cmdline.md) を使って基本的なモデルを変換することもできます.

