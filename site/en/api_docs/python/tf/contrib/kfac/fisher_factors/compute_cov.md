

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.fisher_factors.compute_cov

``` python
tf.contrib.kfac.fisher_factors.compute_cov(
    tensor,
    tensor_right=None,
    normalizer=None
)
```



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_factors.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/kfac/python/ops/fisher_factors.py).

Compute the empirical second moment of the rows of a 2D Tensor.

This function is meant to be applied to random matrices for which the true row
mean is zero, so that the true second moment equals the true covariance.

#### Args:

* <b>`tensor`</b>: A 2D Tensor.
* <b>`tensor_right`</b>: An optional 2D Tensor. If provided, this function computes
    the matrix product tensor^T * tensor_right instead of tensor^T * tensor.
* <b>`normalizer`</b>: optional scalar for the estimator (by default, the normalizer is
      the number of rows of tensor).


#### Returns:

A square 2D Tensor with as many rows/cols as the number of input columns.