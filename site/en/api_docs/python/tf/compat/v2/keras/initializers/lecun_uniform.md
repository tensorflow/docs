page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.keras.initializers.lecun_uniform

LeCun uniform initializer.

### Aliases:

* `tf.compat.v2.initializers.lecun_uniform`
* `tf.compat.v2.keras.initializers.lecun_uniform`

``` python
tf.compat.v2.keras.initializers.lecun_uniform(seed=None)
```



Defined in [`python/ops/init_ops_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/init_ops_v2.py).

<!-- Placeholder for "Used in" -->

It draws samples from a uniform distribution within [-limit, limit]
where `limit` is `sqrt(3 / fan_in)`
where `fan_in` is the number of input units in the weight tensor.

#### Arguments:


* <b>`seed`</b>: A Python integer. Used to seed the random generator.


#### Returns:

An initializer.



#### References:

- Self-Normalizing Neural Networks,
[Klambauer et al., 2017](https://papers.nips.cc/paper/6698-self-normalizing-neural-networks) # pylint: disable=line-too-long
([pdf](https://papers.nips.cc/paper/6698-self-normalizing-neural-networks.pdf))
- Efficient Backprop,
[Lecun et al., 1998](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)
