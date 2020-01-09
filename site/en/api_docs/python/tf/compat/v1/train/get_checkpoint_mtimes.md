page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.train.get_checkpoint_mtimes


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/checkpoint_management.py#L396-L439">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the mtimes (modification timestamps) of the checkpoints. (deprecated)

``` python
tf.compat.v1.train.get_checkpoint_mtimes(checkpoint_prefixes)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use standard file utilities to get mtimes.

Globs for the checkpoints pointed to by `checkpoint_prefixes`.  If the files
exist, collect their mtime.  Both V2 and V1 checkpoints are considered, in
that priority.

This is the recommended way to get the mtimes, since it takes into account
the naming difference between V1 and V2 formats.

Note: If not all checkpoints exist, the length of the returned mtimes list
will be smaller than the length of `checkpoint_prefixes` list, so mapping
checkpoints to corresponding mtimes will not be possible.

#### Args:


* <b>`checkpoint_prefixes`</b>: a list of checkpoint paths, typically the results of
  `Saver.save()` or those of <a href="../../../../tf/train/latest_checkpoint"><code>tf.train.latest_checkpoint()</code></a>, regardless of
  sharded/non-sharded or V1/V2.

#### Returns:

A list of mtimes (in microseconds) of the found checkpoints.
