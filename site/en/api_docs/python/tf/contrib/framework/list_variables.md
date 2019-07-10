page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.list_variables

Returns list of all variables in the latest checkpoint.

``` python
tf.contrib.framework.list_variables(checkpoint_dir)
```



Defined in [`contrib/framework/python/framework/checkpoint_utils.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/framework/checkpoint_utils.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`checkpoint_dir`</b>: Directory with checkpoints file or path to checkpoint.


#### Returns:

List of tuples `(name, shape)`.
