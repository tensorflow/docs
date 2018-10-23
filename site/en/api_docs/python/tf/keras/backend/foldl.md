

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.foldl

``` python
tf.keras.backend.foldl(
    fn,
    elems,
    initializer=None,
    name=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/keras/_impl/keras/backend.py).

Reduce elems using fn to combine them from left to right.

#### Arguments:

* <b>`fn`</b>: Callable that will be called upon each element in elems and an
        accumulator, for instance `lambda acc, x: acc + x`
* <b>`elems`</b>: tensor
* <b>`initializer`</b>: The first value used (`elems[0]` in case of None)
* <b>`name`</b>: A string name for the foldl node in the graph


#### Returns:

Tensor with same type and shape as `initializer`.