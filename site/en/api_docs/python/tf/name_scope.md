page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.name_scope


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/name_scope">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L6251-L6361">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `name_scope`

A context manager for use when defining a Python op.



### Aliases:

* Class <a href="/api_docs/python/tf/name_scope"><code>tf.compat.v1.keras.backend.name_scope</code></a>
* Class <a href="/api_docs/python/tf/name_scope"><code>tf.compat.v1.name_scope</code></a>
* Class <a href="/api_docs/python/tf/name_scope"><code>tf.keras.backend.name_scope</code></a>


<!-- Placeholder for "Used in" -->

This context manager validates that the given `values` are from the
same graph, makes that graph the default graph, and pushes a
name scope in that graph (see
<a href="../tf/Graph#name_scope"><code>tf.Graph.name_scope</code></a>
for more details on that).

For example, to define a new Python op called `my_op`:

```python
def my_op(a, b, c, name=None):
  with tf.name_scope(name, "MyOp", [a, b, c]) as scope:
    a = tf.convert_to_tensor(a, name="a")
    b = tf.convert_to_tensor(b, name="b")
    c = tf.convert_to_tensor(c, name="c")
    # Define some computation that uses `a`, `b`, and `c`.
    return foo_op(..., name=scope)
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L6277-L6303">View source</a>

``` python
__init__(
    name,
    default_name=None,
    values=None
)
```

Initialize the context manager.


#### Args:


* <b>`name`</b>: The name argument that is passed to the op function.
* <b>`default_name`</b>: The default name to use if the `name` argument is `None`.
* <b>`values`</b>: The list of `Tensor` arguments that are passed to the op function.


#### Raises:


* <b>`TypeError`</b>: if `default_name` is passed in but not a string.



## Properties

<h3 id="name"><code>name</code></h3>






## Methods

<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L6305-L6350">View source</a>

``` python
__enter__()
```

Start the scope block.


#### Returns:

The scope name.



#### Raises:


* <b>`ValueError`</b>: if neither `name` nor `default_name` is provided
  but `values` are.

<h3 id="__exit__"><code>__exit__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L6352-L6361">View source</a>

``` python
__exit__(
    type_arg,
    value_arg,
    traceback_arg
)
```
