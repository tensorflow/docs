

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.truncated_normal

``` python
truncated_normal(
    shape,
    mean=0.0,
    stddev=1.0,
    dtype=None,
    seed=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Returns a tensor with truncated random normal distribution of values.

The generated values follow a normal distribution
with specified mean and standard deviation,
except that values whose magnitude is more than
two standard deviations from the mean are dropped and re-picked.

#### Arguments:

    shape: A tuple of integers, the shape of tensor to create.
    mean: Mean of the values.
    stddev: Standard deviation of the values.
    dtype: String, dtype of returned tensor.
    seed: Integer, random seed.


#### Returns:

    A tensor.