page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.function

``` python
tf.keras.backend.function(
    inputs,
    outputs,
    updates=None,
    **kwargs
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/backend.py).

Instantiates a Keras function.

#### Arguments:

* <b>`inputs`</b>: List of placeholder tensors.
* <b>`outputs`</b>: List of output tensors.
* <b>`updates`</b>: List of update ops.
* <b>`**kwargs`</b>: Passed to <a href="../../../tf/Session#run"><code>tf.Session.run</code></a>.


#### Returns:

Output values as Numpy arrays.


#### Raises:

* <b>`ValueError`</b>: if invalid kwargs are passed in.