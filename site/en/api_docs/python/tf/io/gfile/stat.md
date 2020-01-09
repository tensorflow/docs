page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.stat


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/gfile/stat">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/lib/io/file_io.py#L730-L745">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns file statistics for a given path.

### Aliases:

* <a href="/api_docs/python/tf/io/gfile/stat"><code>tf.compat.v1.io.gfile.stat</code></a>
* <a href="/api_docs/python/tf/io/gfile/stat"><code>tf.compat.v2.io.gfile.stat</code></a>


``` python
tf.io.gfile.stat(path)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`path`</b>: string, path to a file


#### Returns:

FileStatistics struct that contains information about the path



#### Raises:


* <b><a href="/api_docs/python/tf/errors/OpError"><code>errors.OpError</code></a></b>: If the operation fails.
