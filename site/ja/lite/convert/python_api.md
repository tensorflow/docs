# コンバータ Python API ガイド

このページでは、TensorFlow 2.0 の Python API による [TensorFlow Lite コンバータ](index.md) の使用例を説明します。

[TOC]

## Python API

TensorFlow 2.0 において、TensorFlow モデルを TensorFlow Lite に変換する Python API は `tf.lite.TFLiteConverter` です。
 `TFLiteConverter` には、元のモデルフォーマットに基づいてモデルを変換する以下のクラスメソッドがあります：

*   `TFLiteConverter.from_saved_model()`: 
    [SavedModel ディレクトリ](https://www.tensorflow.org/guide/saved_model) を変換します。
*   `TFLiteConverter.from_keras_model()`: 
    [`tf.keras` モデル](https://www.tensorflow.org/guide/keras/overview) を変換します。
*   `TFLiteConverter.from_concrete_functions()`: 
    [具象関数](concrete_function.md) を変換します。

Node: TensorFlow Lite 2.0 alpha には、 [`from_concrete_function`](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/lite/TFLiteConverter#from_concrete_function) だけを含むような、異なるバージョンの `TFLiteConverter` API があります。
このドキュメントで記述されている API は、[`tf-nightly-2.0-preview`](#installing_the_tensorflow_20_nightly_) を PIP でインストールすることで使えるようになります。


このドキュメントでは API の [使用例](＃examples) 、 [1.X と 2.0 の間の API の変更点の詳細なリスト](#differences) 、 異なるバージョンの TensorFlow で実行する [方法](#versioning) を含みます。

## 例 <a name="examples"></a>

### SavedModel を変換する <a name="saved_model"></a>

以下の例は [SavedModel](https://www.tensorflow.org/guide/saved_model) を TensorFlow Lite [`FlatBuffer`](https://google.github.io/flatbuffers/) に変換する方法を示しています。

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

以下の例は [`tf.keras` モデル](https://www.tensorflow.org/guide/keras/overview) を TensorFlow Lite [`FlatBuffer`](https://google.github.io/flatbuffers/) に変換する方法を示しています.


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

以下の例は TensorFlow の[具象関数](concrete_function.md)を TensorFlow Lite [`FlatBuffer`](https://google.github.io/flatbuffers/) に変換する方法を示しています。


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
# 現在のところは1つの関数のみをサポートしています。 複数関数の変換は開発中です
converter = tf.lite.TFLiteConverter.from_concrete_functions([concrete_func])
tflite_model = converter.convert()
```

### End-to-end な MobileNet の変換 <a name="mobilenet"></a>

以下の例は、訓練済みの `tf.keras` MobileNet モデルを TensorFlow Lite に変換して実行する方法を示しています。
また、 元の TensorFlow モデルと TensorFlow Lite モデルの結果をランダムデータで比較しています。
モデルをファイルからロードするために、 `model_content` の代わりに ` model_path` を使用します。


```python
import numpy as np
import tensorflow as tf

# MobileNet tf.keras モデルをロード
model = tf.keras.applications.MobileNetV2(
    weights="imagenet", input_shape=(224, 224, 3))

# モデルを変換
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# TFLite モデルを変換し、テンソルを割当てる
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

# 入出力テンソルを取得
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# TensorFlow Lite モデルをランダムな入力データでテスト
input_shape = input_details[0]['shape']
input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()
# `get_tensor()` はテンソルのコピーを返す
# テンソルのポインタを取得したい場合は `tensor()` を使う 
tflite_results = interpreter.get_tensor(output_details[0]['index'])

# 元の TensorFlow モデルをランダムな入力データでテスト
tf_results = model(tf.constant(input_data))

# 結果を比較
for tf_result, tflite_result in zip(tf_results, tflite_results):
  np.testing.assert_almost_equal(tf_result, tflite_result, decimal=5)
```

## 1.X から 2.0 への Python API の変更点まとめ <a name="differences"></a>

以降の章では、Python API の 1.X から 2.0 への変更点についてまとめていますが、
もしなにか懸念が生じた場合は GitHub の [issue](https://github.com/tensorflow/tensorflow/issues) を出してください。

### `TFLiteConverter` のサポートしているフォーマット

2.0の `TFLiteConverter` は 1.X と 2.0 で生成された SavedModel と Keras
モデルファイルをサポートしますが、1.X で生成された frozen `GraphDefs` はサポートしません。 frozen `GraphDefs` を
TensorFlow Lite に変換したい場合は `tf.compat.v1.lite.TFLiteConverter` を使う必要があります。

### Quantization-aware training

[quantization-aware training](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/quantize) に関連する以下の属性とメソッドは、 TensorFlow 2.0 の `TFLiteConverter` から削除されました:


*   `inference_type`
*   `inference_input_type`
*   `quantized_input_stats`
*   `default_ranges_stats`
*   `reorder_across_fake_quant`
*   `change_concat_input_ranges`
*   `post_training_quantize` - 1.X API で非推奨
*   `get_input_arrays()`

quantization-aware training をサポートしていた計算グラフの書き換え関数は、TensorFlow
2.0によるモデルをサポートしません。 また、TensorFlow Lite の quantization API は、Keras API を通じて
quantization-aware training をサポートする方向で作り直しと合理化を勧めている最中です。 新しい quantization API
がローンチされるまでは、これらの属性は 2.0 API から削除されます。 書き換え関数によってモデルを変換したい場合は
`tf.compat.v1.lite.TFLiteConverter` を使ってください。

### `TFLiteConverter` の属性に対する変更点

`target_ops` 属性は `TargetSpec` の属性となり、将来追加される予定の最適化フレームワークに合わせて `supported_ops` にリネームされました。
また、以下の属性が削除されています:

*   `drop_control_dependency` (default: `True`) - 現在のところコントロールフローは TFLite でサポートされていないので、常に `True` です。
*   _Graph visualization_ - TensorFlow 2.0 において、 TensorFlow Lite グラフの可視化で推奨されるのは [visualize.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/tools/visualize.py) を使うことです。 GraphViz と違い、 post training quantization が施された後のグラフを可視化できます。 また、グラフの可視化に関する以下の属性は削除される予定です:
    *   `output_format`
    *   `dump_graphviz_dir`
    *   `dump_graphviz_video`

### 一般的な API に対する変更点

#### 変換方法

1.X で既に非推奨となっていた以下のメソッドは、 2.0 では削除されています:

*   `lite.toco_convert`
*   `lite.TocoConverter`

#### `lite.constants`

`lite.constants` API は、 TensorFlow と TensorFlow Lite の間の重複を減らすために 2.0 で削除されました。
`lite.constant` の型と TensorFlow の型の対応は以下のとおりです。

*   `lite.constants.FLOAT`: `tf.float32`
*   `lite.constants.INT8`: `tf.int8`
*   `lite.constants.INT32`: `tf.int32`
*   `lite.constants.INT64`: `tf.int64`
*   `lite.constants.STRING`: `tf.string`
*   `lite.constants.QUANTIZED_UINT8`: `tf.uint8`

また、`lite.constants.TFLITE` と `lite.constants.GRAPHVIZ_DOT` は、 `TFLiteConverter` の `output_format` の廃止に伴い削除されました。

#### `lite.OpHint`

`OpHint` API は、2.0 API との互換性がないため、現在 2.0 では利用できません。
この API は LSTM ベースのモデルの変換を可能にするものですが、2.0 における LSTM のサポートは検証中のため、関連する `lite.experimental` API はすべて削除されています。

## TensorFlow のインストール <a name="versioning"></a>

### TensorFlow 2.0 nightly のインストール <a name="2.0-nightly"></a>

TensorFlow 2.0 nightly は以下のコマンドでインストールできます:

```
pip install tf-nightly-2.0-preview
```

### インストール済の TensorFlow 1.X から 2.0 を使う <a name="use-2.0-from-1.X"></a>

TensorFlow 2.0 は、最近の 1.X から以下のようにして利用できます。

```python
import tensorflow.compat.v2 as tf

tf.enable_v2_behavior()
```

### ソースコードからのビルド <a name="latest_package"></a>

TensorFlow Lite コンバータ Python API の最新バージョンを実行するには、 [pip](https://www.tensorflow.org/install/pip) (推奨) または [Docker](https://www.tensorflow.org/install/docker) を使用してナイトリービルドをインストールするか、[ソースから pip パッケージをビルド](https://www.tensorflow.org/install/source) してください。
