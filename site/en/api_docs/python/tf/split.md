description: Splits a tensor value into a list of sub tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.split" />
<meta itemprop="path" content="Stable" />
</div>

# tf.split

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/array_ops.py#L1888-L1962">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Splits a tensor `value` into a list of sub tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.split`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.split(
    value, num_or_size_splits, axis=0, num=None, name='split'
)
</code></pre>



<!-- Placeholder for "Used in" -->

See also <a href="../tf/unstack.md"><code>tf.unstack</code></a>.

If `num_or_size_splits` is an integer, then `value` is split along the
dimension `axis` into `num_split` smaller tensors. This requires that
`value.shape[axis]` is divisible by `num_split`.

If `num_or_size_splits` is a 1-D Tensor (or list), we call it `size_splits`
and `value` is split into `len(size_splits)` elements. The shape of the `i`-th
element has the same size as the `value` except along dimension `axis` where
the size is `size_splits[i]`.

#### For example:



```
>>> x = tf.Variable(tf.random.uniform([5, 30], -1, 1))
```

Split `x` into 3 tensors along dimension 1
>>> s0, s1, s2 = tf.split(x, num_or_size_splits=3, axis=1)
>>> tf.shape(s0).numpy()
array([ 5, 10], dtype=int32)

Split `x` into 3 tensors with sizes [4, 15, 11] along dimension 1
>>> split0, split1, split2 = tf.split(x, [4, 15, 11], 1)
>>> tf.shape(split0).numpy()
array([5, 4], dtype=int32)
>>> tf.shape(split1).numpy()
array([ 5, 15], dtype=int32)
>>> tf.shape(split2).numpy()
array([ 5, 11], dtype=int32)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
The `Tensor` to split.
</td>
</tr><tr>
<td>
`num_or_size_splits`
</td>
<td>
Either an integer indicating the number of splits along
`axis` or a 1-D integer `Tensor` or Python list containing the sizes of
each output tensor along `axis`. If a scalar, then it must evenly divide
`value.shape[axis]`; otherwise the sum of sizes along the split axis
must match that of the `value`.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
An integer or scalar `int32` `Tensor`. The dimension along which to
split. Must be in the range `[-rank(value), rank(value))`. Defaults to 0.
</td>
</tr><tr>
<td>
`num`
</td>
<td>
Optional, used to specify the number of outputs when it cannot be
inferred from the shape of `size_splits`.
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
if `num_or_size_splits` is a scalar returns a list of `num_or_size_splits`
`Tensor` objects; if `num_or_size_splits` is a 1-D Tensor returns
`num_or_size_splits.get_shape[0]` `Tensor` objects resulting from splitting
`value`.
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
If `num` is unspecified and cannot be inferred.
</td>
</tr>
</table>

