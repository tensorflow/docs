

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.executing_eagerly

### Aliases:

* `tf.contrib.eager.executing_eagerly`
* `tf.contrib.eager.in_eager_mode`
* `tf.executing_eagerly`

``` python
tf.executing_eagerly()
```



Defined in [`tensorflow/python/eager/context.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/eager/context.py).

Returns True if the current thread has eager execution enabled.

Eager execution is typically enabled via <a href="../tf/enable_eager_execution"><code>tf.enable_eager_execution</code></a>,
but may also be enabled within the context of a Python function via
tf.contrib.eager.py_func.