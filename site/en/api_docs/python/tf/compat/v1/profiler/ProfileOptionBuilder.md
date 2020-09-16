description: Option Builder for Profiling API.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.profiler.ProfileOptionBuilder" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="account_displayed_op_only"/>
<meta itemprop="property" content="build"/>
<meta itemprop="property" content="float_operation"/>
<meta itemprop="property" content="order_by"/>
<meta itemprop="property" content="select"/>
<meta itemprop="property" content="time_and_memory"/>
<meta itemprop="property" content="trainable_variables_parameter"/>
<meta itemprop="property" content="with_accounted_types"/>
<meta itemprop="property" content="with_empty_output"/>
<meta itemprop="property" content="with_file_output"/>
<meta itemprop="property" content="with_max_depth"/>
<meta itemprop="property" content="with_min_execution_time"/>
<meta itemprop="property" content="with_min_float_operations"/>
<meta itemprop="property" content="with_min_memory"/>
<meta itemprop="property" content="with_min_occurrence"/>
<meta itemprop="property" content="with_min_parameters"/>
<meta itemprop="property" content="with_node_names"/>
<meta itemprop="property" content="with_pprof_output"/>
<meta itemprop="property" content="with_stdout_output"/>
<meta itemprop="property" content="with_step"/>
<meta itemprop="property" content="with_timeline_output"/>
</div>

# tf.compat.v1.profiler.ProfileOptionBuilder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L27-L465">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Option Builder for Profiling API.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.profiler.ProfileOptionBuilder(
    options=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

For tutorial on the options, see
https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/options.md

```python
# Users can use pre-built options:
opts = (
    tf.profiler.ProfileOptionBuilder.trainable_variables_parameter())

# Or, build your own options:
opts = (tf.compat.v1.profiler.ProfileOptionBuilder()
    .with_max_depth(10)
    .with_min_micros(1000)
    .select(['accelerator_micros'])
    .with_stdout_output()
    .build()

# Or customize the pre-built options:
opts = (tf.compat.v1.profiler.ProfileOptionBuilder(
    tf.profiler.ProfileOptionBuilder.time_and_memory())
    .with_displaying_options(show_name_regexes=['.*rnn.*'])
    .build())

# Finally, profiling with the options:
_ = tf.compat.v1.profiler.profile(tf.compat.v1.get_default_graph(),
                        run_meta=run_meta,
                        cmd='scope',
                        options=opts)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`options`
</td>
<td>
Optional initial option dict to start with.
</td>
</tr>
</table>



## Methods

<h3 id="account_displayed_op_only"><code>account_displayed_op_only</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L372-L385">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>account_displayed_op_only(
    is_true
)
</code></pre>

Whether only account the statistics of displayed profiler nodes.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`is_true`
</td>
<td>
If true, only account statistics of nodes eventually
displayed by the outputs.
Otherwise, a node's statistics are accounted by its parents
as long as it's types match 'account_type_regexes', even if
it is hidden from the output, say, by hide_name_regexes.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
self
</td>
</tr>

</table>



<h3 id="build"><code>build</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L193-L199">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>build()
</code></pre>

Build a profiling option.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dict of profiling options.
</td>
</tr>

</table>



<h3 id="float_operation"><code>float_operation</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L114-L141">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>float_operation()
</code></pre>

Options used to profile float operations.

Please see https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/profile_model_architecture.md
on the caveats of calculating float operations.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dict of profiling options.
</td>
</tr>

</table>



<h3 id="order_by"><code>order_by</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L421-L435">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>order_by(
    attribute
)
</code></pre>

Order the displayed profiler nodes based on a attribute.

Supported attribute includes micros, bytes, occurrence, params, etc.
https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/options.md

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`attribute`
</td>
<td>
An attribute the profiler node has.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
self
</td>
</tr>

</table>



<h3 id="select"><code>select</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L437-L451">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>select(
    attributes
)
</code></pre>

Select the attributes to display.

See https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/options.md
for supported attributes.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`attributes`
</td>
<td>
A list of attribute the profiler node has.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
self
</td>
</tr>

</table>



<h3 id="time_and_memory"><code>time_and_memory</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L143-L191">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>time_and_memory(
    min_micros=1, min_bytes=1, min_accelerator_micros=0, min_cpu_micros=0,
    min_peak_bytes=0, min_residual_bytes=0, min_output_bytes=0
)
</code></pre>

Show operation time and memory consumptions.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`min_micros`
</td>
<td>
Only show profiler nodes with execution time
no less than this. It sums accelerator and cpu times.
</td>
</tr><tr>
<td>
`min_bytes`
</td>
<td>
Only show profiler nodes requested to allocate no less bytes
than this.
</td>
</tr><tr>
<td>
`min_accelerator_micros`
</td>
<td>
Only show profiler nodes spend no less than
this time on accelerator (e.g. GPU).
</td>
</tr><tr>
<td>
`min_cpu_micros`
</td>
<td>
Only show profiler nodes spend no less than
this time on cpu.
</td>
</tr><tr>
<td>
`min_peak_bytes`
</td>
<td>
Only show profiler nodes using no less than this bytes
at peak (high watermark). For profiler nodes consist of multiple
graph nodes, it sums the graph nodes' peak_bytes.
</td>
</tr><tr>
<td>
`min_residual_bytes`
</td>
<td>
Only show profiler nodes have no less than
this bytes not being de-allocated after Compute() ends. For
profiler nodes consist of multiple graph nodes, it sums the
graph nodes' residual_bytes.
</td>
</tr><tr>
<td>
`min_output_bytes`
</td>
<td>
Only show profiler nodes have no less than this bytes
output. The output are not necessarily allocated by this profiler
nodes.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dict of profiling options.
</td>
</tr>

</table>



<h3 id="trainable_variables_parameter"><code>trainable_variables_parameter</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L88-L112">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>trainable_variables_parameter()
</code></pre>

Options used to profile trainable variable parameters.

Normally used together with 'scope' view.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dict of profiling options.
</td>
</tr>

</table>



<h3 id="with_accounted_types"><code>with_accounted_types</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L316-L336">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_accounted_types(
    account_type_regexes
)
</code></pre>

Selectively counting statistics based on node types.

Here, 'types' means the profiler nodes' properties. Profiler by default
consider device name (e.g. /job:xx/.../device:GPU:0) and operation type
(e.g. MatMul) as profiler nodes' properties. User can also associate
customized 'types' to profiler nodes through OpLogProto proto.

For example, user can select profiler nodes placed on gpu:0 with:
`account_type_regexes=['.*gpu:0.*']`

If none of a node's properties match the specified regexes, the node is
not displayed nor accounted.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`account_type_regexes`
</td>
<td>
A list of regexes specifying the types.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
self.
</td>
</tr>

</table>



<h3 id="with_empty_output"><code>with_empty_output</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L387-L390">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_empty_output()
</code></pre>

Do not generate side-effect outputs.


<h3 id="with_file_output"><code>with_file_output</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L397-L400">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_file_output(
    outfile
)
</code></pre>

Print the result to a file.


<h3 id="with_max_depth"><code>with_max_depth</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L201-L214">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_max_depth(
    max_depth
)
</code></pre>

Set the maximum depth of display.

The depth depends on profiling view. For 'scope' view, it's the
depth of name scope hierarchy (tree), for 'op' view, it's the number
of operation types (list), etc.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`max_depth`
</td>
<td>
Maximum depth of the data structure to display.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
self
</td>
</tr>

</table>



<h3 id="with_min_execution_time"><code>with_min_execution_time</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L245-L264">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_min_execution_time(
    min_micros=0, min_accelerator_micros=0, min_cpu_micros=0
)
</code></pre>

Only show profiler nodes consuming no less than 'min_micros'.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`min_micros`
</td>
<td>
Only show profiler nodes with execution time
no less than this. It sums accelerator and cpu times.
</td>
</tr><tr>
<td>
`min_accelerator_micros`
</td>
<td>
Only show profiler nodes spend no less than
this time on accelerator (e.g. GPU).
</td>
</tr><tr>
<td>
`min_cpu_micros`
</td>
<td>
Only show profiler nodes spend no less than
this time on cpu.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
self
</td>
</tr>

</table>



<h3 id="with_min_float_operations"><code>with_min_float_operations</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L299-L314">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_min_float_operations(
    min_float_ops
)
</code></pre>

Only show profiler nodes consuming no less than 'min_float_ops'.

Please see https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/profile_model_architecture.md
on the caveats of calculating float operations.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`min_float_ops`
</td>
<td>
Only show profiler nodes with float operations
no less than this.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
self
</td>
</tr>

</table>



<h3 id="with_min_memory"><code>with_min_memory</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L216-L243">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_min_memory(
    min_bytes=0, min_peak_bytes=0, min_residual_bytes=0, min_output_bytes=0
)
</code></pre>

Only show profiler nodes consuming no less than 'min_bytes'.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`min_bytes`
</td>
<td>
Only show profiler nodes requested to allocate no less bytes
than this.
</td>
</tr><tr>
<td>
`min_peak_bytes`
</td>
<td>
Only show profiler nodes using no less than this bytes
at peak (high watermark). For profiler nodes consist of multiple
graph nodes, it sums the graph nodes' peak_bytes.
</td>
</tr><tr>
<td>
`min_residual_bytes`
</td>
<td>
Only show profiler nodes have no less than
this bytes not being de-allocated after Compute() ends. For
profiler nodes consist of multiple graph nodes, it sums the
graph nodes' residual_bytes.
</td>
</tr><tr>
<td>
`min_output_bytes`
</td>
<td>
Only show profiler nodes have no less than this bytes
output. The output are not necessarily allocated by this profiler
nodes.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
self
</td>
</tr>

</table>



<h3 id="with_min_occurrence"><code>with_min_occurrence</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L281-L297">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_min_occurrence(
    min_occurrence
)
</code></pre>

Only show profiler nodes including no less than 'min_occurrence' graph nodes.

A "node" means a profiler output node, which can be a python line
(code view), an operation type (op view), or a graph node
(graph/scope view). A python line includes all graph nodes created by that
line, while an operation type includes all graph nodes of that type.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`min_occurrence`
</td>
<td>
Only show nodes including no less than this.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
self
</td>
</tr>

</table>



<h3 id="with_min_parameters"><code>with_min_parameters</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L266-L279">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_min_parameters(
    min_params
)
</code></pre>

Only show profiler nodes holding no less than 'min_params' parameters.

'Parameters' normally refers the weights of in TensorFlow variables.
It reflects the 'capacity' of models.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`min_params`
</td>
<td>
Only show profiler nodes holding number parameters
no less than this.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
self
</td>
</tr>

</table>



<h3 id="with_node_names"><code>with_node_names</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L338-L370">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_node_names(
    start_name_regexes=None, show_name_regexes=None, hide_name_regexes=None,
    trim_name_regexes=None
)
</code></pre>

Regular expressions used to select profiler nodes to display.

After 'with_accounted_types' is evaluated, 'with_node_names' are
evaluated as follows:

  For a profile data structure, profiler first finds the profiler
  nodes matching 'start_name_regexes', and starts displaying profiler
  nodes from there. Then, if a node matches 'show_name_regexes' and
  doesn't match 'hide_name_regexes', it's displayed. If a node matches
  'trim_name_regexes', profiler stops further searching that branch.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`start_name_regexes`
</td>
<td>
list of node name regexes to start displaying.
</td>
</tr><tr>
<td>
`show_name_regexes`
</td>
<td>
list of node names regexes to display.
</td>
</tr><tr>
<td>
`hide_name_regexes`
</td>
<td>
list of node_names regexes that should be hidden.
</td>
</tr><tr>
<td>
`trim_name_regexes`
</td>
<td>
list of node name regexes from where to stop.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
self
</td>
</tr>

</table>



<h3 id="with_pprof_output"><code>with_pprof_output</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L407-L419">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_pprof_output(
    pprof_file
)
</code></pre>

Generate a pprof profile gzip file.


#### To use the pprof file:

pprof -png --nodecount=100 --sample_index=1 <pprof_file>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`pprof_file`
</td>
<td>
filename for output, usually suffixed with .pb.gz.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
self.
</td>
</tr>

</table>



<h3 id="with_stdout_output"><code>with_stdout_output</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L392-L395">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_stdout_output()
</code></pre>

Print the result to stdout.


<h3 id="with_step"><code>with_step</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L453-L465">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_step(
    step
)
</code></pre>

Which profile step to use for profiling.

The 'step' here refers to the step defined by `Profiler.add_step()` API.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`step`
</td>
<td>
When multiple steps of profiles are available, select which step's
profile to use. If -1, use average of all available steps.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
self
</td>
</tr>

</table>



<h3 id="with_timeline_output"><code>with_timeline_output</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/option_builder.py#L402-L405">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>with_timeline_output(
    timeline_file
)
</code></pre>

Generate a timeline json file.




