page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.lite.OpHint


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/lite/python/op_hint.py#L93-L462">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `OpHint`

A class that helps build tflite function invocations.



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

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/lite/python/op_hint.py#L308-L346">View source</a>

``` python
__init__(
    function_name,
    level=1,
    children_inputs_mappings=None,
    **kwargs
)
```

Create a OpHint.


#### Args:


* <b>`function_name`</b>: Name of the function (the custom op name in tflite)
* <b>`level`</b>: OpHint level.
* <b>`children_inputs_mappings`</b>: Children OpHint inputs/outputs mapping.
  children_inputs_mappings should like below:
  "parent_first_child_input":
      [{"parent_input_index": num, "child_input_index": num}, ...]
  "parent_last_child_output":
      [{"parent_output_index": num, "child_output_index": num}, ...]
  "internal_children_input_output":
      [{"child_input_index": num, "child_output_index": num}, ...]
* <b>`**kwargs`</b>: Keyword arguments of any constant attributes for the function.



## Child Classes
[`class OpHintArgumentTracker`](../../../../tf/compat/v1/lite/OpHint/OpHintArgumentTracker)

## Methods

<h3 id="add_input"><code>add_input</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/lite/python/op_hint.py#L384-L404">View source</a>

``` python
add_input(
    *args,
    **kwargs
)
```

Add a wrapped input argument to the hint.


#### Args:


* <b>`*args`</b>: The input tensor.
* <b>`**kwargs`</b>:   "name" label
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

#### Returns:

The wrapped input tensor.


<h3 id="add_inputs"><code>add_inputs</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/lite/python/op_hint.py#L428-L444">View source</a>

``` python
add_inputs(
    *args,
    **kwargs
)
```

Add a sequence of inputs to the function invocation.


#### Args:


* <b>`*args`</b>: List of inputs to be converted (should be Tf.Tensor).
* <b>`**kwargs`</b>: This allows 'names' which should be a list of names.

#### Returns:

Wrapped inputs (identity standins that have additional metadata). These
are also are also tf.Tensor's.


<h3 id="add_output"><code>add_output</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/lite/python/op_hint.py#L406-L426">View source</a>

``` python
add_output(
    *args,
    **kwargs
)
```

Add a wrapped output argument to the hint.


#### Args:


* <b>`*args`</b>: The output tensor.
* <b>`**kwargs`</b>:   "name" label
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

#### Returns:

The wrapped output tensor.


<h3 id="add_outputs"><code>add_outputs</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/lite/python/op_hint.py#L446-L462">View source</a>

``` python
add_outputs(
    *args,
    **kwargs
)
```

Add a sequence of outputs to the function invocation.


#### Args:


* <b>`*args`</b>: List of outputs to be converted (should be tf.Tensor).
* <b>`**kwargs`</b>: See

#### Returns:

Wrapped outputs (identity standins that have additional metadata). These
are also tf.Tensor's.




## Class Members

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
