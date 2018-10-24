

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.initializers.he_normal

``` python
tf.keras.initializers.he_normal(seed=None)
```



Defined in [`tensorflow/python/keras/initializers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/initializers.py).

He normal initializer.

It draws samples from a truncated normal distribution centered on 0
with `stddev = sqrt(2 / fan_in)`
where `fan_in` is the number of input units in the weight tensor.

#### Arguments:

* <b>`seed`</b>: A Python integer. Used to seed the random generator.


#### Returns:

    An initializer.

References:
    He et al., http://arxiv.org/abs/1502.01852