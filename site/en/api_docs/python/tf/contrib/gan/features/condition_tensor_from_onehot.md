page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.features.condition_tensor_from_onehot

Condition a tensor based on a one-hot tensor.

``` python
tf.contrib.gan.features.condition_tensor_from_onehot(
    tensor,
    one_hot_labels,
    embedding_size=256
)
```



Defined in [`contrib/gan/python/features/python/conditioning_utils_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/features/python/conditioning_utils_impl.py).

<!-- Placeholder for "Used in" -->

Conditioning scheme based on https://arxiv.org/abs/1609.03499.

#### Args:


* <b>`tensor`</b>: Tensor to be conditioned.
* <b>`one_hot_labels`</b>: A Tensor of one-hot labels. Shape is
  [batch_size, num_classes].
* <b>`embedding_size`</b>: The size of the class embedding.


#### Returns:

`tensor` conditioned on `one_hot_labels`.



#### Raises:


* <b>`ValueError`</b>: `one_hot_labels` isn't 2D, if non-batch dimensions aren't
  fully defined, or if batch sizes don't match.