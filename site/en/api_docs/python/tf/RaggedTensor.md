description: Represents a ragged tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.RaggedTensor" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__abs__"/>
<meta itemprop="property" content="__add__"/>
<meta itemprop="property" content="__and__"/>
<meta itemprop="property" content="__bool__"/>
<meta itemprop="property" content="__div__"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__floordiv__"/>
<meta itemprop="property" content="__ge__"/>
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__gt__"/>
<meta itemprop="property" content="__invert__"/>
<meta itemprop="property" content="__le__"/>
<meta itemprop="property" content="__lt__"/>
<meta itemprop="property" content="__mod__"/>
<meta itemprop="property" content="__mul__"/>
<meta itemprop="property" content="__ne__"/>
<meta itemprop="property" content="__neg__"/>
<meta itemprop="property" content="__nonzero__"/>
<meta itemprop="property" content="__or__"/>
<meta itemprop="property" content="__pow__"/>
<meta itemprop="property" content="__radd__"/>
<meta itemprop="property" content="__rand__"/>
<meta itemprop="property" content="__rdiv__"/>
<meta itemprop="property" content="__rfloordiv__"/>
<meta itemprop="property" content="__rmod__"/>
<meta itemprop="property" content="__rmul__"/>
<meta itemprop="property" content="__ror__"/>
<meta itemprop="property" content="__rpow__"/>
<meta itemprop="property" content="__rsub__"/>
<meta itemprop="property" content="__rtruediv__"/>
<meta itemprop="property" content="__rxor__"/>
<meta itemprop="property" content="__sub__"/>
<meta itemprop="property" content="__truediv__"/>
<meta itemprop="property" content="__xor__"/>
<meta itemprop="property" content="bounding_shape"/>
<meta itemprop="property" content="consumers"/>
<meta itemprop="property" content="from_nested_row_lengths"/>
<meta itemprop="property" content="from_nested_row_splits"/>
<meta itemprop="property" content="from_nested_value_rowids"/>
<meta itemprop="property" content="from_row_lengths"/>
<meta itemprop="property" content="from_row_limits"/>
<meta itemprop="property" content="from_row_splits"/>
<meta itemprop="property" content="from_row_starts"/>
<meta itemprop="property" content="from_sparse"/>
<meta itemprop="property" content="from_tensor"/>
<meta itemprop="property" content="from_uniform_row_length"/>
<meta itemprop="property" content="from_value_rowids"/>
<meta itemprop="property" content="get_shape"/>
<meta itemprop="property" content="merge_dims"/>
<meta itemprop="property" content="nested_row_lengths"/>
<meta itemprop="property" content="nested_value_rowids"/>
<meta itemprop="property" content="nrows"/>
<meta itemprop="property" content="numpy"/>
<meta itemprop="property" content="row_lengths"/>
<meta itemprop="property" content="row_limits"/>
<meta itemprop="property" content="row_starts"/>
<meta itemprop="property" content="to_list"/>
<meta itemprop="property" content="to_sparse"/>
<meta itemprop="property" content="to_tensor"/>
<meta itemprop="property" content="value_rowids"/>
<meta itemprop="property" content="with_flat_values"/>
<meta itemprop="property" content="with_row_splits_dtype"/>
<meta itemprop="property" content="with_values"/>
</div>

# tf.RaggedTensor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L61-L2119">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents a ragged tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.RaggedTensor`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->

A `RaggedTensor` is a tensor with one or more *ragged dimensions*, which are
dimensions whose slices may have different lengths.  For example, the inner
(column) dimension of `rt=[[3, 1, 4, 1], [], [5, 9, 2], [6], []]` is ragged,
since the column slices (`rt[0, :]`, ..., `rt[4, :]`) have different lengths.
Dimensions whose slices all have the same length are called *uniform
dimensions*.  The outermost dimension of a `RaggedTensor` is always uniform,
since it consists of a single slice (and so there is no possibility for
differing slice lengths).

The total number of dimensions in a `RaggedTensor` is called its *rank*,
and the number of ragged dimensions in a `RaggedTensor` is called its
*ragged-rank*.  A `RaggedTensor`'s ragged-rank is fixed at graph creation
time: it can't depend on the runtime values of `Tensor`s, and can't vary
dynamically for different session runs.

Note that the `__init__` constructor is private. Please use one of the
following methods to construct a `RaggedTensor`:

    * <a href="../tf/RaggedTensor.md#from_row_lengths"><code>tf.RaggedTensor.from_row_lengths</code></a>
    * <a href="../tf/RaggedTensor.md#from_value_rowids"><code>tf.RaggedTensor.from_value_rowids</code></a>
    * <a href="../tf/RaggedTensor.md#from_row_splits"><code>tf.RaggedTensor.from_row_splits</code></a>
    * <a href="../tf/RaggedTensor.md#from_row_starts"><code>tf.RaggedTensor.from_row_starts</code></a>
    * <a href="../tf/RaggedTensor.md#from_row_limits"><code>tf.RaggedTensor.from_row_limits</code></a>
    * <a href="../tf/RaggedTensor.md#from_nested_row_splits"><code>tf.RaggedTensor.from_nested_row_splits</code></a>
    * <a href="../tf/RaggedTensor.md#from_nested_row_lengths"><code>tf.RaggedTensor.from_nested_row_lengths</code></a>
    * <a href="../tf/RaggedTensor.md#from_nested_value_rowids"><code>tf.RaggedTensor.from_nested_value_rowids</code></a>

### Potentially Ragged Tensors

Many ops support both `Tensor`s and `RaggedTensor`s.  The term "potentially
ragged tensor" may be used to refer to a tensor that might be either a
`Tensor` or a `RaggedTensor`.  The ragged-rank of a `Tensor` is zero.

### Documenting RaggedTensor Shapes

When documenting the shape of a RaggedTensor, ragged dimensions can be
indicated by enclosing them in parentheses.  For example, the shape of
a 3-D `RaggedTensor` that stores the fixed-size word embedding for each
word in a sentence, for each sentence in a batch, could be written as
`[num_sentences, (num_words), embedding_size]`.  The parentheses around
`(num_words)` indicate that dimension is ragged, and that the length
of each element list in that dimension may vary for each item.

### Component Tensors

Internally, a `RaggedTensor` consists of a concatenated list of values that
are partitioned into variable-length rows.  In particular, each `RaggedTensor`
consists of:

  * A `values` tensor, which concatenates the variable-length rows into a
    flattened list.  For example, the `values` tensor for
    `[[3, 1, 4, 1], [], [5, 9, 2], [6], []]` is `[3, 1, 4, 1, 5, 9, 2, 6]`.

  * A `row_splits` vector, which indicates how those flattened values are
    divided into rows.  In particular, the values for row `rt[i]` are stored
    in the slice `rt.values[rt.row_splits[i]:rt.row_splits[i+1]]`.

#### Example:



```
>>> print(tf.RaggedTensor.from_row_splits(
...       values=[3, 1, 4, 1, 5, 9, 2, 6],
...       row_splits=[0, 4, 4, 7, 8, 8]))
<tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>
```

### Alternative Row-Partitioning Schemes

In addition to `row_splits`, ragged tensors provide support for five other
row-partitioning schemes:

  * `row_lengths`: a vector with shape `[nrows]`, which specifies the length
    of each row.

  * `value_rowids` and `nrows`: `value_rowids` is a vector with shape
    `[nvals]`, corresponding one-to-one with `values`, which specifies
    each value's row index.  In particular, the row `rt[row]` consists of the
    values `rt.values[j]` where `value_rowids[j]==row`.  `nrows` is an
    integer scalar that specifies the number of rows in the
    `RaggedTensor`. (`nrows` is used to indicate trailing empty rows.)

  * `row_starts`: a vector with shape `[nrows]`, which specifies the start
    offset of each row.  Equivalent to `row_splits[:-1]`.

  * `row_limits`: a vector with shape `[nrows]`, which specifies the stop
    offset of each row.  Equivalent to `row_splits[1:]`.

  * `uniform_row_length`: A scalar tensor, specifying the length of every
    row.  This row-partitioning scheme may only be used if all rows have
    the same length.

Example: The following ragged tensors are equivalent, and all represent the
nested list `[[3, 1, 4, 1], [], [5, 9, 2], [6], []]`.

```
>>> values = [3, 1, 4, 1, 5, 9, 2, 6]
>>> rt1 = RaggedTensor.from_row_splits(values, row_splits=[0, 4, 4, 7, 8, 8])
>>> rt2 = RaggedTensor.from_row_lengths(values, row_lengths=[4, 0, 3, 1, 0])
>>> rt3 = RaggedTensor.from_value_rowids(
...     values, value_rowids=[0, 0, 0, 0, 2, 2, 2, 3], nrows=5)
>>> rt4 = RaggedTensor.from_row_starts(values, row_starts=[0, 4, 4, 7, 8])
>>> rt5 = RaggedTensor.from_row_limits(values, row_limits=[4, 4, 7, 8, 8])
```

### Multiple Ragged Dimensions

`RaggedTensor`s with multiple ragged dimensions can be defined by using
a nested `RaggedTensor` for the `values` tensor.  Each nested `RaggedTensor`
adds a single ragged dimension.

```
>>> inner_rt = RaggedTensor.from_row_splits(  # =rt1 from above
...     values=[3, 1, 4, 1, 5, 9, 2, 6], row_splits=[0, 4, 4, 7, 8, 8])
>>> outer_rt = RaggedTensor.from_row_splits(
...     values=inner_rt, row_splits=[0, 3, 3, 5])
>>> print(outer_rt.to_list())
[[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]]
>>> print(outer_rt.ragged_rank)
2
```

The factory function <a href="../tf/RaggedTensor.md#from_nested_row_splits"><code>RaggedTensor.from_nested_row_splits</code></a> may be used to
construct a `RaggedTensor` with multiple ragged dimensions directly, by
providing a list of `row_splits` tensors:

```
>>> RaggedTensor.from_nested_row_splits(
...     flat_values=[3, 1, 4, 1, 5, 9, 2, 6],
...     nested_row_splits=([0, 3, 3, 5], [0, 4, 4, 7, 8, 8])).to_list()
[[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]]
```

### Uniform Inner Dimensions

`RaggedTensor`s with uniform inner dimensions can be defined
by using a multidimensional `Tensor` for `values`.

```
>>> rt = RaggedTensor.from_row_splits(values=tf.ones([5, 3], tf.int32),
...                                   row_splits=[0, 2, 5])
>>> print(rt.to_list())
[[[1, 1, 1], [1, 1, 1]],
 [[1, 1, 1], [1, 1, 1], [1, 1, 1]]]
>>> print(rt.shape)
(2, None, 3)
```

### Uniform Outer Dimensions

`RaggedTensor`s with uniform outer dimensions can be defined by using
one or more `RaggedTensor` with a `uniform_row_length` row-partitioning
tensor.  For example, a `RaggedTensor` with shape `[2, 2, None]` can be
constructed with this method from a `RaggedTensor` values with shape
`[4, None]`:

```
>>> values = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])
>>> print(values.shape)
(4, None)
>>> rt6 = tf.RaggedTensor.from_uniform_row_length(values, 2)
>>> print(rt6)
<tf.RaggedTensor [[[1, 2, 3], [4]], [[5, 6], [7, 8, 9, 10]]]>
>>> print(rt6.shape)
(2, 2, None)
```

Note that `rt6` only contains one ragged dimension (the innermost
dimension). In contrast, if `from_row_splits` is used to construct a similar
`RaggedTensor`, then that `RaggedTensor` will have two ragged dimensions:

```
>>> rt7 = tf.RaggedTensor.from_row_splits(values, [0, 2, 4])
>>> print(rt7.shape)
(2, None, None)
```

Uniform and ragged outer dimensions may be interleaved, meaning that a
tensor with any combination of ragged and uniform dimensions may be created.
For example, a RaggedTensor `t4` with shape `[3, None, 4, 8, None, 2]` could
be constructed as follows:

```python
t0 = tf.zeros([1000, 2])                           # Shape:         [1000, 2]
t1 = RaggedTensor.from_row_lengths(t0, [...])      #           [160, None, 2]
t2 = RaggedTensor.from_uniform_row_length(t1, 8)   #         [20, 8, None, 2]
t3 = RaggedTensor.from_uniform_row_length(t2, 4)   #       [5, 4, 8, None, 2]
t4 = RaggedTensor.from_row_lengths(t3, [...])      # [3, None, 4, 8, None, 2]
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`dtype`
</td>
<td>
The `DType` of values in this tensor.
</td>
</tr><tr>
<td>
`flat_values`
</td>
<td>
The innermost `values` tensor for this ragged tensor.

Concretely, if `rt.values` is a `Tensor`, then `rt.flat_values` is
`rt.values`; otherwise, `rt.flat_values` is `rt.values.flat_values`.

Conceptually, `flat_values` is the tensor formed by flattening the
outermost dimension and all of the ragged dimensions into a single
dimension.

`rt.flat_values.shape = [nvals] + rt.shape[rt.ragged_rank + 1:]`
(where `nvals` is the number of items in the flattened dimensions).

#### Example:

```
>>> rt = tf.ragged.constant([[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]])
>>> print(rt.flat_values)
tf.Tensor([3 1 4 1 5 9 2 6], shape=(8,), dtype=int32)
```
</td>
</tr><tr>
<td>
`nested_row_splits`
</td>
<td>
A tuple containing the row_splits for all ragged dimensions.

`rt.nested_row_splits` is a tuple containing the `row_splits` tensors for
all ragged dimensions in `rt`, ordered from outermost to innermost.  In
particular, `rt.nested_row_splits = (rt.row_splits,) + value_splits` where:

* `value_splits = ()` if `rt.values` is a `Tensor`.
* `value_splits = rt.values.nested_row_splits` otherwise.

#### Example:

```
>>> rt = tf.ragged.constant(
...     [[[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]]])
>>> for i, splits in enumerate(rt.nested_row_splits):
...   print('Splits for dimension %d: %s' % (i+1, splits.numpy()))
Splits for dimension 1: [0 3]
Splits for dimension 2: [0 3 3 5]
Splits for dimension 3: [0 4 4 7 8 8]
```
</td>
</tr><tr>
<td>
`ragged_rank`
</td>
<td>
The number of times the RaggedTensor's flat_values is partitioned.


```
>>> values = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])
>>> values.ragged_rank
1
```

```
>>> rt = tf.RaggedTensor.from_uniform_row_length(values, 2)
>>> rt.ragged_rank
2
```
</td>
</tr><tr>
<td>
`row_splits`
</td>
<td>
The row-split indices for this ragged tensor's `values`.

`rt.row_splits` specifies where the values for each row begin and end in
`rt.values`.  In particular, the values for row `rt[i]` are stored in
the slice `rt.values[rt.row_splits[i]:rt.row_splits[i+1]]`.

#### Example:

```
>>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
>>> print(rt.row_splits)  # indices of row splits in rt.values
tf.Tensor([0 4 4 7 8 8], shape=(6,), dtype=int64)
```
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
The statically known shape of this ragged tensor.



```
>>> tf.ragged.constant([[0], [1, 2]]).shape
TensorShape([2, None])
```

```
>>> tf.ragged.constant([[[0, 1]], [[1, 2], [3, 4]]], ragged_rank=1).shape
TensorShape([2, None, 2])
```
</td>
</tr><tr>
<td>
`uniform_row_length`
</td>
<td>
The length of each row in this ragged tensor, or None if rows are ragged.

```
>>> rt1 = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])
>>> print(rt1.uniform_row_length)  # rows are ragged.
None
```

```
>>> rt2 = tf.RaggedTensor.from_uniform_row_length(
...     values=rt1, uniform_row_length=2)
>>> print(rt2)
<tf.RaggedTensor [[[1, 2, 3], [4]], [[5, 6], [7, 8, 9, 10]]]>
>>> print(rt2.uniform_row_length)  # rows are not ragged (all have size 2).
tf.Tensor(2, shape=(), dtype=int64)
```

A RaggedTensor's rows are only considered to be uniform (i.e. non-ragged)
if it can be determined statically (at graph construction time) that the
rows all have the same length.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
The concatenated rows for this ragged tensor.

`rt.values` is a potentially ragged tensor formed by flattening the two
outermost dimensions of `rt` into a single dimension.

`rt.values.shape = [nvals] + rt.shape[2:]` (where `nvals` is the
number of items in the outer two dimensions of `rt`).

`rt.ragged_rank = self.ragged_rank - 1`

#### Example:

```
>>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
>>> print(rt.values)
tf.Tensor([3 1 4 1 5 9 2 6], shape=(8,), dtype=int32)
```
</td>
</tr>
</table>



## Methods

<h3 id="bounding_shape"><code>bounding_shape</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1244-L1299">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>bounding_shape(
    axis=None, name=None, out_type=None
)
</code></pre>

Returns the tight bounding box shape for this `RaggedTensor`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`axis`
</td>
<td>
An integer scalar or vector indicating which axes to return the
bounding box for.  If not specified, then the full bounding box is
returned.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensor (optional).
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
`dtype` for the returned tensor.  Defaults to
`self.row_splits.dtype`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An integer `Tensor` (`dtype=self.row_splits.dtype`).  If `axis` is not
specified, then `output` is a vector with
`output.shape=[self.shape.ndims]`.  If `axis` is a scalar, then the
`output` is a scalar.  If `axis` is a vector, then `output` is a vector,
where `output[i]` is the bounding size for dimension `axis[i]`.
</td>
</tr>

</table>


#### Example:

```
>>> rt = tf.ragged.constant([[1, 2, 3, 4], [5], [], [6, 7, 8, 9], [10]])
>>> rt.bounding_shape().numpy()
array([5, 4])
```

<h3 id="consumers"><code>consumers</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L2118-L2119">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>consumers()
</code></pre>




<h3 id="from_nested_row_lengths"><code>from_nested_row_lengths</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L742-L780">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_nested_row_lengths(
    flat_values, nested_row_lengths, name=None, validate=(True)
)
</code></pre>

Creates a `RaggedTensor` from a nested list of `row_lengths` tensors.


#### Equivalent to:



```python
result = flat_values
for row_lengths in reversed(nested_row_lengths):
  result = from_row_lengths(result, row_lengths)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`flat_values`
</td>
<td>
A potentially ragged tensor.
</td>
</tr><tr>
<td>
`nested_row_lengths`
</td>
<td>
A list of 1-D integer tensors.  The `i`th tensor is
used as the `row_lengths` for the `i`th ragged dimension.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the RaggedTensor (optional).
</td>
</tr><tr>
<td>
`validate`
</td>
<td>
If true, then use assertions to check that the arguments form
a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
since they must be checked for each tensor value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor` (or `flat_values` if `nested_row_lengths` is empty).
</td>
</tr>

</table>



<h3 id="from_nested_row_splits"><code>from_nested_row_splits</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L702-L740">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_nested_row_splits(
    flat_values, nested_row_splits, name=None, validate=(True)
)
</code></pre>

Creates a `RaggedTensor` from a nested list of `row_splits` tensors.


#### Equivalent to:



```python
result = flat_values
for row_splits in reversed(nested_row_splits):
  result = from_row_splits(result, row_splits)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`flat_values`
</td>
<td>
A potentially ragged tensor.
</td>
</tr><tr>
<td>
`nested_row_splits`
</td>
<td>
A list of 1-D integer tensors.  The `i`th tensor is
used as the `row_splits` for the `i`th ragged dimension.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the RaggedTensor (optional).
</td>
</tr><tr>
<td>
`validate`
</td>
<td>
If true, then use assertions to check that the arguments form
a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
since they must be checked for each tensor value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor` (or `flat_values` if `nested_row_splits` is empty).
</td>
</tr>

</table>



<h3 id="from_nested_value_rowids"><code>from_nested_value_rowids</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L645-L700">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_nested_value_rowids(
    flat_values, nested_value_rowids, nested_nrows=None, name=None, validate=(True)
)
</code></pre>

Creates a `RaggedTensor` from a nested list of `value_rowids` tensors.


#### Equivalent to:



```python
result = flat_values
for (rowids, nrows) in reversed(zip(nested_value_rowids, nested_nrows)):
  result = from_value_rowids(result, rowids, nrows)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`flat_values`
</td>
<td>
A potentially ragged tensor.
</td>
</tr><tr>
<td>
`nested_value_rowids`
</td>
<td>
A list of 1-D integer tensors.  The `i`th tensor is
used as the `value_rowids` for the `i`th ragged dimension.
</td>
</tr><tr>
<td>
`nested_nrows`
</td>
<td>
A list of integer scalars.  The `i`th scalar is used as the
`nrows` for the `i`th ragged dimension.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the RaggedTensor (optional).
</td>
</tr><tr>
<td>
`validate`
</td>
<td>
If true, then use assertions to check that the arguments form
a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
since they must be checked for each tensor value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor` (or `flat_values` if `nested_value_rowids` is empty).
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `len(nested_values_rowids) != len(nested_nrows)`.
</td>
</tr>
</table>



<h3 id="from_row_lengths"><code>from_row_lengths</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L450-L491">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_row_lengths(
    values, row_lengths, name=None, validate=(True)
)
</code></pre>

Creates a `RaggedTensor` with rows partitioned by `row_lengths`.

The returned `RaggedTensor` corresponds with the python list defined by:

```python
result = [[values.pop(0) for i in range(length)]
          for length in row_lengths]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`values`
</td>
<td>
A potentially ragged tensor with shape `[nvals, ...]`.
</td>
</tr><tr>
<td>
`row_lengths`
</td>
<td>
A 1-D integer tensor with shape `[nrows]`.  Must be
nonnegative.  `sum(row_lengths)` must be `nvals`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the RaggedTensor (optional).
</td>
</tr><tr>
<td>
`validate`
</td>
<td>
If true, then use assertions to check that the arguments form
a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
since they must be checked for each tensor value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor`.  `result.rank = values.rank + 1`.
`result.ragged_rank = values.ragged_rank + 1`.
</td>
</tr>

</table>


#### Example:

```
>>> print(tf.RaggedTensor.from_row_lengths(
...     values=[3, 1, 4, 1, 5, 9, 2, 6],
...     row_lengths=[4, 0, 3, 1, 0]))
<tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>
```

<h3 id="from_row_limits"><code>from_row_limits</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L533-L568">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_row_limits(
    values, row_limits, name=None, validate=(True)
)
</code></pre>

Creates a `RaggedTensor` with rows partitioned by `row_limits`.

Equivalent to: `from_row_splits(values, concat([0, row_limits]))`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`values`
</td>
<td>
A potentially ragged tensor with shape `[nvals, ...]`.
</td>
</tr><tr>
<td>
`row_limits`
</td>
<td>
A 1-D integer tensor with shape `[nrows]`.  Must be sorted in
ascending order.  If `nrows>0`, then `row_limits[-1]` must be `nvals`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the RaggedTensor (optional).
</td>
</tr><tr>
<td>
`validate`
</td>
<td>
If true, then use assertions to check that the arguments form
a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
since they must be checked for each tensor value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor`.  `result.rank = values.rank + 1`.
`result.ragged_rank = values.ragged_rank + 1`.
</td>
</tr>

</table>


#### Example:

```
>>> print(tf.RaggedTensor.from_row_limits(
...     values=[3, 1, 4, 1, 5, 9, 2, 6],
...     row_limits=[4, 4, 7, 8, 8]))
<tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>
```

<h3 id="from_row_splits"><code>from_row_splits</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L403-L448">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_row_splits(
    values, row_splits, name=None, validate=(True)
)
</code></pre>

Creates a `RaggedTensor` with rows partitioned by `row_splits`.

The returned `RaggedTensor` corresponds with the python list defined by:

```python
result = [values[row_splits[i]:row_splits[i + 1]]
          for i in range(len(row_splits) - 1)]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`values`
</td>
<td>
A potentially ragged tensor with shape `[nvals, ...]`.
</td>
</tr><tr>
<td>
`row_splits`
</td>
<td>
A 1-D integer tensor with shape `[nrows+1]`.  Must not be
empty, and must be sorted in ascending order.  `row_splits[0]` must be
zero and `row_splits[-1]` must be `nvals`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the RaggedTensor (optional).
</td>
</tr><tr>
<td>
`validate`
</td>
<td>
If true, then use assertions to check that the arguments form
a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
since they must be checked for each tensor value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor`.  `result.rank = values.rank + 1`.
`result.ragged_rank = values.ragged_rank + 1`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `row_splits` is an empty list.
</td>
</tr>
</table>


#### Example:

```
>>> print(tf.RaggedTensor.from_row_splits(
...     values=[3, 1, 4, 1, 5, 9, 2, 6],
...     row_splits=[0, 4, 4, 7, 8, 8]))
<tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>
```

<h3 id="from_row_starts"><code>from_row_starts</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L493-L531">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_row_starts(
    values, row_starts, name=None, validate=(True)
)
</code></pre>

Creates a `RaggedTensor` with rows partitioned by `row_starts`.

Equivalent to: `from_row_splits(values, concat([row_starts, nvals]))`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`values`
</td>
<td>
A potentially ragged tensor with shape `[nvals, ...]`.
</td>
</tr><tr>
<td>
`row_starts`
</td>
<td>
A 1-D integer tensor with shape `[nrows]`.  Must be
nonnegative and sorted in ascending order.  If `nrows>0`, then
`row_starts[0]` must be zero.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the RaggedTensor (optional).
</td>
</tr><tr>
<td>
`validate`
</td>
<td>
If true, then use assertions to check that the arguments form
a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
since they must be checked for each tensor value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor`.  `result.rank = values.rank + 1`.
`result.ragged_rank = values.ragged_rank + 1`.
</td>
</tr>

</table>


#### Example:

```
>>> print(tf.RaggedTensor.from_row_starts(
...     values=[3, 1, 4, 1, 5, 9, 2, 6],
...     row_starts=[0, 4, 4, 7, 8]))
<tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>
```

<h3 id="from_sparse"><code>from_sparse</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1770-L1832">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_sparse(
    st_input, name=None, row_splits_dtype=tf.dtypes.int64
)
</code></pre>

Converts a 2D <a href="../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a> to a `RaggedTensor`.

Each row of the `output` `RaggedTensor` will contain the explicit values
from the same row in `st_input`.  `st_input` must be ragged-right.  If not
it is not ragged-right, then an error will be generated.

#### Example:



```
>>> indices = [[0, 0], [0, 1], [0, 2], [1, 0], [3, 0]]
>>> st = tf.sparse.SparseTensor(indices=indices,
...                             values=[1, 2, 3, 4, 5],
...                             dense_shape=[4, 3])
>>> tf.RaggedTensor.from_sparse(st).to_list()
[[1, 2, 3], [4], [], [5]]
```

Currently, only two-dimensional `SparseTensors` are supported.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`st_input`
</td>
<td>
The sparse tensor to convert.  Must have rank 2.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensors (optional).
</td>
</tr><tr>
<td>
`row_splits_dtype`
</td>
<td>
`dtype` for the returned `RaggedTensor`'s `row_splits`
tensor.  One of <a href="../tf.md#int32"><code>tf.int32</code></a> or <a href="../tf.md#int64"><code>tf.int64</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor` with the same values as `st_input`.
`output.ragged_rank = rank(st_input) - 1`.
`output.shape = [st_input.dense_shape[0], None]`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If the number of dimensions in `st_input` is not known
statically, or is not two.
</td>
</tr>
</table>



<h3 id="from_tensor"><code>from_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1492-L1697">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_tensor(
    tensor, lengths=None, padding=None, ragged_rank=1, name=None,
    row_splits_dtype=tf.dtypes.int64
)
</code></pre>

Converts a <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> into a `RaggedTensor`.

The set of absent/default values may be specified using a vector of lengths
or a padding value (but not both).  If `lengths` is specified, then the
output tensor will satisfy `output[row] = tensor[row][:lengths[row]]`. If
'lengths' is a list of lists or tuple of lists, those lists will be used
as nested row lengths. If `padding` is specified, then any row *suffix*
consisting entirely of `padding` will be excluded from the returned
`RaggedTensor`.  If neither `lengths` nor `padding` is specified, then the
returned `RaggedTensor` will have no absent/default values.

#### Examples:



```
>>> dt = tf.constant([[5, 7, 0], [0, 3, 0], [6, 0, 0]])
>>> tf.RaggedTensor.from_tensor(dt)
<tf.RaggedTensor [[5, 7, 0], [0, 3, 0], [6, 0, 0]]>
>>> tf.RaggedTensor.from_tensor(dt, lengths=[1, 0, 3])
<tf.RaggedTensor [[5], [], [6, 0, 0]]>
```

```
>>> tf.RaggedTensor.from_tensor(dt, padding=0)
<tf.RaggedTensor [[5, 7], [0, 3], [6]]>
```

```
>>> dt = tf.constant([[[5, 0], [7, 0], [0, 0]],
...                   [[0, 0], [3, 0], [0, 0]],
...                   [[6, 0], [0, 0], [0, 0]]])
>>> tf.RaggedTensor.from_tensor(dt, lengths=([2, 0, 3], [1, 1, 2, 0, 1]))
<tf.RaggedTensor [[[5], [7]], [], [[6, 0], [], [0]]]>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`tensor`
</td>
<td>
The `Tensor` to convert.  Must have rank `ragged_rank + 1` or
higher.
</td>
</tr><tr>
<td>
`lengths`
</td>
<td>
An optional set of row lengths, specified using a 1-D integer
`Tensor` whose length is equal to `tensor.shape[0]` (the number of rows
in `tensor`).  If specified, then `output[row]` will contain
`tensor[row][:lengths[row]]`.  Negative lengths are treated as zero. You
may optionally pass a list or tuple of lengths to this argument, which
will be used as nested row lengths to construct a ragged tensor with
multiple ragged dimensions.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
An optional padding value.  If specified, then any row suffix
consisting entirely of `padding` will be excluded from the returned
RaggedTensor.  `padding` is a `Tensor` with the same dtype as `tensor`
and with `shape=tensor.shape[ragged_rank + 1:]`.
</td>
</tr><tr>
<td>
`ragged_rank`
</td>
<td>
Integer specifying the ragged rank for the returned
`RaggedTensor`.  Must be greater than zero.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensors (optional).
</td>
</tr><tr>
<td>
`row_splits_dtype`
</td>
<td>
`dtype` for the returned `RaggedTensor`'s `row_splits`
tensor.  One of <a href="../tf.md#int32"><code>tf.int32</code></a> or <a href="../tf.md#int64"><code>tf.int64</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor` with the specified `ragged_rank`.  The shape of the
returned ragged tensor is compatible with the shape of `tensor`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If both `lengths` and `padding` are specified.
</td>
</tr>
</table>



<h3 id="from_uniform_row_length"><code>from_uniform_row_length</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L570-L643">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_uniform_row_length(
    values, uniform_row_length, nrows=None, validate=(True), name=None
)
</code></pre>

Creates a `RaggedTensor` with rows partitioned by `uniform_row_length`.

This method can be used to create `RaggedTensor`s with multiple uniform
outer dimensions.  For example, a `RaggedTensor` with shape `[2, 2, None]`
can be constructed with this method from a `RaggedTensor` values with shape
`[4, None]`:

```
>>> values = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])
>>> print(values.shape)
(4, None)
>>> rt1 = tf.RaggedTensor.from_uniform_row_length(values, 2)
>>> print(rt1)
<tf.RaggedTensor [[[1, 2, 3], [4]], [[5, 6], [7, 8, 9, 10]]]>
>>> print(rt1.shape)
(2, 2, None)
```

Note that `rt1` only contains one ragged dimension (the innermost
dimension). In contrast, if `from_row_splits` is used to construct a similar
`RaggedTensor`, then that `RaggedTensor` will have two ragged dimensions:

```
>>> rt2 = tf.RaggedTensor.from_row_splits(values, [0, 2, 4])
>>> print(rt2.shape)
(2, None, None)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`values`
</td>
<td>
A potentially ragged tensor with shape `[nvals, ...]`.
</td>
</tr><tr>
<td>
`uniform_row_length`
</td>
<td>
A scalar integer tensor.  Must be nonnegative. The
size of the outer axis of `values` must be evenly divisible by
`uniform_row_length`.
</td>
</tr><tr>
<td>
`nrows`
</td>
<td>
The number of rows in the constructed RaggedTensor.  If not
specified, then it defaults to `nvals/uniform_row_length` (or `0` if
`uniform_row_length==0`).  `nrows` only needs to be specified if
`uniform_row_length` might be zero.  `uniform_row_length*nrows` must
be `nvals`.
</td>
</tr><tr>
<td>
`validate`
</td>
<td>
If true, then use assertions to check that the arguments form
a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
since they must be checked for each tensor value.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the RaggedTensor (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor` that corresponds with the python list defined by:

```python
result = [[values.pop(0) for i in range(uniform_row_length)]
for _ in range(nrows)]
```

`result.rank = values.rank + 1`.
`result.ragged_rank = values.ragged_rank + 1`.
</td>
</tr>

</table>



<h3 id="from_value_rowids"><code>from_value_rowids</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L344-L401">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_value_rowids(
    values, value_rowids, nrows=None, name=None, validate=(True)
)
</code></pre>

Creates a `RaggedTensor` with rows partitioned by `value_rowids`.

The returned `RaggedTensor` corresponds with the python list defined by:

```python
result = [[values[i] for i in range(len(values)) if value_rowids[i] == row]
          for row in range(nrows)]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`values`
</td>
<td>
A potentially ragged tensor with shape `[nvals, ...]`.
</td>
</tr><tr>
<td>
`value_rowids`
</td>
<td>
A 1-D integer tensor with shape `[nvals]`, which corresponds
one-to-one with `values`, and specifies each value's row index.  Must be
nonnegative, and must be sorted in ascending order.
</td>
</tr><tr>
<td>
`nrows`
</td>
<td>
An integer scalar specifying the number of rows.  This should be
specified if the `RaggedTensor` may containing empty training rows. Must
be greater than `value_rowids[-1]` (or zero if `value_rowids` is empty).
Defaults to `value_rowids[-1]` (or zero if `value_rowids` is empty).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the RaggedTensor (optional).
</td>
</tr><tr>
<td>
`validate`
</td>
<td>
If true, then use assertions to check that the arguments form
a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
since they must be checked for each tensor value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor`.  `result.rank = values.rank + 1`.
`result.ragged_rank = values.ragged_rank + 1`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `nrows` is incompatible with `value_rowids`.
</td>
</tr>
</table>


#### Example:

```
>>> print(tf.RaggedTensor.from_value_rowids(
...     values=[3, 1, 4, 1, 5, 9, 2, 6],
...     value_rowids=[0, 0, 0, 0, 2, 2, 2, 3],
...     nrows=5))
<tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>
```

<h3 id="get_shape"><code>get_shape</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L849-L868">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_shape()
</code></pre>

The statically known shape of this ragged tensor.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `TensorShape` containing the statically known shape of this ragged
tensor.  Ragged dimensions have a size of `None`.
</td>
</tr>

</table>


Alias for `shape` property.

#### Examples:



```
>>> tf.ragged.constant([[0], [1, 2]]).get_shape()
TensorShape([2, None])
```

```
>>> tf.ragged.constant(
...    [[[0, 1]], [[1, 2], [3, 4]]], ragged_rank=1).get_shape()
TensorShape([2, None, 2])
```

<h3 id="merge_dims"><code>merge_dims</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1386-L1432">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>merge_dims(
    outer_axis, inner_axis
)
</code></pre>

Merges outer_axis...inner_axis into a single dimension.

Returns a copy of this RaggedTensor with the specified range of dimensions
flattened into a single dimension, with elements in row-major order.

#### Examples:

```
>>> rt = tf.ragged.constant([[[1, 2], [3]], [[4, 5, 6]]])
>>> print(rt.merge_dims(0, 1))
<tf.RaggedTensor [[1, 2], [3], [4, 5, 6]]>
>>> print(rt.merge_dims(1, 2))
<tf.RaggedTensor [[1, 2, 3], [4, 5, 6]]>
>>> print(rt.merge_dims(0, 2))
tf.Tensor([1 2 3 4 5 6], shape=(6,), dtype=int32)
```

To mimic the behavior of `np.flatten` (which flattens all dimensions), use
`rt.merge_dims(0, -1).  To mimic the behavior of `tf.layers.Flatten` (which
flattens all dimensions except the outermost batch dimension), use
`rt.merge_dims(1, -1)`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`outer_axis`
</td>
<td>
`int`: The first dimension in the range of dimensions to
merge. May be negative if `self.shape.rank` is statically known.
</td>
</tr><tr>
<td>
`inner_axis`
</td>
<td>
`int`: The last dimension in the range of dimensions to merge.
May be negative if `self.shape.rank` is statically known.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A copy of this tensor, with the specified dimensions merged into a
single dimension.  The shape of the returned tensor will be
`self.shape[:outer_axis] + [N] + self.shape[inner_axis + 1:]`, where `N`
is the total number of slices in the merged dimensions.
</td>
</tr>

</table>



<h3 id="nested_row_lengths"><code>nested_row_lengths</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1223-L1242">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>nested_row_lengths(
    name=None
)
</code></pre>

Returns a tuple containing the row_lengths for all ragged dimensions.

`rt.nested_row_lengths()` is a tuple containing the `row_lengths` tensors
for all ragged dimensions in `rt`, ordered from outermost to innermost.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensors (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `tuple` of 1-D integer `Tensors`.  The length of the tuple is equal to
`self.ragged_rank`.
</td>
</tr>

</table>



<h3 id="nested_value_rowids"><code>nested_value_rowids</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1064-L1099">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>nested_value_rowids(
    name=None
)
</code></pre>

Returns a tuple containing the value_rowids for all ragged dimensions.

`rt.nested_value_rowids` is a tuple containing the `value_rowids` tensors
for
all ragged dimensions in `rt`, ordered from outermost to innermost.  In
particular, `rt.nested_value_rowids = (rt.value_rowids(),) + value_ids`
where:

    * `value_ids = ()` if `rt.values` is a `Tensor`.
    * `value_ids = rt.values.nested_value_rowids` otherwise.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensors (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `tuple` of 1-D integer `Tensor`s.
</td>
</tr>

</table>


#### Example:

```
>>> rt = tf.ragged.constant(
...     [[[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]]])
>>> for i, ids in enumerate(rt.nested_value_rowids()):
...   print('row ids for dimension %d: %s' % (i+1, ids.numpy()))
row ids for dimension 1: [0 0 0]
row ids for dimension 2: [0 0 0 2 2]
row ids for dimension 3: [0 0 0 0 2 2 2 3]
```

<h3 id="nrows"><code>nrows</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1101-L1122">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>nrows(
    out_type=None, name=None
)
</code></pre>

Returns the number of rows in this ragged tensor.

I.e., the size of the outermost dimension of the tensor.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`out_type`
</td>
<td>
`dtype` for the returned tensor.  Defaults to
`self.row_splits.dtype`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensor (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A scalar `Tensor` with dtype `out_type`.
</td>
</tr>

</table>


#### Example:

```
>>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
>>> print(rt.nrows())  # rt has 5 rows.
tf.Tensor(5, shape=(), dtype=int64)
```

<h3 id="numpy"><code>numpy</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1974-L2012">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>numpy()
</code></pre>

Returns a numpy `array` with the values for this `RaggedTensor`.

Requires that this `RaggedTensor` was constructed in eager execution mode.

Ragged dimensions are encoded using numpy `arrays` with `dtype=object` and
`rank=1`, where each element is a single row.

#### Examples

In the following example, the value returned by <a href="../tf/RaggedTensor.md#numpy"><code>RaggedTensor.numpy()</code></a>
contains three numpy `array` objects: one for each row (with `rank=1` and
`dtype=int64`), and one to combine them (with `rank=1` and `dtype=object`):

```
>>> tf.ragged.constant([[1, 2, 3], [4, 5]], dtype=tf.int64).numpy()
array([array([1, 2, 3]), array([4, 5])], dtype=object)
```

Uniform dimensions are encoded using multidimensional numpy `array`s.  In
the following example, the value returned by <a href="../tf/RaggedTensor.md#numpy"><code>RaggedTensor.numpy()</code></a> contains
a single numpy `array` object, with `rank=2` and `dtype=int64`:

```
>>> tf.ragged.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.int64).numpy()
array([[1, 2, 3], [4, 5, 6]])
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A numpy `array`.
</td>
</tr>

</table>



<h3 id="row_lengths"><code>row_lengths</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1174-L1221">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>row_lengths(
    axis=1, name=None
)
</code></pre>

Returns the lengths of the rows in this ragged tensor.

`rt.row_lengths()[i]` indicates the number of values in the
`i`th row of `rt`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`axis`
</td>
<td>
An integer constant indicating the axis whose row lengths should be
returned.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensor (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A potentially ragged integer Tensor with shape `self.shape[:axis]`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `axis` is out of bounds.
</td>
</tr>
</table>


#### Example:

```
>>> rt = tf.ragged.constant(
...     [[[3, 1, 4], [1]], [], [[5, 9], [2]], [[6]], []])
>>> print(rt.row_lengths())  # lengths of rows in rt
tf.Tensor([2 0 2 1 0], shape=(5,), dtype=int64)
>>> print(rt.row_lengths(axis=2))  # lengths of axis=2 rows.
<tf.RaggedTensor [[3, 1], [], [2, 1], [1], []]>
```

<h3 id="row_limits"><code>row_limits</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1149-L1172">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>row_limits(
    name=None
)
</code></pre>

Returns the limit indices for rows in this ragged tensor.

These indices specify where the values for each row end in
`self.values`.  `rt.row_limits(self)` is equal to `rt.row_splits[:-1]`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensor (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A 1-D integer Tensor with shape `[nrows]`.
The returned tensor is nonnegative, and is sorted in ascending order.
</td>
</tr>

</table>


#### Example:

```
>>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
>>> print(rt.values)
tf.Tensor([3 1 4 1 5 9 2 6], shape=(8,), dtype=int32)
>>> print(rt.row_limits())  # indices of row limits in rt.values
tf.Tensor([4 4 7 8 8], shape=(5,), dtype=int64)
```

<h3 id="row_starts"><code>row_starts</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1124-L1147">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>row_starts(
    name=None
)
</code></pre>

Returns the start indices for rows in this ragged tensor.

These indices specify where the values for each row begin in
`self.values`.  `rt.row_starts()` is equal to `rt.row_splits[:-1]`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensor (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A 1-D integer Tensor with shape `[nrows]`.
The returned tensor is nonnegative, and is sorted in ascending order.
</td>
</tr>

</table>


#### Example:

```
>>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
>>> print(rt.values)
tf.Tensor([3 1 4 1 5 9 2 6], shape=(8,), dtype=int32)
>>> print(rt.row_starts())  # indices of row starts in rt.values
tf.Tensor([0 4 4 7 8], shape=(5,), dtype=int64)
```

<h3 id="to_list"><code>to_list</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L2014-L2027">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_list()
</code></pre>

Returns a nested Python `list` with the values for this `RaggedTensor`.

Requires that `rt` was constructed in eager execution mode.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A nested Python `list`.
</td>
</tr>

</table>



<h3 id="to_sparse"><code>to_sparse</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1834-L1858">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_sparse(
    name=None
)
</code></pre>

Converts this `RaggedTensor` into a <a href="../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a>.


#### Example:



```
>>> rt = tf.ragged.constant([[1, 2, 3], [4], [], [5, 6]])
>>> print(rt.to_sparse())
SparseTensor(indices=tf.Tensor(
                 [[0 0] [0 1] [0 2] [1 0] [3 0] [3 1]],
                 shape=(6, 2), dtype=int64),
             values=tf.Tensor([1 2 3 4 5 6], shape=(6,), dtype=int32),
             dense_shape=tf.Tensor([4 3], shape=(2,), dtype=int64))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensors (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A SparseTensor with the same values as `self`.
</td>
</tr>

</table>



<h3 id="to_tensor"><code>to_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1699-L1768">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_tensor(
    default_value=None, name=None, shape=None
)
</code></pre>

Converts this `RaggedTensor` into a <a href="../tf/Tensor.md"><code>tf.Tensor</code></a>.

If `shape` is specified, then the result is padded and/or truncated to
the specified shape.

#### Examples:



```
>>> rt = tf.ragged.constant([[9, 8, 7], [], [6, 5], [4]])
>>> print(rt.to_tensor())
tf.Tensor(
    [[9 8 7] [0 0 0] [6 5 0] [4 0 0]], shape=(4, 3), dtype=int32)
>>> print(rt.to_tensor(shape=[5, 2]))
tf.Tensor(
    [[9 8] [0 0] [6 5] [4 0] [0 0]], shape=(5, 2), dtype=int32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`default_value`
</td>
<td>
Value to set for indices not specified in `self`. Defaults
to zero.  `default_value` must be broadcastable to
`self.shape[self.ragged_rank + 1:]`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensors (optional).
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
The shape of the resulting dense tensor.  In particular,
`result.shape[i]` is `shape[i]` (if `shape[i]` is not None), or
`self.bounding_shape(i)` (otherwise).`shape.rank` must be `None` or
equal to `self.rank`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with shape `ragged.bounding_shape(self)` and the
values specified by the non-empty values in `self`.  Empty values are
assigned `default_value`.
</td>
</tr>

</table>



<h3 id="value_rowids"><code>value_rowids</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1037-L1062">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>value_rowids(
    name=None
)
</code></pre>

Returns the row indices for the `values` in this ragged tensor.

`rt.value_rowids()` corresponds one-to-one with the outermost dimension of
`rt.values`, and specifies the row containing each value.  In particular,
the row `rt[row]` consists of the values `rt.values[j]` where
`rt.value_rowids()[j] == row`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensor (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A 1-D integer `Tensor` with shape `self.values.shape[:1]`.
The returned tensor is nonnegative, and is sorted in ascending order.
</td>
</tr>

</table>


#### Example:

```
>>> rt = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
>>> print(rt.values)
tf.Tensor([3 1 4 1 5 9 2 6], shape=(8,), dtype=int32)
>>> print(rt.value_rowids())  # corresponds 1:1 with rt.values
tf.Tensor([0 0 0 0 2 2 2 3], shape=(8,), dtype=int64)
```

<h3 id="with_flat_values"><code>with_flat_values</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1334-L1354">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_flat_values(
    new_values
)
</code></pre>

Returns a copy of `self` with `flat_values` replaced by `new_value`.

Preserves cached row-partitioning tensors such as `self.cached_nrows` and
`self.cached_value_rowids` if they have values.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`new_values`
</td>
<td>
Potentially ragged tensor that should replace
`self.flat_values`.  Must have `rank > 0`, and must have the same number
of rows as `self.flat_values`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor`.
`result.rank = self.ragged_rank + new_values.rank`.
`result.ragged_rank = self.ragged_rank + new_values.ragged_rank`.
</td>
</tr>

</table>



<h3 id="with_row_splits_dtype"><code>with_row_splits_dtype</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1356-L1384">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_row_splits_dtype(
    dtype
)
</code></pre>

Returns a copy of this RaggedTensor with the given `row_splits` dtype.

For RaggedTensors with multiple ragged dimensions, the `row_splits` for all
nested `RaggedTensor` objects are cast to the given dtype.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`dtype`
</td>
<td>
The dtype for `row_splits`.  One of <a href="../tf.md#int32"><code>tf.int32</code></a> or <a href="../tf.md#int64"><code>tf.int64</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A copy of this RaggedTensor, with the `row_splits` cast to the given
type.
</td>
</tr>

</table>



<h3 id="with_values"><code>with_values</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor.py#L1305-L1332">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_values(
    new_values
)
</code></pre>

Returns a copy of `self` with `values` replaced by `new_value`.

Preserves cached row-partitioning tensors such as `self.cached_nrows` and
`self.cached_value_rowids` if they have values.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`new_values`
</td>
<td>
Potentially ragged tensor to use as the `values` for the
returned `RaggedTensor`.  Must have `rank > 0`, and must have the same
number of rows as `self.values`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor`.  `result.rank = 1 + new_values.rank`.
`result.ragged_rank = 1 + new_values.ragged_rank`
</td>
</tr>

</table>



<h3 id="__abs__"><code>__abs__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L358-L401">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__abs__(
    x, name=None
)
</code></pre>

Computes the absolute value of a tensor.

Given a tensor of integer or floating-point values, this operation returns a
tensor of the same type, where each element contains the absolute value of the
corresponding element in the input.

Given a tensor `x` of complex numbers, this operation returns a tensor of type
`float32` or `float64` that is the absolute value of each element in `x`. For
a complex number \\(a + bj\\), its absolute value is computed as
\\(\sqrt{a^2 + b^2}\\).

#### For example:



```
>>> # real number
>>> x = tf.constant([-2.25, 3.25])
>>> tf.abs(x)
<tf.Tensor: shape=(2,), dtype=float32,
numpy=array([2.25, 3.25], dtype=float32)>
```

```
>>> # complex number
>>> x = tf.constant([[-2.25 + 4.75j], [-3.25 + 5.75j]])
>>> tf.abs(x)
<tf.Tensor: shape=(2, 1), dtype=float64, numpy=
array([[5.25594901],
       [6.60492241]])>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor` or `SparseTensor` of type `float16`, `float32`, `float64`,
`int32`, `int64`, `complex64` or `complex128`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` or `SparseTensor` of the same size, type and sparsity as `x`,
with absolute values. Note, for `complex64` or `complex128` input, the
returned `Tensor` will be of type `float32` or `float64`, respectively.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.abs(x.values, ...), x.dense_shape)`
</td>
</tr>

</table>



<h3 id="__add__"><code>__add__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__add__(
    x, y, name=None
)
</code></pre>

Returns x + y element-wise.

*NOTE*: <a href="../tf/math/add.md"><code>math.add</code></a> supports broadcasting. `AddN` does not. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

Given two input tensors, the <a href="../tf/math/add.md"><code>tf.add</code></a> operation computes the sum for every element in the tensor.

Both input and output have a range `(-inf, inf)`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `string`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `x`.
</td>
</tr>

</table>



<h3 id="__and__"><code>__and__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L1568-L1607">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__and__(
    x, y, name=None
)
</code></pre>

Logical AND function.

The operation works for the following input types:

- Two single elements of type `bool`
- One <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> of type `bool` and one single `bool`, where the result will
  be calculated by applying logical AND with the single element to each
  element in the larger Tensor.
- Two <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> objects of type `bool` of the same shape. In this case,
  the result will be the element-wise logical AND of the two input tensors.

#### Usage:



```
>>> a = tf.constant([True])
>>> b = tf.constant([False])
>>> tf.math.logical_and(a, b)
<tf.Tensor: shape=(1,), dtype=bool, numpy=array([False])>
```

```
>>> c = tf.constant([True])
>>> x = tf.constant([False, True, True, False])
>>> tf.math.logical_and(c, x)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False,  True,  True, False])>
```

```
>>> y = tf.constant([False, False, True, True])
>>> z = tf.constant([False, True, False, True])
>>> tf.math.logical_and(y, z)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, False, False,  True])>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> type bool.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> of type bool.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> of type bool with the same size as that of x or y.
</td>
</tr>

</table>



<h3 id="__bool__"><code>__bool__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_operators.py#L89-L91">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__bool__(
    _
)
</code></pre>

Dummy method to prevent a RaggedTensor from being used as a Python bool.


<h3 id="__div__"><code>__div__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L1339-L1363">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__div__(
    x, y, name=None
)
</code></pre>

Divides x / y elementwise (using Python 2 division operator semantics). (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Deprecated in favor of operator or tf.math.divide.

NOTE: Prefer using the Tensor division operator or tf.divide which obey Python
3 division operator semantics.

This function divides `x` and `y`, forcing Python 2 semantics. That is, if `x`
and `y` are both integers then the result will be an integer. This is in
contrast to Python 3, where division with `/` is always a float while division
with `//` is always an integer.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
`Tensor` numerator of real numeric type.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
`Tensor` denominator of real numeric type.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`x / y` returns the quotient of x and y.
</td>
</tr>

</table>



<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L1718-L1753">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

The operation invoked by the <a href="../tf/RaggedTensor.md#__eq__"><code>Tensor.__eq__</code></a> operator.

Compares two tensors element-wise for equality if they are
broadcast-compatible; or returns False if they are not broadcast-compatible.
(Note that this behavior differs from <a href="../tf/math/equal.md"><code>tf.math.equal</code></a>, which raises an
exception if the two tensors are not broadcast-compatible.)

#### Purpose in the API:


This method is exposed in TensorFlow's API so that library developers
can register dispatching for <a href="../tf/RaggedTensor.md#__eq__"><code>Tensor.__eq__</code></a> to allow it to handle
custom composite tensors & other custom objects.

The API symbol is not intended to be called by users directly and does
appear in TensorFlow's generated documentation.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`self`
</td>
<td>
The left-hand side of the `==` operator.
</td>
</tr><tr>
<td>
`other`
</td>
<td>
The right-hand side of the `==` operator.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The result of the elementwise `==` operation, or `False` if the arguments
are not broadcast-compatible.
</td>
</tr>

</table>



<h3 id="__floordiv__"><code>__floordiv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L1419-L1447">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__floordiv__(
    x, y, name=None
)
</code></pre>

Divides `x / y` elementwise, rounding toward the most negative integer.

The same as <a href="../tf/RaggedTensor.md#__div__"><code>tf.compat.v1.div(x,y)</code></a> for integers, but uses
`tf.floor(tf.compat.v1.div(x,y))` for
floating point arguments so that the result is always an integer (though
possibly an integer represented as floating point).  This op is generated by
`x // y` floor division in Python 3 and in Python 2.7 with
`from __future__ import division`.

`x` and `y` must have the same type, and the result will have the same type
as well.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
`Tensor` numerator of real numeric type.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
`Tensor` denominator of real numeric type.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`x / y` rounded down.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If the inputs are complex.
</td>
</tr>
</table>



<h3 id="__ge__"><code>__ge__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ge__(
    x, y, name=None
)
</code></pre>

Returns the truth value of (x >= y) element-wise.

*NOTE*: <a href="../tf/math/greater_equal.md"><code>math.greater_equal</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Example:



```python
x = tf.constant([5, 4, 6, 7])
y = tf.constant([5, 2, 5, 10])
tf.math.greater_equal(x, y) ==> [True, True, True, False]

x = tf.constant([5, 4, 6, 7])
y = tf.constant([5])
tf.math.greater_equal(x, y) ==> [True, False, True, True]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `bool`.
</td>
</tr>

</table>



<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_getitem.py#L35-L103">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__getitem__(
    key
)
</code></pre>

Returns the specified piece of this RaggedTensor.

Supports multidimensional indexing and slicing, with one restriction:
indexing into a ragged inner dimension is not allowed.  This case is
problematic because the indicated value may exist in some rows but not
others.  In such cases, it's not obvious whether we should (1) report an
IndexError; (2) use a default value; or (3) skip that value and return a
tensor with fewer rows than we started with.  Following the guiding
principles of Python ("In the face of ambiguity, refuse the temptation to
guess"), we simply disallow this operation.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`self`
</td>
<td>
The RaggedTensor to slice.
</td>
</tr><tr>
<td>
`key`
</td>
<td>
Indicates which piece of the RaggedTensor to return, using standard
Python semantics (e.g., negative values index from the end).  `key`
may have any of the following types:

* `int` constant
* Scalar integer `Tensor`
* `slice` containing integer constants and/or scalar integer
`Tensor`s
* `Ellipsis`
* <a href="../tf.md#newaxis"><code>tf.newaxis</code></a>
* `tuple` containing any of the above (for multidimensional indexing)
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` or `RaggedTensor` object.  Values that include at least one
ragged dimension are returned as `RaggedTensor`.  Values that include no
ragged dimensions are returned as `Tensor`.  See above for examples of
expressions that return `Tensor`s vs `RaggedTensor`s.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `key` is out of bounds.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `key` is not supported.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If the indices in `key` have an unsupported type.
</td>
</tr>
</table>



#### Examples:



```
>>> # A 2-D ragged tensor with 1 ragged dimension.
>>> rt = tf.ragged.constant([['a', 'b', 'c'], ['d', 'e'], ['f'], ['g']])
>>> rt[0].numpy()                 # First row (1-D `Tensor`)
array([b'a', b'b', b'c'], dtype=object)
>>> rt[:3].to_list()              # First three rows (2-D RaggedTensor)
[[b'a', b'b', b'c'], [b'd', b'e'], [b'f']]
>>> rt[3, 0].numpy()              # 1st element of 4th row (scalar)
b'g'
```

```
>>> # A 3-D ragged tensor with 2 ragged dimensions.
>>> rt = tf.ragged.constant([[[1, 2, 3], [4]],
...                          [[5], [], [6]],
...                          [[7]],
...                          [[8, 9], [10]]])
>>> rt[1].to_list()               # Second row (2-D RaggedTensor)
[[5], [], [6]]
>>> rt[3, 0].numpy()              # First element of fourth row (1-D Tensor)
array([8, 9], dtype=int32)
>>> rt[:, 1:3].to_list()          # Items 1-3 of each row (3-D RaggedTensor)
[[[4]], [[], [6]], [], [[10]]]
>>> rt[:, -1:].to_list()          # Last item of each row (3-D RaggedTensor)
[[[4]], [[6]], [[7]], [[10]]]
```

<h3 id="__gt__"><code>__gt__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__gt__(
    x, y, name=None
)
</code></pre>

Returns the truth value of (x > y) element-wise.

*NOTE*: <a href="../tf/math/greater.md"><code>math.greater</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Example:



```python
x = tf.constant([5, 4, 6])
y = tf.constant([5, 2, 5])
tf.math.greater(x, y) ==> [False, True, True]

x = tf.constant([5, 4, 6])
y = tf.constant([5])
tf.math.greater(x, y) ==> [False, False, True]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `bool`.
</td>
</tr>

</table>



<h3 id="__invert__"><code>__invert__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__invert__(
    x, name=None
)
</code></pre>

Returns the truth value of `NOT x` element-wise.


#### Example:



```
>>> tf.math.logical_not(tf.constant([True, False]))
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([False,  True])>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor` of type `bool`. A `Tensor` of type `bool`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `bool`.
</td>
</tr>

</table>



<h3 id="__le__"><code>__le__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__le__(
    x, y, name=None
)
</code></pre>

Returns the truth value of (x <= y) element-wise.

*NOTE*: <a href="../tf/math/less_equal.md"><code>math.less_equal</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Example:



```python
x = tf.constant([5, 4, 6])
y = tf.constant([5])
tf.math.less_equal(x, y) ==> [True, True, False]

x = tf.constant([5, 4, 6])
y = tf.constant([5, 6, 6])
tf.math.less_equal(x, y) ==> [True, True, True]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `bool`.
</td>
</tr>

</table>



<h3 id="__lt__"><code>__lt__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__lt__(
    x, y, name=None
)
</code></pre>

Returns the truth value of (x < y) element-wise.

*NOTE*: <a href="../tf/math/less.md"><code>math.less</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Example:



```python
x = tf.constant([5, 4, 6])
y = tf.constant([5])
tf.math.less(x, y) ==> [False, True, False]

x = tf.constant([5, 4, 6])
y = tf.constant([5, 6, 7])
tf.math.less(x, y) ==> [False, True, True]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `bool`.
</td>
</tr>

</table>



<h3 id="__mod__"><code>__mod__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__mod__(
    x, y, name=None
)
</code></pre>

Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

true, this follows Python semantics in that the result here is consistent
with a flooring divide. E.g. `floor(x / y) * y + mod(x, y) = x`.

*NOTE*: <a href="../tf/math/floormod.md"><code>math.floormod</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`, `uint64`, `bfloat16`, `half`, `float32`, `float64`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `x`.
</td>
</tr>

</table>



<h3 id="__mul__"><code>__mul__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L472-L518">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__mul__(
    x, y, name=None
)
</code></pre>

Returns an element-wise x * y.


#### For example:



```
>>> x = tf.constant(([1, 2, 3, 4]))
>>> tf.math.multiply(x, x)
<tf.Tensor: shape=(4,), dtype=..., numpy=array([ 1,  4,  9, 16], dtype=int32)>
```

Since <a href="../tf/math/multiply.md"><code>tf.math.multiply</code></a> will convert its arguments to `Tensor`s, you can also
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
<tr><th colspan="2">Args</th></tr>

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
<tr><th colspan="2">Returns</th></tr>


</table>


A `Tensor`.  Has the same type as `x`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>
<tr class="alt">
<td colspan="2">
* InvalidArgumentError: When `x` and `y` have incomptatible shapes or types.
</td>
</tr>

</table>



<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L1756-L1789">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ne__(
    other
)
</code></pre>

The operation invoked by the <a href="../tf/RaggedTensor.md#__ne__"><code>Tensor.__ne__</code></a> operator.

Compares two tensors element-wise for inequality if they are
broadcast-compatible; or returns True if they are not broadcast-compatible.
(Note that this behavior differs from <a href="../tf/math/not_equal.md"><code>tf.math.not_equal</code></a>, which raises an
exception if the two tensors are not broadcast-compatible.)

#### Purpose in the API:


This method is exposed in TensorFlow's API so that library developers
can register dispatching for <a href="../tf/RaggedTensor.md#__ne__"><code>Tensor.__ne__</code></a> to allow it to handle
custom composite tensors & other custom objects.

The API symbol is not intended to be called by users directly and does
appear in TensorFlow's generated documentation.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`self`
</td>
<td>
The left-hand side of the `!=` operator.
</td>
</tr><tr>
<td>
`other`
</td>
<td>
The right-hand side of the `!=` operator.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The result of the elementwise `!=` operation, or `True` if the arguments
are not broadcast-compatible.
</td>
</tr>

</table>



<h3 id="__neg__"><code>__neg__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__neg__(
    x, name=None
)
</code></pre>

Computes numerical negative value element-wise.

I.e., \\(y = -x\\).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `x`.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.negative(x.values, ...), x.dense_shape)`
</td>
</tr>

</table>



<h3 id="__nonzero__"><code>__nonzero__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_operators.py#L89-L91">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__nonzero__(
    _
)
</code></pre>

Dummy method to prevent a RaggedTensor from being used as a Python bool.


<h3 id="__or__"><code>__or__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__or__(
    x, y, name=None
)
</code></pre>

Returns the truth value of x OR y element-wise.

*NOTE*: <a href="../tf/math/logical_or.md"><code>math.logical_or</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor` of type `bool`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A `Tensor` of type `bool`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `bool`.
</td>
</tr>

</table>



<h3 id="__pow__"><code>__pow__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L645-L670">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__pow__(
    x, y, name=None
)
</code></pre>

Computes the power of one value to another.

Given a tensor `x` and a tensor `y`, this operation computes \\(x^y\\) for
corresponding elements in `x` and `y`. For example:

```python
x = tf.constant([[2, 2], [3, 3]])
y = tf.constant([[8, 16], [2, 3]])
tf.pow(x, y)  # [[256, 65536], [9, 27]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
`complex64`, or `complex128`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
`complex64`, or `complex128`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`.
</td>
</tr>

</table>



<h3 id="__radd__"><code>__radd__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__radd__(
    x, y, name=None
)
</code></pre>

Returns x + y element-wise.

*NOTE*: <a href="../tf/math/add.md"><code>math.add</code></a> supports broadcasting. `AddN` does not. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

Given two input tensors, the <a href="../tf/math/add.md"><code>tf.add</code></a> operation computes the sum for every element in the tensor.

Both input and output have a range `(-inf, inf)`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `string`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `x`.
</td>
</tr>

</table>



<h3 id="__rand__"><code>__rand__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L1568-L1607">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rand__(
    x, y, name=None
)
</code></pre>

Logical AND function.

The operation works for the following input types:

- Two single elements of type `bool`
- One <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> of type `bool` and one single `bool`, where the result will
  be calculated by applying logical AND with the single element to each
  element in the larger Tensor.
- Two <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> objects of type `bool` of the same shape. In this case,
  the result will be the element-wise logical AND of the two input tensors.

#### Usage:



```
>>> a = tf.constant([True])
>>> b = tf.constant([False])
>>> tf.math.logical_and(a, b)
<tf.Tensor: shape=(1,), dtype=bool, numpy=array([False])>
```

```
>>> c = tf.constant([True])
>>> x = tf.constant([False, True, True, False])
>>> tf.math.logical_and(c, x)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False,  True,  True, False])>
```

```
>>> y = tf.constant([False, False, True, True])
>>> z = tf.constant([False, True, False, True])
>>> tf.math.logical_and(y, z)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, False, False,  True])>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> type bool.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> of type bool.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> of type bool with the same size as that of x or y.
</td>
</tr>

</table>



<h3 id="__rdiv__"><code>__rdiv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L1339-L1363">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rdiv__(
    x, y, name=None
)
</code></pre>

Divides x / y elementwise (using Python 2 division operator semantics). (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Deprecated in favor of operator or tf.math.divide.

NOTE: Prefer using the Tensor division operator or tf.divide which obey Python
3 division operator semantics.

This function divides `x` and `y`, forcing Python 2 semantics. That is, if `x`
and `y` are both integers then the result will be an integer. This is in
contrast to Python 3, where division with `/` is always a float while division
with `//` is always an integer.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
`Tensor` numerator of real numeric type.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
`Tensor` denominator of real numeric type.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`x / y` returns the quotient of x and y.
</td>
</tr>

</table>



<h3 id="__rfloordiv__"><code>__rfloordiv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L1419-L1447">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rfloordiv__(
    x, y, name=None
)
</code></pre>

Divides `x / y` elementwise, rounding toward the most negative integer.

The same as <a href="../tf/RaggedTensor.md#__div__"><code>tf.compat.v1.div(x,y)</code></a> for integers, but uses
`tf.floor(tf.compat.v1.div(x,y))` for
floating point arguments so that the result is always an integer (though
possibly an integer represented as floating point).  This op is generated by
`x // y` floor division in Python 3 and in Python 2.7 with
`from __future__ import division`.

`x` and `y` must have the same type, and the result will have the same type
as well.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
`Tensor` numerator of real numeric type.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
`Tensor` denominator of real numeric type.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`x / y` rounded down.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If the inputs are complex.
</td>
</tr>
</table>



<h3 id="__rmod__"><code>__rmod__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rmod__(
    x, y, name=None
)
</code></pre>

Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

true, this follows Python semantics in that the result here is consistent
with a flooring divide. E.g. `floor(x / y) * y + mod(x, y) = x`.

*NOTE*: <a href="../tf/math/floormod.md"><code>math.floormod</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`, `uint64`, `bfloat16`, `half`, `float32`, `float64`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `x`.
</td>
</tr>

</table>



<h3 id="__rmul__"><code>__rmul__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L472-L518">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rmul__(
    x, y, name=None
)
</code></pre>

Returns an element-wise x * y.


#### For example:



```
>>> x = tf.constant(([1, 2, 3, 4]))
>>> tf.math.multiply(x, x)
<tf.Tensor: shape=(4,), dtype=..., numpy=array([ 1,  4,  9, 16], dtype=int32)>
```

Since <a href="../tf/math/multiply.md"><code>tf.math.multiply</code></a> will convert its arguments to `Tensor`s, you can also
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
<tr><th colspan="2">Args</th></tr>

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
<tr><th colspan="2">Returns</th></tr>


</table>


A `Tensor`.  Has the same type as `x`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>
<tr class="alt">
<td colspan="2">
* InvalidArgumentError: When `x` and `y` have incomptatible shapes or types.
</td>
</tr>

</table>



<h3 id="__ror__"><code>__ror__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ror__(
    x, y, name=None
)
</code></pre>

Returns the truth value of x OR y element-wise.

*NOTE*: <a href="../tf/math/logical_or.md"><code>math.logical_or</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor` of type `bool`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A `Tensor` of type `bool`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `bool`.
</td>
</tr>

</table>



<h3 id="__rpow__"><code>__rpow__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L645-L670">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rpow__(
    x, y, name=None
)
</code></pre>

Computes the power of one value to another.

Given a tensor `x` and a tensor `y`, this operation computes \\(x^y\\) for
corresponding elements in `x` and `y`. For example:

```python
x = tf.constant([[2, 2], [3, 3]])
y = tf.constant([[8, 16], [2, 3]])
tf.pow(x, y)  # [[256, 65536], [9, 27]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
`complex64`, or `complex128`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
`complex64`, or `complex128`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`.
</td>
</tr>

</table>



<h3 id="__rsub__"><code>__rsub__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L533-L561">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rsub__(
    x, y, name=None
)
</code></pre>

Returns x - y element-wise.

*NOTE*: `Subtract` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `uint32`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `x`.
</td>
</tr>

</table>



<h3 id="__rtruediv__"><code>__rtruediv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L1306-L1336">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rtruediv__(
    x, y, name=None
)
</code></pre>

Divides x / y elementwise (using Python 3 division operator semantics).

NOTE: Prefer using the Tensor operator or tf.divide which obey Python
division operator semantics.

This function forces Python 3 division operator semantics where all integer
arguments are cast to floating types first.   This op is generated by normal
`x / y` division in Python 3 and in Python 2.7 with
`from __future__ import division`.  If you want integer division that rounds
down, use `x // y` or `tf.math.floordiv`.

`x` and `y` must have the same numeric type.  If the inputs are floating
point, the output will have the same type.  If the inputs are integral, the
inputs are cast to `float32` for `int8` and `int16` and `float64` for `int32`
and `int64` (matching the behavior of Numpy).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
`Tensor` numerator of numeric type.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
`Tensor` denominator of numeric type.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`x / y` evaluated in floating point.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `x` and `y` have different dtypes.
</td>
</tr>
</table>



<h3 id="__rxor__"><code>__rxor__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L1519-L1565">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rxor__(
    x, y, name='LogicalXor'
)
</code></pre>

Logical XOR function.

x ^ y = (x | y) & ~(x & y)

The operation works for the following input types:

- Two single elements of type `bool`
- One <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> of type `bool` and one single `bool`, where the result will
  be calculated by applying logical XOR with the single element to each
  element in the larger Tensor.
- Two <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> objects of type `bool` of the same shape. In this case,
  the result will be the element-wise logical XOR of the two input tensors.

#### Usage:



```
>>> a = tf.constant([True])
>>> b = tf.constant([False])
>>> tf.math.logical_xor(a, b)
<tf.Tensor: shape=(1,), dtype=bool, numpy=array([ True])>
```

```
>>> c = tf.constant([True])
>>> x = tf.constant([False, True, True, False])
>>> tf.math.logical_xor(c, x)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([ True, False, False,  True])>
```

```
>>> y = tf.constant([False, False, True, True])
>>> z = tf.constant([False, True, False, True])
>>> tf.math.logical_xor(y, z)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False,  True,  True, False])>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> type bool.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> of type bool.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> of type bool with the same size as that of x or y.
</td>
</tr>

</table>



<h3 id="__sub__"><code>__sub__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L533-L561">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__sub__(
    x, y, name=None
)
</code></pre>

Returns x - y element-wise.

*NOTE*: `Subtract` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `uint32`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `x`.
</td>
</tr>

</table>



<h3 id="__truediv__"><code>__truediv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L1306-L1336">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__truediv__(
    x, y, name=None
)
</code></pre>

Divides x / y elementwise (using Python 3 division operator semantics).

NOTE: Prefer using the Tensor operator or tf.divide which obey Python
division operator semantics.

This function forces Python 3 division operator semantics where all integer
arguments are cast to floating types first.   This op is generated by normal
`x / y` division in Python 3 and in Python 2.7 with
`from __future__ import division`.  If you want integer division that rounds
down, use `x // y` or `tf.math.floordiv`.

`x` and `y` must have the same numeric type.  If the inputs are floating
point, the output will have the same type.  If the inputs are integral, the
inputs are cast to `float32` for `int8` and `int16` and `float64` for `int32`
and `int64` (matching the behavior of Numpy).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
`Tensor` numerator of numeric type.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
`Tensor` denominator of numeric type.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`x / y` evaluated in floating point.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `x` and `y` have different dtypes.
</td>
</tr>
</table>



<h3 id="__xor__"><code>__xor__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L1519-L1565">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__xor__(
    x, y, name='LogicalXor'
)
</code></pre>

Logical XOR function.

x ^ y = (x | y) & ~(x & y)

The operation works for the following input types:

- Two single elements of type `bool`
- One <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> of type `bool` and one single `bool`, where the result will
  be calculated by applying logical XOR with the single element to each
  element in the larger Tensor.
- Two <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> objects of type `bool` of the same shape. In this case,
  the result will be the element-wise logical XOR of the two input tensors.

#### Usage:



```
>>> a = tf.constant([True])
>>> b = tf.constant([False])
>>> tf.math.logical_xor(a, b)
<tf.Tensor: shape=(1,), dtype=bool, numpy=array([ True])>
```

```
>>> c = tf.constant([True])
>>> x = tf.constant([False, True, True, False])
>>> tf.math.logical_xor(c, x)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([ True, False, False,  True])>
```

```
>>> y = tf.constant([False, False, True, True])
>>> z = tf.constant([False, True, False, True])
>>> tf.math.logical_xor(y, z)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False,  True,  True, False])>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`x`
</td>
<td>
A <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> type bool.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> of type bool.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> of type bool with the same size as that of x or y.
</td>
</tr>

</table>





