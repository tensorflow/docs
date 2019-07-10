page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.latest_checkpoint

``` python
tf.train.latest_checkpoint(
    checkpoint_dir,
    latest_filename=None
)
```



Defined in [`tensorflow/python/training/checkpoint_management.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/training/checkpoint_management.py).

Finds the filename of latest saved checkpoint file.

#### Args:

* <b>`checkpoint_dir`</b>: Directory where the variables were saved.
* <b>`latest_filename`</b>: Optional name for the protocol buffer file that
    contains the list of most recent checkpoint filenames.
    See the corresponding argument to `Saver.save()`.


#### Returns:

The full path to the latest checkpoint or `None` if no checkpoint was found.