page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.map_fn

Map the function fn over the elements elems and return the outputs.

### Aliases:

* `tf.compat.v1.keras.backend.map_fn`
* `tf.compat.v2.keras.backend.map_fn`
* `tf.keras.backend.map_fn`

``` python
tf.keras.backend.map_fn(
    fn,
    elems,
    name=None,
    dtype=None
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`fn`</b>: Callable that will be called upon each element in elems
* <b>`elems`</b>: tensor
* <b>`name`</b>: A string name for the map node in the graph
* <b>`dtype`</b>: Output data type.


#### Returns:

Tensor with dtype `dtype`.
