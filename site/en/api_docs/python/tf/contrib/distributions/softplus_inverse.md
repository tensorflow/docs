page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distributions.softplus_inverse

Computes the inverse softplus, i.e., x = softplus_inverse(softplus(x)).

``` python
tf.contrib.distributions.softplus_inverse(
    x,
    name=None
)
```



Defined in [`python/ops/distributions/util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/distributions/util.py).

<!-- Placeholder for "Used in" -->

Mathematically this op is equivalent to:

```none
softplus_inverse = log(exp(x) - 1.)
```

#### Args:


* <b>`x`</b>: `Tensor`. Non-negative (not enforced), floating-point.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`Tensor`. Has the same type/shape as input `x`.
