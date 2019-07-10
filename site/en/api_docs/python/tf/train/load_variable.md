page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.load_variable

Returns the tensor value of the given variable in the checkpoint.

### Aliases:

* `tf.compat.v1.train.load_variable`
* `tf.compat.v2.train.load_variable`
* `tf.train.load_variable`

``` python
tf.train.load_variable(
    ckpt_dir_or_file,
    name
)
```



Defined in [`python/training/checkpoint_utils.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/checkpoint_utils.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`ckpt_dir_or_file`</b>: Directory with checkpoints file or path to checkpoint.
* <b>`name`</b>: Name of the variable to return.


#### Returns:

A numpy `ndarray` with a copy of the value of this variable.
