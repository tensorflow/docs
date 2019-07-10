page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.generate_checkpoint_state_proto

``` python
tf.train.generate_checkpoint_state_proto(
    save_dir,
    model_checkpoint_path,
    all_model_checkpoint_paths=None,
    all_model_checkpoint_timestamps=None,
    last_preserved_timestamp=None
)
```



Defined in [`tensorflow/python/training/checkpoint_management.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/training/checkpoint_management.py).

Generates a checkpoint state proto.

#### Args:

* <b>`save_dir`</b>: Directory where the model was saved.
* <b>`model_checkpoint_path`</b>: The checkpoint file.
* <b>`all_model_checkpoint_paths`</b>: List of strings.  Paths to all not-yet-deleted
    checkpoints, sorted from oldest to newest.  If this is a non-empty list,
    the last element must be equal to model_checkpoint_path.  These paths
    are also saved in the CheckpointState proto.
* <b>`all_model_checkpoint_timestamps`</b>: A list of floats, indicating the number of
    seconds since the Epoch when each checkpoint was generated.
* <b>`last_preserved_timestamp`</b>: A float, indicating the number of seconds since
    the Epoch when the last preserved checkpoint was written, e.g. due to a
    `keep_checkpoint_every_n_hours` parameter (see
    <a href="../../tf/train/CheckpointManager"><code>tf.contrib.checkpoint.CheckpointManager</code></a> for an implementation).

#### Returns:

CheckpointState proto with model_checkpoint_path and
all_model_checkpoint_paths updated to either absolute paths or
relative paths to the current save_dir.


#### Raises:

* <b>`ValueError`</b>: If `all_model_checkpoint_timestamps` was provided but its length
    does not match `all_model_checkpoint_paths`.