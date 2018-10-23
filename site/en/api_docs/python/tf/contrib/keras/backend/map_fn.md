

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.backend.map_fn

### `tf.contrib.keras.backend.map_fn`

``` python
map_fn(
    fn,
    elems,
    name=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/backend.py).

Map the function fn over the elements elems and return the outputs.

#### Arguments:

    fn: Callable that will be called upon each element in elems
    elems: tensor
    name: A string name for the map node in the graph


#### Returns:

    Tensor with first dimension equal to the elems and second depending on
    fn