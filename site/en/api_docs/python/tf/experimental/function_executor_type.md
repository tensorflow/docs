page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.experimental.function_executor_type

``` python
tf.experimental.function_executor_type(executor_type)
```



Defined in [`tensorflow/python/eager/context.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/eager/context.py).

Context manager for setting the executor of eagar defined functions.

Eager defined functions are functions decorated by tf.contrib.eager.defun.

#### Args:

* <b>`executor_type`</b>: a string for the name of the executor to be used
  to execute functions defined by tf.contrib.eager.defun.


#### Returns:

Context manager for setting the executor of eager defined functions.