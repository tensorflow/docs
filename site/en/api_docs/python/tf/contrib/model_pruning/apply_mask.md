page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.model_pruning.apply_mask

``` python
tf.contrib.model_pruning.apply_mask(
    x,
    scope=''
)
```



Defined in [`tensorflow/contrib/model_pruning/python/pruning.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/model_pruning/python/pruning.py).

Apply mask to a given weight tensor.

#### Args:

* <b>`x`</b>: Input weight tensor
* <b>`scope`</b>: The current variable scope. Defaults to "".

#### Returns:

Tensor representing masked_weights