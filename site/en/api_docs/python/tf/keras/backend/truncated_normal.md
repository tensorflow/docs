page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.truncated_normal

Returns a tensor with truncated random normal distribution of values.

### Aliases:

* `tf.compat.v1.keras.backend.truncated_normal`
* `tf.compat.v2.keras.backend.truncated_normal`
* `tf.keras.backend.truncated_normal`

``` python
tf.keras.backend.truncated_normal(
    shape,
    mean=0.0,
    stddev=1.0,
    dtype=None,
    seed=None
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->

The generated values follow a normal distribution
with specified mean and standard deviation,
except that values whose magnitude is more than
two standard deviations from the mean are dropped and re-picked.

#### Arguments:


* <b>`shape`</b>: A tuple of integers, the shape of tensor to create.
* <b>`mean`</b>: Mean of the values.
* <b>`stddev`</b>: Standard deviation of the values.
* <b>`dtype`</b>: String, dtype of returned tensor.
* <b>`seed`</b>: Integer, random seed.


#### Returns:

A tensor.
