

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.Print

``` python
Print(
    input_,
    data,
    message=None,
    first_n=None,
    summarize=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/logging_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/ops/logging_ops.py).

See the guide: [Control Flow > Debugging Operations](../../../api_guides/python/control_flow_ops#Debugging_Operations)

Prints a list of tensors.

This is an identity op (behaves like `tf.identity`) with the side effect
of printing `data` when evaluating.

Note: This op prints to the standard error. It is not currently compatible
  with jupyter notebook (printing to the notebook *server's* output, not into
  the notebook).

#### Args:

* <b>`input_`</b>: A tensor passed through this op.
* <b>`data`</b>: A list of tensors to print out when op is evaluated.
* <b>`message`</b>: A string, prefix of the error message.
* <b>`first_n`</b>: Only log `first_n` number of times. Negative numbers log always;
           this is the default.
* <b>`summarize`</b>: Only print this many entries of each tensor. If None, then a
             maximum of 3 elements are printed per input tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type and contents as `input_`.