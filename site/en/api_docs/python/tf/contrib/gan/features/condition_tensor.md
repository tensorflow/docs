

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.gan.features.condition_tensor

``` python
condition_tensor(
    tensor,
    conditioning
)
```



Defined in [`tensorflow/contrib/gan/python/features/python/conditioning_utils_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/gan/python/features/python/conditioning_utils_impl.py).

Condition the value of a tensor.

Conditioning scheme based on https://arxiv.org/abs/1609.03499.

#### Args:

* <b>`tensor`</b>: A minibatch tensor to be conditioned.
* <b>`conditioning`</b>: A minibatch Tensor of to condition on. Must be 2D, with first
    dimension the same as `tensor`.


#### Returns:

`tensor` conditioned on `conditioning`.


#### Raises:

* <b>`ValueError`</b>: If the non-batch dimensions of `tensor` aren't fully defined.
* <b>`ValueError`</b>: If `conditioning` isn't at least 2D.
* <b>`ValueError`</b>: If the batch dimension for the input Tensors don't match.