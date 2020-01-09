page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.name_scope


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/ops.py#L6386-L6454">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `name_scope`

A context manager for use when defining a Python op.

Inherits From: [`name_scope`](../tf/compat/v1/keras/backend/name_scope)

### Aliases:

* Class `tf.compat.v2.name_scope`


<!-- Placeholder for "Used in" -->

This context manager pushes a name scope, which will make the name of all
operations added within it have a prefix.

For example, to define a new Python op called `my_op`:

```python
def my_op(a, b, c, name=None):
  with tf.name_scope("MyOp") as scope:
    a = tf.convert_to_tensor(a, name="a")
    b = tf.convert_to_tensor(b, name="b")
    c = tf.convert_to_tensor(c, name="c")
    # Define some computation that uses `a`, `b`, and `c`.
    return foo_op(..., name=scope)
```

When executed, the Tensors `a`, `b`, `c`, will have names `MyOp/a`, `MyOp/b`,
and `MyOp/c`.

If the scope name already exists, the name will be made unique by appending
`_n`. For example, calling `my_op` the second time will generate `MyOp_1/a`,
etc.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/ops.py#L6412-L6424">View source</a>

``` python
__init__(name)
```

Initialize the context manager.


#### Args:


* <b>`name`</b>: The prefix to use on all names created within the name scope.


#### Raises:


* <b>`ValueError`</b>: If name is None, or not a string.



## Properties

<h3 id="name"><code>name</code></h3>






## Methods

<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/ops.py#L6430-L6449">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/ops.py#L6451-L6454">View source</a>

``` python
__exit__(
    type_arg,
    value_arg,
    traceback_arg
)
```
