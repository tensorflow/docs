# 训练模型

本文假定读者已经读过了[模型和层](models_and_layers.md)一文。

TensorFlow.js有两种训练机器学习模型的方法：

1. 使用 Layers API <code>[LayersModel.fit()](https://js.tensorflow.org/api/latest/#tf.Model.fit)</code> 或者 <code>[LayersModel.fitDataset()](https://js.tensorflow.org/api/latest/#tf.Model.fitDataset)</code>.
2. 使用 Core API <code>[Optimizer.minimize()](https://js.tensorflow.org/api/latest/#tf.train.Optimizer.minimize)</code>.

我们首先会用高层API：Layers API来训练模型。然后，我们会展示如何用Core API来训练相同的模型。


## 引言

一个机器学习 _模型_ 是一个具有可学习参数并可以将输入映射到所需输出的函数。最优的参数可以通过训练模型习得。

训练需要几个步骤:

*   生成一个 [batch](https://developers.google.com/machine-learning/glossary/#batch) 的数据供模型使用。
*   让模型做一次预测。
*   将预测结果与“真实值”做比较。
*   决定每一个参数需要变化多少，使模型可以在以后对同一个 batch 做出更好的预测。

一个训练好的模型可以提供一个准确的输入到所需输出的映射。

## 模型函数

我们先使用 Layers API 来定义一个简单的两层网络模型：

```js
const model = tf.sequential({
 layers: [
   tf.layers.dense({inputShape: [784], units: 32, activation: 'relu'}),
   tf.layers.dense({units: 10, activation: 'softmax'}),
 ]
});
```
本质上讲, 模型拥有在训练过程中可以学习的参数(也被称为 _权重_)。 让我们，打印出来这个模型的权重（weight）和权重对应的形状（shape）：

```js
model.weights.forEach(w => {
 console.log(w.name, w.shape);
});
```

我们会得到以下输出:

```
> dense_Dense1/kernel [784, 32]
> dense_Dense1/bias [32]
> dense_Dense2/kernel [32, 10]
> dense_Dense2/bias [10]
```
这里总共有四个权重（weights），每两个权重作为一个全连接层（dense layer）。全连接层是个可以将输入张量（tensor）`x` 映射到输出张量 `y` 函数。这个函数的表达式是 `y = Ax + b`， 其中 `A`（kernel）和 `b`（bias）是该全连接层的参数。因此，这个输出是我们预期的结果。

> 注意：默认设置下全连接层包含一个 bias 参数。不过，你可以在创建全连接层时，通过设置 `{useBias: false}` 来去掉。

`model.summary()` 可以用来查看模型的整体结构和参数的总数：

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
   <td colspan="3" >Total params: 25450<br>Trainable params: 25450<br>Non-trainable params: 0
   </td>
  </tr>
</table>

在模型中，每一个权重都会被一个 <code>[Variable](https://js.tensorflow.org/api/0.14.2/#class:Variable)</code> 对象支持。在 TensorFlow.js 中，一个 <code>[Variable](https://js.tensorflow.org/api/0.14.2/#class:Variable)</code> 就是一个带有 <code>assign()</code> 方法用于更新自己值的浮点数 <code>Tensor</code>。Layers API 可以自动的以最优值来初始化权重。为了演示方便，我们可以通过调用 <code>assign()</code> 来覆写权重。
```js
model.weights.forEach(w => {
  const newVals = tf.randomNormal(w.shape);
  // w.val is an instance of tf.Variable
  w.val.assign(newVals);
});
```

## 优化器，损失和指标

在训练之前，您需要决定三个方面：


1.  **优化器**. 优化器可以根据当前模型的预测结果，决定模型中每一个参数变化多少。 当您在使用 Layers API时，您可以提供一个字符串来表示已存在的优化器（如 `'sgd'` 或者 `'adam'`）或是直接提供一个 <code>[Optimizer](https://js.tensorflow.org/api/latest/#Training-Optimizers)</code> 类的实例。
1.  <strong>损失函数</strong>. 损失函数是模型试图最小化的目标。他的目的是通过给定一个数值来表示模型当前的预测的错误程度。该损失会在每一批（batch）数据训练完后被计算，并根据此来更新模型权重。当使用 Layers API 时,您可以提供一个字符串来表示一个已存在的损失函数（如 <code>'categoricalCrossentropy'</code>）或是任意一个接收预测结果和真实值并返回损失的函数。详见 [list of available losses](https://js.tensorflow.org/api/latest/#Training-Losses) 。
1.  <strong>指标.</strong> 与损失类似, 指标也会计算出一个数字, 用来衡量我们的模型. 指标通常会在每一轮（epoch）训练结束的时候计算。至少，我们想要观测到损失会随着时间变小。但是，我们想要一下更友好的指标比如准确率（accuracy）。当使用 Layers API 时, 我们可以提供一个字符串来表示已存在的指标（比如 <code>'accuracy'</code>），或者任意一个可以接受预测值和真实值并返回一个分数的函数。详见 [list of available metrics](https://js.tensorflow.org/api/latest/#Metrics) 。

当您决定好这三个方面，通过调用 <code>model.compile()</code> 和您的配置来编译生成一个 <code>LayersModel</code>

```js
model.compile({
  optimizer: 'sgd',
  loss: 'categoricalCrossentropy',
  metrics: ['accuracy']
});
```

在编译过程中，模型会做校验以保证您的配置与其他配置互相兼容。

## 训练

主要有两种训练 `LayersModel` 的方法：

*   使用 `model.fit()` 同时提供一个大的张量来表示整个数据集.
*   使用 `model.fitDataset()` 同时通过 `Dataset` 类来提供数据。

### model.fit()

如果您的数据集可以放入整个内存中，并且可以表示为一个张量，您可以通过调用 `fit()` 来训练模型：

```js
// Generate dummy data.
const data = tf.randomNormal([100, 784]);
const labels = tf.randomUniform([100, 10]);

function onBatchEnd(batch, logs) {
  console.log('Accuracy', logs.acc);
}

// Train for 5 epochs with batch size of 32.
model.fit(data, labels, {
   epochs: 5,
   batchSize: 32,
   callbacks: {onBatchEnd}
 }).then(info => {
   console.log('Final accuracy', info.history.acc);
 });
```

本质上将, `model.fit()` 可以为我们做很多:

*   将数据分为训练集和验证集，并使用验证集来衡量我们的训练程度。
*   仅在把数据集分开后，对数据进行乱序排列（shuffle）。为了安全起见，您应当在将数据乱序排序（shuffle）后传入 `fit()`。
*   将大的数据张量分成较小的张量，其中每一个小张量大小为 `batchSize`。
*   当对每一个 batch 计算模型损失函数时， 调用 `optimizer.minimize()`。
*   它可以在每一个 epoch 或者 batch 的开始和结束时通知您。对于 TensorFlowjs 来说，我们可以通过设置 `callbacks.onBatchEnd `获得通知。同时还有其他的选项，如：`onTrainBegin`, `onTrainEnd`, `onEpochBegin`, `onEpochEnd` 和 `onBatchBegin`。
*  为了保证 JS 的事件循环机制可以被及时处理，我们的训练会对主线程做出让步。

详情可见 [documentation](https://js.tensorflow.org/api/latest/#tf.Sequential.fit) 中关于 `fit()` 的章节. 需要注意的是，如果您使用的是 Core API， 您将会需要实现所有的逻辑。

### model.fitDataset()

如果您的数据并不能完全放入内存，或者数据是以流（stream）的形式传入的，您可以通过 `fitDataset()` 来训练模型。该方法接受一个 `Dataset` 类。下面是和之前一样的训练代码，但是我们现在用一个生成器（generator）来包装数据集：

```js
function* data() {
 for (let i = 0; i < 100; i++) {
   // Generate one sample at a time.
   yield tf.randomNormal([784]);
 }
}

function* labels() {
 for (let i = 0; i < 100; i++) {
   // Generate one sample at a time.
   yield tf.randomUniform([10]);
 }
}

const xs = tf.data.generator(data);
const ys = tf.data.generator(labels);
// We zip the data and labels together, shuffle and batch 32 samples at a time.
const ds = tf.data.zip({xs, ys}).shuffle(100 /* bufferSize */).batch(32);

// Train the model for 5 epochs.
model.fitDataset(ds, {epochs: 5}).then(info => {
 console.log('Accuracy', info.history.acc);
});
```

关于 datasets 的更多资料, 详见 [documentation](https://js.tensorflow.org/api/latest/#tf.Model.fitDataset) `model.fitDataset()` 词条。

## 预测新的数据

当模型训练好后，您可以通过调用 `model.predict()` 来对未知数据做预测：

```js
// Predict 3 random samples.
const prediction = model.predict(tf.randomNormal([3, 784]));
prediction.print();
```

注意：正如我们在 [Models and Layers](models_and_layers) 提到的，`LayersModel`需要将输入的最外层的维度设置为 batch 的大小。正如上面的例子，batch 的大小为3。

## Core API

早先，我们提到了 TensorFlow.js 中有两种训练模型的方法。

总体来讲，我们首先应该尝试 Layers API，因为它是根据广泛采用的 Kears API 建立的。Layers API 也提供了很多现成的解决方案，如权重初始化，模型序列化，监控训练流程，便携性，和安全检查。

您可能会在以下情况中使用 Core API:

*   您需要最大程度的控制和灵活性。
*   您不需要序列化模型，或是能够自己实现序列化逻辑。 

关于这个 API 的更多细节, 可以阅读 [Models and Layers](models_and_layers.md) 中 "Core API" 这一章节。

同上的模型，使用 Core API 编写：

```js
// The weights and biases for the two dense layers.
const w1 = tf.variable(tf.randomNormal([784, 32]));
const b1 = tf.variable(tf.randomNormal([32]));
const w2 = tf.variable(tf.randomNormal([32, 10]));
const b2 = tf.variable(tf.randomNormal([10]));

function model(x) {
  return x.matMul(w1).add(b1).relu().matMul(w2).add(b2);
}
```

除了 Layers API，Data API 也同样可以和 Core API 无缝衔接。让我们继续使用我们在 [model.fitDataset()](#model.fitDataset()) 一节中定义的数据集。 其中数据分批（batch）和数据乱序排序（shuffle）已经由 Data API 为我们实现；

```js
const xs = tf.data.generator(data);
const ys = tf.data.generator(labels);
// Zip the data and labels together, shuffle and batch 32 samples at a time.
const ds = tf.data.zip({xs, ys}).shuffle(100 /* bufferSize */).batch(32);
```

让我们训练这个模型:

```js
const optimizer = tf.train.sgd(0.1 /* learningRate */);
// Train for 5 epochs.
for (let epoch = 0; epoch < 5; epoch++) {
  await ds.forEachAsync(({xs, ys}) => {
    optimizer.minimize(() => {
      const predYs = model(xs);
      const loss = tf.losses.softmaxCrossEntropy(ys, predYs);
      loss.data().then(l => console.log('Loss', l));
      return loss;
    });
  });
  console.log('Epoch', epoch);
}
```

以上代码就是一个使用 Core API 进行模型训练的标准操作：

*   循环 Epoch 的次数。
*   在每一个 Epoch 内，循环你的所有批数据（batch of data）。当使用 `Dataset` 时， <code>[dataset.forEachAsync()](https://js.tensorflow.org/api/0.15.1/#tf.data.Dataset.forEachAsync) </code> 会是一个很方便的遍历整个批数据的方法。
*   对于每一个 Batch，调用 <code>[optimizer.minimize(f)](https://js.tensorflow.org/api/latest/#tf.train.Optimizer.minimize)</code>。 它可以帮助我们执行 <code>f</code> 并且通过计算对于我们上面定义的四个变量的梯度来最小化我们的输出。
*   <code>f</code> 计算损失. 它会调用我们预先定义好的损失函数，并传入模型的预测值和真实值。
