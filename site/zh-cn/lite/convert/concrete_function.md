# 生成一个具体函数

为了将 TensorFlow 2.0 的模型转换成 TensorFlow Lite，模型需要转换成有具体的函数。这篇文档将会阐述什么是具体的函数以及如何根据现有的模型生成函数。

[TOC]

## 背景

在 TensorFlow 2.0 中，在一般情况下是优先执行的。TensorFlow 的优先执行是一个命令式的编程环境，可以立即执行评估操作，并且无需建立图形。评估操作会返回具体值，而不是在后续运行所构建的计算图形。一份关于优先执行的详细指南[此处获取](https://github.com/tensorflow/docs/blob/master/site/en/r2/guide/eager.ipynb)。

虽然通过执行优先执行将会使得开发环境和调试更加具有互动性，但是它却不允许部署在设备上。`tf.function` API接口可以将模型作为图片保存，这需要在 TensorFlow Lite 2.0 版本中运行。包含在  `tf.function` 装饰器中的所有操作都可以导出为图形，然后可以将其转换成 TensorFlow Lite FlatBuffer 的格式。

## 术语

本文档后续中用到的一些术语。

* **签名** - 输入和输出的一组操作。
* **具体函数** - 具有一个签名的图表。
* **多态函数** - Python 可以调用封装了几个具体函数图的API。

## 方法

这一部分描述了如何生成一个具体函数。

### 使用 `tf.function` 注释函数

使用 `tf.function` 注释函数会生成包含这些操作的*多态函数*。所有未使用 `tf.function` 注释的操作都将通过优先执行进行评估。以下示例显示了如何使用 `tf.function`。

```python
@tf.function
def pow(x):
  return x ** 2
```

```python
tf.function(lambda x : x ** 2)
```

### 创建要保存的对象

`tf.function` 可以选择存储为 `tf.Module` 对象的一部分。变量只能在 `tf.Module` 中定义一次。下面的示例显示了创建 `Checkpoint` 的继承类的两种不同方法。

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

### 生成具体函数

具体函数定义的图表，可以被转化成 TensorFlow Lite 的模型或者导出到 SavedModel。为了从多态函数中导出具体函数，首先需要定义签名。签名可以根据以下方式定义：

* 在 `tf.function` 中定义 `input_signature` 参数。
* 将 `tf.TensorSpec` 传递给 `get_concrete_function`：例如 `tf.TensorSpec（shape = [1]，dtype = tf.float32）`。
* 将样本输入量传递给 `get_concrete_function`：例如 `tf.constant（1。，shape = [1]）`。

下面的例子展示了如何在 `tf.function` 中`input_signature` 参数。

```python
class BasicModel(tf.Module):

  def __init__(self):
    self.const = None

  @tf.function(input_signature=[tf.TensorSpec(shape=[1], dtype=tf.float32)])
  def pow(self, x):
    if self.const is None:
      self.const = tf.Variable(2.)
    return x ** self.const

# 创建 tf.Module 对象。
root = BasicModel()

# 获取具体函数。
concrete_func = root.pow.get_concrete_function()
```

下面的示例展示了将样本输入量传递给 `get_concrete_function`。

```python
# 创建 tf.Module 对象。
root = tf.Module()
root.const = tf.Variable(2.)
root.pow = tf.function(lambda x : x ** root.const)

# 获取具体函数。
input_data = tf.constant(1., shape=[1])
concrete_func = root.pow.get_concrete_function(input_data)
```

## 示例代码

```python
import tensorflow as tf

# 初始化 tf.Module 对象。
root = tf.Module()

# 初始化变量一次。
root.var = None

# 定义一个函数，可以不用预先进行计算操作。
@tf.function
def exported_function(x):
  # 每个变量只能被定义一次。变量可以在函数中定义。
  # 但是该函数需要包含有函数外部的引用。
  if root.var is None:
    root.var = tf.Variable(tf.random.uniform([2, 2]))
  root.const = tf.constant([[37.0, -23.0], [1.0, 4.0]])
  root.mult = tf.matmul(root.const, root.var)
  return root.mult * x

# 将函数保存为 tf.function 对象的一部分。
root.func = exported_function

# 获取具体函数。
concrete_func = root.func.get_concrete_function(
  tf.TensorSpec([1, 1], tf.float32))
```

## 常见问题

### 怎么才能将一个具体函数保存为 SavedModel ？

想要在 TensorFlow 模型转换成 TensorFlow Lite 之前保存的用户应该将模型保存为 SavedModel。获取具体函数之后，调用 `tf.saved_model.save` 来保存模型。可以使用下面的指令来保存上面的例子。

```python
tf.saved_model.save(root, export_dir, concrete_func)
```

参考
[指南](https://github.com/tensorflow/docs/blob/master/site/en/r2/guide/saved_model.ipynb)
来获取保存模型的详细介绍。

### 怎么才能从 SavedModel 中获得一个具体函数？

SavedModel 中的每个具体功能都可以通过签名密钥进行标识。 默认签名密钥是`tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY`。 下面的示例显示了如何从模型中获取具体功能。

```python
model = tf.saved_model.load(export_dir)
concrete_func = model.signatures[
  tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
```

### 如何获得 `tf.Keras` 模型的具体功能？

有下面两种办法你可以使用：

1. 将模型保存为 SavedModel。在保存过程中会生成一个具体函数，可以在加载模型时访问其功能。
2. 使用 `tf.function` 注释模型，如下所示。

```python
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x=[-1, 0, 1, 2, 3, 4], y=[-3, -1, 1, 3, 5, 7], epochs=50)

# 从 Keras 模型中得到一个具体函数。
run_model = tf.function(lambda x : model(x))

# 保存函数。
concrete_func = run_model.get_concrete_function(
    tf.TensorSpec(model.inputs[0].shape, model.inputs[0].dtype))
```
