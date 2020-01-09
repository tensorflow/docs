page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.get_checkpoint_state


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/train/get_checkpoint_state">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/checkpoint_management.py#L244-L298">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns CheckpointState proto from the "checkpoint" file.

### Aliases:

* <a href="/api_docs/python/tf/train/get_checkpoint_state"><code>tf.compat.v1.train.get_checkpoint_state</code></a>
* <a href="/api_docs/python/tf/train/get_checkpoint_state"><code>tf.compat.v2.train.get_checkpoint_state</code></a>


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
