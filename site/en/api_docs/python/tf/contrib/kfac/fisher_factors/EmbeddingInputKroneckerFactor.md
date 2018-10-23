

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.fisher_factors.EmbeddingInputKroneckerFactor

## Class `EmbeddingInputKroneckerFactor`

Inherits From: [`DiagonalFactor`](../../../../tf/contrib/kfac/fisher_factors/DiagonalFactor)



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_factors.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/kfac/python/ops/fisher_factors.py).

FisherFactor for input to an embedding layer.

Given input_ids = [batch_size, input_size] representing indices into an
[vocab_size, embedding_size] embedding matrix, approximate input covariance by
a diagonal matrix,

  Cov(input_ids, input_ids) =
      (1/batch_size) sum_{i} diag(n_hot(input[i]) ** 2).

where n_hot() constructs an n-hot binary vector and diag() constructs a
diagonal matrix of size [vocab_size, vocab_size].

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    input_ids,
    vocab_size,
    dtype=None
)
```

Instantiate EmbeddingInputKroneckerFactor.

#### Args:

* <b>`input_ids`</b>: Tuple of Tensors of shape [batch_size, input_size] and dtype
    int32.  Indices into embedding matrix.
* <b>`vocab_size`</b>: int or 0-D Tensor. Maximum value for entries in 'input_ids'.
* <b>`dtype`</b>: dtype for covariance statistics. Must be a floating point type.
    Defaults to float32.

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





