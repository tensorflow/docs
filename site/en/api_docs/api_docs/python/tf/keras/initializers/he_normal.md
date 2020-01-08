

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.initializers.he_normal

``` python
tf.keras.initializers.he_normal(seed=None)
```



Defined in [`tensorflow/python/keras/initializers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/initializers.py).

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