description: Auto profile and advise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.profiler.advise" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.profiler.advise

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/profiler/model_analyzer.py#L384-L420">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Auto profile and advise.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.profiler.advise(
    graph=None, run_meta=None, options=_DEFAULT_ADVISE_OPTIONS
)
</code></pre>



<!-- Placeholder for "Used in" -->

  Builds profiles and automatically check anomalies of various
  aspects. For more details:
  https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/README.md

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`graph`
</td>
<td>
tf.Graph. If None and eager execution is not enabled, use
default graph.
</td>
</tr><tr>
<td>
`run_meta`
</td>
<td>
optional tensorflow.RunMetadata proto. It is necessary to
to support run time information profiling, such as time and memory.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
see ALL_ADVICE example above. Default checks everything.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Returns AdviceProto proto
</td>
</tr>

</table>

