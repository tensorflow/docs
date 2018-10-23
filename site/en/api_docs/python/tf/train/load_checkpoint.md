

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.load_checkpoint

``` python
tf.train.load_checkpoint(ckpt_dir_or_file)
```



Defined in [`tensorflow/python/training/checkpoint_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/training/checkpoint_utils.py).

Returns `CheckpointReader` for checkpoint found in `ckpt_dir_or_file`.

If `ckpt_dir_or_file` resolves to a directory with multiple checkpoints,
reader for the latest checkpoint is returned.

#### Args:

* <b>`ckpt_dir_or_file`</b>: Directory with checkpoints file or path to checkpoint
    file.


#### Returns:

`CheckpointReader` object.


#### Raises:

* <b>`ValueError`</b>: If `ckpt_dir_or_file` resolves to a directory with no
    checkpoints.