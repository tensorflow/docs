page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.load_variable


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/checkpoint_utils.py#L69-L84">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the tensor value of the given variable in the checkpoint.

### Aliases:

* `tf.compat.v1.train.load_variable`
* `tf.compat.v2.train.load_variable`


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
