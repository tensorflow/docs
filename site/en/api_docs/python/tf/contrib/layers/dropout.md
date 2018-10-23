

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.layers.dropout

### `tf.contrib.layers.dropout`

``` python
dropout(
    *args,
    **kwargs
)
```



Defined in [`tensorflow/contrib/framework/python/ops/arg_scope.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/framework/python/ops/arg_scope.py).

Returns a dropout op applied to the input.

With probability `keep_prob`, outputs the input element scaled up by
`1 / keep_prob`, otherwise outputs `0`.  The scaling is so that the expected
sum is unchanged.

#### Args:

* <b>`inputs`</b>: The tensor to pass to the nn.dropout op.
* <b>`keep_prob`</b>: A scalar `Tensor` with the same type as x. The probability
    that each element is kept.
* <b>`noise_shape`</b>: A 1-D `Tensor` of type `int32`, representing the
    shape for randomly generated keep/drop flags.
* <b>`is_training`</b>: A bool `Tensor` indicating whether or not the model
    is in training mode. If so, dropout is applied and values scaled.
    Otherwise, inputs is returned.
* <b>`outputs_collections`</b>: Collection to add the outputs.
* <b>`scope`</b>: Optional scope for name_scope.


#### Returns:

  A tensor representing the output of the operation.