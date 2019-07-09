page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.is_tensor

``` python
tf.contrib.framework.is_tensor(x)
```



Defined in [`tensorflow/python/framework/tensor_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/framework/tensor_util.py).

See the guide: [Framework (contrib)](../../../../../api_guides/python/contrib.framework)

Check whether `x` is of tensor type.

Check whether an object is a tensor. This check is equivalent to calling
`isinstance(x, (tf.Tensor, tf.SparseTensor, tf.Variable))` and also checks
if all the component variables of a MirroredVariable or a TowerLocalVariable
are tensors.

#### Args:

* <b>`x`</b>: A python object to check.


#### Returns:

`True` if `x` is a tensor, `False` if not.