page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lite.OpHint

## Class `OpHint`





Defined in [`tensorflow/contrib/lite/python/op_hint.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/lite/python/op_hint.py).

A class that helps build tflite function invocations.

It allows you to take a bunch of TensorFlow ops and annotate the construction
such that toco knows how to convert it to tflite. This embeds a pseudo
function in a TensorFlow graph. This allows embedding high-level API usage
information in a lower level TensorFlow implementation so that an alternative
implementation can be substituted later.

Essentially, any "input" into this pseudo op is fed into an identity, and
attributes are added to that input before being used by the constituent ops
that make up the pseudo op. A similar process is done to any output that
is to be exported from the current op.

TODO(aselle): When TensorFlow functions functionality works for arbitrary
constructs, this mechanism can be retired and changed to use python defun's.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    function_name,
    **kwargs
)
```

Create a OpHint.

#### Args:

* <b>`function_name`</b>: Name of the function (the custom op name in tflite)
* <b>`**kwargs`</b>: Keyword arguments of any constant attributes for the function.



## Child Classes
[`class OpHintArgumentTracker`](../../../tf/contrib/lite/OpHint/OpHintArgumentTracker)

## Methods

<h3 id="add_input"><code>add_input</code></h3>

``` python
add_input(
    *args,
    **kwargs
)
```

Add a wrapped input argument to the hint.

#### Args:

* <b>`*args`</b>: The input tensor.
* <b>`**kwargs`</b>:     "name" label
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

``` python
add_output(
    *args,
    **kwargs
)
```

Add a wrapped output argument to the hint.

#### Args:

* <b>`*args`</b>: The output tensor.
* <b>`**kwargs`</b>:     "name" label
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

<h3 id="AGGREGATE_FIRST"><code>AGGREGATE_FIRST</code></h3>

<h3 id="AGGREGATE_LAST"><code>AGGREGATE_LAST</code></h3>

<h3 id="AGGREGATE_STACK"><code>AGGREGATE_STACK</code></h3>

<h3 id="FUNCTION_AGGREGATE_ATTR"><code>FUNCTION_AGGREGATE_ATTR</code></h3>

<h3 id="FUNCTION_INPUT_INDEX_ATTR"><code>FUNCTION_INPUT_INDEX_ATTR</code></h3>

<h3 id="FUNCTION_NAME_ATTR"><code>FUNCTION_NAME_ATTR</code></h3>

<h3 id="FUNCTION_OUTPUT_INDEX_ATTR"><code>FUNCTION_OUTPUT_INDEX_ATTR</code></h3>

<h3 id="FUNCTION_SORT_INDEX_ATTR"><code>FUNCTION_SORT_INDEX_ATTR</code></h3>

<h3 id="FUNCTION_UUID_ATTR"><code>FUNCTION_UUID_ATTR</code></h3>

<h3 id="TFLITE_INPUT_INDICES"><code>TFLITE_INPUT_INDICES</code></h3>

