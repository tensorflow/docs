# 具象関数の生成

TensorFlow 2.0 モデルを TensorFlow Lite に変換するには、モデルを具象関数 (concrete function) としてエクスポートする必要があります。 このドキュメントでは、具象関数とは何か、既存のモデルからどのように具象関数を生成するか、について概説します。

[TOC]

## 背景

TensorFlow 2.0 では、Eager Execution がデフォルトでオンになっています。 TensorFlow において Eager Execution とは、グラフを作成せずにオペレーションを即時評価する命令型プログラミング環境のことです。各オペレーションは、後で実行するために計算グラフを構築するのではなく、具体的な値を返します。 Eager Execution に関する詳細なガイドは[こちら](https://github.com/tensorflow/docs/blob/master/site/en/guide/eager.ipynb)にあります。

Eager Execution で命令的に実行すると開発とデバッグがより対話的になりますが、デバイスへのデプロイはできなくなります。 `tf.function` API はモデルをグラフとして保存することを可能にします。 これは TensorFlow2.0 で TensorFlow Lite を実行するために必要です。 `tf.function` デコレータでラップされたオペレーションはすべてグラフとしてエクスポートできるので、 TensorFlow Lite FlatBuffer フォーマットに変換できます。

## 用語

この文書では次の用語を使用します。

*   **シグネチャ** - 一連のオペレーションの入力と出力.
*   **具象関数**  - 単一のシグネチャを持つグラフ.
*   **多相関数**  -  いくつかの具象関数グラフを1つの関数内にカプセル化した Python の呼び出し可能オブジェクト.

## 方法論

この章では、具象関数をエクスポートする方法を解説します。

### 関数に `tf.function` デコーレータを付与する

関数に `tf.function` デコレータを付与すると、その関数のオペレーションを含む *多相関数* が生成されます。 `tf.function` のデコレータが付けられていないオペレーションはすべて Eager Execution で評価されます。 以下の例は `tf.function` の使い方を示しています。

```python
@tf.function
def pow(x):
  return x ** 2
```

```python
tf.function(lambda x : x ** 2)
```

### 保存したいオブジェクトを生成する

`tf.function` は、` tf.Module` オブジェクトの一部として保存することもできます。 その際、変数は `tf.Module` 内で一度だけ定義されるべきです。 以下の例は `Checkpoint` を派生するクラスを作成するための2つの異なるアプローチを示しています。

```python
class BasicModel(tf.Module):

  def __init__(self):
    self.const = None

  @tf.function
  def pow(self, x):
    if self.const is None:
      self.const = tf.Variable(2.)
    return x ** self.const

root = BasicModel()
```

```python
root = tf.Module()
root.const = tf.Variable(2.)
root.pow = tf.function(lambda x : x ** root.const)
```

### 具象関数をエクスポートする

具象関数は、TensorFlow Lite モデルに変換したり、SavedModel にエクスポートしたりできるグラフを定義します。
多相関数から具象関数をエクスポートするには、シグネチャを定義する必要があります。
シグネチャは次のようにして定義できます。

*   `tf.function` に ` input_signature` パラメータを定義します。
*   `tf.TensorSpec` を ` get_concrete_function` に渡します: 例) `tf.TensorSpec(shape=[1], dtype = tf.float32)`
*   サンプルの入力テンソルを `get_concrete_function` に渡します: 例) `tf.constant(1., shape=[1])`

次の例は `tf.function` の ` input_signature` パラメータを定義する方法を示しています。

```python
class BasicModel(tf.Module):

  def __init__(self):
    self.const = None

  @tf.function(input_signature=[tf.TensorSpec(shape=[1], dtype=tf.float32)])
  def pow(self, x):
    if self.const is None:
      self.const = tf.Variable(2.)
    return x ** self.const

# tf.Module オブジェクトを生成
root = BasicModel()

# 具象関数を取得
concrete_func = root.pow.get_concrete_function()
```

以下の例では、サンプルの入力テンソルを `get_concrete_function` に渡しています。

```python
# tf.Module オブジェクトを生成
root = tf.Module()
root.const = tf.Variable(2.)
root.pow = tf.function(lambda x : x ** root.const)

# 具象関数を取得
input_data = tf.constant(1., shape=[1])
concrete_func = root.pow.get_concrete_function(input_data)
```

## プログラム例

```python
import tensorflow as tf

# tf.Module オブジェクトを初期化
root = tf.Module()

# 変数を一度だけインスタンス化する
root.var = None

# 演算が事前に計算されないように関数を定義
@tf.function
def exported_function(x):
  # 変数は一度だけ定義できます。変数は関数内で定義できますが、関数外の参照を含める必要があります。
  if root.var is None:
    root.var = tf.Variable(tf.random.uniform([2, 2]))
  root.const = tf.constant([[37.0, -23.0], [1.0, 4.0]])
  root.mult = tf.matmul(root.const, root.var)
  return root.mult * x

# tf.Moduleオブジェクトの一部として関数を保存
root.func = exported_function

# 具象関数を取得
concrete_func = root.func.get_concrete_function(
  tf.TensorSpec([1, 1], tf.float32))
```

## よくある質問

### 具象関数を SavedModel として保存するにはどうすればいいですか？

TensorFlow Lite に変換する前に TensorFlow モデルを保存したい場合は、 SavedModel として保存する必要があります。
具象関数を取得したあとで `tf.saved_model.save` を呼び出すことでモデルを保存できます。上述の例の場合、以下のようにして保存できます。

```python
tf.saved_model.save(root, export_dir, concrete_func)
```

SavedModel の使用方法の詳細については、[SavedModel ガイド](https://github.com/tensorflow/docs/blob/master/site/en/guide/saved_model.ipynb) を参照してください。


### SavedModel から具象関数を得るにはどうすればいいですか？

SavedModel 内の各象徴関数は、シグネチャキーによって識別できます。
デフォルトのシグネチャキーは `tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY` です。以下の例は、モデルから具象関数を取得する方法を示しています。

```python
model = tf.saved_model.load(export_dir)
concrete_func = model.signatures[
  tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
```

### `tf.Keras` モデルから具象関数を得るにはどうしたらいいですか？

方法が2つあります:

1.  モデルを SavedModel として保存します。保存処理中に具象関数が生成されるので、上述の要領でモデルをロードして具象関数を取得することができます。
2.  下記のようにモデルを `tf.function` でラップします。


```python
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x=[-1, 0, 1, 2, 3, 4], y=[-3, -1, 1, 3, 5, 7], epochs=50)

# 具象関数を Keras モデルから取得
run_model = tf.function(lambda x : model(x))

# 具象関数を保存
concrete_func = run_model.get_concrete_function(
    tf.TensorSpec(model.inputs[0].shape, model.inputs[0].dtype))
```
