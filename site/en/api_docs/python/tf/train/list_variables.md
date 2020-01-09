page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.list_variables


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/checkpoint_utils.py#L87-L103">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns list of all variables in the checkpoint.

### Aliases:

* `tf.compat.v1.train.list_variables`
* `tf.compat.v2.train.list_variables`


``` python
tf.train.list_variables(ckpt_dir_or_file)
```



### Used in the guide:

* [Training checkpoints](https://www.tensorflow.org/guide/checkpoint)




#### Args:


* <b>`ckpt_dir_or_file`</b>: Directory with checkpoints file or path to checkpoint.


#### Returns:

List of tuples `(name, shape)`.
