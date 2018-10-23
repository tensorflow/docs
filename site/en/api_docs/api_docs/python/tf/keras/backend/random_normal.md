

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.random_normal

``` python
random_normal(
    shape,
    mean=0.0,
    stddev=1.0,
    dtype=None,
    seed=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/backend.py).

Returns a tensor with normal distribution of values.

#### Arguments:

* <b>`shape`</b>: A tuple of integers, the shape of tensor to create.
* <b>`mean`</b>: A float, mean of the normal distribution to draw samples.
* <b>`stddev`</b>: A float, standard deviation of the normal distribution
        to draw samples.
* <b>`dtype`</b>: String, dtype of returned tensor.
* <b>`seed`</b>: Integer, random seed.


#### Returns:

A tensor.