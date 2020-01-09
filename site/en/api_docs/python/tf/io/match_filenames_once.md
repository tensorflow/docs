page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.match_filenames_once


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/match_filenames_once">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/input.py#L58-L78">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Save the list of files matching pattern, so it is only computed once.

### Aliases:

* <a href="/api_docs/python/tf/io/match_filenames_once"><code>tf.compat.v1.io.match_filenames_once</code></a>
* <a href="/api_docs/python/tf/io/match_filenames_once"><code>tf.compat.v1.train.match_filenames_once</code></a>
* <a href="/api_docs/python/tf/io/match_filenames_once"><code>tf.compat.v2.io.match_filenames_once</code></a>
* <a href="/api_docs/python/tf/io/match_filenames_once"><code>tf.train.match_filenames_once</code></a>


``` python
tf.io.match_filenames_once(
    pattern,
    name=None
)
```



<!-- Placeholder for "Used in" -->

NOTE: The order of the files returned is deterministic.

#### Args:


* <b>`pattern`</b>: A file pattern (glob), or 1D tensor of file patterns.
* <b>`name`</b>: A name for the operations (optional).


#### Returns:

A variable that is initialized to the list of files matching the pattern(s).
