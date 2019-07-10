page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.initializers.lecun_normal

### Aliases:

* `tf.initializers.lecun_normal`
* `tf.keras.initializers.lecun_normal`

``` python
tf.keras.initializers.lecun_normal(seed=None)
```



Defined in [`tensorflow/python/ops/init_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/init_ops.py).

LeCun normal initializer.

It draws samples from a truncated normal distribution centered on 0
with `stddev = sqrt(1 / fan_in)`
where `fan_in` is the number of input units in the weight tensor.

#### Arguments:

* <b>`seed`</b>: A Python integer. Used to seed the random generator.


#### Returns:

    An initializer.

References:
    - Self-Normalizing Neural Networks,
    [Klambauer et al., 2017](https://papers.nips.cc/paper/6698-self-normalizing-neural-networks)
    ([pdf](https://papers.nips.cc/paper/6698-self-normalizing-neural-networks.pdf))
    - Efficient Backprop,
    [Lecun et al., 1998](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)