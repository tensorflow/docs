page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.list_variables

``` python
tf.contrib.framework.list_variables(checkpoint_dir)
```



Defined in [`tensorflow/contrib/framework/python/framework/checkpoint_utils.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/framework/python/framework/checkpoint_utils.py).

Returns list of all variables in the latest checkpoint.

#### Args:

* <b>`checkpoint_dir`</b>: Directory with checkpoints file or path to checkpoint.


#### Returns:

List of tuples `(name, shape)`.