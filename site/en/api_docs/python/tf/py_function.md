description: Wraps a python function into a TensorFlow op that executes it eagerly.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.py_function" />
<meta itemprop="path" content="Stable" />
</div>

# tf.py_function

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/script_ops.py#L431-L513">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Wraps a python function into a TensorFlow op that executes it eagerly.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.py_function`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.py_function(
    func, inp, Tout, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function allows expressing computations in a TensorFlow graph as
Python functions. In particular, it wraps a Python function `func`
in a once-differentiable TensorFlow operation that executes it with eager
execution enabled. As a consequence, <a href="../tf/py_function.md"><code>tf.py_function</code></a> makes it
possible to express control flow using Python constructs (`if`, `while`,
`for`, etc.), instead of TensorFlow control flow constructs (<a href="../tf/cond.md"><code>tf.cond</code></a>,
<a href="../tf/while_loop.md"><code>tf.while_loop</code></a>). For example, you might use <a href="../tf/py_function.md"><code>tf.py_function</code></a> to
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

You can also use <a href="../tf/py_function.md"><code>tf.py_function</code></a> to debug your models at runtime
using Python tools, i.e., you can isolate portions of your code that
you want to debug, wrap them in Python functions and insert `pdb` tracepoints
or print statements as desired, and wrap those functions in
<a href="../tf/py_function.md"><code>tf.py_function</code></a>.

For more information on eager execution, see the
[Eager guide](https://tensorflow.org/guide/eager).

<a href="../tf/py_function.md"><code>tf.py_function</code></a> is similar in spirit to <a href="../tf/compat/v1/py_func.md"><code>tf.compat.v1.py_func</code></a>, but unlike
the latter, the former lets you use TensorFlow operations in the wrapped
Python function. In particular, while <a href="../tf/compat/v1/py_func.md"><code>tf.compat.v1.py_func</code></a> only runs on CPUs
and
wraps functions that take NumPy arrays as inputs and return NumPy arrays as
outputs, <a href="../tf/py_function.md"><code>tf.py_function</code></a> can be placed on GPUs and wraps functions
that take Tensors as inputs, execute TensorFlow operations in their bodies,
and return Tensors as outputs.

Like <a href="../tf/compat/v1/py_func.md"><code>tf.compat.v1.py_func</code></a>, <a href="../tf/py_function.md"><code>tf.py_function</code></a> has the following limitations
with respect to serialization and distribution:

* The body of the function (i.e. `func`) will not be serialized in a
  `GraphDef`. Therefore, you should not use this function if you need to
  serialize your model and restore it in a different environment.

* The operation must run in the same address space as the Python program
  that calls <a href="../tf/py_function.md"><code>tf.py_function()</code></a>. If you are using distributed
  TensorFlow, you must run a <a href="../tf/distribute/Server.md"><code>tf.distribute.Server</code></a> in the same process as the
  program that calls <a href="../tf/py_function.md"><code>tf.py_function()</code></a> and you must pin the created
  operation to a device in that server (e.g. using `with tf.device():`).


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`func`
</td>
<td>
A Python function which accepts a list of `Tensor` objects having
element types that match the corresponding <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> objects in `inp`
and returns a list of `Tensor` objects (or a single `Tensor`, or `None`)
having element types that match the corresponding values in `Tout`.
</td>
</tr><tr>
<td>
`inp`
</td>
<td>
A list of `Tensor` objects.
</td>
</tr><tr>
<td>
`Tout`
</td>
<td>
A list or tuple of tensorflow data types or a single tensorflow data
type if there is only one, indicating what `func` returns; an empty list
if no value is returned (i.e., if the return value is `None`).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list of `Tensor` or a single `Tensor` which `func` computes; an empty list
if `func` returns None.
</td>
</tr>

</table>

