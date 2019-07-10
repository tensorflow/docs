page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.flatten

``` python
tf.contrib.layers.flatten(
    inputs,
    outputs_collections=None,
    scope=None
)
```



Defined in [`tensorflow/contrib/layers/python/layers/layers.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/layers/python/layers/layers.py).

Flattens the input while maintaining the batch_size.

  Assumes that the first dimension represents the batch.

#### Args:

* <b>`inputs`</b>: A tensor of size [batch_size, ...].
* <b>`outputs_collections`</b>: Collection to add the outputs.
* <b>`scope`</b>: Optional scope for name_scope.


#### Returns:

A flattened tensor with shape [batch_size, k].

#### Raises:

* <b>`ValueError`</b>: If inputs rank is unknown or less than 2.