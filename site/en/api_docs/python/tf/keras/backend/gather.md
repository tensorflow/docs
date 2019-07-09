page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.gather

``` python
tf.keras.backend.gather(
    reference,
    indices
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/backend.py).

Retrieves the elements of indices `indices` in the tensor `reference`.

#### Arguments:

* <b>`reference`</b>: A tensor.
* <b>`indices`</b>: An integer tensor of indices.


#### Returns:

A tensor of same type as `reference`.