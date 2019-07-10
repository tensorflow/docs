page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.model_pruning.apply_mask

Apply mask to a given weight tensor.

``` python
tf.contrib.model_pruning.apply_mask(
    x,
    scope=''
)
```



Defined in [`contrib/model_pruning/python/pruning.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/model_pruning/python/pruning.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: Input weight tensor
* <b>`scope`</b>: The current variable scope. Defaults to "".

#### Returns:

Tensor representing masked_weights
