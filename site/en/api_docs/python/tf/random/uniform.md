description: Outputs random values from a uniform distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.uniform" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.uniform

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/random_ops.py#L204-L307">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Outputs random values from a uniform distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.random.uniform`, `tf.compat.v1.random_uniform`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.uniform(
    shape, minval=0, maxval=None, dtype=tf.dtypes.float32, seed=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The generated values follow a uniform distribution in the range
`[minval, maxval)`. The lower bound `minval` is included in the range, while
the upper bound `maxval` is excluded.

For floats, the default range is `[0, 1)`.  For ints, at least `maxval` must
be specified explicitly.

In the integer case, the random integers are slightly biased unless
`maxval - minval` is an exact power of two.  The bias is small for values of
`maxval - minval` significantly smaller than the range of the output (either
`2**32` or `2**64`).

#### Examples:



```
>>> tf.random.uniform(shape=[2])
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([..., ...], dtype=float32)>
>>> tf.random.uniform(shape=[], minval=-1., maxval=0.)
<tf.Tensor: shape=(), dtype=float32, numpy=-...>
>>> tf.random.uniform(shape=[], minval=5, maxval=10, dtype=tf.int64)
<tf.Tensor: shape=(), dtype=int64, numpy=...>
```

The `seed` argument produces a deterministic sequence of tensors across
multiple calls. To repeat that sequence, use <a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a>:

```
>>> tf.random.set_seed(5)
>>> tf.random.uniform(shape=[], maxval=3, dtype=tf.int32, seed=10)
<tf.Tensor: shape=(), dtype=int32, numpy=2>
>>> tf.random.uniform(shape=[], maxval=3, dtype=tf.int32, seed=10)
<tf.Tensor: shape=(), dtype=int32, numpy=0>
>>> tf.random.set_seed(5)
>>> tf.random.uniform(shape=[], maxval=3, dtype=tf.int32, seed=10)
<tf.Tensor: shape=(), dtype=int32, numpy=2>
>>> tf.random.uniform(shape=[], maxval=3, dtype=tf.int32, seed=10)
<tf.Tensor: shape=(), dtype=int32, numpy=0>
```

Without <a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a> but with a `seed` argument is specified, small
changes to function graphs or previously executed operations will change the
returned value. See <a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a> for details.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
A 1-D integer Tensor or Python array. The shape of the output tensor.
</td>
</tr><tr>
<td>
`minval`
</td>
<td>
A Tensor or Python value of type `dtype`, broadcastable with
`maxval`. The lower bound on the range of random values to generate
(inclusive).  Defaults to 0.
</td>
</tr><tr>
<td>
`maxval`
</td>
<td>
A Tensor or Python value of type `dtype`, broadcastable with
`minval`. The upper bound on the range of random values to generate
(exclusive). Defaults to 1 if `dtype` is floating point.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of the output: `float16`, `float32`, `float64`, `int32`,
or `int64`.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A Python integer. Used in combination with <a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a> to
create a reproducible sequence of tensors across multiple calls.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor of the specified shape filled with random uniform values.
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
If `dtype` is integral and `maxval` is not specified.
</td>
</tr>
</table>

