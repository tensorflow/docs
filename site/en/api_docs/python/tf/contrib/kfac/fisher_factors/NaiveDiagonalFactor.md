

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.fisher_factors.NaiveDiagonalFactor

## Class `NaiveDiagonalFactor`

Inherits From: [`DiagonalFactor`](../../../../tf/contrib/kfac/fisher_factors/DiagonalFactor)



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_factors.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/kfac/python/ops/fisher_factors.py).

FisherFactor for a diagonal approximation of any type of param's Fisher.

Note that this uses the naive "square the sum estimator", and so is applicable
to any type of parameter in principle, but has very high variance.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    params_grads,
    batch_size
)
```

Initializes NaiveDiagonalFactor instance.

#### Args:

* <b>`params_grads`</b>: Sequence of Tensors, each with same shape as parameters this
    FisherFactor corresponds to. For example, the gradient of the loss with
    respect to parameters.
* <b>`batch_size`</b>: int or 0-D Tensor. Size

<h3 id="get_cov"><code>get_cov</code></h3>

``` python
get_cov()
```



<h3 id="get_cov_var"><code>get_cov_var</code></h3>

``` python
get_cov_var()
```

Get variable backing this FisherFactor.

May or may not be the same as self.get_cov()

#### Returns:

Variable of shape self._cov_shape.

<h3 id="instantiate_covariance"><code>instantiate_covariance</code></h3>

``` python
instantiate_covariance()
```

Instantiates the covariance Variable as the instance member _cov.

<h3 id="left_multiply"><code>left_multiply</code></h3>

``` python
left_multiply(
    x,
    damping
)
```



<h3 id="left_multiply_inverse"><code>left_multiply_inverse</code></h3>

``` python
left_multiply_inverse(
    x,
    damping
)
```



<h3 id="make_covariance_update_op"><code>make_covariance_update_op</code></h3>

``` python
make_covariance_update_op(ema_decay)
```

Constructs and returns the covariance update Op.

#### Args:

* <b>`ema_decay`</b>: The exponential moving average decay (float or Tensor).

#### Returns:

An Op for updating the covariance Variable referenced by _cov.

<h3 id="make_inverse_update_ops"><code>make_inverse_update_ops</code></h3>

``` python
make_inverse_update_ops()
```



<h3 id="register_damped_inverse"><code>register_damped_inverse</code></h3>

``` python
register_damped_inverse(damping)
```



<h3 id="right_multiply"><code>right_multiply</code></h3>

``` python
right_multiply(
    x,
    damping
)
```



<h3 id="right_multiply_inverse"><code>right_multiply_inverse</code></h3>

``` python
right_multiply_inverse(
    x,
    damping
)
```





