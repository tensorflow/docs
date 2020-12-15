description: Conceptually tracks indices of arguments of "OpHint functions".

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.lite.OpHint.OpHintArgumentTracker" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add"/>
</div>

# tf.compat.v1.lite.OpHint.OpHintArgumentTracker

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/lite/python/op_hint.py#L162-L310">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Conceptually tracks indices of arguments of "OpHint functions".

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.lite.OpHint.OpHintArgumentTracker(
    function_name, unique_function_id, node_name_prefix, attr_name, level=1,
    children_inputs_mappings=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The inputs and arguments of these functions both use an instance
of the class so they can have independent numbering.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`function_name`
</td>
<td>
Name of the function that this tracks arguments for.
</td>
</tr><tr>
<td>
`unique_function_id`
</td>
<td>
UUID of function that this tracks arguments for.
</td>
</tr><tr>
<td>
`node_name_prefix`
</td>
<td>
How identities that are created are named.
</td>
</tr><tr>
<td>
`attr_name`
</td>
<td>
Name of attribute to use to store the index for this hint.
i.e. FUNCTION_INPUT_INDEX or FUNCTION_OUTPUT_INDEX
</td>
</tr><tr>
<td>
`level`
</td>
<td>
Hierarchical level of the Ophint node, a number.
</td>
</tr><tr>
<td>
`children_inputs_mappings`
</td>
<td>
Inputs/Outputs mapping for children hints.
</td>
</tr>
</table>



## Methods

<h3 id="add"><code>add</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/lite/python/op_hint.py#L229-L310">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add(
    arg, tag=None, name=None, aggregate=None, index_override=None
)
</code></pre>

Return a wrapped tensor of an input tensor as an argument.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`arg`
</td>
<td>
A TensorFlow tensor that should be considered an argument.
</td>
</tr><tr>
<td>
`tag`
</td>
<td>
String tag to identify arguments that should be packed.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Name of argument. This is included in the Identity hint op names.
</td>
</tr><tr>
<td>
`aggregate`
</td>
<td>
Strategy to aggregate.
Acceptable values are OpHint.AGGREGATE_FIRST, OpHint.AGGREGATE_LAST,
and OpHint.AGGREGATE_STACK.
Note, aggregate is only valid if tag is specified.
</td>
</tr><tr>
<td>
`index_override`
</td>
<td>
Specify what input/output index should this be in the
final stub. i.e. add(arg0, index=1); add(arg1, index=0) will make the
final stub be as stub_func(inputs[arg1, arg0], outputs=[]) rather than
the default call order based ordering.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A tensor representing the wrapped argument.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
When indices are not consistent.
</td>
</tr>
</table>





