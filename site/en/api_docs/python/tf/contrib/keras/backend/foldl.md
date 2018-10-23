

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.backend.foldl

### `tf.contrib.keras.backend.foldl`

``` python
foldl(
    fn,
    elems,
    initializer=None,
    name=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/backend.py).

Reduce elems using fn to combine them from left to right.

#### Arguments:

    fn: Callable that will be called upon each element in elems and an
        accumulator, for instance `lambda acc, x: acc + x`
    elems: tensor
    initializer: The first value used (`elems[0]` in case of None)
    name: A string name for the foldl node in the graph


#### Returns:

    Same type and shape as initializer