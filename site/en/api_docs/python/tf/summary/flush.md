description: Forces summary writer to send any buffered data to storage.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.summary.flush" />
<meta itemprop="path" content="Stable" />
</div>

# tf.summary.flush

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/summary_ops_v2.py#L1036-L1061">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Forces summary writer to send any buffered data to storage.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.summary.flush(
    writer=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation blocks until that finishes.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`writer`
</td>
<td>
The <a href="../../tf/summary/SummaryWriter.md"><code>tf.summary.SummaryWriter</code></a> resource to flush.
The thread default will be used if this parameter is None.
Otherwise a <a href="../../tf/no_op.md"><code>tf.no_op</code></a> is returned.
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
The created <a href="../../tf/Operation.md"><code>tf.Operation</code></a>.
</td>
</tr>

</table>

