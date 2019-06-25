# TensorFlow Probability


Note: これらのドキュメントは私たちTensorFlowコミュニティが翻訳したものです。コミュニティによる
翻訳は**ベストエフォート**であるため、この翻訳が正確であることや[英語の公式ドキュメント](https://www.tensorflow.org/?hl=en)の
最新の状態を反映したものであることを保証することはできません。
この翻訳の品質を向上させるためのご意見をお持ちの方は、GitHubリポジトリ[tensorflow/docs](https://github.com/tensorflow/docs)にプルリクエストをお送りください。
\
コミュニティによる翻訳やレビューに参加していただける方は、
[docs-ja@tensorflow.org メーリングリスト](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)にご連絡ください。  

TensorFlow Probability は TensorFlow における確率的推論と統計的分析のためのライブラリです。
TensorFlow エコシステムの一部として、TensorFlow Probability は確率的手法とさまざまな手法や機能との統合を提供します。
たとえば、深層ネットワークを用いた確率的な手法、自動微分を用いた勾配に基づく推論、GPU のようなハードウェア高速化や分散処理による大きなデータセットやモデルに対するスケーラビリティなどです。

TensorFlow Probability を始めるためには、[インストールガイド](./install) や
[Python notebook チュートリアル](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/)を参照してください。

## コンポーネント

我々の確率的機械学習ツール群は以下のような構造になっています:

### Layer 0: TensorFlow

*数値処理*—特に、`LinearOperator`
クラスが可能にする、効率的な演算のための特定の構造 (対角、低ランク) を開発できるようにする行列フリーな実装。 
TensorFlow Probability チームによりメンテナンスされていて、TensorFlow コアの [`tf.linalg`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/ops/linalg) の一部です。

### Layer 1: 確率的なブロックの構築

* *Distributions* ([`tfp.distributions`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/distributions),
  [`tf.distributions`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/ops/distributions)):
  バッチや[ブロードキャスティング](https://docs.scipy.org/doc/numpy-1.14.0/user/basics.broadcasting.html)の仕組みを取り入れた、多くの確率分布やそれに関連する統計量の処理
* *Bijectors* ([`tfp.bijectors`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/bijectors)):
  ランダム変数の可逆で組み立て可能な変換。 Bijectors は変換された分布の豊富なクラスを提供します。それは、古典的な
  [対数正規分布](https://en.wikipedia.org/wiki/Log-normal_distribution)から
  [masked autoregressive flows](https://arxiv.org/abs/1705.07057) のような洗練された深層学習モデルにまで及びます。

### Layer 2: モデル構築

*   *Edward2*
    ([`tfp.edward2`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/edward2)):
    プログラムとして柔軟な確率的モデルを定義するための確率的プログラミング言語
*   *Probabilistic layers*
    ([`tfp.layers`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/layers)):
    TensorFlow の layers を拡張して、それらが表現する関数の不確実性を出力できるニューラルネットワーク層
*   *Trainable distributions*
    ([`tfp.trainable_distributions`](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/python/trainable_distributions)):
    確率分布を出力するニューラルネットワークを構築することを簡単にする、1つの Tensor によるパラメータをもつ確率分布

### Layer 3: 確率的推論

*   *Markov chain Monte Carlo*
    ([`tfp.mcmc`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/mcmc)):
    サンプリングによる積分近似のためのアルゴリズム
    [ハミルトンモンテカルロ法](https://en.wikipedia.org/wiki/Hamiltonian_Monte_Carlo)、
    ランダムウォークメトロポリス・ヘイスティング法、カスタム遷移カーネルを構築することができる機能を含みます。
*   *Variational Inference*
    ([`tfp.vi`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/vi)):
    最適化による積分近似のためのアルゴリズム
*   *Optimizers*
    ([`tfp.optimizer`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/optimizer)):
    TensorFlow Optimizers を拡張した、確率的最適化モジュール。
    [Stochastic Gradient Langevin Dynamics](http://www.icml-2011.org/papers/398_icmlpaper.pdf) を含みます。
*   *Monte Carlo*
    ([`tfp.monte_carlo`](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/python/monte_carlo)):
    モンテカルロ法を用いたツール群

TensorFlow Probability は開発中であるため、インタフェースは変更される可能性があります。

## 使用例

ナビゲーションに載っている [Python notebook チュートリアル](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/)
に加えて、いくつかのスクリプト例が利用できます:

* [Variational Autoencoders](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/examples/vae.py)
  —latent code と変分推論による表現学習
* [Vector-Quantized Autoencoder](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/examples/vq_vae.py)
  —ベクトル量子化による離散表現学習
* [ベイジアンニューラルネットワーク](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/examples/bayesian_neural_network.py)
  —重みの不確実性を出力するニューラルネットワーク
* [ベイズロジスティック回帰](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/examples/logistic_regression.py)
  —二値分類のためのベイズ推論

## issue の報告

バグ報告や機能要望は
[TensorFlow Probability issue tracker](https://github.com/tensorflow/probability/issues) を使用してください。
