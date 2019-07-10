page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.foldl

Reduce elems using fn to combine them from left to right.

### Aliases:

* `tf.compat.v1.keras.backend.foldl`
* `tf.compat.v2.keras.backend.foldl`
* `tf.keras.backend.foldl`

``` python
tf.keras.backend.foldl(
    fn,
    elems,
    initializer=None,
    name=None
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`fn`</b>: Callable that will be called upon each element in elems and an
    accumulator, for instance `lambda acc, x: acc + x`
* <b>`elems`</b>: tensor
* <b>`initializer`</b>: The first value used (`elems[0]` in case of None)
* <b>`name`</b>: A string name for the foldl node in the graph


#### Returns:

Tensor with same type and shape as `initializer`.
