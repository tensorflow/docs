# 安装

## 浏览器安装

有两种在主要的方式将Tensorflow.js安装在你的项目中：

- 使用  [脚本标签(script tags)](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_JavaScript_within_a_webpage)。
- 从[NPM](https://www.npmjs.com)安装并且使用[Parcel](https://parceljs.org/), [WebPack](https://webpack.js.org/)或是 [Rollup](https://rollupjs.org/guide/en)这样的构建工具。

如果你是一个新的web开发或是从未听说过类似于webpack或是parcel这样的工具，_我们建议你使用脚本标签_。如果你有很多的经验或是希望写一个大型程序，那么值得你使用构建工具进行探索。

### 通过脚本标签使用

添加下列所有的脚本标签在你的HTML主要程序中。


```html
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.0.0/dist/tf.min.js"></script>
```

<section class="expandable">
  <h4 class="showalways">See code sample script tag setup</h4>
  <pre class="prettyprint">
// 定义一个模型或是线性回归
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

你可以使用 [npm cli](https://docs.npmjs.com/cli/npm)工具或是[yarn](https://yarnpkg.com/en/)安装Tensorflow.js。

```
yarn add @tensorflow/tfjs
```

_or_

```
npm install @tensorflow/tfjs
```

<section class="expandable">
  <h4 class="showalways">See sample code for installation via NPM</h4>
  <pre class="prettyprint">
import * as tf from '@tensorflow/tfjs';

// 定义一个模型或是线性回归
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

你可以使用 [npm cli](https://docs.npmjs.com/cli/npm)工具或是[yarn](https://yarnpkg.com/en/)安装Tensorflow.js。

**Option 1:** 使用原生C++安装Tensorflow.js。

```
yarn add @tensorflow/tfjs-node
```

_or_

```
npm install @tensorflow/tfjs-node
```

**Option 2:** (仅支持Linux) 如果你的系统里有NVIDIA® GPU并 [支持CUDA](https://www.tensorflow.org/install/install_linux#NVIDIARequirements),为了更高的性能使用GPU包。

```
yarn add @tensorflow/tfjs-node-gpu
```

_or_

```
npm install @tensorflow/tfjs-node-gpu
```

**Option 3:** 安装纯JavaScript版本，这是性能方面最慢的选项。 

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

// 选择加载绑定
// Use '@tensorflow/tfjs-node-gpu' if running with GPU.
require('@tensorflow/tfjs-node');

// 训练简单模型:
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
当使用TypeScript时,如果您的项目使用严格的空检查，或者在编译过程中遇到错误，你需要在你的 `tsconfig.json`文件中。
设置`skipLibCheck: true`。