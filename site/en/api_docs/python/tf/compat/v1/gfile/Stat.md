page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.gfile.Stat


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L714-L727">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns file statistics for a given path.

``` python
tf.compat.v1.gfile.Stat(filename)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`filename`</b>: string, path to a file


#### Returns:

FileStatistics struct that contains information about the path



#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.
