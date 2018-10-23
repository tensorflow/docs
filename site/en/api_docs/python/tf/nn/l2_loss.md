

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.nn.l2_loss

### `tf.nn.l2_loss`

``` python
l2_loss(
    t,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_nn_ops.py`.

See the guide: [Neural Network > Losses](../../../../api_guides/python/nn#Losses)

L2 Loss.

Computes half the L2 norm of a tensor without the `sqrt`:

    output = sum(t ** 2) / 2

#### Args:

* <b>`t`</b>: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
    Typically 2-D, but may have any dimensions.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor`. Has the same type as `t`. 0-D.