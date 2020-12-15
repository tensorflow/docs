description: Returns all V2-style summary ops defined in the current default graph.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.summary.all_v2_summary_ops" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.summary.all_v2_summary_ops

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/summary_ops_v2.py#L638-L651">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns all V2-style summary ops defined in the current default graph.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.summary.all_v2_summary_ops()
</code></pre>



<!-- Placeholder for "Used in" -->

This includes ops from TF 2.0 tf.summary and TF 1.x tf.contrib.summary (except
for `tf.contrib.summary.graph` and `tf.contrib.summary.import_event`), but
does *not* include TF 1.x tf.summary ops.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
List of summary ops, or None if called under eager execution.
</td>
</tr>

</table>

