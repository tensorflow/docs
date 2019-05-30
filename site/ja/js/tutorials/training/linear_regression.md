# 2次元データを予測する

Note: これらのドキュメントは私たちTensorFlowコミュニティが翻訳したものです。コミュニティによる
翻訳は**ベストエフォート**であるため、この翻訳が正確であることや[英語の公式ドキュメント](https://www.tensorflow.org/?hl=en)の
最新の状態を反映したものであることを保証することはできません。
この翻訳の品質を向上させるためのご意見をお持ちの方は、GitHubリポジトリ[tensorflow/docs](https://github.com/tensorflow/docs)にプルリクエストをお送りください。
\
コミュニティによる翻訳やレビューに参加していただける方は、
[docs-ja@tensorflow.org メーリングリスト](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)にご連絡ください。

このチュートリアルでは、一連の自動車を表現した数値データを予測するモデルを訓練します。

この演習は様々な種類のモデルの訓練に共通する手順を紹介するものですが、使用するのは小さなデータセットと単純な（浅い）モデルです。主な目的はTensorFlow.jsでモデルを訓練する際に使用する基本的な用語や概念、構文に慣れる手助けをし、さらに調査と学習を進める足がかりを提供することです。

<a class="button button-white" href="https://codelabs.developers.google.com/codelabs/tfjs-training-regression/index.html#0">CodeLabを開く</a>
