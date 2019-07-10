page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.numpy_function

Wraps a python function and uses it as a TensorFlow op.

### Aliases:

* `tf.compat.v1.numpy_function`
* `tf.compat.v2.numpy_function`
* `tf.numpy_function`

``` python
tf.numpy_function(
    func,
    inp,
    Tout,
    name=None
)
```



Defined in [`python/ops/script_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/script_ops.py).

<!-- Placeholder for "Used in" -->

Given a python function `func`, which takes numpy arrays as its
arguments and returns numpy arrays as its outputs, wrap this function as an
operation in a TensorFlow graph. The following snippet constructs a simple
TensorFlow graph that invokes the `np.sinh()` NumPy function as a operation
in the graph:

```python
def my_func(x):
  # x will be a numpy array with the contents of the placeholder below
  return np.sinh(x)
input = tf.compat.v1.placeholder(tf.float32)
y = tf.compat.v1.numpy_function(my_func, [input], tf.float32)
```

**N.B.** The <a href="../tf/numpy_function"><code>tf.compat.v1.numpy_function()</code></a> operation has the following known
limitations:

* The body of the function (i.e. `func`) will not be serialized in a
  `GraphDef`. Therefore, you should not use this function if you need to
  serialize your model and restore it in a different environment.

* The operation must run in the same address space as the Python program
  that calls <a href="../tf/numpy_function"><code>tf.compat.v1.numpy_function()</code></a>. If you are using distributed
  TensorFlow, you
  must run a <a href="../tf/distribute/Server"><code>tf.distribute.Server</code></a> in the same process as the program that
  calls
  <a href="../tf/numpy_function"><code>tf.compat.v1.numpy_function()</code></a> and you must pin the created operation to a device
  in that
  server (e.g. using `with tf.device():`).

#### Args:


* <b>`func`</b>: A Python function, which accepts `ndarray` objects as arguments and
  returns a list of `ndarray` objects (or a single `ndarray`). This function
  must accept as many arguments as there are tensors in `inp`, and these
  argument types will match the corresponding <a href="../tf/Tensor"><code>tf.Tensor</code></a> objects in `inp`.
  The returns `ndarray`s must match the number and types defined `Tout`.
  Important Note: Input and output numpy `ndarray`s of `func` are not
    guaranteed to be copies. In some cases their underlying memory will be
    shared with the corresponding TensorFlow tensors. In-place modification
    or storing `func` input or return values in python datastructures
    without explicit (np.)copy can have non-deterministic consequences.
* <b>`inp`</b>: A list of `Tensor` objects.
* <b>`Tout`</b>: A list or tuple of tensorflow data types or a single tensorflow data
  type if there is only one, indicating what `func` returns.
* <b>`stateful`</b>: (Boolean.) If True, the function should be considered stateful. If
  a function is stateless, when given the same input it will return the same
  output and have no observable side effects. Optimizations such as common
  subexpression elimination are only performed on stateless operations.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A list of `Tensor` or a single `Tensor` which `func` computes.
