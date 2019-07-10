page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.wait_for_new_checkpoint

Waits until a new checkpoint file is found.

``` python
tf.contrib.training.wait_for_new_checkpoint(
    checkpoint_dir,
    last_checkpoint=None,
    seconds_to_sleep=1,
    timeout=None
)
```



Defined in [`contrib/training/python/training/evaluation.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/training/python/training/evaluation.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`checkpoint_dir`</b>: The directory in which checkpoints are saved.
* <b>`last_checkpoint`</b>: The last checkpoint path used or `None` if we're expecting
  a checkpoint for the first time.
* <b>`seconds_to_sleep`</b>: The number of seconds to sleep for before looking for a
  new checkpoint.
* <b>`timeout`</b>: The maximum number of seconds to wait. If left as `None`, then the
  process will wait indefinitely.


#### Returns:

a new checkpoint path, or None if the timeout was reached.
