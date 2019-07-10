page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.initializers.lecun_normal

``` python
tf.keras.initializers.lecun_normal(seed=None)
```



Defined in [`tensorflow/python/keras/initializers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/initializers.py).

LeCun normal initializer.

It draws samples from a truncated normal distribution centered on 0
with `stddev = sqrt(1 / fan_in)`
where `fan_in` is the number of input units in the weight tensor.

#### Arguments:

* <b>`seed`</b>: A Python integer. Used to seed the random generator.


#### Returns:

    An initializer.

References:
    - [Self-Normalizing Neural Networks](https://arxiv.org/abs/1706.02515)
    - [Efficient
    Backprop](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)