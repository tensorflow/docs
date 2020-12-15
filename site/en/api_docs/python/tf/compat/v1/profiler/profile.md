description: Profile model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.profiler.profile" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.profiler.profile

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/profiler/model_analyzer.py#L309-L381">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Profile model.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.profiler.profile(
    graph=None, run_meta=None, op_log=None, cmd='scope',
    options=_DEFAULT_PROFILE_OPTIONS
)
</code></pre>



<!-- Placeholder for "Used in" -->

  Tutorials and examples can be found in:
  https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/profiler/g3doc/python_api.md

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
`op_log`
</td>
<td>
tensorflow.tfprof.OpLogProto proto. User can assign "types" to
graph nodes with op_log. "types" allow user to flexibly group and
account profiles using options['accounted_type_regexes'].
</td>
</tr><tr>
<td>
`cmd`
</td>
<td>
string. Either 'op', 'scope', 'graph' or 'code'.
'op' view organizes profile using operation type. (e.g. MatMul)
'scope' view organizes profile using graph node name scope.
'graph' view organizes profile using graph node inputs/outputs.
'code' view organizes profile using Python call stack.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
A dict of options. See core/profiler/g3doc/options.md.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
If cmd is 'scope' or 'graph', returns GraphNodeProto proto.
If cmd is 'op' or 'code', returns MultiGraphNodeProto proto.
Side effect: stdout/file/timeline.json depending on options['output']
</td>
</tr>

</table>

