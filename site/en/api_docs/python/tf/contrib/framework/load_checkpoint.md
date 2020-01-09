page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.load_checkpoint


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/framework/checkpoint_utils.py#L48-L64">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns CheckpointReader for latest checkpoint.

``` python
tf.contrib.framework.load_checkpoint(filepattern)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`filepattern`</b>: Directory with checkpoints file or path to checkpoint.


#### Returns:

`CheckpointReader` object.



#### Raises:


* <b>`ValueError`</b>: if checkpoint_dir doesn't have 'checkpoint' file or checkpoints.
