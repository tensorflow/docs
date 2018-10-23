

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.initializers.lecun_uniform

``` python
tf.keras.initializers.lecun_uniform(seed=None)
```



Defined in [`tensorflow/python/keras/initializers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/initializers.py).

LeCun uniform initializer.

It draws samples from a uniform distribution within [-limit, limit]
where `limit` is `sqrt(3 / fan_in)`
where `fan_in` is the number of input units in the weight tensor.

#### Arguments:

* <b>`seed`</b>: A Python integer. Used to seed the random generator.


#### Returns:

    An initializer.

References:
    LeCun 98, Efficient Backprop,
    http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf