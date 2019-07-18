# 準備

Note: これらのドキュメントは私たちTensorFlowコミュニティが翻訳したものです。コミュニティによる
翻訳は**ベストエフォート**であるため、この翻訳が正確であることや[英語の公式ドキュメント](https://www.tensorflow.org/?hl=en)の
最新の状態を反映したものであることを保証することはできません。
この翻訳の品質を向上させるためのご意見をお持ちの方は、GitHubリポジトリ[tensorflow/docs](https://github.com/tensorflow/docs)にプルリクエストをお送りください。
\
コミュニティによる翻訳やレビューに参加していただける方は、
[docs-ja@tensorflow.org メーリングリスト](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)にご連絡ください。

## ブラウザの準備

ブラウザベースのプロジェクトでTensorFlow.jsを利用する方法は主に2つあります。 

- [scriptタグ](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_JavaScript_within_a_webpage)を使用する 
- [NPM](https://www.npmjs.com)からインストールし、[Parcel](https://parceljs.org/)や[WebPack](https://webpack.js.org/)、[Rollup](https://rollupjs.org/guide/en)などのビルドツールを使用する

ウェブ開発に馴染みがなかったり、webpackやparcelなどのツールについて聞いたことがなければ、_scriptタグを使用することをおすすめします。_経験が豊富だったり、より大きなプログラムを書こうとしている場合には、ビルドツールの利用を試みる価値があるでしょう。

### scriptタグから使用する

以下のscriptタグをメインのHTMLファイルに追加してください。

```html
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.0.0/dist/tf.min.js"></script>
```

<section class="expandable">
  <h4 class="showalways">See code sample script tag setup</h4>
  <pre class="prettyprint">
// 線形回帰モデルを定義
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));

model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});

// 訓練用の模擬データを生成
const xs = tf.tensor2d([1, 2, 3, 4], [4, 1]);
const ys = tf.tensor2d([1, 3, 5, 7], [4, 1]);

// データを使用してモデルを訓練
model.fit(xs, ys, {epochs: 10}).then(() => {
  // モデルを使用してモデルが見たことのないデータポイントを推論
  model.predict(tf.tensor2d([5], [1, 1])).print();
  // 結果を確認するためにブラウザのDevToolsを開く
});
  </pre>
</section>

### NPMからインストール

[npm cli](https://docs.npmjs.com/cli/npm)ツールと[yarn](https://yarnpkg.com/en/)のどちらでもTensorFlow.jsをインストールできます。

```
yarn add @tensorflow/tfjs
```

_または_

```
npm install @tensorflow/tfjs
```

<section class="expandable">
  <h4 class="showalways">See sample code for installation via NPM</h4>
  <pre class="prettyprint">
import * as tf from '@tensorflow/tfjs';

// 線形回帰モデルを定義
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));

model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});

// 訓練用の模擬データを生成
const xs = tf.tensor2d([1, 2, 3, 4], [4, 1]);
const ys = tf.tensor2d([1, 3, 5, 7], [4, 1]);

// データを使用してモデルを訓練
model.fit(xs, ys, {epochs: 10}).then(() => {
  // モデルを使用してモデルが見たことのないデータポイントを推論
  model.predict(tf.tensor2d([5], [1, 1])).print();
  // 結果を確認するためにブラウザのDevToolsを開く
});
  </pre>
</section>


## Node.jsの準備

[npm cli](https://docs.npmjs.com/cli/npm)ツールと[yarn](https://yarnpkg.com/en/)のどちらでもTensorFlow.jsをインストールできます。

**オプション1:** ネイティブC++バインディングの付属するTensorFlow.jsをインストール

```
yarn add @tensorflow/tfjs-node
```

_または_

```
npm install @tensorflow/tfjs-node
```

**オプション2:** (Linuxのみ)
システムに[CUDA support](https://www.tensorflow.org/install/install_linux#NVIDIARequirements)のあるNVIDIA®
GPUがあれば、より高いパフォーマンスを実現するためにGPUパッケージを使用

```
yarn add @tensorflow/tfjs-node-gpu
```

_または_

```
npm install @tensorflow/tfjs-node-gpu
```

**オプション3:** ピュアJavaScriptバージョンをインストール。パフォーマンスの観点からは最も遅い選択肢です。

```
yarn add @tensorflow/tfjs
```

_または_

```
npm install @tensorflow/tfjs
```


<section class="expandable">
  <h4 class="showalways">See sample code for Node.js usage</h4>
  <pre class="prettyprint">
const tf = require('@tensorflow/tfjs');

// オプションとしてバインディングを読み込み
// GPU上で動作する場合は'@tensorflow/tfjs-node-gpu'を使用してください
require('@tensorflow/tfjs-node');

// 単純なモデルを訓練
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

TypeScriptを使用していて、プロジェクトで厳密なnullチェックを使用していると`tsconfig.json`ファイルで`skipLibCheck:
true`を設定する必要があるでしょう。そうしなければコンパイル中にエラーが発生します。
