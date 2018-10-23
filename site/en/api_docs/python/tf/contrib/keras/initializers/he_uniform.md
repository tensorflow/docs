

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.initializers.he_uniform

### `tf.contrib.keras.initializers.he_uniform`

``` python
he_uniform(seed=None)
```



Defined in [`tensorflow/contrib/keras/python/keras/initializers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/initializers.py).

He uniform variance scaling initializer.

It draws samples from a uniform distribution within [-limit, limit]
where `limit` is `sqrt(6 / fan_in)`
where `fan_in` is the number of input units in the weight tensor.

#### Arguments:

    seed: A Python integer. Used to seed the random generator.


#### Returns:

    An initializer.

References:
    He et al., http://arxiv.org/abs/1502.01852