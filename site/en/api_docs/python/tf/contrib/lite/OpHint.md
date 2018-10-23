

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lite.OpHint

## Class `OpHint`





Defined in [`tensorflow/contrib/lite/python/op_hint.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/lite/python/op_hint.py).

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

## Methods

<h3 id="__init__"><code>__init__</code></h3>

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

<h3 id="add_inputs"><code>add_inputs</code></h3>

``` python
add_inputs(*args)
```

Add a sequence of inputs to the function invocation.

#### Args:

* <b>`*args`</b>: List of inputs to be converted (should be Tf.Tensor).

#### Returns:

Wrapped inputs (identity standins that have additional metadata). These
are also are also tf.Tensor's.

<h3 id="add_outputs"><code>add_outputs</code></h3>

``` python
add_outputs(*args)
```

Add a sequence of outputs to the function invocation.

#### Args:

* <b>`*args`</b>: List of outputs to be converted (should be tf.Tensor).

#### Returns:

Wrapped outputs (identity standins that have additional metadata). These
are also tf.Tensor's.



## Class Members

<h3 id="FUNCTION_INPUT_INDEX_ATTR"><code>FUNCTION_INPUT_INDEX_ATTR</code></h3>

<h3 id="FUNCTION_NAME_ATTR"><code>FUNCTION_NAME_ATTR</code></h3>

<h3 id="FUNCTION_OUTPUT_INDEX_ATTR"><code>FUNCTION_OUTPUT_INDEX_ATTR</code></h3>

<h3 id="FUNCTION_UUID_ATTR"><code>FUNCTION_UUID_ATTR</code></h3>

