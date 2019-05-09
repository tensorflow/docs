# CNNを使用した手書き数字認識

Note: これらのドキュメントは私たちTensorFlowコミュニティが翻訳したものです。コミュニティによる
翻訳は**ベストエフォート**であるため、この翻訳が正確であることや[英語の公式ドキュメント](https://www.tensorflow.org/?hl=en)の
最新の状態を反映したものであることを保証することはできません。
この翻訳の品質を向上させるためのご意見をお持ちの方は、GitHubリポジトリ[tensorflow/docs](https://github.com/tensorflow/docs)にプルリクエストをお送りください。
\
コミュニティによる翻訳やレビューに参加していただける方は、
[docs-ja@tensorflow.org メーリングリスト](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)にご連絡ください。

このチュートリアルでは、畳み込みニューラルネットワークを使用して手書きの数字を認識するTensorFlow.jsモデルを構築します。はじめに、数千の手書きの数字とそのラベルを「見せて」分類器を訓練します。次にモデルがまだ見たことのないテストデータを使用して分類器の精度を評価します。

<a class="button button-white" href="https://codelabs.developers.google.com/codelabs/tfjs-training-classfication/index.html#0">CodeLabを開く</a>
