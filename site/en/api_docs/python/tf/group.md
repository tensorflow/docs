description: Create an op that groups multiple operations.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.group" />
<meta itemprop="path" content="Stable" />
</div>

# tf.group

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/control_flow_ops.py#L2871-L2946">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Create an op that groups multiple operations.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.group`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.group(
    *inputs, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

When this op finishes, all ops in `inputs` have finished. This op has no
output.

Note: *In TensorFlow 2 with eager and/or Autograph, you should not require
this method, as code executes in your expected order.* Only use tf.group when
working with v1-style code or in a graph context such as inside <a href="../tf/data/Dataset.md#map"><code>Dataset.map</code></a>.

When operating in a v1-style graph context, ops are not executed in the same
order as specified in the code; TensorFlow will attempt to execute ops in
parallel or in an order convienient to the result it is computing.  <a href="../tf/group.md"><code>tf.group</code></a>
allows you to request that one or more results finish before execution
continues.

<a href="../tf/group.md"><code>tf.group</code></a> creates a single op (of type `NoOp`), and then adds appropriate
control dependencies.  Thus, `c = tf.group(a, b)` will compute the same graph
as this:

    with tf.control_dependencies([a, b]):
        c = tf.no_op()

See also <a href="../tf/tuple.md"><code>tf.tuple</code></a> and
<a href="../tf/control_dependencies.md"><code>tf.control_dependencies</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`*inputs`
</td>
<td>
Zero or more tensors to group.
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
An Operation that executes all its inputs.
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
If an unknown keyword argument is provided.
</td>
</tr>
</table>

