page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.load_variable

``` python
tf.contrib.framework.load_variable(
    checkpoint_dir,
    name
)
```



Defined in [`tensorflow/contrib/framework/python/framework/checkpoint_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/framework/python/framework/checkpoint_utils.py).

See the guide: [Framework (contrib) > Checkpoint utilities](../../../../../api_guides/python/contrib.framework#Checkpoint_utilities)

Returns a Tensor with the contents of the given variable in the checkpoint.

#### Args:

* <b>`checkpoint_dir`</b>: Directory with checkpoints file or path to checkpoint.
* <b>`name`</b>: Name of the tensor to return.


#### Returns:

`Tensor` object.