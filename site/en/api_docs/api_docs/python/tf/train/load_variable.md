

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.load_variable

``` python
load_variable(
    ckpt_dir_or_file,
    name
)
```



Defined in [`tensorflow/python/training/checkpoint_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/training/checkpoint_utils.py).

Returns the tensor value of the given variable in the checkpoint.

#### Args:

* <b>`ckpt_dir_or_file`</b>: Directory with checkpoints file or path to checkpoint.
* <b>`name`</b>: Name of the variable to return.


#### Returns:

  A numpy `ndarray` with a copy of the value of this variable.