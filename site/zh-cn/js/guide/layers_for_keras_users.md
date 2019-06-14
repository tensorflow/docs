# 用于 Keras 用户使用的 TensorFlow.js layers API

TensorFlow.js 的Layers API以Keras为模型。考虑到 JavaScript 和 Python 之间的差异，我们努力使[Layers API](https://js.tensorflow.org/api/latest/) 与Keras 类似。这让具有使用Python开发Keras模型经验的用户可以更轻松地将项目迁移到 JavaScript中的TensorFlow.js Layers。例如，以下 Keras 代码转换为 JavaScript：

```python
# Python:
import keras
import numpy as np

# 建立并编译模型.
model = keras.Sequential()
model.add(keras.layers.Dense(units=1, input_shape=[1]))
model.compile(optimizer='sgd', loss='mean_squared_error')

# 生成一些用于训练的数据.
xs = np.array([[1], [2], [3], [4]])
ys = np.array([[1], [3], [5], [7]])

# 用 fit() 训练模型.
model.fit(xs, ys, epochs=1000)

# 用 predict() 推理.
print(model.predict(np.array([[5]])))
```

```js
// JavaScript:
import * as tf from '@tensorlowjs/tfjs';

// 建立并编译模型.
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));
model.compile({optimizer: 'sgd', loss: 'meanSquaredError'});

// 生成一些用于训练的数据.
const xs = tf.tensor2d([[1], [2], [3], [4]], [4, 1]);
const ys = tf.tensor2d([[1], [3], [5], [7]], [4, 1]);

// 用 fit() 训练模型.
await model.fit(xs, ys, {epochs: 1000});

// 用 predict() 推理.
model.predict(tf.tensor2d([[5]], [1, 1])).print();
```

但是，我们希望在本文档中说明并解释一些差异。一旦理解了这些差异及其背后的基本原理，将您的程序从Python 迁移到JavaScript（或反向迁移）应该会是一种相对平稳的体验。

## 构造函数将 JavaScript 对象作为配置

比较上面示例中的以下 Python 和 JavaScript 代码：它们都创建了一个[全连接层](https://keras.io/layers/core/#dense)。

```python
# Python:
keras.layers.Dense(units=1, inputShape=[1])
```

```js
// JavaScript:
tf.layers.dense({units: 1, inputShape: [1]});
```

JavaScript函数在Python 函数中没有等效的关键字参数。我们希望避免在 JavaScript 中实现构造函数选项作为位置参数，这对于记忆和使用具有大量关键字参数的构造函数（如[LSTM](https://keras.io/layers/recurrent/#lstm)尤其麻烦 。这就是我们使用JavaScript 配置对象的原因。这些对象提供与Python关键字参数相同的位置不变性和灵活性。

Model 类的一些方法（例如，[`Model.compile()`](https://keras.io/models/model/#model-class-api)）也将 JavaScript 配置对象作为输入。但是，请记住 Model.fit()、Model.evaluate() 和 Model.predict() 略有不同。因为这些方法将强制 x（feature 特征）和 y（label 标签或 target 目标）数据作为输入；x 和 y 是与后续配置对象分开的位置参数，属于关键字参数。例如：


## Model.fit()是异步的

`Model.fit()` 是用户在Tensorflow.js中执行模型训练的主要方法。这个方法往往是长时间运行的（持续数秒或数分钟）。因此，我们利用了JavaScript语言的“异步”特性。所以在浏览器中运行时，这样使用此函数就不会阻塞主UI线程。这和JavaScript中其他可能长期运行的函数类似，例如`async`[获取](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)。需要注意`async`是一个在python中不存在的构造。当[`fit()`](https://keras.io/models/model/#model-class-api)方法在keras中返回一个历史对象, 在JavaScript中`fit()`方法的对应项返回一个包含训练历史的[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)这个应答可以[await(等待)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)，也可以与then()方法一起使用。


## TensorFlow.js 中没有 NumPy

Python Keras 用户经常使用[NumPy](http://www.numpy.org/)来执行基本的数值和数组的操作，例如在上面的示例中生成 2D 张量。

```python
# Python:
xs = np.array([[1], [2], [3], [4]])
```

在 TensorFlow.js 中，这种基本的数字的操作是使用包本身完成的。例如：

```js
// JavaScript:
const xs = tf.tensor2d([[1], [2], [3], [4]], [4, 1]);
```

该 tf.* 命名空间还提供数组和线性代数的operations（操作），如矩阵乘法。有关更多信息，请参阅 [TensorFlow.js核心文档](https://js.tensorflow.org/api/latest/)。

## 使用factory(工厂)方法，而不是构造函数

Python 中的这一行（来自上面的例子）是一个构造函数调用：

```python
# Python:
model = keras.Sequential()
```

如果严格转换为 JavaScript，则等效构造函数调用将如下所示：

```js
// JavaScript:
const model = new tf.Sequential();  // 不！ 要！ 这！ 样！ 做！ 
```

然而，我们决定不使用“new”构造函数，因为 1)“new”关键字会使代码更加膨胀；2)“new”构造函数被视为 JavaScript 的“bad part”：一个潜在的陷阱，如在[*JavaScript: the Good Parts*](http://archive.oreilly.com/pub/a/javascript/excerpts/javascript-good-parts/bad-parts.html).中的争论。要在 TensorFlow.js 中创建模型和 Layer ，可以调用被称为 lowerCamelCase（小驼峰命名）的工厂方法，例如：

```js
// JavaScript:
const model = tf.sequential();

const layer = tf.layers.batchNormalization({axis: 1});
```

## 选项字符串值为小驼峰命名，而不是 snake_case

在 JavaScript 中，与 Python 相比，更常见的是使用小驼峰作为符号名称（例如，[Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html#naming-camel-case-defined)），而 Python 中 snake_case 很常见（例如，在 Keras 中）。因此，我们决定使用小驼峰命名作为选项的字符串值，包括以下内容：

* DataFormat，例如，channelsFirst 而不是 channels_first
* Initializer，例如，glorotNormal 而不是 glorot_normal
* Loss and metrics，例如，meanSquaredError 而不是 mean_squared_error，categoricalCrossentropy 而不是 categorical_crossentropy。

例如，如上例所示：

```js
// JavaScript:
model.compile({optimizer: 'sgd', loss: 'meanSquaredError'});
```

对于模型序列化和反序列化，请放心。请放心。TensorFlow.js 的内部机制确保正确处理 JSON 对象中的 snake_case ，例如，从 Python Keras 加载预训练模型时。


## 使用 apply() 运行 Layer 对象，而不是将其作为函数调用

在 Keras 中，Layer 对象定义了`__call__`方法。因此，用户可以通过将对象作为函数调用来调用 Layer 的逻辑，例如:

```python
# Python:
my_input = keras.Input(shape=[2, 4])
flatten = keras.layers.Flatten()

print(flatten(my_input).shape)
```

这个 Python 语法糖在 TensorFlow.js 中以 apply() 方法实现：

```js
// JavaScript:
const myInput = tf.input{shape: [2, 4]});
const flatten = tf.layers.flatten();

console.log(flatten.apply(myInput).shape);
```

## Layer.apply() 支持对具体 Tensor（张量）的命令式（Eager）执行

目前，在 Keras 中，`__call__`方法只能对（Python）TensorFlow 的 `tf.Tensor` 对象进行操作（假设 TensorFlow 是后端），这些对象是符号化的并且不包含实际的数值。这就是上一节中的示例中所显示的内容。但是，在 TensorFlow.js 中，Layer 的  `apply()` 方法可以在符号和命令模式下运行。如果用 SymbolicTensor 调用 `apply()`（类似于 tf.Tensor）调用，则返回值将为 SymbolicTensor。这通常发生在模型构建期间。但是如果用实际的具体 Tensor（张量）值调用  `apply()`，将返回一个具体的 Tensor（张量）。例如：

```js
// JavaScript:
const flatten = tf.layers.flatten();

flatten.apply(tf.ones([2, 3, 4])).print();
```

这个特性让人联想到（Python）TensorFlow 的[Eager Execution](https://www.tensorflow.org/guide/eager)。它在模型开发期间提供了更大的交互性和可调试性，并且为组成动态神经网络打开了大门。

## Optimizers（优化器）在 train.* 下，而不是 optimizers.*

在 Keras 中，Optimizer（优化器）对象的构造函数位于 keras.optimizers.* 命名空间下。在 TensorFlow.js Layer 中，Optimizer（优化器）的工厂方法位于 tf.train.* 命名空间下。例如：

```python
# Python:
my_sgd = keras.optimizers.sgd(lr=0.2)
```

```js
// JavaScript:
const mySGD = tf.train.sgd({lr: 0.2});
```

## loadLayersModel() 从 URL 加载，而不是 HDF5 文件

在 Keras 中，模型通常[保存](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model)为 HDF5（.h5）文件，然后可以使用 `keras.models.load_model()`方法加载 。该方法采用 .h5 文件的路径。TensorFlow.js 中的 load_model() 对应的是[`tf.loadLayersModel()`](https://js.tensorflow.org/api/latest/#loadLayersModel)。由于 HDF5 文件格式对浏览器并不友好，因此 tf.loadLayersModel() 采用 TensorFlow.js 特定的格式。tf.lloadLayersModel() 将 model.json 文件作为其输入参数。可以使用 tensorflowjs 的 pip 包从 Keras HDF5 文件转换 model.json。

```js
// JavaScript:
const model = await tf.loadLayersModel('https://foo.bar/model.json');
```

还要注意的是`tf.loadLayersModel()`返回的是[`tf.Model`](https://js.tensorflow.org/api/latest/#class:Model)的[应答`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)。

通常，tf.Model在 TensorFlow.js中保存和加载分别使用`tf.Model.save`和`tf.loadLayersModel`方法。我们将这些 API 设计为类似于Keras[the save and load_model API](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model)。但是浏览器环境与 Keras 等主要深度学习框架运行的后端环境完全不同，特别是用于持久化和传输数据的路由数组中。因此，TensorFlow.js 和 Keras 中的 save/load API 之间存在一些有趣的差异。有关更多详细信息，请参阅我们关于 [保存和加载tf.Model](./save_load.md)的教程。

## 用`fitDataset()`训练模型使用`tf.data.Dataset`对象

在python版本的tensorflow keras中， 一个模型可以使用[Dataset](https://www.tensorflow.org/guide/datasets)对象进行训练。模型的`fit()`方法直接接受这样的对象。一个Tensorflow.js方法可以使用相当于Dataset对象的Javascript进行训练，详见[TensorFlow.js的tf.data API文档](https://js.tensorflow.org/api/latest/#Data)。然而，与python不同， 基于Dataset的训练是通过一个专门的方法来完成的这个方法称之为[fitDataset](https://js.tensorflow.org/api/0.15.1/#tf.Model.fitDataset)。[fit()](https://js.tensorflow.org/api/latest/#tf.Model.fitDataset) 只针对基于Tensor(张量)的模型训练。

## Layer(层)对象和Model(模型)对象的内存管理

TensorFlow.js在浏览器中的WebGL上运行，其中层和模型对象的权重由WebGL纹理支持。然而WebGL并不支持内置的垃圾收集。在推理和训练的过程中，Layer(层)和Model(模型)对象为用户在内部管理Tensor(张量)内存。但是它们也允许用户清理它们以释放它们占用的WebGL内存。这对于在单页加载过程中创建和释放许多模型实例的情况很有用。想要清理一个Layer(层)和Model(模型)对象，使用`dispose()` 方法。
