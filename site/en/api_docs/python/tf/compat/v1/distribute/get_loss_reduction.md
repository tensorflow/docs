description: <a href="../../../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> corresponding to the last loss reduction.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.distribute.get_loss_reduction" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.distribute.get_loss_reduction

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribute_lib.py#L270-L289">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



<a href="../../../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> corresponding to the last loss reduction.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.distribute.get_loss_reduction()
</code></pre>



<!-- Placeholder for "Used in" -->

This is used to decide whether loss should be scaled in optimizer (used only
for estimator + v1 optimizer use case).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
<a href="../../../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> corresponding to the last loss reduction for
estimator and v1 optimizer use case. <a href="../../../../tf/distribute/ReduceOp.md#SUM"><code>tf.distribute.ReduceOp.SUM</code></a> otherwise.
</td>
</tr>

</table>

