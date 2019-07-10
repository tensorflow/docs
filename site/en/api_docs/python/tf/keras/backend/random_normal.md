page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.random_normal

Returns a tensor with normal distribution of values.

### Aliases:

* `tf.compat.v1.keras.backend.random_normal`
* `tf.compat.v2.keras.backend.random_normal`
* `tf.keras.backend.random_normal`

``` python
tf.keras.backend.random_normal(
    shape,
    mean=0.0,
    stddev=1.0,
    dtype=None,
    seed=None
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`shape`</b>: A tuple of integers, the shape of tensor to create.
* <b>`mean`</b>: A float, mean of the normal distribution to draw samples.
* <b>`stddev`</b>: A float, standard deviation of the normal distribution
    to draw samples.
* <b>`dtype`</b>: String, dtype of returned tensor.
* <b>`seed`</b>: Integer, random seed.


#### Returns:

A tensor.
