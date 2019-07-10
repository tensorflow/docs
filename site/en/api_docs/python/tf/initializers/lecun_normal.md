page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initializers.lecun_normal

LeCun normal initializer.

### Aliases:

* `tf.compat.v1.initializers.lecun_normal`
* `tf.compat.v1.keras.initializers.lecun_normal`
* `tf.initializers.lecun_normal`
* `tf.keras.initializers.lecun_normal`

``` python
tf.initializers.lecun_normal(seed=None)
```



Defined in [`python/ops/init_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/init_ops.py).

<!-- Placeholder for "Used in" -->

It draws samples from a truncated normal distribution centered on 0
with standard deviation (after truncation) given by
`stddev = sqrt(1 / fan_in)` where `fan_in` is the number of
input units in the weight tensor.

#### Arguments:


* <b>`seed`</b>: A Python integer. Used to seed the random generator.


#### Returns:

An initializer.



#### References:

- Self-Normalizing Neural Networks,
[Klambauer et al.,
2017](https://papers.nips.cc/paper/6698-self-normalizing-neural-networks)
# pylint: disable=line-too-long
([pdf](https://papers.nips.cc/paper/6698-self-normalizing-neural-networks.pdf))
- Efficient Backprop,
[Lecun et al., 1998](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)
