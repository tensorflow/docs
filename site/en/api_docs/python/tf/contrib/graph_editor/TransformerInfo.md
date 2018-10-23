


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.graph_editor.TransformerInfo

### `class tf.contrib.graph_editor.TransformerInfo`

"Contains information about the result of a transform operation.

## Methods

<h3 id="__init__"><code>__init__(info)</code></h3>

Constructor.

#### Args:

* <b>`info`</b>: an instance of Transformer._TmpInfo containing various internal
    information about the transform operation.

<h3 id="original"><code>original(transformed, missing_fn=None)</code></h3>

Return the original op/tensor corresponding to the transformed one.

Note that the output of this function mimics the hierarchy
of its input argument `transformed`.
Given an iterable, it returns a list. Given an operation or a tensor,
it will return an operation or a tensor.

#### Args:

* <b>`transformed`</b>: the transformed tensor/operation.
* <b>`missing_fn`</b>: function handling the case where the counterpart
    cannot be found. By default, None is returned.
Returns:
  the original tensor/operation (or None if no match is found).

<h3 id="transformed"><code>transformed(original, missing_fn=None)</code></h3>

Return the transformed op/tensor corresponding to the original one.

Note that the output of this function mimics the hierarchy
of its input argument `original`.
Given an iterable, it returns a list. Given an operation or a tensor,
it will return an operation or a tensor.

#### Args:

* <b>`original`</b>: the original tensor/operation.
* <b>`missing_fn`</b>: function handling the case where the counterpart
    cannot be found. By default, None is returned.
Returns:
  the transformed tensor/operation (or None if no match is found).





Defined in [`tensorflow/contrib/graph_editor/transform.py`](https://www.tensorflow.org/code/tensorflow/contrib/graph_editor/transform.py).

