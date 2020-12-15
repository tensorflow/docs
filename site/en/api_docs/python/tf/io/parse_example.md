description: Parses Example protos into a dict of tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.parse_example" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.parse_example

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/parsing_ops.py#L80-L315">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Parses `Example` protos into a `dict` of tensors.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.parse_example(
    serialized, features, example_names=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Parses a number of serialized [`Example`](https://www.tensorflow.org/code/tensorflow/core/example/example.proto)
protos given in `serialized`. We refer to `serialized` as a batch with
`batch_size` many entries of individual `Example` protos.

`example_names` may contain descriptive names for the corresponding serialized
protos. These may be useful for debugging purposes, but they have no effect on
the output. If not `None`, `example_names` must be the same length as
`serialized`.

This op parses serialized examples into a dictionary mapping keys to `Tensor`
`SparseTensor`, and `RaggedTensor` objects. `features` is a dict from keys to
`VarLenFeature`, `SparseFeature`, `RaggedFeature`, and `FixedLenFeature`
objects. Each `VarLenFeature` and `SparseFeature` is mapped to a
`SparseTensor`; each `FixedLenFeature` is mapped to a `Tensor`; and each
`RaggedFeature` is mapped to a `RaggedTensor`.

Each `VarLenFeature` maps to a `SparseTensor` of the specified type
representing a ragged matrix. Its indices are `[batch, index]` where `batch`
identifies the example in `serialized`, and `index` is the value's index in
the list of values associated with that feature and example.

Each `SparseFeature` maps to a `SparseTensor` of the specified type
representing a Tensor of `dense_shape` `[batch_size] + SparseFeature.size`.
Its `values` come from the feature in the examples with key `value_key`.
A `values[i]` comes from a position `k` in the feature of an example at batch
entry `batch`. This positional information is recorded in `indices[i]` as
`[batch, index_0, index_1, ...]` where `index_j` is the `k-th` value of
the feature in the example at with key <a href="../../tf/io/SparseFeature.md#index_key"><code>SparseFeature.index_key[j]</code></a>.
In other words, we split the indices (except the first index indicating the
batch entry) of a `SparseTensor` by dimension into different features of the
`Example`. Due to its complexity a `VarLenFeature` should be preferred over a
`SparseFeature` whenever possible.

Each `FixedLenFeature` `df` maps to a `Tensor` of the specified type (or
<a href="../../tf.md#float32"><code>tf.float32</code></a> if not specified) and shape `(serialized.size(),) + df.shape`.

`FixedLenFeature` entries with a `default_value` are optional. With no default
value, we will fail if that `Feature` is missing from any example in
`serialized`.

Each `FixedLenSequenceFeature` `df` maps to a `Tensor` of the specified type
(or <a href="../../tf.md#float32"><code>tf.float32</code></a> if not specified) and shape
`(serialized.size(), None) + df.shape`.
All examples in `serialized` will be padded with `default_value` along the
second dimension.

Each `RaggedFeature` maps to a `RaggedTensor` of the specified type.  It
is formed by stacking the `RaggedTensor` for each example, where the
`RaggedTensor` for each individual example is constructed using the tensors
specified by `RaggedTensor.values_key` and `RaggedTensor.partition`.  See
the <a href="../../tf/io/RaggedFeature.md"><code>tf.io.RaggedFeature</code></a> documentation for details and examples.

#### Examples:



For example, if one expects a <a href="../../tf.md#float32"><code>tf.float32</code></a> `VarLenFeature` `ft` and three
serialized `Example`s are provided:

```
serialized = [
  features
    { feature { key: "ft" value { float_list { value: [1.0, 2.0] } } } },
  features
    { feature []},
  features
    { feature { key: "ft" value { float_list { value: [3.0] } } }
]
```

then the output will look like:

```python
{"ft": SparseTensor(indices=[[0, 0], [0, 1], [2, 0]],
                    values=[1.0, 2.0, 3.0],
                    dense_shape=(3, 2)) }
```

If instead a `FixedLenSequenceFeature` with `default_value = -1.0` and
`shape=[]` is used then the output will look like:

```python
{"ft": [[1.0, 2.0], [3.0, -1.0]]}
```

Given two `Example` input protos in `serialized`:

```
[
  features {
    feature { key: "kw" value { bytes_list { value: [ "knit", "big" ] } } }
    feature { key: "gps" value { float_list { value: [] } } }
  },
  features {
    feature { key: "kw" value { bytes_list { value: [ "emmy" ] } } }
    feature { key: "dank" value { int64_list { value: [ 42 ] } } }
    feature { key: "gps" value { } }
  }
]
```

And arguments

```
example_names: ["input0", "input1"],
features: {
    "kw": VarLenFeature(tf.string),
    "dank": VarLenFeature(tf.int64),
    "gps": VarLenFeature(tf.float32),
}
```

Then the output is a dictionary:

```python
{
  "kw": SparseTensor(
      indices=[[0, 0], [0, 1], [1, 0]],
      values=["knit", "big", "emmy"]
      dense_shape=[2, 2]),
  "dank": SparseTensor(
      indices=[[1, 0]],
      values=[42],
      dense_shape=[2, 1]),
  "gps": SparseTensor(
      indices=[],
      values=[],
      dense_shape=[2, 0]),
}
```

For dense results in two serialized `Example`s:

```
[
  features {
    feature { key: "age" value { int64_list { value: [ 0 ] } } }
    feature { key: "gender" value { bytes_list { value: [ "f" ] } } }
   },
   features {
    feature { key: "age" value { int64_list { value: [] } } }
    feature { key: "gender" value { bytes_list { value: [ "f" ] } } }
  }
]
```

#### We can use arguments:



```
example_names: ["input0", "input1"],
features: {
    "age": FixedLenFeature([], dtype=tf.int64, default_value=-1),
    "gender": FixedLenFeature([], dtype=tf.string),
}
```

And the expected output is:

```python
{
  "age": [[0], [-1]],
  "gender": [["f"], ["f"]],
}
```

An alternative to `VarLenFeature` to obtain a `SparseTensor` is
`SparseFeature`. For example, given two `Example` input protos in
`serialized`:

```
[
  features {
    feature { key: "val" value { float_list { value: [ 0.5, -1.0 ] } } }
    feature { key: "ix" value { int64_list { value: [ 3, 20 ] } } }
  },
  features {
    feature { key: "val" value { float_list { value: [ 0.0 ] } } }
    feature { key: "ix" value { int64_list { value: [ 42 ] } } }
  }
]
```

And arguments

```
example_names: ["input0", "input1"],
features: {
    "sparse": SparseFeature(
        index_key="ix", value_key="val", dtype=tf.float32, size=100),
}
```

Then the output is a dictionary:

```python
{
  "sparse": SparseTensor(
      indices=[[0, 3], [0, 20], [1, 42]],
      values=[0.5, -1.0, 0.0]
      dense_shape=[2, 100]),
}
```

See the <a href="../../tf/io/RaggedFeature.md"><code>tf.io.RaggedFeature</code></a> documentation for examples showing how
`RaggedFeature` can be used to obtain `RaggedTensor`s.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`serialized`
</td>
<td>
A vector (1-D Tensor) of strings, a batch of binary
serialized `Example` protos.
</td>
</tr><tr>
<td>
`features`
</td>
<td>
A `dict` mapping feature keys to `FixedLenFeature`,
`VarLenFeature`, `SparseFeature`, and `RaggedFeature` values.
</td>
</tr><tr>
<td>
`example_names`
</td>
<td>
A vector (1-D Tensor) of strings (optional), the names of
the serialized protos in the batch.
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
A `dict` mapping feature keys to `Tensor`, `SparseTensor`, and
`RaggedTensor` values.
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
if any feature is invalid.
</td>
</tr>
</table>

