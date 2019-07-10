page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.load_variable

Returns a Tensor with the contents of the given variable in the checkpoint.

``` python
tf.contrib.framework.load_variable(
    checkpoint_dir,
    name
)
```



Defined in [`contrib/framework/python/framework/checkpoint_utils.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/framework/checkpoint_utils.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`checkpoint_dir`</b>: Directory with checkpoints file or path to checkpoint.
* <b>`name`</b>: Name of the tensor to return.


#### Returns:

`Tensor` object.
