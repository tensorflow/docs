

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.initializers.glorot_normal

``` python
glorot_normal(seed=None)
```



Defined in [`tensorflow/python/keras/_impl/keras/initializers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/initializers.py).

Glorot normal initializer, also called Xavier normal initializer.

It draws samples from a truncated normal distribution centered on 0
with `stddev = sqrt(2 / (fan_in + fan_out))`
where `fan_in` is the number of input units in the weight tensor
and `fan_out` is the number of output units in the weight tensor.

#### Arguments:

* <b>`seed`</b>: A Python integer. Used to seed the random generator.


#### Returns:

    An initializer.

References:
    Glorot & Bengio, AISTATS 2010
    http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf