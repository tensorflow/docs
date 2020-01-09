page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.remove


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/gfile/remove">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/lib/io/file_io.py#L300-L311">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Deletes the path located at 'path'.

### Aliases:

* <a href="/api_docs/python/tf/io/gfile/remove"><code>tf.compat.v1.io.gfile.remove</code></a>
* <a href="/api_docs/python/tf/io/gfile/remove"><code>tf.compat.v2.io.gfile.remove</code></a>


``` python
tf.io.gfile.remove(path)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`path`</b>: string, a path


#### Raises:


* <b><a href="/api_docs/python/tf/errors/OpError"><code>errors.OpError</code></a></b>: Propagates any errors reported by the FileSystem API.  E.g.,
NotFoundError if the path does not exist.
