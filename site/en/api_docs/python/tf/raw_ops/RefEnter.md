description: Creates or finds a child frame, and makes data available to the child frame.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RefEnter" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RefEnter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates or finds a child frame, and makes `data` available to the child frame.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RefEnter`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RefEnter(
    data, frame_name, is_constant=(False), parallel_iterations=10, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The unique `frame_name` is used by the `Executor` to identify frames. If
`is_constant` is true, `output` is a constant in the child frame; otherwise
it may be changed in the child frame. At most `parallel_iterations` iterations
are run in parallel in the child frame.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`data`
</td>
<td>
A mutable `Tensor`.
The tensor to be made available to the child frame.
</td>
</tr><tr>
<td>
`frame_name`
</td>
<td>
A `string`. The name of the child frame.
</td>
</tr><tr>
<td>
`is_constant`
</td>
<td>
An optional `bool`. Defaults to `False`.
If true, the output is constant within the child frame.
</td>
</tr><tr>
<td>
`parallel_iterations`
</td>
<td>
An optional `int`. Defaults to `10`.
The number of iterations allowed to run in parallel.
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
A mutable `Tensor`. Has the same type as `data`.
</td>
</tr>

</table>

