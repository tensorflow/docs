

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.utils.tensors_to_column

``` python
tf.contrib.kfac.utils.tensors_to_column(tensors)
```



Defined in [`tensorflow/contrib/kfac/python/ops/utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/kfac/python/ops/utils.py).

Converts a tensor or list of tensors to a column vector.

#### Args:

* <b>`tensors`</b>: A tensor or list of tensors.


#### Returns:

The tensors reshaped into vectors and stacked on top of each other.