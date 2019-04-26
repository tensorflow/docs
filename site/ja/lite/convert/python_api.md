# コンバーター Python API ガイド

このページでは、TensorFlow 2.0でPython API による [TensorFlow Lite コンバーター](TensorFlow Lite converter)の使用例を説明します.

[TOC]

## Python API

TensorFlow 2.0において、TensorFlowモデルをTensorFlow Liteに変換するのPython APIは `tf.lite.TFLiteConverter`です.
 `TFLiteConverter`には、元のモデルフォーマットに基づいてモデルを変換する以下のクラスメソッドがあります：

*   `TFLiteConverter.from_saved_model()`: 
    [SavedModel ディレクトリ](https://www.tensorflow.org/alpha/guide/saved_model) を変換します.
*   `TFLiteConverter.from_keras_model()`: 
    [`tf.keras` モデル](https://www.tensorflow.org/alpha/guide/keras/overview) を変換します.
*   `TFLiteConverter.from_concrete_functions()`: 
    [concrete functions](concrete_function.md) を変換します.

このドキュメントではAPIの[使用例](＃examples)、[1.X と 2.0 の間のAPIの変更点の詳細なリスト](#differences)、TensorFlowの異なるバージョンで実行する[方法](#versioning)を含みます.

## 例 <a name="examples"></a>

### SavedModelを変換する <a name="saved_model"></a>

以下の例は[SavedModel](https://www.tensorflow.org/alpha/guide/saved_model) を TensorFlow Lite [`FlatBuffer`](https://google.github.io/flatbuffers/) に変換する方法を示しています.

```python
import tensorflow as tf

# 基本的な関数を構築
root = tf.train.Checkpoint()
root.v1 = tf.Variable(3.)
root.v2 = tf.Variable(2.)
root.f = tf.function(lambda x: root.v1 * root.v2 * x)

# モデルを保存
export_dir = "/tmp/test_saved_model"
input_data = tf.constant(1., shape=[1, 1])
to_save = root.f.get_concrete_function(input_data)
tf.saved_model.save(root, export_dir, to_save)

# モデルを変換
converter = tf.lite.TFLiteConverter.from_saved_model(export_dir)
tflite_model = converter.convert()
```

### Keras モデルを変換する <a name="keras"></a>

以下の例は[`tf.keras` model](https://www.tensorflow.org/alpha/guide/keras/overview)を TensorFlow Lite [`FlatBuffer`](https://google.github.io/flatbuffers/) に変換する方法を示しています.


```python
import tensorflow as tf

# シンプルな Keras モデルを構築
x = [-1, 0, 1, 2, 3, 4]
y = [-3, -1, 1, 3, 5, 7]

model = tf.keras.models.Sequential(
    [tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x, y, epochs=50)

# モデルを変換
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
```

### 具象関数を変換する <a name="concrete_function"></a>

以下の例は TensorFlow[具象関数](concrete_function.md) をTensorFlow Lite [`FlatBuffer`](https://google.github.io/flatbuffers/) に変換する方法を示しています.


```python
import tensorflow as tf

# 基本的な関数を構築
root = tf.train.Checkpoint()
root.v1 = tf.Variable(3.)
root.v2 = tf.Variable(2.)
root.f = tf.function(lambda x: root.v1 * root.v2 * x)

# 具象関数を生成
input_data = tf.constant(1., shape=[1, 1])
concrete_func = root.f.get_concrete_function(input_data)

# モデルを変換
#
# `from_concrete_function` は具象関数のリストを引数に取りますが、
# 現在のところは1つの関数のみをサポートしています. 複数関数の変換は開発中です
converter = tf.lite.TFLiteConverter.from_concrete_functions([concrete_func])
tflite_model = converter.convert()
```

### End-to-end な MobileNet の変換 <a name="mobilenet"></a>

以下の例は、事前に訓練された `tf.keras` MobileNetモデルをTensorFlow Liteに変換して実行する方法を示しています.
また、 元のTensorFlowモデルとTensorFlow Liteモデルの結果をランダムデータで比較しています.
モデルをファイルからロードするために、 `model_content`の代わりに` model_path`を使用しています.


```python
import numpy as np
import tensorflow as tf

# MobileNet tf.keras モデルをロード.
model = tf.keras.applications.MobileNetV2(
    weights="imagenet", input_shape=(224, 224, 3))

# モデルを変換.
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# TFLite モデルを変換し、テンソルを割当て
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

# 入出力テンソルを取得.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# TensorFlow Lite モデルをランダムな入力データでテスト
input_shape = input_details[0]['shape']
input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()
tflite_results = interpreter.get_tensor(output_details[0]['index'])

# 元の TensorFlow モデルをランダムな入力データでテスト
tf_results = model(tf.constant(input_data))

# 結果を比較
for tf_result, tflite_result in zip(tf_results, tflite_results):
  np.testing.assert_almost_equal(tf_result, tflite_result, decimal=5)
```

## 1.Xと2.0の間のPython APIの変更のまとめ <a name="differences"></a>

以降の章では、Python APIの1.Xから2.0への変更点についてまとめていますが、
もしなにか懸念が生じた場合は[GitHubのissue](https://github.com/tensorflow/tensorflow/issues)を出してください.

### `TFLiteConverter`のサポートしているフォーマット

2.0の `TFLiteConverter`は1.Xと2.0の両方で生成されたSavedModelとKerasモデルファイルをサポートしていますが、
1.Xで生成されたfrozen `GraphDefs`はサポートしていません.
frozen `GraphDefs`をTensorFlow Liteに変換したい場合は` tf.compat.v1.TFLiteConverter`を使う必要があります.


### Quantization-aware training

以下の、[quantization-aware training](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/quantize) に関連する属性とメソッドは、TensorFlow 2.0の `TFLiteConverter`から削除されました:


*   `inference_type`
*   `inference_input_type`
*   `quantized_input_stats`
*   `default_ranges_stats`
*   `reorder_across_fake_quant`
*   `change_concat_input_ranges`
*   `post_training_quantize` - Deprecated in the 1.X API
*   `get_input_arrays()`

quantization-aware training をサポートしていた計算グラフの書き換えは、TensorFlow 2.0によるモデルをサポートしません.
さらに、TensorFlow Liteの quantization API は、Keras API通じて quantization-aware training をサポートする方向で作り直されて合理化されている最中です.新しい quantization APIがローンチされるまでは、これらの属性は2.0 APIから削除されます.
リライタ関数によってモデルを変換したい場合は `tf.compat.v1.TFLiteConverter`を使うことができます.

### `TFLiteConverter` の属性に対する変更点

`target_ops` 属性は `TargetSpec` 型となり、将来追加される予定の最適化フレームワークに合わせて `supported_ops` にリネームされました.
更に、以下の属性が削除されています:

*   `drop_control_dependency` (default: `True`) - 現在のところコントロールフローはTFLiteでサポートされていないので、常に `True` です.
*   _Graph visualization_ - TensorFlow 2.0 において、 TensorFlow Lite グラフの可視化で推奨されるのは　
    [visualize.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/tools/visualize.py) を使うことです.
    GraphViz と違い、 post training quantization が施された後のグラフを可視化できます.グラフの可視化に関する以下の属性は削除される予定です:
    *   `output_format`
    *   `dump_graphviz_dir`
    *   `dump_graphviz_video`

### 一般的な API に対する変更点

#### 変換方法


4310/5000
次のセクションでは、Python APIの1.Xから2.0への変更点について要約します。いずれかの変更で懸念が生じた場合は、GitHubの問題（https://github.com/tensorflow/tensorflow/issues）を提出してください。

### `TFLiteConverter`がサポートしているフォーマット

2.0の `TFLiteConverter`は1.Xと2.0の両方で生成されたSavedModelとKerasモデルファイルをサポートします。しかしながら、変換プロセスは1.Xで生成された凍結された `GraphDefs`をもはやサポートしません。凍結した `GraphDefs`をTensorFlow Liteに変換したいユーザーは` tf.compat.v1.TFLiteConverter`を使うべきです。

###量子化を意識したトレーニング

以下の属性と量子化を意識したトレーニングに関連するメソッドはTensorFlow 2.0の `TFLiteConverter`から削除されました：

* `inference_type`
* `inference_input_type`
* `quantized_input_stats`
* `default_ranges_stats`
* `reorder_across_fake_quant`
* `change_concat_input_ranges`
* `post_training_quantize`  -  1.X APIでは推奨されていません
* `get_input_arrays（）`

量子化対応トレーニングをサポートするリライタ機能は、TensorFlow 2.0によって生成されたモデルをサポートしません。さらに、TensorFlow Liteの量子化APIは、Keras APIを介した量子化対応トレーニングをサポートする方向に作り直され、合理化されています。新しい量子化APIが起動されるまで、これらの属性は2.0 APIで削除されます。リライタ関数によって生成されたモデルを変換したいユーザは `tf.compat.v1.TFLiteConverter`を使うことができます。

### `TFLiteConverter`属性への変更

`target_ops`属性は` TargetSpec`の属性となり、最適化フレームワークへの将来の追加に合わせて `supported_ops`に改名されました。

さらに、次の属性が削除されました。

* `drop_control_dependency`（デフォルト：` True`） - 制御フローは現在ありません
    TFLiteによってサポートされているので、それは常に `True`です。
* _Graph visualization_  - を視覚化するための推奨アプローチ
    TensorFlow 2.0のTensorFlow Liteグラフは使用することになります
    [visualize.py]（https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/tools/visualize.py）。
    GraphVizとは異なり、ユーザーはトレーニング後の量子化が行われた後にグラフを視覚化できます。グラフの視覚化に関連する次の属性は削除されます。
    * `output_format`
    * `dump_graphviz_dir`
    * `dump_graphviz_video`

###一般的なAPIの変更

####変換方法

1.Xで既にdeprecatedとなっていた以下のメソッドは、2.0では削除されています:

*   `lite.toco_convert`
*   `lite.TocoConverter`

#### `lite.constants`

TensorFlowとTensorFlow Liteの間の重複を減らすために `lite.constants` APIは2.0で削除されました.
`lite.constant`型とTensorFlow型の対応は以下のとおりです.

*   `lite.constants.FLOAT`: `tf.float32`
*   `lite.constants.INT8`: `tf.int8`
*   `lite.constants.INT32`: `tf.int32`
*   `lite.constants.INT64`: `tf.int64`
*   `lite.constants.STRING`: `tf.string`
*   `lite.constants.QUANTIZED_UINT8`: `tf.uint8`

更に、`lite.constants.TFLITE` と `lite.constants.GRAPHVIZ_DOT` は、
`TFLiteConverter` の `output_format` の廃止に伴い削除されました.

#### `lite.OpHint`

`OpHint` APIは、2.0 APIとの互換性がないため、現在2.0では利用できません.
このAPIはLSTMベースのモデルの変換を可能にするものですが、2.0におけるLSTMのサポートは検証中のため、
関連する `lite.experimental` APIはすべて削除されています.

The `OpHint` API is currently not available in 2.0 due to an incompatibility
with the 2.0 APIs. This API enables conversion of LSTM based models. Support for
LSTMs in 2.0 is being investigated. All related `lite.experimental` APIs have
been removed due to this issue.

## TensorFlow のインストール <a name="versioning"></a>

### TensorFlow 2.0 nightly のインストール <a name="2.0-nightly"></a>

TensorFlow 2.0 nightly は以下のコマンドでインストールできます:

```
pip install tf-nightly-2.0-preview
```

### インストール済の TensorFlow 1.X から 2.0 を使う <a name="use-2.0-from-1.X"></a>

TensorFlow 2.0 は、最近の 1.X から以下のようにして利用することができます

```python
import tensorflow.compat.v2 as tf

tf.enable_v2_behavior()
```

### ソースコードからのビルド <a name="latest_package"></a>

TensorFlow LiteコンバータPython APIの最新バージョンを実行するには、[pip](https://www.tensorflow.org/install/pip)（推奨）または[Docker]（https://www.tensorflow.org/install/docker）を使用してナイトリービルドをインストールするか、[ソースからpipパッケージをビルド]（https://www.tensorflow.org/install/source）してください.
