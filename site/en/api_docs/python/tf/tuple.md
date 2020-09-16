description: Group tensors together.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.tuple" />
<meta itemprop="path" content="Stable" />
</div>

# tf.tuple

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/control_flow_ops.py#L2924-L2957">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Group tensors together.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.tuple(
    tensors, control_inputs=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This creates a tuple of tensors with the same values as the `tensors`
argument, except that the value of each tensor is only returned after the
values of all tensors have been computed.

`control_inputs` contains additional ops that have to finish before this op
finishes, but whose outputs are not returned.

This can be used as a "join" mechanism for parallel computations: all the
argument tensors can be computed in parallel, but the values of any tensor
returned by `tuple` are only available after all the parallel computations
are done.

See also <a href="../tf/group.md"><code>tf.group</code></a> and
<a href="../tf/control_dependencies.md"><code>tf.control_dependencies</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensors`
</td>
<td>
A list of `Tensor`s or `IndexedSlices`, some entries can be `None`.
</td>
</tr><tr>
<td>
`control_inputs`
</td>
<td>
List of additional ops to finish before returning.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(optional) A name to use as a `name_scope` for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Same as `tensors`.
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
If `tensors` does not contain any `Tensor` or `IndexedSlices`.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If `control_inputs` is not a list of `Operation` or `Tensor`
objects.
</td>
</tr>
</table>

