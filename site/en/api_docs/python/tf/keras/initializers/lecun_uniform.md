page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.initializers.lecun_uniform

### Aliases:

* `tf.initializers.lecun_uniform`
* `tf.keras.initializers.lecun_uniform`

``` python
tf.keras.initializers.lecun_uniform(seed=None)
```



Defined in [`tensorflow/python/ops/init_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/ops/init_ops.py).

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