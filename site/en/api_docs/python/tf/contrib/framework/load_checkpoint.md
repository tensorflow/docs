page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.load_checkpoint

Returns CheckpointReader for latest checkpoint.

``` python
tf.contrib.framework.load_checkpoint(filepattern)
```



Defined in [`contrib/framework/python/framework/checkpoint_utils.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/framework/checkpoint_utils.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`filepattern`</b>: Directory with checkpoints file or path to checkpoint.


#### Returns:

`CheckpointReader` object.



#### Raises:


* <b>`ValueError`</b>: if checkpoint_dir doesn't have 'checkpoint' file or checkpoints.