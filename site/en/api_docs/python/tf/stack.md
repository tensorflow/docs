description: Stacks a list of rank-R tensors into one rank-(R+1) tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.stack" />
<meta itemprop="path" content="Stable" />
</div>

# tf.stack

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L1351-L1412">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Stacks a list of rank-`R` tensors into one rank-`(R+1)` tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.stack`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.stack(
    values, axis=0, name='stack'
)
</code></pre>



<!-- Placeholder for "Used in" -->

See also <a href="../tf/concat.md"><code>tf.concat</code></a>, <a href="../tf/tile.md"><code>tf.tile</code></a>, <a href="../tf/repeat.md"><code>tf.repeat</code></a>.

Packs the list of tensors in `values` into a tensor with rank one higher than
each tensor in `values`, by packing them along the `axis` dimension.
Given a list of length `N` of tensors of shape `(A, B, C)`;

if `axis == 0` then the `output` tensor will have the shape `(N, A, B, C)`.
if `axis == 1` then the `output` tensor will have the shape `(A, N, B, C)`.
Etc.

#### For example:



```
>>> x = tf.constant([1, 4])
>>> y = tf.constant([2, 5])
>>> z = tf.constant([3, 6])
>>> tf.stack([x, y, z])
<tf.Tensor: shape=(3, 2), dtype=int32, numpy=
array([[1, 4],
       [2, 5],
       [3, 6]], dtype=int32)>
>>> tf.stack([x, y, z], axis=1)
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
array([[1, 2, 3],
       [4, 5, 6]], dtype=int32)>
```

This is the opposite of unstack.  The numpy equivalent is `np.stack`

```
>>> np.array_equal(np.stack([x, y, z]), tf.stack([x, y, z]))
True
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`values`
</td>
<td>
A list of `Tensor` objects with the same shape and type.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
An `int`. The axis to stack along. Defaults to the first dimension.
Negative values wrap around, so the valid range is `[-(R+1), R+1)`.
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

<tr>
<td>
`output`
</td>
<td>
A stacked `Tensor` with the same type as `values`.
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
If `axis` is out of the range [-(R+1), R+1).
</td>
</tr>
</table>

