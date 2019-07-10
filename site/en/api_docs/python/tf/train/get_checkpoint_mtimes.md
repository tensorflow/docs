page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.get_checkpoint_mtimes

Returns the mtimes (modification timestamps) of the checkpoints. (deprecated)

### Aliases:

* `tf.compat.v1.train.get_checkpoint_mtimes`
* `tf.train.get_checkpoint_mtimes`

``` python
tf.train.get_checkpoint_mtimes(checkpoint_prefixes)
```



Defined in [`python/training/checkpoint_management.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/checkpoint_management.py).

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
  <a href="../../tf/train/Saver#save"><code>Saver.save()</code></a> or those of <a href="../../tf/train/latest_checkpoint"><code>tf.train.latest_checkpoint()</code></a>, regardless of
  sharded/non-sharded or V1/V2.

#### Returns:

A list of mtimes (in microseconds) of the found checkpoints.
