description: Outputs deterministic pseudorandom random integers from a uniform distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.StatelessRandomUniformFullInt" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.StatelessRandomUniformFullInt

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Outputs deterministic pseudorandom random integers from a uniform distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StatelessRandomUniformFullInt`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StatelessRandomUniformFullInt(
    shape, seed, dtype=tf.dtypes.uint64, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The generated values are uniform integers covering the whole range of `dtype`.

The outputs are a deterministic function of `shape` and `seed`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
The shape of the output tensor.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`, `uint32`, `uint64`.
2 seeds (shape [2]).
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int32, tf.int64, tf.uint32, tf.uint64`. Defaults to <a href="../../tf.md#uint64"><code>tf.uint64</code></a>.
The type of the output.
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
A `Tensor` of type `dtype`.
</td>
</tr>

</table>

