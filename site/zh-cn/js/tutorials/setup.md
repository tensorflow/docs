# 安装

## 浏览器安装

在您基于浏览器的项目中获取TensorFlow.js有以下两种主要方法

-   使用
    [脚本标签(script tags)](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_JavaScript_within_a_webpage)。
-   从[NPM](https://www.npmjs.com)安装并且使用[Parcel](https://parceljs.org/),
    [WebPack](https://webpack.js.org/)或是
    [Rollup](https://rollupjs.org/guide/en)这样的构建工具。

如果您不熟悉Web开发，或者从未听说过webpack或parcel等工具，_我们建议您使用脚本标签(script
tags)_。如果您经验丰富或想要编写更大的程序，那么使用构建工具进行探索可能更加合适。

### 使用脚本标签(script tags)

将以下脚本标签添加到您的主HTML文件中：


```html
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.0.0/dist/tf.min.js"></script>
```

有关脚本标签的设置，请参阅代码示例：

<section class="expandable">
  <h4 class="showalways">See code sample script tag setup</h4>
  <pre class="prettyprint">
//定义一个线性回归模型。
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));

model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});

// 为训练生成一些合成数据
const xs = tf.tensor2d([1, 2, 3, 4], [4, 1]);
const ys = tf.tensor2d([1, 3, 5, 7], [4, 1]);

// 使用数据训练模型
model.fit(xs, ys, {epochs: 10}).then(() => {
// 在该模型从未看到过的数据点上使用模型进行推理

  model.predict(tf.tensor2d([5], [1, 1])).print();
  // 打开浏览器开发工具查看输出
});
  </pre>
</section>

### 从NPM安装

您可以使用
[npm cli](https://docs.npmjs.com/cli/npm)工具或是[yarn](https://yarnpkg.com/en/)安装TensorFlow.js。

```
yarn add @tensorflow/tfjs
```

_或者_

```
npm install @tensorflow/tfjs
```

<section class="expandable">
  <h4 class="showalways">See sample code for installation via NPM</h4>
  <pre class="prettyprint">
import * as tf from '@tensorflow/tfjs';

//定义一个线性回归模型。
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));

model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});

// 为训练生成一些合成数据
const xs = tf.tensor2d([1, 2, 3, 4], [4, 1]);
const ys = tf.tensor2d([1, 3, 5, 7], [4, 1]);

// 使用数据训练模型
model.fit(xs, ys, {epochs: 10}).then(() => {
  // 在该模型从未看到过的数据点上使用模型进行推理
  model.predict(tf.tensor2d([5], [1, 1])).print();
  //  打开浏览器开发工具查看输出
});
  </pre>
</section>


## Node.js 安装

您可以使用
[npm cli](https://docs.npmjs.com/cli/npm)工具或是[yarn](https://yarnpkg.com/en/)安装TensorFlow.js。

**选项1:** 安装带有原生C++绑定的TensorFlow.js。

```
yarn add @tensorflow/tfjs-node
```

_或者_

```
npm install @tensorflow/tfjs-node
```

**选项2:**
（仅限Linux）如果您的系统具有[支持CUDA](https://www.tensorflow.org/install/install_linux#NVIDIARequirements)的NVIDIA®GPU，请使用GPU包以获得更高的性能。

```
yarn add @tensorflow/tfjs-node-gpu
```

_or_

```
npm install @tensorflow/tfjs-node-gpu
```

**选项3:** 安装纯JavaScript版本，这是性能方面最慢的选项。

```
yarn add @tensorflow/tfjs
```

_or_

```
npm install @tensorflow/tfjs
```

<section class="expandable">
  <h4 class="showalways">See sample code for Node.js usage</h4>
  <pre class="prettyprint">
const tf = require('@tensorflow/tfjs');

// 可选加载绑定：
// 如果使用GPU运行，请使用'@tensorflow/tfjs-node-gpu'
require('@tensorflow/tfjs-node');

// 训练一个简单模型:
const model = tf.sequential();
model.add(tf.layers.dense({units: 100, activation: 'relu', inputShape: [10]}));
model.add(tf.layers.dense({units: 1, activation: 'linear'}));
model.compile({optimizer: 'sgd', loss: 'meanSquaredError'});

const xs = tf.randomNormal([100, 10]);
const ys = tf.randomNormal([100, 1]);

model.fit(xs, ys, {
  epochs: 100,
  callbacks: {
    onEpochEnd: (epoch, log) => console.log(`Epoch ${epoch}: loss = ${log.loss}`)
  }
});
  </pre>
</section>

### TypeScript

当使用TypeScript时，如果您的项目使用严格的空值检查，或者在编译过程中遇到错误，则您可能需要在您的`tsconfig.json`文件中设置`skipLibCheck：true`。
