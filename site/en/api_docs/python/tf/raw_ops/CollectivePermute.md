description: An Op to permute tensors across replicated TPU instances.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.CollectivePermute" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.CollectivePermute

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



An Op to permute tensors across replicated TPU instances.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CollectivePermute`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CollectivePermute(
    input, source_target_pairs, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Each instance supplies its own input.

For example, suppose there are 4 TPU instances: `[A, B, C, D]`. Passing
source_target_pairs=`[[0,1],[1,2],[2,3],[3,0]]` gets the outputs:
`[D, A, B, C]`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
The local input to be permuted. Currently only supports float and
bfloat16.
</td>
</tr><tr>
<td>
`source_target_pairs`
</td>
<td>
A `Tensor` of type `int32`.
A tensor with shape [num_pairs, 2].
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

