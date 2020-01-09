page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.stat


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L730-L745">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns file statistics for a given path.

### Aliases:

* `tf.compat.v1.io.gfile.stat`
* `tf.compat.v2.io.gfile.stat`


``` python
tf.io.gfile.stat(path)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`path`</b>: string, path to a file


#### Returns:

FileStatistics struct that contains information about the path



#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.
