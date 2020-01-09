page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.py_function


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/py_function">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/script_ops.py#L345-L425">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Wraps a python function into a TensorFlow op that executes it eagerly.

### Aliases:

* <a href="/api_docs/python/tf/py_function"><code>tf.compat.v1.py_function</code></a>
* <a href="/api_docs/python/tf/py_function"><code>tf.compat.v2.py_function</code></a>
* <a href="/api_docs/python/tf/py_function"><code>tf.contrib.eager.py_func</code></a>


``` python
tf.py_function(
    func,
    inp,
    Tout,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This function allows expressing computations in a TensorFlow graph as
Python functions. In particular, it wraps a Python function `func`
in a once-differentiable TensorFlow operation that executes it with eager
execution enabled. As a consequence, <a href="../tf/py_function"><code>tf.py_function</code></a> makes it
possible to express control flow using Python constructs (`if`, `while`,
`for`, etc.), instead of TensorFlow control flow constructs (<a href="../tf/cond"><code>tf.cond</code></a>,
<a href="../tf/while_loop"><code>tf.while_loop</code></a>). For example, you might use <a href="../tf/py_function"><code>tf.py_function</code></a> to
implement the log huber function:

```python
def log_huber(x, m):
  if tf.abs(x) <= m:
    return x**2
  else:
    return m**2 * (1 - 2 * tf.math.log(m) + tf.math.log(x**2))

x = tf.compat.v1.placeholder(tf.float32)
m = tf.compat.v1.placeholder(tf.float32)

y = tf.py_function(func=log_huber, inp=[x, m], Tout=tf.float32)
dy_dx = tf.gradients(y, x)[0]

with tf.compat.v1.Session() as sess:
  # The session executes `log_huber` eagerly. Given the feed values below,
  # it will take the first branch, so `y` evaluates to 1.0 and
  # `dy_dx` evaluates to 2.0.
  y, dy_dx = sess.run([y, dy_dx], feed_dict={x: 1.0, m: 2.0})
```

You can also use <a href="../tf/py_function"><code>tf.py_function</code></a> to debug your models at runtime
using Python tools, i.e., you can isolate portions of your code that
you want to debug, wrap them in Python functions and insert `pdb` tracepoints
or print statements as desired, and wrap those functions in
<a href="../tf/py_function"><code>tf.py_function</code></a>.

For more information on eager execution, see the
[Eager guide](https://tensorflow.org/guide/eager).

<a href="../tf/py_function"><code>tf.py_function</code></a> is similar in spirit to <a href="../tf/py_func"><code>tf.compat.v1.py_func</code></a>, but unlike
the latter, the former lets you use TensorFlow operations in the wrapped
Python function. In particular, while <a href="../tf/py_func"><code>tf.compat.v1.py_func</code></a> only runs on CPUs
and
wraps functions that take NumPy arrays as inputs and return NumPy arrays as
outputs, <a href="../tf/py_function"><code>tf.py_function</code></a> can be placed on GPUs and wraps functions
that take Tensors as inputs, execute TensorFlow operations in their bodies,
and return Tensors as outputs.

Like <a href="../tf/py_func"><code>tf.compat.v1.py_func</code></a>, <a href="../tf/py_function"><code>tf.py_function</code></a> has the following limitations
with respect to serialization and distribution:

* The body of the function (i.e. `func`) will not be serialized in a
  `GraphDef`. Therefore, you should not use this function if you need to
  serialize your model and restore it in a different environment.

* The operation must run in the same address space as the Python program
  that calls <a href="../tf/py_function"><code>tf.py_function()</code></a>. If you are using distributed
  TensorFlow, you must run a <a href="../tf/distribute/Server"><code>tf.distribute.Server</code></a> in the same process as the
  program that calls <a href="../tf/py_function"><code>tf.py_function()</code></a> and you must pin the created
  operation to a device in that server (e.g. using `with tf.device():`).


#### Args:


* <b>`func`</b>: A Python function which accepts a list of `Tensor` objects having
  element types that match the corresponding <a href="../tf/Tensor"><code>tf.Tensor</code></a> objects in `inp`
  and returns a list of `Tensor` objects (or a single `Tensor`, or `None`)
  having element types that match the corresponding values in `Tout`.
* <b>`inp`</b>: A list of `Tensor` objects.
* <b>`Tout`</b>: A list or tuple of tensorflow data types or a single tensorflow data
  type if there is only one, indicating what `func` returns; an empty list
  if no value is returned (i.e., if the return value is `None`).
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A list of `Tensor` or a single `Tensor` which `func` computes; an empty list
if `func` returns None.
