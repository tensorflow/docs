page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.keras.backend.name_scope


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L735-L760">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A context manager for use when defining a Python op.

``` python
tf.compat.v2.keras.backend.name_scope(name)
```



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
