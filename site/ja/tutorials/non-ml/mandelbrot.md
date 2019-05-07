# マンデルブロ集合

Note: これらのドキュメントは私たちTensorFlowコミュニティが翻訳したものです。コミュニティによる
翻訳は**ベストエフォート**であるため、この翻訳が正確であることや[英語の公式ドキュメント](https://www.tensorflow.org/?hl=en)の
最新の状態を反映したものであることを保証することはできません。
この翻訳の品質を向上させるためのご意見をお持ちの方は、GitHubリポジトリ[tensorflow/docs](https://github.com/tensorflow/docs)にプルリクエストをお送りください。
\
コミュニティによる翻訳やレビューに参加していただける方は、
[docs-ja@tensorflow.org メーリングリスト](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)にご連絡ください。

[マンデルブロ集合](https://en.wikipedia.org/wiki/Mandelbrot_set)の可視化は
機械学習とは何の関係もありませんが、
一般的な数学に対してTensorFlowを使う面白い例として役立ちます。
実際には可視化の非常に単純な実装ですが、この例は要点を示しています。
（最終的にはより美しい画像を生成するためにもっと複雑な実装を
提供することになるかもしれません。）

## 基本的な設定

始めにいくつかインポートが必要です。

```python
# シミュレーションのためにライブラリをインポート
import tensorflow as tf
import numpy as np

# 可視化のためにインポート
import PIL.Image
from io import BytesIO
from IPython.display import Image, display
```

今度は、反復回数を受け取って実際に画像を表示する関数を定義します。

```python
def DisplayFractal(a, fmt='jpeg'):
  """色彩豊かなフラクタルの画像として
     反復回数の配列を表示します"""
  a_cyclic = (6.28*a/20.0).reshape(list(a.shape)+[1])
  img = np.concatenate([10+20*np.cos(a_cyclic),
                        30+50*np.sin(a_cyclic),
                        155-80*np.cos(a_cyclic)], 2)
  img[a==a.max()] = 0
  a = img
  a = np.uint8(np.clip(a, 0, 255))
  f = BytesIO()
  PIL.Image.fromarray(a).save(f, fmt)
  display(Image(data=f.getvalue()))
```

## セッションと変数の初期化

実際に試すために、私たちはよく対話型セッションを使いますが、
通常のセッションでも同様にうまく動きます。

```python
sess = tf.InteractiveSession()
```

NumPyとTensorFlowを自由に組み合わせることができて便利です。

```python
# Use NumPy to create a 2D array of complex numbers

Y, X = np.mgrid[-1.3:1.3:0.005, -2:1:0.005]
Z = X+1j*Y
```

それでは、TensorFlowのテンソルの定義と初期化をします。

```python
xs = tf.constant(Z.astype(np.complex64))
zs = tf.Variable(xs)
ns = tf.Variable(tf.zeros_like(xs, tf.float32))
```

TensorFlowではテンソルの使用するために明示的に初期化する必要があります。

```python
tf.global_variables_initializer().run()
```

## 計算の定義と実行

それでは、追加の計算を記述します...

```python
# 新しいzの値を計算します z: z^2 + x
zs_ = zs*zs + xs

# 新しい値は発散しているか？
not_diverged = tf.abs(zs_) < 4

# zsと反復回数を更新する演算
#
# 注意: 新しいzsの値が発散していてもzsを更新し続けている！これは大変無駄である！
#       多少単純ではなくなるが、これを実行するより良い方法はある
#
step = tf.group(
  zs.assign(zs_),
  ns.assign_add(tf.cast(not_diverged, tf.float32))
  )
```

... そして200ステップ実行します。

```python
for i in range(200): step.run()
```

結果を見てみましょう。

```python
DisplayFractal(ns.eval())
```

![jpeg](https://www.tensorflow.org/images/mandelbrot_output.jpg)

なかなか悪くないですね！

