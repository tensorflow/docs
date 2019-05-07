# 偏微分方程式

Note: これらのドキュメントは私たちTensorFlowコミュニティが翻訳したものです。コミュニティによる
翻訳は**ベストエフォート**であるため、この翻訳が正確であることや[英語の公式ドキュメント](https://www.tensorflow.org/?hl=en)の
最新の状態を反映したものであることを保証することはできません。
この翻訳の品質を向上させるためのご意見をお持ちの方は、GitHubリポジトリ[tensorflow/docs](https://github.com/tensorflow/docs)にプルリクエストをお送りください。
\
コミュニティによる翻訳やレビューに参加していただける方は、
[docs-ja@tensorflow.org メーリングリスト](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)にご連絡ください。

TensorFlowは機械学習だけのものではありません。ここでは[偏微分方程式](
https://en.wikipedia.org/wiki/Partial_differential_equation)の振る舞いを
シミュレートするためにTensorFlowを使った(ややありきたりな)例を示します。
いくつかの雨粒が落ちた場合における正方形の池の表面をシミュレートします。

## 基本的な設定

いくつかのインポートが必要になります。

```python
# シミュレーションのためにライブラリをインポート
import tensorflow as tf
import numpy as np

# 可視化のためにインポート
import PIL.Image
from io import BytesIO
from IPython.display import clear_output, Image, display
```

以下は画像として池の表面の状態を表示する関数です。

```python
def DisplayArray(a, fmt='jpeg', rng=[0,1]):
  """画像として配列を表示する"""
  a = (a - rng[0])/float(rng[1] - rng[0])*255
  a = np.uint8(np.clip(a, 0, 255))
  f = BytesIO()
  PIL.Image.fromarray(a).save(f, fmt)
  clear_output(wait = True)
  display(Image(data=f.getvalue()))
```

ここで私たちは遊んで便利に対話型TensorFlowセッションを開始します。
実行可能な.pyファイルでこれを行っている場合は、
通常のセッションも同様に機能します。

```python
sess = tf.InteractiveSession()
```

## 計算の便宜関数


```python
def make_kernel(a):
  """畳込みカーネルに2次元配列を変形する"""
  a = np.asarray(a)
  a = a.reshape(list(a.shape) + [1,1])
  return tf.constant(a, dtype=1)

def simple_conv(x, k):
  """簡略化された2次元畳込み演算"""
  x = tf.expand_dims(tf.expand_dims(x, 0), -1)
  y = tf.nn.depthwise_conv2d(x, k, [1, 1, 1, 1], padding='SAME')
  return y[0, :, :, 0]

def laplace(x):
  """配列の2次元ラプラシアンを計算する"""
  laplace_k = make_kernel([[0.5, 1.0, 0.5],
                           [1.0, -6., 1.0],
                           [0.5, 1.0, 0.5]])
  return simple_conv(x, laplace_k)
```

## PDEの定義

私たちの池は完全500 x 500の正方形で、
自然界に見られるほとんどの池のケースと同様なものとなっています。

```python
N = 500
```

ここで私たちは池を作り、そこにいくつかの雨粒を降らせます。

```python
# 初期条件 -- いくつかの雨粒を池に降らせる

# すべてを0で設定
u_init = np.zeros([N, N], dtype=np.float32)
ut_init = np.zeros([N, N], dtype=np.float32)

# いくつかの雨粒をランダムなポイントで池に降らせる
for n in range(40):
  a,b = np.random.randint(0, N, 2)
  u_init[a,b] = np.random.uniform()

DisplayArray(u_init, rng=[-0.1, 0.1])
```

![jpeg](https://www.tensorflow.org/images/pde_output_1.jpg)


それでは、微分方程式の詳細を記述しましょう。


```python
# パラメータ:
# eps -- 時間分解能
# damping -- 波減衰
eps = tf.placeholder(tf.float32, shape=())
damping = tf.placeholder(tf.float32, shape=())

# シミュレーションの状態のための変数を生成する
U  = tf.Variable(u_init)
Ut = tf.Variable(ut_init)

# 離散化したPDEの更新ルール
U_ = U + eps * Ut
Ut_ = Ut + eps * (laplace(U) - damping * Ut)

# 状態を更新するための演算
step = tf.group(
  U.assign(U_),
  Ut.assign(Ut_))
```

## シミュレーションの実行

ここがおもしろくなるところです -- 単純なforループで時間を進めてみましょう。

```python
# 状態を初期条件で初期化する
tf.global_variables_initializer().run()

# PDEを1000ステップ実行
for i in range(1000):
  # シミュレーションのステップ実行
  step.run({eps: 0.03, damping: 0.04})
  DisplayArray(U.eval(), rng=[-0.1, 0.1])
```

![jpeg](https://www.tensorflow.org/images/pde_output_2.jpg)

見てください! さざ波です!
