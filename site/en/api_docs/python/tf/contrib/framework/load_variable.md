page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.load_variable

``` python
tf.contrib.framework.load_variable(
    checkpoint_dir,
    name
)
```



Defined in [`tensorflow/contrib/framework/python/framework/checkpoint_utils.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/framework/python/framework/checkpoint_utils.py).

Returns a Tensor with the contents of the given variable in the checkpoint.

#### Args:

* <b>`checkpoint_dir`</b>: Directory with checkpoints file or path to checkpoint.
* <b>`name`</b>: Name of the tensor to return.


#### Returns:

`Tensor` object.