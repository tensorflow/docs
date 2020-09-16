description: TensorFlow multi-step profiler.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.profiler.Profiler" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add_step"/>
<meta itemprop="property" content="advise"/>
<meta itemprop="property" content="profile_graph"/>
<meta itemprop="property" content="profile_name_scope"/>
<meta itemprop="property" content="profile_operations"/>
<meta itemprop="property" content="profile_python"/>
<meta itemprop="property" content="serialize_to_string"/>
</div>

# tf.compat.v1.profiler.Profiler

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/profiler/model_analyzer.py#L126-L306">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



TensorFlow multi-step profiler.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.profiler.Profiler(
    graph=None, op_log=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/README.md

```python
Typical use case:
  # Currently we are only allowed to create 1 profiler per process.
  profiler = Profiler(sess.graph)

  for i in xrange(total_steps):
    if i % 10000 == 0:
      run_meta = tf.compat.v1.RunMetadata()
      _ = sess.run(...,
                   options=tf.compat.v1.RunOptions(
                       trace_level=tf.RunOptions.FULL_TRACE),
                   run_metadata=run_meta)
      profiler.add_step(i, run_meta)

      # Profile the parameters of your model.
      profiler.profile_name_scope(options=(option_builder.ProfileOptionBuilder
          .trainable_variables_parameter()))

      # Or profile the timing of your model operations.
      opts = option_builder.ProfileOptionBuilder.time_and_memory()
      profiler.profile_operations(options=opts)

      # Or you can generate a timeline:
      opts = (option_builder.ProfileOptionBuilder(
              option_builder.ProfileOptionBuilder.time_and_memory())
              .with_step(i)
              .with_timeline_output(filename).build())
      profiler.profile_graph(options=opts)
    else:
      _ = sess.run(...)
  # Auto detect problems and generate advice.
  profiler.advise()
```

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
`op_log`
</td>
<td>
optional. tensorflow::tfprof::OpLogProto proto. Used to define
extra op types.
</td>
</tr>
</table>



## Methods

<h3 id="add_step"><code>add_step</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/profiler/model_analyzer.py#L189-L205">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_step(
    step, run_meta
)
</code></pre>

Add statistics of a step.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`step`
</td>
<td>
int, An id used to group one or more different `run_meta` together.
When profiling with the profile_xxx APIs, user can use the `step`
id in the `options` to profile these `run_meta` together.
</td>
</tr><tr>
<td>
`run_meta`
</td>
<td>
RunMetadata proto that contains statistics of a session run.
</td>
</tr>
</table>



<h3 id="advise"><code>advise</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/profiler/model_analyzer.py#L279-L291">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>advise(
    options
)
</code></pre>

Automatically detect problems and generate reports.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`options`
</td>
<td>
A dict of options. See ALL_ADVICE example above.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An Advise proto that contains the reports from all checkers.
</td>
</tr>

</table>



<h3 id="profile_graph"><code>profile_graph</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/profiler/model_analyzer.py#L262-L277">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>profile_graph(
    options
)
</code></pre>

Profile the statistics of graph nodes, organized by dataflow graph.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
a GraphNodeProto that records the results.
</td>
</tr>

</table>



<h3 id="profile_name_scope"><code>profile_name_scope</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/profiler/model_analyzer.py#L245-L260">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>profile_name_scope(
    options
)
</code></pre>

Profile the statistics of graph nodes, organized by name scope.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
a GraphNodeProto that records the results.
</td>
</tr>

</table>



<h3 id="profile_operations"><code>profile_operations</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/profiler/model_analyzer.py#L228-L243">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>profile_operations(
    options
)
</code></pre>

Profile the statistics of the Operation types (e.g. MatMul, Conv2D).


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
a MultiGraphNodeProto that records the results.
</td>
</tr>

</table>



<h3 id="profile_python"><code>profile_python</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/profiler/model_analyzer.py#L207-L226">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>profile_python(
    options
)
</code></pre>

Profile the statistics of the Python codes.

  By default, it shows the call stack from root. To avoid
  redundant output, you may use options to filter as below
    options['show_name_regexes'] = ['.*my_code.py.*']

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
a MultiGraphNodeProto that records the results.
</td>
</tr>

</table>



<h3 id="serialize_to_string"><code>serialize_to_string</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/profiler/model_analyzer.py#L293-L302">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>serialize_to_string()
</code></pre>

Serialize the ProfileProto to a binary string.

  Users can write it to file for offline analysis by tfprof commandline
  or graphical interface.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
ProfileProto binary string.
</td>
</tr>

</table>





