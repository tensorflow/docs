description: Returns the truth value of (x == y) element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.equal" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.equal

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/math_ops.py#L1581-L1614">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the truth value of (x == y) element-wise.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.equal`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.equal`, `tf.compat.v1.math.equal`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.equal(
    x, y, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Performs a [broadcast](
https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) with the
arguments and then an element-wise equality comparison, returning a Tensor of
boolean values.

#### For example:



```
>>> x = tf.constant([2, 4])
>>> y = tf.constant(2)
>>> tf.math.equal(x, y)
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True,  False])>
```

```
>>> x = tf.constant([2, 4])
>>> y = tf.constant([2, 4])
>>> tf.math.equal(x, y)
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True,  True])>
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
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or <a href="../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a> or <a href="../../tf/IndexedSlices.md"><code>tf.IndexedSlices</code></a>.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or <a href="../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a> or <a href="../../tf/IndexedSlices.md"><code>tf.IndexedSlices</code></a>.
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
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of type bool with the same size as that of x or y.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>
<tr class="alt">
<td colspan="2">
<a href="../../tf/errors/InvalidArgumentError.md"><code>tf.errors.InvalidArgumentError</code></a>: If shapes of arguments are incompatible
</td>
</tr>

</table>

