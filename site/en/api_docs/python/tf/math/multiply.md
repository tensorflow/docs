description: Returns an element-wise x * y.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.multiply" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.multiply

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L472-L518">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns an element-wise x * y.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.multiply`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.multiply`, `tf.compat.v1.multiply`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.multiply(
    x, y, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### For example:



```
>>> x = tf.constant(([1, 2, 3, 4]))
>>> tf.math.multiply(x, x)
<tf.Tensor: shape=(4,), dtype=..., numpy=array([ 1,  4,  9, 16], dtype=int32)>
```

Since <a href="../../tf/math/multiply.md"><code>tf.math.multiply</code></a> will convert its arguments to `Tensor`s, you can also
pass in non-`Tensor` arguments:

```
>>> tf.math.multiply(7,6)
<tf.Tensor: shape=(), dtype=int32, numpy=42>
```

If `x.shape` is not thes same as `y.shape`, they will be broadcast to a
compatible shape. (More about broadcasting
[here](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).)

#### For example:



```
>>> x = tf.ones([1, 2]);
>>> y = tf.ones([2, 1]);
>>> x * y  # Taking advantage of operator overriding
<tf.Tensor: shape=(2, 2), dtype=float32, numpy=
array([[1., 1.],
     [1., 1.]], dtype=float32)>
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
A Tensor. Must be one of the following types: `bfloat16`,
`half`, `float32`, `float64`, `uint8`, `int8`, `uint16`,
`int16`, `int32`, `int64`, `complex64`, `complex128`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
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


</table>


A `Tensor`.  Has the same type as `x`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>
<tr class="alt">
<td colspan="2">
* InvalidArgumentError: When `x` and `y` have incomptatible shapes or types.
</td>
</tr>

</table>

