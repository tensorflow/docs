description: Parses a batch of SequenceExample protos.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.parse_sequence_example" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.parse_sequence_example

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/parsing_ops.py#L455-L573">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Parses a batch of `SequenceExample` protos.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.io.parse_sequence_example`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.parse_sequence_example(
    serialized, context_features=None, sequence_features=None, example_names=None,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Parses a vector of serialized
[`SequenceExample`](https://www.tensorflow.org/code/tensorflow/core/example/example.proto)
protos given in `serialized`.

This op parses serialized sequence examples into a tuple of dictionaries,
each mapping keys to `Tensor` and `SparseTensor` objects.
The first dictionary contains mappings for keys appearing in
`context_features`, and the second dictionary contains mappings for keys
appearing in `sequence_features`.

At least one of `context_features` and `sequence_features` must be provided
and non-empty.

The `context_features` keys are associated with a `SequenceExample` as a
whole, independent of time / frame.  In contrast, the `sequence_features` keys
provide a way to access variable-length data within the `FeatureList` section
of the `SequenceExample` proto.  While the shapes of `context_features` values
are fixed with respect to frame, the frame dimension (the first dimension)
of `sequence_features` values may vary between `SequenceExample` protos,
and even between `feature_list` keys within the same `SequenceExample`.

`context_features` contains `VarLenFeature`, `RaggedFeature`, and
`FixedLenFeature`  objects. Each `VarLenFeature` is mapped to a
`SparseTensor`; each `RaggedFeature` is  mapped to a `RaggedTensor`; and each
`FixedLenFeature` is mapped to a `Tensor`, of the specified type, shape, and
default value.

`sequence_features` contains `VarLenFeature`, `RaggedFeature`, and
`FixedLenSequenceFeature` objects. Each `VarLenFeature` is mapped to a
`SparseTensor`; each `RaggedFeature` is mapped to a `RaggedTensor; and
each `FixedLenSequenceFeature` is mapped to a `Tensor`, each of the specified
type. The shape will be `(B,T,) + df.dense_shape` for
`FixedLenSequenceFeature` `df`, where `B` is the batch size, and `T` is the
length of the associated `FeatureList` in the `SequenceExample`. For instance,
`FixedLenSequenceFeature([])` yields a scalar 2-D `Tensor` of static shape
`[None, None]` and dynamic shape `[B, T]`, while
`FixedLenSequenceFeature([k])` (for `int k >= 1`) yields a 3-D matrix `Tensor`
of static shape `[None, None, k]` and dynamic shape `[B, T, k]`.

Like the input, the resulting output tensors have a batch dimension. This
means that the original per-example shapes of `VarLenFeature`s and
`FixedLenSequenceFeature`s can be lost. To handle that situation, this op also
provides dicts of shape tensors as part of the output. There is one dict for
the context features, and one for the feature_list features. Context features
of type `FixedLenFeature`s will not be present, since their shapes are already
known by the caller. In situations where the input 'FixedLenFeature`s are of
different lengths across examples, the shorter examples will be padded with
default datatype values: 0 for numeric types, and the empty string for string
types.

Each `SparseTensor` corresponding to `sequence_features` represents a ragged
vector.  Its indices are `[time, index]`, where `time` is the `FeatureList`
entry and `index` is the value's index in the list of values associated with
that time.

`FixedLenFeature` entries with a `default_value` and `FixedLenSequenceFeature`
entries with `allow_missing=True` are optional; otherwise, we will fail if
that `Feature` or `FeatureList` is missing from any example in `serialized`.

`example_name` may contain a descriptive name for the corresponding serialized
proto. This may be useful for debugging purposes, but it has no effect on the
output. If not `None`, `example_name` must be a scalar.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`serialized`
</td>
<td>
A vector (1-D Tensor) of type string containing binary
serialized `SequenceExample` protos.
</td>
</tr><tr>
<td>
`context_features`
</td>
<td>
A `dict` mapping feature keys to `FixedLenFeature` or
`VarLenFeature` or `RaggedFeature` values. These features are associated
with a `SequenceExample` as a whole.
</td>
</tr><tr>
<td>
`sequence_features`
</td>
<td>
A `dict` mapping feature keys to
`FixedLenSequenceFeature` or `VarLenFeature` or `RaggedFeature` values.
These features are associated with data within the `FeatureList` section
of the `SequenceExample` proto.
</td>
</tr><tr>
<td>
`example_names`
</td>
<td>
A vector (1-D Tensor) of strings (optional), the name of the
serialized protos.
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
A tuple of three `dict`s, each mapping keys to `Tensor`s,
`SparseTensor`s, and `RaggedTensor`. The first dict contains the context
key/values, the second dict contains the feature_list key/values, and the
final dict contains the lengths of any dense feature_list features.
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

