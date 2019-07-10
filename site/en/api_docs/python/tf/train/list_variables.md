page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.list_variables

Returns list of all variables in the checkpoint.

### Aliases:

* `tf.compat.v1.train.list_variables`
* `tf.compat.v2.train.list_variables`
* `tf.train.list_variables`

``` python
tf.train.list_variables(ckpt_dir_or_file)
```



Defined in [`python/training/checkpoint_utils.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/checkpoint_utils.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`ckpt_dir_or_file`</b>: Directory with checkpoints file or path to checkpoint.


#### Returns:

List of tuples `(name, shape)`.
