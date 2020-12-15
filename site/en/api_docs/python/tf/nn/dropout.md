description: Computes dropout: randomly sets elements to zero to prevent overfitting.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.dropout" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.dropout

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_ops.py#L5062-L5181">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes dropout: randomly sets elements to zero to prevent overfitting.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.dropout(
    x, rate, noise_shape=None, seed=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note: The behavior of dropout has changed between TensorFlow 1.x and 2.x.
When converting 1.x code, please use named arguments to ensure behavior stays
consistent.

See also: <a href="../../tf/keras/layers/Dropout.md"><code>tf.keras.layers.Dropout</code></a> for a dropout layer.

[Dropout](https://arxiv.org/abs/1207.0580) is useful for regularizing DNN
models. Inputs elements are randomly set to zero (and the other elements are
rescaled). This encourages each node to be independently useful, as it cannot
rely on the output of other nodes.

More precisely: With probability `rate` elements of `x` are set to `0`.
The remaining elements are scaled up by `1.0 / (1 - rate)`, so that the
expected value is preserved.

```
>>> tf.random.set_seed(0)
>>> x = tf.ones([3,5])
>>> tf.nn.dropout(x, rate = 0.5, seed = 1).numpy()
array([[2., 0., 0., 2., 2.],
     [2., 2., 2., 2., 2.],
     [2., 0., 2., 0., 2.]], dtype=float32)
```

```
>>> tf.random.set_seed(0)
>>> x = tf.ones([3,5])
>>> tf.nn.dropout(x, rate = 0.8, seed = 1).numpy()
array([[0., 0., 0., 5., 5.],
     [0., 5., 0., 5., 0.],
     [5., 0., 5., 0., 5.]], dtype=float32)
```

```
>>> tf.nn.dropout(x, rate = 0.0) == x
<tf.Tensor: shape=(3, 5), dtype=bool, numpy=
  array([[ True,  True,  True,  True,  True],
         [ True,  True,  True,  True,  True],
         [ True,  True,  True,  True,  True]])>
```


By default, each element is kept or dropped independently.  If `noise_shape`
is specified, it must be
[broadcastable](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
to the shape of `x`, and only dimensions with `noise_shape[i] == shape(x)[i]`
will make independent decisions. This is useful for dropping whole
channels from an image or sequence. For example:

```
>>> tf.random.set_seed(0)
>>> x = tf.ones([3,10])
>>> tf.nn.dropout(x, rate = 2/3, noise_shape=[1,10], seed=1).numpy()
array([[0., 0., 0., 3., 3., 0., 3., 3., 3., 0.],
     [0., 0., 0., 3., 3., 0., 3., 3., 3., 0.],
     [0., 0., 0., 3., 3., 0., 3., 3., 3., 0.]], dtype=float32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A floating point tensor.
</td>
</tr><tr>
<td>
`rate`
</td>
<td>
A scalar `Tensor` with the same type as x. The probability
that each element is dropped. For example, setting rate=0.1 would drop
10% of input elements.
</td>
</tr><tr>
<td>
`noise_shape`
</td>
<td>
A 1-D `Tensor` of type `int32`, representing the
shape for randomly generated keep/drop flags.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A Python integer. Used to create random seeds. See
<a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a> for behavior.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Tensor of the same shape of `x`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `rate` is not in `[0, 1)` or if `x` is not a floating point
tensor. `rate=1` is disallowed, because the output would be all zeros,
which is likely not what was intended.
</td>
</tr>
</table>

