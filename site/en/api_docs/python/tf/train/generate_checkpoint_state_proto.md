

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.generate_checkpoint_state_proto

### `tf.train.generate_checkpoint_state_proto`

``` python
generate_checkpoint_state_proto(
    save_dir,
    model_checkpoint_path,
    all_model_checkpoint_paths=None
)
```



Defined in [`tensorflow/python/training/saver.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/training/saver.py).

Generates a checkpoint state proto.

#### Args:

* <b>`save_dir`</b>: Directory where the model was saved.
* <b>`model_checkpoint_path`</b>: The checkpoint file.
* <b>`all_model_checkpoint_paths`</b>: List of strings.  Paths to all not-yet-deleted
    checkpoints, sorted from oldest to newest.  If this is a non-empty list,
    the last element must be equal to model_checkpoint_path.  These paths
    are also saved in the CheckpointState proto.


#### Returns:

  CheckpointState proto with model_checkpoint_path and
  all_model_checkpoint_paths updated to either absolute paths or
  relative paths to the current save_dir.