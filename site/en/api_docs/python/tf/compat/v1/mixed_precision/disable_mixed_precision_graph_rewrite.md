description: Disables the mixed precision graph rewrite.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.mixed_precision.disable_mixed_precision_graph_rewrite" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.mixed_precision.disable_mixed_precision_graph_rewrite

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/experimental/mixed_precision.py#L391-L418">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Disables the mixed precision graph rewrite.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.train.experimental.disable_mixed_precision_graph_rewrite`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.mixed_precision.disable_mixed_precision_graph_rewrite()
</code></pre>



<!-- Placeholder for "Used in" -->

After this is called, the mixed precision graph rewrite will no longer run for
new Sessions, and so float32 operations will no longer be converted to float16
in such Sessions. However, any existing Sessions will continue to have the
graph rewrite enabled if they were created after
`enable_mixed_precision_graph_rewrite` was called but before
`disable_mixed_precision_graph_rewrite` was called.

This does not undo the effects of loss scaling. Any optimizers wrapped with a
LossScaleOptimizer will continue to do loss scaling, although this loss
scaling will no longer be useful if the optimizer is used in new Sessions, as
the graph rewrite no longer converts the graph to use float16.

This function is useful for unit testing. A unit tests can test using the
mixed precision graph rewrite, then disable it so future unit tests continue
using float32. If this is done, unit tests should not share a single session,
as `enable_mixed_precision_graph_rewrite` and
`disable_mixed_precision_graph_rewrite` have no effect on existing sessions.