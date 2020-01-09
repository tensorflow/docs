page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.latest_checkpoint


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/train/latest_checkpoint">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/checkpoint_management.py#L320-L347">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Finds the filename of latest saved checkpoint file.

### Aliases:

* <a href="/api_docs/python/tf/train/latest_checkpoint"><code>tf.compat.v1.train.latest_checkpoint</code></a>
* <a href="/api_docs/python/tf/train/latest_checkpoint"><code>tf.compat.v2.train.latest_checkpoint</code></a>


``` python
tf.train.latest_checkpoint(
    checkpoint_dir,
    latest_filename=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`checkpoint_dir`</b>: Directory where the variables were saved.
* <b>`latest_filename`</b>: Optional name for the protocol buffer file that
  contains the list of most recent checkpoint filenames.
  See the corresponding argument to <a href="../../tf/train/Saver#save"><code>Saver.save()</code></a>.


#### Returns:

The full path to the latest checkpoint or `None` if no checkpoint was found.
