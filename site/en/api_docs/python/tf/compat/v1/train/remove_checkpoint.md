page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.train.remove_checkpoint


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/checkpoint_management.py#L442-L467">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Removes a checkpoint given by `checkpoint_prefix`. (deprecated)

``` python
tf.compat.v1.train.remove_checkpoint(
    checkpoint_prefix,
    checkpoint_format_version=tf.train.SaverDef.V2,
    meta_graph_suffix='meta'
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use standard file APIs to delete files with this prefix.

#### Args:


* <b>`checkpoint_prefix`</b>: The prefix of a V1 or V2 checkpoint. Typically the result
  of `Saver.save()` or that of <a href="../../../../tf/train/latest_checkpoint"><code>tf.train.latest_checkpoint()</code></a>, regardless of
  sharded/non-sharded or V1/V2.
* <b>`checkpoint_format_version`</b>: `SaverDef.CheckpointFormatVersion`, defaults to
  `SaverDef.V2`.
* <b>`meta_graph_suffix`</b>: Suffix for `MetaGraphDef` file. Defaults to 'meta'.
