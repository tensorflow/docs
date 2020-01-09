page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.load_checkpoint


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/train/load_checkpoint">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/checkpoint_utils.py#L44-L66">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns `CheckpointReader` for checkpoint found in `ckpt_dir_or_file`.

### Aliases:

* <a href="/api_docs/python/tf/train/load_checkpoint"><code>tf.compat.v1.train.load_checkpoint</code></a>
* <a href="/api_docs/python/tf/train/load_checkpoint"><code>tf.compat.v2.train.load_checkpoint</code></a>


``` python
tf.train.load_checkpoint(ckpt_dir_or_file)
```



<!-- Placeholder for "Used in" -->

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
