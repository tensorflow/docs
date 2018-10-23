

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.framework.load_checkpoint

``` python
load_checkpoint(filepattern)
```



Defined in [`tensorflow/contrib/framework/python/framework/checkpoint_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/framework/python/framework/checkpoint_utils.py).

See the guide: [Framework (contrib) > Checkpoint utilities](../../../../../api_guides/python/contrib.framework#Checkpoint_utilities)

Returns CheckpointReader for latest checkpoint.

#### Args:

* <b>`filepattern`</b>: Directory with checkpoints file or path to checkpoint.


#### Returns:

`CheckpointReader` object.


#### Raises:

* <b>`ValueError`</b>: if checkpoint_dir doesn't have 'checkpoint' file or checkpoints.