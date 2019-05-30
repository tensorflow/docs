# 音声識別器の転移学習

Note: これらのドキュメントは私たちTensorFlowコミュニティが翻訳したものです。コミュニティによる
翻訳は**ベストエフォート**であるため、この翻訳が正確であることや[英語の公式ドキュメント](https://www.tensorflow.org/?hl=en)の
最新の状態を反映したものであることを保証することはできません。
この翻訳の品質を向上させるためのご意見をお持ちの方は、GitHubリポジトリ[tensorflow/docs](https://github.com/tensorflow/docs)にプルリクエストをお送りください。
\
コミュニティによる翻訳やレビューに参加していただける方は、
[docs-ja@tensorflow.org メーリングリスト](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)にご連絡ください。

このチュートリアルでは、TensorFlow.jsを使用してブラウザ上で学習し、独自の音声分類器を構築する方法について学びます。

転移学習を使用して、比較的少ない学習データで短い音を分類するモデルを作成します。ここでは[音声コマンド認識](https://github.com/tensorflow/tfjs-models/tree/master/speech-commands)のための学習済みモデルを使用します。このモデルを土台として新しいモデルを訓練して独自の音声クラスを認識します。

このチュートリアルはコードラボとして提供されます。[次のリンクに従ってコードラボを開いてください。](https://codelabs.developers.google.com/codelabs/tensorflowjs-audio-codelab/index.html)
