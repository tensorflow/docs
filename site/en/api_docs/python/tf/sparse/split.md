description: Split a SparseTensor into num_split tensors along axis.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.split" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.split

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/sparse_ops.py#L1028-L1093">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Split a `SparseTensor` into `num_split` tensors along `axis`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.split(
    sp_input=None, num_split=None, axis=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If the `sp_input.dense_shape[axis]` is not an integer multiple of `num_split`
each slice starting from 0:`shape[axis] % num_split` gets extra one
dimension. For example:

```
>>> indices = [[0, 2], [0, 4], [0, 5], [1, 0], [1, 1]]
>>> values = [1, 2, 3, 4, 5]
>>> t = tf.SparseTensor(indices=indices, values=values, dense_shape=[2, 7])
>>> tf.sparse.to_dense(t)
<tf.Tensor: shape=(2, 7), dtype=int32, numpy=
array([[0, 0, 1, 0, 2, 3, 0],
       [4, 5, 0, 0, 0, 0, 0]], dtype=int32)>
```

```
>>> output = tf.sparse.split(sp_input=t, num_split=2, axis=1)
>>> tf.sparse.to_dense(output[0])
<tf.Tensor: shape=(2, 4), dtype=int32, numpy=
array([[0, 0, 1, 0],
       [4, 5, 0, 0]], dtype=int32)>
>>> tf.sparse.to_dense(output[1])
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
array([[2, 3, 0],
       [0, 0, 0]], dtype=int32)>
```

```
>>> output = tf.sparse.split(sp_input=t, num_split=2, axis=0)
>>> tf.sparse.to_dense(output[0])
<tf.Tensor: shape=(1, 7), dtype=int32, numpy=array([[0, 0, 1, 0, 2, 3, 0]],
dtype=int32)>
>>> tf.sparse.to_dense(output[1])
<tf.Tensor: shape=(1, 7), dtype=int32, numpy=array([[4, 5, 0, 0, 0, 0, 0]],
dtype=int32)>
```

```
>>> output = tf.sparse.split(sp_input=t, num_split=2, axis=-1)
>>> tf.sparse.to_dense(output[0])
<tf.Tensor: shape=(2, 4), dtype=int32, numpy=
array([[0, 0, 1, 0],
       [4, 5, 0, 0]], dtype=int32)>
>>> tf.sparse.to_dense(output[1])
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
array([[2, 3, 0],
       [0, 0, 0]], dtype=int32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_input`
</td>
<td>
The `SparseTensor` to split.
</td>
</tr><tr>
<td>
`num_split`
</td>
<td>
A Python integer. The number of ways to split.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
A 0-D `int32` `Tensor`. The dimension along which to split. Must be in
range [-rank, rank), where rank is the number of dimensions in the input
`SparseTensor`.
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
`num_split` `SparseTensor` objects resulting from splitting `value`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `sp_input` is not a `SparseTensor`.
</td>
</tr>
</table>

