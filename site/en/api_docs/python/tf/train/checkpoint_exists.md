page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.checkpoint_exists

Checks whether a V1 or V2 checkpoint exists with the specified prefix. (deprecated)

### Aliases:

* `tf.compat.v1.train.checkpoint_exists`
* `tf.train.checkpoint_exists`

``` python
tf.train.checkpoint_exists(checkpoint_prefix)
```



Defined in [`python/training/checkpoint_management.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/checkpoint_management.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use standard file APIs to check for files with this prefix.

This is the recommended way to check if a checkpoint exists, since it takes
into account the naming difference between V1 and V2 formats.

#### Args:


* <b>`checkpoint_prefix`</b>: the prefix of a V1 or V2 checkpoint, with V2 taking
  priority.  Typically the result of <a href="../../tf/train/Saver#save"><code>Saver.save()</code></a> or that of
  <a href="../../tf/train/latest_checkpoint"><code>tf.train.latest_checkpoint()</code></a>, regardless of sharded/non-sharded or
  V1/V2.

#### Returns:

A bool, true iff a checkpoint referred to by `checkpoint_prefix` exists.
