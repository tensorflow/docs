

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.update_checkpoint_state

``` python
update_checkpoint_state(
    save_dir,
    model_checkpoint_path,
    all_model_checkpoint_paths=None,
    latest_filename=None
)
```



Defined in [`tensorflow/python/training/saver.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/training/saver.py).

See the guide: [Variables > Saving and Restoring Variables](../../../../api_guides/python/state_ops#Saving_and_Restoring_Variables)

Updates the content of the 'checkpoint' file.

This updates the checkpoint file containing a CheckpointState
proto.

#### Args:

* <b>`save_dir`</b>: Directory where the model was saved.
* <b>`model_checkpoint_path`</b>: The checkpoint file.
* <b>`all_model_checkpoint_paths`</b>: List of strings.  Paths to all not-yet-deleted
    checkpoints, sorted from oldest to newest.  If this is a non-empty list,
    the last element must be equal to model_checkpoint_path.  These paths
    are also saved in the CheckpointState proto.
* <b>`latest_filename`</b>: Optional name of the checkpoint file.  Default to
    'checkpoint'.


#### Raises:

* <b>`RuntimeError`</b>: If any of the model checkpoint paths conflict with the file
    containing CheckpointSate.