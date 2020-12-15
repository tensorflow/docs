description: Configuration for passing a RaggedTensor input feature.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.RaggedFeature" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="RowLengths"/>
<meta itemprop="property" content="RowLimits"/>
<meta itemprop="property" content="RowSplits"/>
<meta itemprop="property" content="RowStarts"/>
<meta itemprop="property" content="UniformRowLength"/>
<meta itemprop="property" content="ValueRowIds"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="partitions"/>
<meta itemprop="property" content="row_splits_dtype"/>
<meta itemprop="property" content="validate"/>
<meta itemprop="property" content="value_key"/>
</div>

# tf.io.RaggedFeature

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/parsing_config.py#L58-L220">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Configuration for passing a RaggedTensor input feature.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.io.RaggedFeature`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.RaggedFeature(
    dtype, value_key=None, partitions=(), row_splits_dtype=tf.dtypes.int32,
    validate=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

`value_key` specifies the feature key for a variable-length list of values;
and `partitions` specifies zero or more feature keys for partitioning those
values into higher dimensions.  Each element of `partitions` must be one of
the following:

  * `tf.io.RaggedFeature.RowSplits(key: string)`
  * `tf.io.RaggedFeature.RowLengths(key: string)`
  * `tf.io.RaggedFeature.RowStarts(key: string)`
  * `tf.io.RaggedFeature.RowLimits(key: string)`
  * `tf.io.RaggedFeature.ValueRowIds(key: string)`
  * `tf.io.RaggedFeature.UniformRowLength(length: int)`.

Where `key` is a feature key whose values are used to partition the values.
Partitions are listed from outermost to innermost.

* If `len(partitions) == 0` (the default), then:

  * A feature from a single `tf.Example` is parsed into a 1D <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a>.
  * A feature from a batch of `tf.Example`s is parsed into a 2D
    <a href="../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>, where the outer dimension is the batch dimension, and
    the inner (ragged) dimension is the feature length in each example.

* If `len(partitions) == 1`, then:

  * A feature from a single `tf.Example` is parsed into a 2D
    <a href="../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>, where the values taken from the `value_key` are
    separated into rows using the partition key.
  * A feature from a batch of `tf.Example`s is parsed into a 3D
    <a href="../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>, where the outer dimension is the batch dimension,
    the two inner dimensions are formed by separating the `value_key` values
    from each example into rows using that example's partition key.

* If `len(partitions) > 1`, then:

  * A feature from a single `tf.Example` is parsed into a <a href="../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>
    whose rank is `len(partitions)+1`, and whose ragged_rank is
    `len(partitions)`.

  * A feature from a batch of `tf.Example`s is parsed into a <a href="../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>
    whose rank is `len(partitions)+2` and whose ragged_rank is
    `len(partitions)+1`, where the outer dimension is the batch dimension.

There is one exception: if the final (i.e., innermost) element(s) of
`partitions` are `UniformRowLength`s, then the values are simply reshaped (as
a higher-dimensional <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a>), rather than being wrapped in a
<a href="../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>.

#### Examples

```
>>> import google.protobuf.text_format as pbtext
>>> example_batch = [
...   pbtext.Merge(r'''
...     features {
...       feature {key: "v" value {int64_list {value: [3, 1, 4, 1, 5, 9]}}}
...       feature {key: "s1" value {int64_list {value: [0, 2, 3, 3, 6]}}}
...       feature {key: "s2" value {int64_list {value: [0, 2, 3, 4]}}}
...     }''', tf.train.Example()).SerializeToString(),
...   pbtext.Merge(r'''
...     features {
...       feature {key: "v" value {int64_list {value: [2, 7, 1, 8, 2, 8, 1]}}}
...       feature {key: "s1" value {int64_list {value: [0, 3, 4, 5, 7]}}}
...       feature {key: "s2" value {int64_list {value: [0, 1, 1, 4]}}}
...     }''', tf.train.Example()).SerializeToString()]
```

```
>>> features = {
...     # Zero partitions: returns 1D tf.Tensor for each Example.
...     'f1': tf.io.RaggedFeature(value_key="v", dtype=tf.int64),
...     # One partition: returns 2D tf.RaggedTensor for each Example.
...     'f2': tf.io.RaggedFeature(value_key="v", dtype=tf.int64, partitions=[
...         tf.io.RaggedFeature.RowSplits("s1")]),
...     # Two partitions: returns 3D tf.RaggedTensor for each Example.
...     'f3': tf.io.RaggedFeature(value_key="v", dtype=tf.int64, partitions=[
...         tf.io.RaggedFeature.RowSplits("s2"),
...         tf.io.RaggedFeature.RowSplits("s1")])
... }
```

```
>>> feature_dict = tf.io.parse_single_example(example_batch[0], features)
>>> for (name, val) in sorted(feature_dict.items()):
...   print('%s: %s' % (name, val))
f1: tf.Tensor([3 1 4 1 5 9], shape=(6,), dtype=int64)
f2: <tf.RaggedTensor [[3, 1], [4], [], [1, 5, 9]]>
f3: <tf.RaggedTensor [[[3, 1], [4]], [[]], [[1, 5, 9]]]>
```

```
>>> feature_dict = tf.io.parse_example(example_batch, features)
>>> for (name, val) in sorted(feature_dict.items()):
...   print('%s: %s' % (name, val))
f1: <tf.RaggedTensor [[3, 1, 4, 1, 5, 9],
                      [2, 7, 1, 8, 2, 8, 1]]>
f2: <tf.RaggedTensor [[[3, 1], [4], [], [1, 5, 9]],
                      [[2, 7, 1], [8], [2], [8, 1]]]>
f3: <tf.RaggedTensor [[[[3, 1], [4]], [[]], [[1, 5, 9]]],
                      [[[2, 7, 1]], [], [[8], [2], [8, 1]]]]>
```

#### Fields:


* <b>`dtype`</b>: Data type of the `RaggedTensor`.  Must be one of:
  <a href="../../tf/dtypes.md#int64"><code>tf.dtypes.int64</code></a>, <a href="../../tf/dtypes.md#float32"><code>tf.dtypes.float32</code></a>, <a href="../../tf/dtypes.md#string"><code>tf.dtypes.string</code></a>.
* <b>`value_key`</b>: (Optional.) Key for a `Feature` in the input `Example`, whose
  parsed `Tensor` will be the resulting <a href="../../tf/RaggedTensor.md#flat_values"><code>RaggedTensor.flat_values</code></a>.  If
  not specified, then it defaults to the key for this `RaggedFeature`.
* <b>`partitions`</b>: (Optional.) A list of objects specifying the row-partitioning
  tensors (from outermost to innermost).  Each entry in this list must be
  one of:
    * `tf.io.RaggedFeature.RowSplits(key: string)`
    * `tf.io.RaggedFeature.RowLengths(key: string)`
    * `tf.io.RaggedFeature.RowStarts(key: string)`
    * `tf.io.RaggedFeature.RowLimits(key: string)`
    * `tf.io.RaggedFeature.ValueRowIds(key: string)`
    * `tf.io.RaggedFeature.UniformRowLength(length: int)`.
  Where `key` is a key for a `Feature` in the input `Example`, whose parsed
  `Tensor` will be the resulting row-partitioning tensor.
* <b>`row_splits_dtype`</b>: (Optional.) Data type for the row-partitioning tensor(s).
  One of `int32` or `int64`.  Defaults to `int32`.
* <b>`validate`</b>: (Optional.) Boolean indicating whether or not to validate that
  the input values form a valid RaggedTensor.  Defaults to `False`.




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`dtype`
</td>
<td>

</td>
</tr><tr>
<td>
`value_key`
</td>
<td>

</td>
</tr><tr>
<td>
`partitions`
</td>
<td>

</td>
</tr><tr>
<td>
`row_splits_dtype`
</td>
<td>

</td>
</tr><tr>
<td>
`validate`
</td>
<td>

</td>
</tr>
</table>



## Child Classes
[`class RowLengths`](../../tf/io/RaggedFeature/RowLengths.md)

[`class RowLimits`](../../tf/io/RaggedFeature/RowLimits.md)

[`class RowSplits`](../../tf/io/RaggedFeature/RowSplits.md)

[`class RowStarts`](../../tf/io/RaggedFeature/RowStarts.md)

[`class UniformRowLength`](../../tf/io/RaggedFeature/UniformRowLength.md)

[`class ValueRowIds`](../../tf/io/RaggedFeature/ValueRowIds.md)

## Class Variables

* `dtype` <a id="dtype"></a>
* `partitions` <a id="partitions"></a>
* `row_splits_dtype` <a id="row_splits_dtype"></a>
* `validate` <a id="validate"></a>
* `value_key` <a id="value_key"></a>
