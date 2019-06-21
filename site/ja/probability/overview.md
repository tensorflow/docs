# TensorFlow Probability

TensorFlow Probability は TensorFlow における確率的推論と統計的分析のためのライブラリです. TensorFlow エコシステムの一部として, TensorFlow
Probability は確率的手法と深層ネットワーク, 自動微分を用いた勾配に基づく推論, GPUによるハードウェア高速化や分散計算による大きなデータセットやモデルに対するスケーラビリティを提供します.

TensorFlow Probability を始めるためには, [インストールガイド](./install) や
[Python notebook チュートリアル](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/){:.external} を参照してください.

## コンポーネント

我々の確率的機械学習ツール群は以下のような構造になっています:

### Layer 0: TensorFlow

*Numerical operations*—in particular, the `LinearOperator`
class—enables matrix-free implementations that can exploit a particular structure
(diagonal, low-rank, etc.) for efficient computation. It is built and maintained
by the TensorFlow Probability team and is part of
[`tf.linalg`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/ops/linalg)
in core TensorFlow.

### Layer 1: 確率的なブロックの構築

* *Distributions* ([`tfp.distributions`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/distributions),
  [`tf.distributions`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/ops/distributions)):
  A large collection of probability distributions and related statistics with
  batch and [broadcasting](https://docs.scipy.org/doc/numpy-1.14.0/user/basics.broadcasting.html){:.external}
  semantics.
* *Bijectors* ([`tfp.bijectors`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/bijectors)):
  Reversible and composable transformations of random variables. Bijectors
  provide a rich class of transformed distributions, from classical examples
  like the
  [log-normal distribution](https://en.wikipedia.org/wiki/Log-normal_distribution){:.external}
  to sophisticated deep learning models such as
  [masked autoregressive flows](https://arxiv.org/abs/1705.07057){:.external}.

### Layer 2: モデル構築

*   *Edward2*
    ([`tfp.edward2`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/edward2)):
    プログラムとして柔軟な確率的モデルを定義するための確率的プログラミング言語です.
*   *Probabilistic layers*
    ([`tfp.layers`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/layers)):
    TensorFlow 層を拡張して、それらが表現する関数の不確実性を出力できるニューラルネットワーク層です.
*   *Trainable distributions*
    ([`tfp.trainable_distributions`](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/python/trainable_distributions)):
    確率分布を出力するニューラルネットワークを構築することを簡単にする、一つの Tensor によるパラメータをもつ確率分布です.

### Layer 3: 確率的推論

*   *Markov chain Monte Carlo*
    ([`tfp.mcmc`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/mcmc)):
    サンプリングによる積分近似のためのアルゴリズム. 
    [ハミルトンモンテカルロ法](https://en.wikipedia.org/wiki/Hamiltonian_Monte_Carlo){:.external},
    ランダムウォークハミルトンヘイスティング法, カスタム遷移カーネルを構築することができる機能を含みます.
*   *Variational Inference*
    ([`tfp.vi`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/vi)):
    最適化による積分近似のためのアルゴリズム.
*   *Optimizers*
    ([`tfp.optimizer`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/optimizer)):
    TensorFlow Optimizers を拡張した, 確率的最適化手法.
    [Stochastic Gradient Langevin Dynamics](http://www.icml-2011.org/papers/398_icmlpaper.pdf){:.external} を含みます.
*   *Monte Carlo*
    ([`tfp.monte_carlo`](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/python/monte_carlo)):
    モンテカルロ法を用いたツール群.

TensorFlow Probability は開発中であるため, インタフェースは変更される可能性があります.

## 使用例

ナビゲーションに載っている [Python notebook チュートリアル](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/){:.external}
に加えて, いくつかのスクリプト例が利用できます:

* [Variational Autoencoders](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/examples/vae.py)
  —Representation learning with a latent code and variational inference.
* [Vector-Quantized Autoencoder](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/examples/vq_vae.py)
  —ベクトル量子化による離散表現学習.
* [Bayesian Neural Networks](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/examples/bayesian_neural_network.py)
  —ウェイトの不確実性を出力するニューラルネットワーク.
* [Bayesian Logistic Regression](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/examples/logistic_regression.py)
  —二値分類のためのベイズ推論.

## Report issues

バグ報告や機能要望は
[TensorFlow Probability issue tracker](https://github.com/tensorflow/probability/issues) を使用してください.
