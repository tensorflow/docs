

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.eager.defun

``` python
defun(func)
```



Defined in [`tensorflow/python/eager/function.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/eager/function.py).

Decorator to compile func into graph_mode.

`defun` converts a function that constructs a TensorFlow graph into a function
that executes the graph. TensorFlow graphs typically execute faster and with a
lower memory-footprint than executing each of the operations that make up the
function individually as the TensorFlow runtime can optimize the graph and
execute sub-operations in parallel.

func must be a Python function that constructs a TensorFlow graph,
typically using functions in the tensorflow module.

Arguments to func can be either Tensor objects or Python
objects. Non-Tensor python objects are treated as constants, and new function
definitions are created internally based on their values.

func must return a tf.Tensor (NOT a Tensor) or a list of tf.Tensor (NOT a
Tensor).

Control flow constructs (e.g., `if`, `while`) are not yet compatible with
`defun`.

Example:

```python
def f(x, y):
  return tf.reduce_mean(tf.multiply(x ** 2, 3) + y)

@tfe.defun
def g(x, y):
  return tf.reduce_mean(tf.multiply(x ** 2, 3) + y)

x = tf.constant([[2.0, 3.0]])
y = tf.constant([[3.0, -2.0]])
# The plain function and defun-compiled function should return the same value.
assert f(x, y).numpy() == g(x, y).numpy()

# After the first invocation, the defun-compiled (graph) function runs faster
# than the plain function because the defun-compiled function does not involve
# Python interpreter overhead during the execution.
%time print(f(x, y))
%time print(g(x, y))
```

#### Args:

* <b>`func`</b>: function to be compiled.


#### Returns:

A callable that will execute the compiled function (and return zero
or more Tensor objects).