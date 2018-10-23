

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.framework.list_variables

``` python
tf.contrib.framework.list_variables(checkpoint_dir)
```



Defined in [`tensorflow/contrib/framework/python/framework/checkpoint_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/framework/python/framework/checkpoint_utils.py).

See the guide: [Framework (contrib) > Checkpoint utilities](../../../../../api_guides/python/contrib.framework#Checkpoint_utilities)

Returns list of all variables in the latest checkpoint.

#### Args:

* <b>`checkpoint_dir`</b>: Directory with checkpoints file or path to checkpoint.


#### Returns:

List of tuples `(name, shape)`.