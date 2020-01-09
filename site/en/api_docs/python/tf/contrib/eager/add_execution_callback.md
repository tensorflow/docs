page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.add_execution_callback


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/eager/execution_callbacks.py#L243-L284">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Add an execution callback to the default eager context.

``` python
tf.contrib.eager.add_execution_callback(callback)
```



<!-- Placeholder for "Used in" -->

An execution callback is invoked immediately after an eager operation or
function has finished execution, providing access to the op's type, name
input and output tensors. Multiple execution callbacks can be added, in
which case the callbacks will be invoked in the order in which they are
added. To clear all execution callbacks that have been added, use
`clear_execution_callbacks()`.

#### Example:


```python
def print_even_callback(op_type, inputs, attrs, outputs, op_name):
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
  `f(op_type, inputs, attrs, outputs, op_name)`.
  `op_type` is the type of the operation that was just executed (e.g.,
     `MatMul`).
  `inputs` is the `list` of input `Tensor`(s) to the op.
  `attrs` contains the attributes of the operation as a `tuple` of
     alternating attribute name and attribute value.
  `outputs` is the `list` of output `Tensor`(s) from the op.
  `op_name` is the name of the operation that was just executed. This
     name is set by the client who created the operation and can be `None`
     if it is unset.
   Return value(s) from the callback are ignored.
