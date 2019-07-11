# はじめに

Note: これらのドキュメントは私たちTensorFlowコミュニティが翻訳したものです。コミュニティによる
翻訳は**ベストエフォート**であるため、この翻訳が正確であることや[英語の公式ドキュメント](https://www.tensorflow.org/?hl=en)の
最新の状態を反映したものであることを保証することはできません。
この翻訳の品質を向上させるためのご意見をお持ちの方は、GitHubリポジトリ[tensorflow/docs](https://github.com/tensorflow/docs)にプルリクエストをお送りください。
\
コミュニティによる翻訳やレビューに参加していただける方は、
[docs-ja@tensorflow.org メーリングリスト](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)にご連絡ください。

TensorFlow.jsは ブラウザとNode.js内で 機械学習モデルの訓練とデプロイを行うための JavaScriptライブラリです。

さまざまな利用目的に合わせて以下のセクションを参照してください。


## Tensorを直接使用せずにMLプログラムをコーディングする

TensorやOptimizerのような低レベルな詳細については考えずに機械学習を始めたい？

TensorFlow.jsを土台として作成されたml5.jsライブラリを利用すると、簡潔でわかりやすいAPIを通じてブラウザ上で機械学習のアルゴリズムとモデルを使用できます。

<a class="button button-white" href="https://ml5js.org">ml5.jsを取得</a>


## TensorFlow.jsを準備する

テンソルやレイヤー、オプティマイザ、損失関数などの概念に馴染みがある？（もしくはそれらに詳しくなりたい？） TensorFlow.jsでは
JavaScriptでニューラルネットワークプログラミングを行うための柔軟な構成要素が利用できます。

ブラウザやNode.jsでTensorFlow.jsのコードを用意して使用する方法については以下を参照してください。

<a class="button button-white" href="/js/tutorials/setup">準備</a>

### 学習済みモデルをTensorFlow.js用に変換する

Pythonの 学習済みモデルをTensorFlow.jsに変換する方法は以下を参照してください。

<a class="button button-white" href="/js/tutorials/conversion/import_keras">Kerasモデル</a>
<a class="button button-white" href="/js/tutorials/conversion/import_saved_model">GraphDefモデル</a>

## TensorFlow.jsの既存コードを元にして学ぶ

tfjs-examplesにTensorFlow.jsを使用してさまざまなMLタスクを実装した小さなコード例があります。

<a class="button button-white" href="https://github.com/tensorflow/tfjs-examples">GitHubで見る</a>

## 自身のTensorFlow.jsモデルの振る舞いを可視化する

tfjs-visはブラウザ上で可視化を行う小さなライブラリで、TensorFlow.jsと合わせて利用するために作られています。

<a class="button button-white" href="https://github.com/tensorflow/tfjs-vis">GitHubで見る</a>
<a class="button button-white" href="https://storage.googleapis.com/tfjs-vis/mnist/dist/index.html">デモを表示</a>

## 自身のデータを TensorFlow.jsで処理できるように準備する

TensorFlow.jsにはMLのベストプラクティスを使用してデータを処理するためのサポートがあります。

<a class="button button-white" href="https://js.tensorflow.org/api/latest/#Data">ドキュメントを見る</a>
