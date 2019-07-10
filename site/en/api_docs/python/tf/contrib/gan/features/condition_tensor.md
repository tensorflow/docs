page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.features.condition_tensor

Condition the value of a tensor.

``` python
tf.contrib.gan.features.condition_tensor(
    tensor,
    conditioning
)
```



Defined in [`contrib/gan/python/features/python/conditioning_utils_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/features/python/conditioning_utils_impl.py).

<!-- Placeholder for "Used in" -->

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