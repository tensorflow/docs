

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.foldr

### `tf.contrib.keras.backend.foldr`

``` python
foldr(
    fn,
    elems,
    initializer=None,
    name=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/backend.py).

Reduce elems using fn to combine them from right to left.

#### Arguments:

    fn: Callable that will be called upon each element in elems and an
        accumulator, for instance `lambda acc, x: acc + x`
    elems: tensor
    initializer: The first value used (`elems[-1]` in case of None)
    name: A string name for the foldr node in the graph


#### Returns:

    Same type and shape as initializer