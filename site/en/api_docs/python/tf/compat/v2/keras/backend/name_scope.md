page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.keras.backend.name_scope

A context manager for use when defining a Python op.

``` python
tf.compat.v2.keras.backend.name_scope(name)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->

This context manager pushes a name scope, which will make the name of all
operations added within it have a prefix.

For example, to define a new Python op called `my_op`:

```python
def my_op(a):
  with tf.name_scope("MyOp") as scope:
    a = tf.convert_to_tensor(a, name="a")
    # Define some computation that uses `a`.
    return foo_op(..., name=scope)
```

When executed, the Tensor `a` will have the name `MyOp/a`.

#### Args:


* <b>`name`</b>: The prefix to use on all names created within the name scope.


#### Returns:

Name scope context manager.
