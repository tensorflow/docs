description: Count the number of times an integer value appears in a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.bincount" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.bincount

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/bincount_ops.py#L254-L451">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Count the number of times an integer value appears in a tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.bincount`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.bincount(
    values, weights=None, axis=0, minlength=None, maxlength=None,
    binary_output=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op takes an N-dimensional `Tensor`, `RaggedTensor`, or `SparseTensor`,
and returns an N-dimensional int64 SparseTensor where element
`[i0...i[axis], j]` contains the number of times the value `j` appears in
slice `[i0...i[axis], :]` of the input tensor.  Currently, only N=0 and
N=-1 are supported.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`values`
</td>
<td>
A Tensor, RaggedTensor, or SparseTensor whose values should be
counted. These tensors must have a rank of 2 if `axis=-1`.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
If non-None, must be the same shape as arr. For each value in
`value`, the bin will be incremented by the corresponding weight instead
of 1.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
The axis to slice over. Axes at and below `axis` will be flattened
before bin counting. Currently, only `0`, and `-1` are supported. If None,
all axes will be flattened (identical to passing `0`).
</td>
</tr><tr>
<td>
`minlength`
</td>
<td>
If given, ensures the output has length at least `minlength`,
padding with zeros at the end if necessary.
</td>
</tr><tr>
<td>
`maxlength`
</td>
<td>
If given, skips values in `values` that are equal or greater than
`maxlength`, ensuring that the output has length at most `maxlength`.
</td>
</tr><tr>
<td>
`binary_output`
</td>
<td>
If True, this op will output 1 instead of the number of times
a token appears (equivalent to one_hot + reduce_any instead of one_hot +
reduce_add). Defaults to False.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this op.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A SparseTensor with `output.shape = values.shape[:axis] + [N]`, where `N` is
* `maxlength` (if set);
* `minlength` (if set, and `minlength > reduce_max(values)`);
* `0` (if `values` is empty);
* `reduce_max(values) + 1` otherwise.
</td>
</tr>

</table>



#### Examples:



**Bin-counting every item in individual batches**

This example takes an input (which could be a Tensor, RaggedTensor, or
SparseTensor) and returns a SparseTensor where the value of (i,j) is the
number of times value j appears in batch i.

```
>>> data = np.array([[10, 20, 30, 20], [11, 101, 11, 10001]], dtype=np.int64)
>>> output = tf.sparse.bincount(data, axis=-1)
>>> print(output)
SparseTensor(indices=tf.Tensor(
[[    0    10]
 [    0    20]
 [    0    30]
 [    1    11]
 [    1   101]
 [    1 10001]], shape=(6, 2), dtype=int64),
 values=tf.Tensor([1 2 1 2 1 1], shape=(6,), dtype=int64),
 dense_shape=tf.Tensor([    2 10002], shape=(2,), dtype=int64))
```

**Bin-counting with defined output shape**

This example takes an input (which could be a Tensor, RaggedTensor, or
SparseTensor) and returns a SparseTensor where the value of (i,j) is the
number of times value j appears in batch i. However, all values of j
above 'maxlength' are ignored. The dense_shape of the output sparse tensor
is set to 'minlength'. Note that, while the input is identical to the
example above, the value '10001' in batch item 2 is dropped, and the
dense shape is [2, 500] instead of [2,10002] or [2, 102].

```
>>> minlength = maxlength = 500
>>> data = np.array([[10, 20, 30, 20], [11, 101, 11, 10001]], dtype=np.int64)
>>> output = tf.sparse.bincount(
...    data, axis=-1, minlength=minlength, maxlength=maxlength)
>>> print(output)
SparseTensor(indices=tf.Tensor(
[[  0  10]
 [  0  20]
 [  0  30]
 [  1  11]
 [  1 101]], shape=(5, 2), dtype=int64),
 values=tf.Tensor([1 2 1 2 1], shape=(5,), dtype=int64),
 dense_shape=tf.Tensor([  2 500], shape=(2,), dtype=int64))
```

**Binary bin-counting**

This example takes an input (which could be a Tensor, RaggedTensor, or
SparseTensor) and returns a SparseTensor where (i,j) is 1 if the value j
appears in batch i at least once and is 0 otherwise. Note that, even though
some values (like 20 in batch 1 and 11 in batch 2) appear more than once,
the 'values' tensor is all 1s.

```
>>> data = np.array([[10, 20, 30, 20], [11, 101, 11, 10001]], dtype=np.int64)
>>> output = tf.sparse.bincount(data, binary_output=True, axis=-1)
>>> print(output)
SparseTensor(indices=tf.Tensor(
[[    0    10]
 [    0    20]
 [    0    30]
 [    1    11]
 [    1   101]
 [    1 10001]], shape=(6, 2), dtype=int64),
 values=tf.Tensor([1 1 1 1 1 1], shape=(6,), dtype=int64),
 dense_shape=tf.Tensor([    2 10002], shape=(2,), dtype=int64))
```

**Weighted bin-counting**

This example takes two inputs - a values tensor and a weights tensor. These
tensors must be identically shaped, and have the same row splits or indices
in the case of RaggedTensors or SparseTensors. When performing a weighted
count, the op will output a SparseTensor where the value of (i, j) is the
sum of the values in the weight tensor's batch i in the locations where
the values tensor has the value j. In this case, the output dtype is the
same as the dtype of the weights tensor.

```
>>> data = np.array([[10, 20, 30, 20], [11, 101, 11, 10001]], dtype=np.int64)
>>> weights = [[2, 0.25, 15, 0.5], [2, 17, 3, 0.9]]
>>> output = tf.sparse.bincount(data, weights=weights, axis=-1)
>>> print(output)
SparseTensor(indices=tf.Tensor(
[[    0    10]
 [    0    20]
 [    0    30]
 [    1    11]
 [    1   101]
 [    1 10001]], shape=(6, 2), dtype=int64),
 values=tf.Tensor([2. 0.75 15. 5. 17. 0.9], shape=(6,), dtype=float32),
 dense_shape=tf.Tensor([    2 10002], shape=(2,), dtype=int64))
```