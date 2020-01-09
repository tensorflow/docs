page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.gfile.ListDirectory


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L599-L615">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a list of entries contained within a directory.

``` python
tf.compat.v1.gfile.ListDirectory(dirname)
```



<!-- Placeholder for "Used in" -->

The list is in arbitrary order. It does not contain the special entries "."
and "..".

#### Args:


* <b>`dirname`</b>: string, path to a directory


#### Returns:

[filename1, filename2, ... filenameN] as strings



#### Raises:

errors.NotFoundError if directory doesn't exist
