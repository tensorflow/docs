# 模型和层

机器学习中，一个 _model_ 是一个带有可训练[参数](https://developers.google.com/machine-learning/glossary/#parameter)的函数。这个函数将输入转化为输出。通俗的来说，这个函数表达了输入和输出之间的变换关系。我们通过在数据集上训练模型来获得最佳参数。训练好的模型可以精确的将输入数据转换为我们想得到的输出。

TensorFlow.js有两种创建机器学习的方法：

1.  用 Layers API（用 _layers_ 来创建模型）
2.  用 Core API（底端算子，例如 `tf.matMul()`或`tf.add()`等）来建立模型

我们首先会用高层API：Layers API来建立模型。然后，我们会展示如何用Core API来搭建相同的模型。

## 用Layers API创建模型

Layers API有两种方式创建模型：第一种是创建 _sequential_ 模型，第二种是创建 _functional_ 模型。下面两段会分别解释这两种模型创建方式。

### 使用sequential model

最常见的模型是<code>[Sequential](https://js.tensorflow.org/api/0.15.1/#class:Sequential)</code>模型。Sequential模型将网络的每一层简单的叠在一起。您可以将需要的层按顺序写在一个列表里，然后将列表作为<code>[sequential()](https://js.tensorflow.org/api/0.15.1/#sequential)</code> 函数的输入：

```js
const model = tf.sequential({
 layers: [
   tf.layers.dense({inputShape: [784], units: 32, activation: 'relu'}),
   tf.layers.dense({units: 10, activation: 'softmax'}),
 ]
});
```

或用 `add()` 方法：

```js
const model = tf.sequential();
model.add(tf.layers.dense({inputShape: [784], units: 32, activation: 'relu'}));
model.add(tf.layers.dense({units: 10, activation: 'softmax'}));
```

> 注意：模型的第一层需要“输入形状”参数（`inputShape`）。不要在“输入型状”中包含batch size（批次大小）。假设您要向模型输入一个形状为`[B, 784]`的张量（`B`是任意batch size），您只需要将“输入型状”设为`[784]`。

您可以通过`model.layers`来使用模型中的每一层。例如，您可以用`model.inputLayers`和`model.outputLayers`来调用输入层和输出层。

### 使用functional model

我们也可以通过`tf.model()`来创建`LayersModel`。`tf.model()`和`tf.sequential()`的主要区别为，您可以用`tf.model()`来创建任何非闭环的计算图。

以下是一段如何用`tf.model()` API 建立和上文相同模型的列子：

```js
// 用apply()方法创建任意计算图
const input = tf.input({shape: [784]});
const dense1 = tf.layers.dense({units: 32, activation: 'relu'}).apply(input);
const dense2 = tf.layers.dense({units: 10, activation: 'softmax'}).apply(dense1);
const model = tf.model({inputs: input, outputs: dense2});
```

我们在每一层用`apply()`将上一层的输出作为本层的输入。`apply()`返回一个`SymbolicTensor`（类似于张量，但不包含任何数值）

不同于sequential model使用`inputShape`来定义第一层的输入，我们用`tf.input()`创建的`SymbolicTensor`作为第一层的输入

如果您向`apply()`输入一个数值张量，它会进行计算并返还一个数值张量：

```js
const t = tf.tensor([-2, 1, 0, 5]);
const o = tf.layers.activation({activation: 'relu'}).apply(t);
o.print(); // [0, 1, 0, 5]
```

这个方式适用于单独测试每一层并检查它们的输出。

和sequential model一样，您可以通过`model.layers`来使用模型中的每一层。例如，您可以用`model.inputLayers`和`model.outputLayers`来调用输入层和输出层。

## 验证

Sequential model和functional model都属于`LayersModel`类。使用`LayersModels`让验证更方便：它要求您定义输入形状，并用您定义的形状来验证您对模型的输入。`LayersModel`会自动计算模型中所有张量的形状。知道张量的形状后，模型就可以自动创建它所需要的参数。您也可以用形状信息来判断两层相邻的层是否相互兼容。

## 模型总览

使用`model.summary()`可以显示很多模型的重要信息，包括：

*   每一层的名字和类型
*   每一层的输出形状
*   每一层的权重数量
*   每一层的输入
*   一个模型拥有的可训练参数总量，和不可训练参数总量

用前面定义的模型来做例子，我们可以在命令行中得到以下信息：

<table>
  <tr>
   <td>Layer (type)
   </td>
   <td>Output shape
   </td>
   <td>Param #
   </td>
  </tr>
  <tr>
   <td>dense_Dense1 (Dense)
   </td>
   <td>[null,32]
   </td>
   <td>25120
   </td>
  </tr>
  <tr>
   <td>dense_Dense2 (Dense)
   </td>
   <td>[null,10]
   </td>
   <td>330
   </td>
  </tr>
  <tr>
   <td colspan="3" >Total params: 25450<br/>Trainable params: 25450<br/> Non-trainable params: 0
   </td>
  </tr>
</table>

注意：每一层的输出形状中都含有`null`值。模型的输入形状包含了批次大小，而批次大小是可以灵活更变的，所以批次的值在张量形状中以`null`显示。

## 序列化

相对于底端API而言，使用`LayersModel`的另一个好处是方便存储、加载模型。`LayersModel`包含如下信息：

*   可用于重建模型的模型架构信息
*   模型的权重
*   训练配置（例如损失函数，优化器和评估方式）
*   优化器的状态（可用于继续训练模型）

存储和加载模型只需要一行代码：

```js
const saveResult = await model.save('localstorage://my-model-1');
const model = await tf.loadLayersModel('localstorage://my-model-1');
```

在这个例子中，模型被存储在浏览器的本地存储里。请访问<code>[model.save()](https://js.tensorflow.org/api/latest/#tf.Model.save)</code>和[save and load](save_load.md)了解如何把模型保存在不同的媒介中（例如 file storage, <code>IndexedDB</code>, 触发下载到浏览器等等）。

## 自定义层

层是创建模型的基础。如果您的模型需要定制化计算模块，您可以写一个自定义层并插入模型中。下面的例子是一个计算平方和的自定义层：

```js
class SquaredSumLayer extends tf.layers.Layer {
 constructor() {
   super({});
 }
 // In this case, the output is a scalar.
 computeOutputShape(inputShape) { return []; }

 // call() is where we do the computation.
 call(input, kwargs) { return input.square().sum();}

 // Every layer needs a unique name.
 getClassName() { return 'SquaredSum'; }
}
```

可以用`apply()`方法在一个张量上测试这个自定义层

```js
const t = tf.tensor([-2, 1, 0, 5]);
const o = new SquaredSumLayer().apply(t);
o.print(); // prints 30
```

> 注意：如果您在模型中包含了自定义层，模型将不能序列化

## 用Core API创建模型

本文开头提到了两种在TensorFlow.js中建立模型的方法。最常用的方式是使用 Layers API，因为它的模式是基于广泛应用的Keras API（详情见 [best practices and reduces cognitive load](https://keras.io/why-use-keras/)）。Layers API提供了大量方便的工具，例如权重初始化，模型序列化，训练监测，可迁移性和安全检查。

当您遇到如下情况时，可能会需要使用Core API：

*   您需要更多灵活性和控制
*   您不需要序列化或可以创造自己的序列化方法

用Core API写的模型包含了一系列的函数。这些函数以一个或多个张量作为输入，并输出另一个张量。我们可以用Core API来重写之前定义的模型：

```js
// The weights and biases for the two dense layers.
const w1 = tf.variable(tf.randomNormal([784, 32]));
const b1 = tf.variable(tf.randomNormal([32]));
const w2 = tf.variable(tf.randomNormal([32, 10]));
const b2 = tf.variable(tf.randomNormal([10]));

function model(x) {
  return x.matMul(w1).add(b1).relu().matMul(w2).add(b2).softmax();
}
```

在Core API中，我们需要自己创建和初始化权重。每个权重都是一个`Variable`，TensorFlow.js会把`Variable`权重设为可训练张量。您可以用[tf.variable()](https://js.tensorflow.org/api/latest/#variable)创建`Variable`或把一个已存在的张量放到`Variable`中。

本文介绍了如何用Layers和Core API创建模型。接下来，请看[training models](train_models.md)学习如何训练模型。
