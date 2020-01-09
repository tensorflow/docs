page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.load_variable


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/train/load_variable">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/checkpoint_utils.py#L69-L84">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the tensor value of the given variable in the checkpoint.

### Aliases:

* <a href="/api_docs/python/tf/train/load_variable"><code>tf.compat.v1.train.load_variable</code></a>
* <a href="/api_docs/python/tf/train/load_variable"><code>tf.compat.v2.train.load_variable</code></a>


``` python
tf.train.load_variable(
    ckpt_dir_or_file,
    name
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`ckpt_dir_or_file`</b>: Directory with checkpoints file or path to checkpoint.
* <b>`name`</b>: Name of the variable to return.


#### Returns:

A numpy `ndarray` with a copy of the value of this variable.
