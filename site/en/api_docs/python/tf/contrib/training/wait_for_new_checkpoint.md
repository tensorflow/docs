page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.wait_for_new_checkpoint


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/training/python/training/evaluation.py#L171-L199">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Waits until a new checkpoint file is found.

``` python
tf.contrib.training.wait_for_new_checkpoint(
    checkpoint_dir,
    last_checkpoint=None,
    seconds_to_sleep=1,
    timeout=None
)
```



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
