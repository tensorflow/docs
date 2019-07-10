page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initializers.he_normal

He normal initializer.

### Aliases:

* `tf.compat.v1.initializers.he_normal`
* `tf.compat.v1.keras.initializers.he_normal`
* `tf.initializers.he_normal`
* `tf.keras.initializers.he_normal`

``` python
tf.initializers.he_normal(seed=None)
```



Defined in [`python/ops/init_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/init_ops.py).

<!-- Placeholder for "Used in" -->

It draws samples from a truncated normal distribution centered on 0
with standard deviation (after truncation) given by
`stddev = sqrt(2 / fan_in)` where `fan_in` is the number of
input units in the weight tensor.

#### Arguments:


* <b>`seed`</b>: A Python integer. Used to seed the random generator.


#### Returns:

An initializer.



#### References:

[He et al., 2015](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/He_Delving_Deep_into_ICCV_2015_paper.html)
# pylint: disable=line-too-long
([pdf](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/He_Delving_Deep_into_ICCV_2015_paper.pdf))
