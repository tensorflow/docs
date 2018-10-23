

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.dropout

``` python
dropout(
    x,
    level,
    noise_shape=None,
    seed=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/backend.py).

Sets entries in `x` to zero at random, while scaling the entire tensor.

#### Arguments:

* <b>`x`</b>: tensor
* <b>`level`</b>: fraction of the entries in the tensor
        that will be set to 0.
* <b>`noise_shape`</b>: shape for randomly generated keep/drop flags,
        must be broadcastable to the shape of `x`
* <b>`seed`</b>: random seed to ensure determinism.


#### Returns:

A tensor.