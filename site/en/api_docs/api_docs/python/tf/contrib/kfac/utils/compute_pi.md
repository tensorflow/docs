

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.utils.compute_pi

``` python
compute_pi(
    left_factor,
    right_factor
)
```



Defined in [`tensorflow/contrib/kfac/python/ops/utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/kfac/python/ops/utils.py).

Computes the scalar constant pi for Tikhonov regularization/damping.

pi = sqrt( (trace(A) / dim(A)) / (trace(B) / dim(B)) )
See section 6.3 of https://arxiv.org/pdf/1503.05671.pdf for details.

#### Args:

* <b>`left_factor`</b>: The left Kronecker factor Tensor.
* <b>`right_factor`</b>: The right Kronecker factor Tensor.


#### Returns:

The computed scalar constant pi for these Kronecker Factors (as a Tensor).