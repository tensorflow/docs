page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.latest_checkpoint

Finds the filename of latest saved checkpoint file.

### Aliases:

* `tf.compat.v1.train.latest_checkpoint`
* `tf.compat.v2.train.latest_checkpoint`
* `tf.train.latest_checkpoint`

``` python
tf.train.latest_checkpoint(
    checkpoint_dir,
    latest_filename=None
)
```



Defined in [`python/training/checkpoint_management.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/checkpoint_management.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`checkpoint_dir`</b>: Directory where the variables were saved.
* <b>`latest_filename`</b>: Optional name for the protocol buffer file that
  contains the list of most recent checkpoint filenames.
  See the corresponding argument to <a href="../../tf/train/Saver#save"><code>Saver.save()</code></a>.


#### Returns:

The full path to the latest checkpoint or `None` if no checkpoint was found.
