description: Wrapper for <a href="../tf/Graph.md#control_dependencies"><code>Graph.control_dependencies()</code></a> using the default graph.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.control_dependencies" />
<meta itemprop="path" content="Stable" />
</div>

# tf.control_dependencies

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L5325-L5359">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Wrapper for <a href="../tf/Graph.md#control_dependencies"><code>Graph.control_dependencies()</code></a> using the default graph.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.control_dependencies`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.control_dependencies(
    control_inputs
)
</code></pre>



<!-- Placeholder for "Used in" -->

See <a href="../tf/Graph.md#control_dependencies"><code>tf.Graph.control_dependencies</code></a>
for more details.

Note: *In TensorFlow 2 with eager and/or Autograph, you should not require
this method, as code executes in the expected order.* Only use
<a href="../tf/control_dependencies.md"><code>tf.control_dependencies</code></a> when working with v1-style code or in a graph
context such as inside <a href="../tf/data/Dataset.md#map"><code>Dataset.map</code></a>.

When eager execution is enabled, any callable object in the `control_inputs`
list will be called.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`control_inputs`
</td>
<td>
A list of `Operation` or `Tensor` objects which must be
executed or computed before running the operations defined in the context.
Can also be `None` to clear the control dependencies. If eager execution
is enabled, any callable object in the `control_inputs` list will be
called.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A context manager that specifies control dependencies for all
operations constructed within the context.
</td>
</tr>

</table>

