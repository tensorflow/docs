page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.add_execution_callback

``` python
tf.contrib.eager.add_execution_callback(callback)
```



Defined in [`tensorflow/python/eager/execution_callbacks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/eager/execution_callbacks.py).

Add an execution callback to the default eager context.

An execution callback is invoked immediately after an eager operation or
function has finished execution, providing access to the op's type, name
input and output tensors. Multiple execution callbacks can be added, in
which case the callbacks will be invoked in the order in which they are
added. To clear all execution callbacks that have been added, use
`clear_execution_callbacks()`.

Example:

```python
def print_even_callback(op_type, op_name, attrs, inputs, outputs):
  # A callback that prints only the even output values.
  if outputs[0].numpy() % 2 == 0:
    print("Even output from %s: %s" % (op_name or op_type,  outputs))
tfe.add_execution_callback(print_even_callback)

x = tf.pow(2.0, 3.0) - 3.0
y = tf.multiply(x, tf.add(1.0, 5.0))
# When the line above is run, you will see all intermediate outputs that are
# even numbers printed to the console.

tfe.clear_execution_callbacks()
```

#### Args:

* <b>`callback`</b>: a callable of the signature
    `f(op_type, op_name, attrs, inputs, outputs)`.
    `op_type` is the type of the operation that was just executed (e.g.,
      `MatMul`).
    `op_name` is the name of the operation that was just executed. This
      name is set by the client who created the operation and can be `None` if
      it is unset.
    `attrs` contains the attributes of the operation as a `tuple` of
      alternating attribute name and attribute value.
    `inputs` is the `list` of input `Tensor`(s) to the op.
    `outputs` is the `list` of output `Tensor`(s) from the op.
     Return value(s) from the callback are ignored.