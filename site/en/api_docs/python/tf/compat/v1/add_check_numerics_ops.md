description: Connect a <a href="../../../tf/debugging/check_numerics.md"><code>tf.debugging.check_numerics</code></a> to every floating point tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.add_check_numerics_ops" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.add_check_numerics_ops

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/numerics.py#L72-L122">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Connect a <a href="../../../tf/debugging/check_numerics.md"><code>tf.debugging.check_numerics</code></a> to every floating point tensor.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.add_check_numerics_ops()
</code></pre>



<!-- Placeholder for "Used in" -->

`check_numerics` operations themselves are added for each `half`, `float`,
or `double` tensor in the current default graph. For all ops in the graph, the
`check_numerics` op for all of its (`half`, `float`, or `double`) inputs
is guaranteed to run before the `check_numerics` op on any of its outputs.

Note: This API is not compatible with the use of <a href="../../../tf/cond.md"><code>tf.cond</code></a> or
<a href="../../../tf/while_loop.md"><code>tf.while_loop</code></a>, and will raise a `ValueError` if you attempt to call it
in such a graph.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `group` op depending on all `check_numerics` ops added.
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
If the graph contains any numeric operations in a control flow
structure.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If called with eager execution enabled.
</td>
</tr>
</table>




#### Eager Compatibility
Not compatible with eager execution. To check for `Inf`s and `NaN`s under
eager execution, call <a href="../../../tf/debugging/enable_check_numerics.md"><code>tf.debugging.enable_check_numerics()</code></a> once before
executing the checked operations.

