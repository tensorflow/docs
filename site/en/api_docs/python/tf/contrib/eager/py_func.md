

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.py_func

``` python
tf.contrib.eager.py_func(
    func,
    inp,
    Tout,
    name=None
)
```



Defined in [`tensorflow/python/ops/script_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/script_ops.py).

Wraps a python function into a TensorFlow op that executes it eagerly.

This function allows expressing computations in a TensorFlow graph as
Python functions. In particular, it wraps a Python function `func`
in a TensorFlow operation that executes it with eager exeuction enabled. As a
consequence, <a href="../../../tf/contrib/eager/py_func"><code>tf.contrib.eager.py_func</code></a> makes it possible to express control
flow using Python constructs (`if`, `while`, `for`, etc.), instead of
TensorFlow control flow constructs (<a href="../../../tf/cond"><code>tf.cond</code></a>, <a href="../../../tf/while_loop"><code>tf.while_loop</code></a>). For
example, you might use <a href="../../../tf/contrib/eager/py_func"><code>tf.contrib.eager.py_func</code></a> to implement the log huber
function:

```python
def log_huber(x, m):
  if tf.abs(x) <= m:
    return x ** 2
  else:
    return m ** 2 * (1 - 2 * tf.log(m) + tf.log(x ** 2))

x = tf.placeholder(tf.float32)
m = tf.placeholder(tf.float32)

y = tf.contrib.eager.py_func(func=log_huber, inp=[x, m], Tout=tf.float32)

with tf.Session() as sess:
  # The session executes `log_huber` eagerly. Given the feed values below,
  # it will take the second branch, so `output` evaluates to 7.24372.
  output = sess.run(y, feed_dict={x: 3.0, m: 2.0})
```

You can also use <a href="../../../tf/contrib/eager/py_func"><code>tf.contrib.eager.py_func</code></a> to debug your models at runtime
using Python tools, i.e., you can isolate portions of your code that
you want to debug, wrap them in Python functions and insert `pdb` tracepoints
or print statements as desired, and wrap those functions in
<a href="../../../tf/contrib/eager/py_func"><code>tf.contrib.eager.py_func</code></a>.

For more information on eager execution, see <a href="../../../../../guide/eager">Eager Execution</a>.

<a href="../../../tf/contrib/eager/py_func"><code>tf.contrib.eager.py_func</code></a> is similar in spirit to <a href="../../../tf/py_func"><code>tf.py_func</code></a>, but unlike
the latter, the former lets you use TensorFlow operations in the wrapped
Python function. In particular, while <a href="../../../tf/py_func"><code>tf.py_func</code></a> only runs on CPUs and
wraps functions that take NumPy arrays as inputs and return NumPy arrays as
outputs, <a href="../../../tf/contrib/eager/py_func"><code>tf.contrib.eager.py_func</code></a> can be placed on GPUs and wraps functions
that take Tensors as inputs, execute TensorFlow operations in their bodies,
and return Tensors as outputs.

<a href="../../../tf/contrib/eager/py_func"><code>tf.contrib.eager.py_func</code></a> is not differentiable, though a gradient may be
implemented in the future; if you would like to differentiate through it,
please file an issue on Github.

Like <a href="../../../tf/py_func"><code>tf.py_func</code></a>, <a href="../../../tf/contrib/eager/py_func"><code>tf.contrib.eager.py_func</code></a> has the following limitations
with respect to serialization and distribution:

* The body of the function (i.e. `func`) will not be serialized in a
  `GraphDef`. Therefore, you should not use this function if you need to
  serialize your model and restore it in a different environment.

* The operation must run in the same address space as the Python program
  that calls `tf.contrib.eager.py_func()`. If you are using distributed
  TensorFlow, you must run a <a href="../../../tf/train/Server"><code>tf.train.Server</code></a> in the same process as the
  program that calls `tf.contrib.eager.py_func()` and you must pin the created
  operation to a device in that server (e.g. using `with tf.device():`).


#### Args:

* <b>`func`</b>: A Python function which accepts a list of `Tensor` objects
    having element types that match the corresponding <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> objects
    in `inp` and returns a list of `Tensor` objects (or a single
    `Tensor`, or `None`) having element types that match the
    corresponding values in `Tout`.
* <b>`inp`</b>: A list of `Tensor` objects.
* <b>`Tout`</b>: A list or tuple of tensorflow data types or a single tensorflow data
    type if there is only one, indicating what `func` returns; an empty list
    if no value is returned (i.e., if the return value is `None`).
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A list of `Tensor` or a single `Tensor` which `func` computes; an empty list
if `func` returns None.