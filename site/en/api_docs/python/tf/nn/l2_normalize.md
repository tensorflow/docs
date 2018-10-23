

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.nn.l2_normalize

### `tf.nn.l2_normalize`

``` python
l2_normalize(
    x,
    dim,
    epsilon=1e-12,
    name=None
)
```



Defined in [`tensorflow/python/ops/nn_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/nn_impl.py).

See the guide: [Neural Network > Normalization](../../../../api_guides/python/nn#Normalization)

Normalizes along dimension `dim` using an L2 norm.

For a 1-D tensor with `dim = 0`, computes

    output = x / sqrt(max(sum(x**2), epsilon))

For `x` with more dimensions, independently normalizes each 1-D slice along
dimension `dim`.

#### Args:

* <b>`x`</b>: A `Tensor`.
* <b>`dim`</b>: Dimension along which to normalize.  A scalar or a vector of
    integers.
* <b>`epsilon`</b>: A lower bound value for the norm. Will use `sqrt(epsilon)` as the
    divisor if `norm < sqrt(epsilon)`.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

  A `Tensor` with the same shape as `x`.