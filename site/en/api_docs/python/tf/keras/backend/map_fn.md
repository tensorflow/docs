

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.map_fn

``` python
tf.keras.backend.map_fn(
    fn,
    elems,
    name=None,
    dtype=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/keras/_impl/keras/backend.py).

Map the function fn over the elements elems and return the outputs.

#### Arguments:

* <b>`fn`</b>: Callable that will be called upon each element in elems
* <b>`elems`</b>: tensor
* <b>`name`</b>: A string name for the map node in the graph
* <b>`dtype`</b>: Output data type.


#### Returns:

Tensor with dtype `dtype`.