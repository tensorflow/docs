# 画像分類器の転移学習

Note: これらのドキュメントは私たちTensorFlowコミュニティが翻訳したものです。コミュニティによる
翻訳は**ベストエフォート**であるため、この翻訳が正確であることや[英語の公式ドキュメント](https://www.tensorflow.org/?hl=en)の
最新の状態を反映したものであることを保証することはできません。
この翻訳の品質を向上させるためのご意見をお持ちの方は、GitHubリポジトリ[tensorflow/docs](https://github.com/tensorflow/docs)にプルリクエストをお送りください。
\
コミュニティによる翻訳やレビューに参加していただける方は、
[docs-ja@tensorflow.org メーリングリスト](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)にご連絡ください。

このチュートリアルでは、TensorFlow.jsを使用してブラウザ上でその場で独自の画像分類器を構築する方法について学びます。

最小の学習データで非常に高精度なモデルを作成するために転移学習を利用できます。ここでは学習済みモデルとしてMobileNetという画像分類器を使用します。このモデルを土台としてモデルを訓練し、認識する画像クラスをカスタマイズします。

このチュートリアルはコードラボとして提供されます。[次のリンクに従ってコードラボを開いてください。](https://codelabs.developers.google.com/codelabs/tensorflowjs-teachablemachine-codelab/index.html)
