page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.remove_checkpoint

``` python
tf.train.remove_checkpoint(
    checkpoint_prefix,
    checkpoint_format_version=tf.train.SaverDef.V2,
    meta_graph_suffix='meta'
)
```



Defined in [`tensorflow/python/training/saver.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/training/saver.py).

Removes a checkpoint given by `checkpoint_prefix`.

#### Args:

* <b>`checkpoint_prefix`</b>: The prefix of a V1 or V2 checkpoint. Typically the result
    of `Saver.save()` or that of `tf.train.latest_checkpoint()`, regardless of
    sharded/non-sharded or V1/V2.
* <b>`checkpoint_format_version`</b>: `SaverDef.CheckpointFormatVersion`, defaults to
    `SaverDef.V2`.
* <b>`meta_graph_suffix`</b>: Suffix for `MetaGraphDef` file. Defaults to 'meta'.