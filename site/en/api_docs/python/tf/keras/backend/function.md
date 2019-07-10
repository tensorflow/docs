page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.function

``` python
tf.keras.backend.function(
    inputs,
    outputs,
    updates=None,
    name=None,
    **kwargs
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/keras/backend.py).

Instantiates a Keras function.

#### Arguments:

* <b>`inputs`</b>: List of placeholder tensors.
* <b>`outputs`</b>: List of output tensors.
* <b>`updates`</b>: List of update ops.
* <b>`name`</b>: String, name of function.
* <b>`**kwargs`</b>: Passed to <a href="../../../tf/InteractiveSession#run"><code>tf.Session.run</code></a>.


#### Returns:

Output values as Numpy arrays.


#### Raises:

* <b>`ValueError`</b>: if invalid kwargs are passed in or if in eager execution.