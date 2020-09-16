description: Connects N outputs from an N-way replicated TPU computation.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.TPUReplicatedOutput" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.TPUReplicatedOutput

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Connects N outputs from an N-way replicated TPU computation.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TPUReplicatedOutput`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TPUReplicatedOutput(
    input, num_replicas, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation holds a replicated output from a `tpu.replicate()` computation subgraph.
Each replicated output has the same shape and type alongside the input.

#### For example:


```
%computation = "tf.Computation"()
%replicated_output:2 = "tf.TPUReplicatedOutput"(%computation)
```
The above computation has a replicated output of two replicas.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`num_replicas`
</td>
<td>
An `int` that is `>= 1`.
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
A list of `num_replicas` `Tensor` objects with the same type as `input`.
</td>
</tr>

</table>

