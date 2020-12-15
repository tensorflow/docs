description: Whether to output all intermediates from functional control flow ops.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.experimental.output_all_intermediates" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.experimental.output_all_intermediates

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/control_flow_v2_toggles.py#L74-L98">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Whether to output all intermediates from functional control flow ops.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.experimental.output_all_intermediates(
    state
)
</code></pre>



<!-- Placeholder for "Used in" -->

The "default" behavior to is to output all intermediates when using v2 control
flow inside Keras models in graph mode (possibly inside Estimators). This is
needed to support taking gradients of v2 control flow. In graph mode, Keras
can sometimes freeze the forward graph before the gradient computation which
does not work for v2 control flow since it requires updating the forward ops
to output the needed intermediates. We work around this by proactively
outputting the needed intermediates when building the forward pass itself.
Ideally any such extra tensors should be pruned out at runtime. However, if
for any reason this doesn't work for you or if you have an inference-only
model you can turn this behavior off using
<a href="../../../../tf/compat/v1/experimental/output_all_intermediates.md"><code>tf.compat.v1.experimental.output_all_intermediates(False)</code></a>.

If with the default behavior you are still seeing errors of the form
"Connecting to invalid output X of source node Y which has Z outputs" try
setting <a href="../../../../tf/compat/v1/experimental/output_all_intermediates.md"><code>tf.compat.v1.experimental.output_all_intermediates(True)</code></a> and
please file an issue at https://github.com/tensorflow/tensorflow/issues.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`state`
</td>
<td>
True, False or None. None restores the default behavior.
</td>
</tr>
</table>

