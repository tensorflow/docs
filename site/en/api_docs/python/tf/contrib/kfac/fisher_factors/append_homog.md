

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.fisher_factors.append_homog

``` python
tf.contrib.kfac.fisher_factors.append_homog(tensor)
```



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_factors.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/kfac/python/ops/fisher_factors.py).

Appends a homogeneous coordinate to the last dimension of a Tensor.

#### Args:

* <b>`tensor`</b>: A Tensor.


#### Returns:

A Tensor identical to the input but one larger in the last dimension.  The
new entries are filled with ones.