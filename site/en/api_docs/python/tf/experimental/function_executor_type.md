page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.experimental.function_executor_type

Context manager for setting the executor of eager defined functions.

### Aliases:

* `tf.compat.v1.experimental.function_executor_type`
* `tf.compat.v2.experimental.function_executor_type`
* `tf.experimental.function_executor_type`

``` python
tf.experimental.function_executor_type(executor_type)
```



Defined in [`python/eager/context.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/eager/context.py).

<!-- Placeholder for "Used in" -->

Eager defined functions are functions decorated by tf.contrib.eager.defun.

#### Args:


* <b>`executor_type`</b>: a string for the name of the executor to be used to execute
  functions defined by tf.contrib.eager.defun.


#### Yields:

Context manager for setting the executor of eager defined functions.
