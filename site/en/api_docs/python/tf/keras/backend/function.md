page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.function

Instantiates a Keras function.

### Aliases:

* `tf.compat.v1.keras.backend.function`
* `tf.compat.v2.keras.backend.function`
* `tf.keras.backend.function`

``` python
tf.keras.backend.function(
    inputs,
    outputs,
    updates=None,
    name=None,
    **kwargs
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`inputs`</b>: List of placeholder tensors.
* <b>`outputs`</b>: List of output tensors.
* <b>`updates`</b>: List of update ops.
* <b>`name`</b>: String, name of function.
* <b>`**kwargs`</b>: Passed to <a href="../../../tf/Session#run"><code>tf.Session.run</code></a>.


#### Returns:

Output values as Numpy arrays.



#### Raises:


* <b>`ValueError`</b>: if invalid kwargs are passed in or if in eager execution.