# Node 中的 TensorFlow.js

## TensorFlow CPU

TensorFlow CPU 包，可以按如下方式导入：


```js
import * as tf from '@tensorflow/tfjs-node'
```


当从这个包导入 TensorFlow.js 时，您导入的模块将由 TensorFlow C 二进制文件加速并在 CPU 上运行。CPU 上的 TensorFlow 使用硬件加速来加速内部的线性代数运算。

此软件包适用于支持 TensorFlow 的 Linux，Windows 和 Mac 平台。

> 注意：您没有必要导入'@tensorflow/tfjs'或者将其添加到您的 package.json 文件中，这是由 Node 库间接导入的。


## TensorFlow GPU

TensorFlow GPU 包，可以按如下方式导入：


```js
import * as tf from '@tensorflow/tfjs-node-gpu'
```

与 CPU 包一样，您导入的模块将由 TensorFlow C 二进制文件加速，但是它将使用 CUDA 在 GPU 上运行张量运算，因此只能运行在 Linux 平台。该绑定比其他可选绑定可以快至少一个数量级。

> 注意：此软件包目前仅适用于 CUDA。在选择本方案之前，您需要在带有 NVIDIA 显卡的的机器上安装 CUDA。

> 注意：您没有必要导入'@tensorflow/tfjs'或将其添加到您的 package.json 文件中，这是由 Node 库间接导入的。


## 普通 CPU

使用普通 CPU 运行 TensorFlow.js 版本，可以按如下方式导入：


```js
import * as tf from '@tensorflow/tfjs'
```

这个包与您在浏览器中使用的包类似。在这个包中，这些调用是在 CPU 上以原生 JavaScript 运行。这个包比其他包小得多，因为它不需要 TensorFlow 二进制文件，但是速度要慢得多。

由于这个软件包不依赖于 TensorFlow，因此它可用于支持 Node.js 的更多设备，而不仅仅是 Linux，Windows 和 Mac平台。


## 生产环境考虑因素

Node.js Bindings 为 TensorFlow.js 提供了一个同步地执行操作的后端。这意味着当您调用一个操作时，例如 `tf.matMul(a, b)`，它将阻塞主线程直到这个操作完成。

因此，当前这种 Bindings 非常适合脚本和离线任务。如果您要在实际应用程序（如：Web 服务器）中使用Node.js Bindings，则应设置一个工作队列或设置一些工作线程，以便您的 TensorFlow.js 代码不会阻止主线程。


## APIs

一旦您在上面的任何选项中将包导入为 tf 后，所有普通的 TensorFlow.js 符号都将出现在导入的模块上。

### tf.browser

在普通的 TensorFlow.js 包中，`tf.browser.*` 命名空间中的符号将在 Node.js 中不可用，因为它们使用特定浏览器的 API。

目前，有如下 API：

*   tf.browser.fromPixels
*   tf.browser.toPixels

### tf.node

有两个 Node.js 包还提供了一个名称为 `tf.node` 的命名空间，其中包含了特定 Node 的 API。

TensorBoard 是一个特定 Node.js API 的重要例子。

这是一个将训练的总结(summaries)导出至Node.js的TensorBoard中的案例

```js
const model = tf.sequential();
model.add(tf.layers.dense({units: 1}));
model.compile({
  loss: 'meanSquaredError',
  optimizer: 'sgd',
  metrics: ['MAE']
});


// 为了演示目的生成一些随机假数据。
const xs = tf.randomUniform([10000, 200]);
const ys = tf.randomUniform([10000, 1]);
const valXs = tf.randomUniform([1000, 200]);
const valYs = tf.randomUniform([1000, 1]);


// 开始模型训练过程。
await model.fit(xs, ys, {
  epochs: 100,
  validationData: [valXs, valYs],
   // 在这里添加 tensorBoard 回调。
  callbacks: tf.node.tensorBoard('/tmp/fit_logs_1')
});
```
