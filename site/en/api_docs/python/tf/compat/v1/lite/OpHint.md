description: A class that helps build tflite function invocations.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.lite.OpHint" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="OpHintArgumentTracker"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add_input"/>
<meta itemprop="property" content="add_inputs"/>
<meta itemprop="property" content="add_output"/>
<meta itemprop="property" content="add_outputs"/>
<meta itemprop="property" content="AGGREGATE_FIRST"/>
<meta itemprop="property" content="AGGREGATE_LAST"/>
<meta itemprop="property" content="AGGREGATE_STACK"/>
<meta itemprop="property" content="CHILDREN_INPUTS_MAPPINGS"/>
<meta itemprop="property" content="FUNCTION_AGGREGATE_ATTR"/>
<meta itemprop="property" content="FUNCTION_INPUT_INDEX_ATTR"/>
<meta itemprop="property" content="FUNCTION_LEVEL_ATTR"/>
<meta itemprop="property" content="FUNCTION_NAME_ATTR"/>
<meta itemprop="property" content="FUNCTION_OUTPUT_INDEX_ATTR"/>
<meta itemprop="property" content="FUNCTION_SORT_INDEX_ATTR"/>
<meta itemprop="property" content="FUNCTION_UUID_ATTR"/>
<meta itemprop="property" content="TFLITE_INPUT_INDICES"/>
</div>

# tf.compat.v1.lite.OpHint

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/lite/python/op_hint.py#L97-L468">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A class that helps build tflite function invocations.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.lite.OpHint(
    function_name, level=1, children_inputs_mappings=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

It allows you to take a bunch of TensorFlow ops and annotate the construction
such that toco knows how to convert it to tflite. This embeds a pseudo
function in a TensorFlow graph. This allows embedding high-level API usage
information in a lower level TensorFlow implementation so that an alternative
implementation can be substituted later.

Essentially, any "input" into this pseudo op is fed into an identity, and
attributes are added to that input before being used by the constituent ops
that make up the pseudo op. A similar process is done to any output that
is to be exported from the current op.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`function_name`
</td>
<td>
Name of the function (the custom op name in tflite)
</td>
</tr><tr>
<td>
`level`
</td>
<td>
OpHint level.
</td>
</tr><tr>
<td>
`children_inputs_mappings`
</td>
<td>
Children OpHint inputs/outputs mapping.
children_inputs_mappings should like below:
"parent_first_child_input":
[{"parent_input_index": num, "child_input_index": num}, ...]
"parent_last_child_output":
[{"parent_output_index": num, "child_output_index": num}, ...]
"internal_children_input_output":
[{"child_input_index": num, "child_output_index": num}, ...]
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Keyword arguments of any constant attributes for the function.
</td>
</tr>
</table>



## Child Classes
[`class OpHintArgumentTracker`](../../../../tf/compat/v1/lite/OpHint/OpHintArgumentTracker.md)

## Methods

<h3 id="add_input"><code>add_input</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/lite/python/op_hint.py#L388-L408">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_input(
    *args, **kwargs
)
</code></pre>

Add a wrapped input argument to the hint.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`*args`
</td>
<td>
The input tensor.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
"name" label
"tag" a tag to group multiple arguments that will be aggregated. I.e.
a string like 'cool_input'. Basically multiple inputs can be added
to the same hint for parallel operations that will eventually be
combined. An example would be static_rnn which creates multiple copies
of state or inputs.
"aggregate" aggregation strategy that is valid only for tag non None.
Acceptable values are OpHint.AGGREGATE_FIRST, OpHint.AGGREGATE_LAST,
and OpHint.AGGREGATE_STACK.
"index_override" The global index to use. This corresponds to the
argument order in the final stub that will be generated.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The wrapped input tensor.
</td>
</tr>

</table>



<h3 id="add_inputs"><code>add_inputs</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/lite/python/op_hint.py#L432-L449">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_inputs(
    *args, **kwargs
)
</code></pre>

Add a sequence of inputs to the function invocation.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`*args`
</td>
<td>
List of inputs to be converted (should be Tf.Tensor).
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
This allows 'names' which should be a list of names.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Wrapped inputs (identity standins that have additional metadata). These
are also are also tf.Tensor's.
</td>
</tr>

</table>



<h3 id="add_output"><code>add_output</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/lite/python/op_hint.py#L410-L430">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_output(
    *args, **kwargs
)
</code></pre>

Add a wrapped output argument to the hint.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`*args`
</td>
<td>
The output tensor.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
"name" label
"tag" a tag to group multiple arguments that will be aggregated. I.e.
a string like 'cool_input'. Basically multiple inputs can be added
to the same hint for parallel operations that will eventually be
combined. An example would be static_rnn which creates multiple copies
of state or inputs.
"aggregate" aggregation strategy that is valid only for tag non None.
Acceptable values are OpHint.AGGREGATE_FIRST, OpHint.AGGREGATE_LAST,
and OpHint.AGGREGATE_STACK.
"index_override" The global index to use. This corresponds to the
argument order in the final stub that will be generated.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The wrapped output tensor.
</td>
</tr>

</table>



<h3 id="add_outputs"><code>add_outputs</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/lite/python/op_hint.py#L451-L468">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_outputs(
    *args, **kwargs
)
</code></pre>

Add a sequence of outputs to the function invocation.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`*args`
</td>
<td>
List of outputs to be converted (should be tf.Tensor).
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
See
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Wrapped outputs (identity standins that have additional metadata). These
are also tf.Tensor's.
</td>
</tr>

</table>





## Class Variables

* `AGGREGATE_FIRST = 'first'` <a id="AGGREGATE_FIRST"></a>
* `AGGREGATE_LAST = 'last'` <a id="AGGREGATE_LAST"></a>
* `AGGREGATE_STACK = 'stack'` <a id="AGGREGATE_STACK"></a>
* `CHILDREN_INPUTS_MAPPINGS = '_tflite_children_ophint_inputs_mapping'` <a id="CHILDREN_INPUTS_MAPPINGS"></a>
* `FUNCTION_AGGREGATE_ATTR = '_tflite_function_aggregate'` <a id="FUNCTION_AGGREGATE_ATTR"></a>
* `FUNCTION_INPUT_INDEX_ATTR = '_tflite_function_input_index'` <a id="FUNCTION_INPUT_INDEX_ATTR"></a>
* `FUNCTION_LEVEL_ATTR = '_tflite_ophint_level'` <a id="FUNCTION_LEVEL_ATTR"></a>
* `FUNCTION_NAME_ATTR = '_tflite_function_name'` <a id="FUNCTION_NAME_ATTR"></a>
* `FUNCTION_OUTPUT_INDEX_ATTR = '_tflite_function_output_index'` <a id="FUNCTION_OUTPUT_INDEX_ATTR"></a>
* `FUNCTION_SORT_INDEX_ATTR = '_tflite_function_sort_index'` <a id="FUNCTION_SORT_INDEX_ATTR"></a>
* `FUNCTION_UUID_ATTR = '_tflite_function_uuid'` <a id="FUNCTION_UUID_ATTR"></a>
* `TFLITE_INPUT_INDICES = '_tflite_input_indices'` <a id="TFLITE_INPUT_INDICES"></a>
