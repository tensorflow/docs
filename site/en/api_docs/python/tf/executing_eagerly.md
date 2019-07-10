page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.executing_eagerly

Returns True if the current thread has eager execution enabled.

### Aliases:

* `tf.compat.v1.executing_eagerly`
* `tf.compat.v2.executing_eagerly`
* `tf.contrib.eager.executing_eagerly`
* `tf.contrib.eager.in_eager_mode`
* `tf.executing_eagerly`

``` python
tf.executing_eagerly()
```



Defined in [`python/eager/context.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/eager/context.py).

<!-- Placeholder for "Used in" -->

Eager execution is typically enabled via
<a href="../tf/enable_eager_execution"><code>tf.compat.v1.enable_eager_execution</code></a>, but may also be enabled within the
context of a Python function via tf.contrib.eager.py_func.