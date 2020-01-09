page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.get_checkpoint_state


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/checkpoint_management.py#L244-L298">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns CheckpointState proto from the "checkpoint" file.

### Aliases:

* `tf.compat.v1.train.get_checkpoint_state`
* `tf.compat.v2.train.get_checkpoint_state`


``` python
tf.train.get_checkpoint_state(
    checkpoint_dir,
    latest_filename=None
)
```



<!-- Placeholder for "Used in" -->

If the "checkpoint" file contains a valid CheckpointState
proto, returns it.

#### Args:


* <b>`checkpoint_dir`</b>: The directory of checkpoints.
* <b>`latest_filename`</b>: Optional name of the checkpoint file.  Default to
  'checkpoint'.


#### Returns:

A CheckpointState if the state was available, None
otherwise.



#### Raises:


* <b>`ValueError`</b>: if the checkpoint read doesn't have model_checkpoint_path set.
