description: A transformation that parses Example protos into a dict of tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.parse_example_dataset" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.parse_example_dataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/experimental/ops/parsing_ops.py#L109-L164">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A transformation that parses `Example` protos into a `dict` of tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.parse_example_dataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.parse_example_dataset(
    features, num_parallel_calls=1, deterministic=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Parses a number of serialized `Example` protos given in `serialized`. We refer
to `serialized` as a batch with `batch_size` many entries of individual
`Example` protos.

This op parses serialized examples into a dictionary mapping keys to `Tensor`,
`SparseTensor`, and `RaggedTensor` objects. `features` is a dict from keys to
`VarLenFeature`, `RaggedFeature`, `SparseFeature`, and `FixedLenFeature`
objects. Each `VarLenFeature` and `SparseFeature` is mapped to a
`SparseTensor`; each `RaggedFeature` is mapped to a `RaggedTensor`; and each
`FixedLenFeature` is mapped to a `Tensor`. See <a href="../../../tf/io/parse_example.md"><code>tf.io.parse_example</code></a> for more
details about feature dictionaries.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`features`
</td>
<td>
A `dict` mapping feature keys to `FixedLenFeature`,
`VarLenFeature`, `RaggedFeature`, and `SparseFeature` values.
</td>
</tr><tr>
<td>
`num_parallel_calls`
</td>
<td>
(Optional.) A <a href="../../../tf.md#int32"><code>tf.int32</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>,
representing the number of parsing processes to call in parallel.
</td>
</tr><tr>
<td>
`deterministic`
</td>
<td>
(Optional.) A boolean controlling whether determinism
should be traded for performance by allowing elements to be produced out
of order if some parsing calls complete faster than others. If
`deterministic` is `None`, the
<a href="../../../tf/data/Options.md#experimental_deterministic"><code>tf.data.Options.experimental_deterministic</code></a> dataset option (`True` by
default) is used to decide whether to produce elements
deterministically.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A dataset transformation function, which can be passed to
<a href="../../../tf/data/Dataset.md#apply"><code>tf.data.Dataset.apply</code></a>.
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
if features argument is None.
</td>
</tr>
</table>

