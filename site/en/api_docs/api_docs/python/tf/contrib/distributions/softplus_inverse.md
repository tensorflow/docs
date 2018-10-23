

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.distributions.softplus_inverse

``` python
softplus_inverse(
    x,
    name=None
)
```



Defined in [`tensorflow/python/ops/distributions/util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/ops/distributions/util.py).

See the guide: [Statistical Distributions (contrib) > Utilities](../../../../../api_guides/python/contrib.distributions#Utilities)

Computes the inverse softplus, i.e., x = softplus_inverse(softplus(x)).

Mathematically this op is equivalent to:

```none
softplus_inverse = log(exp(x) - 1.)
```

#### Args:

* <b>`x`</b>: `Tensor`. Non-negative (not enforced), floating-point.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`Tensor`. Has the same type/shape as input `x`.