page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.gfile.Rename


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L489-L502">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Rename or move a file / directory.

``` python
tf.compat.v1.gfile.Rename(
    oldname,
    newname,
    overwrite=False
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`oldname`</b>: string, pathname for a file
* <b>`newname`</b>: string, pathname to which the file needs to be moved
* <b>`overwrite`</b>: boolean, if false it's an error for `newname` to be occupied by
  an existing file.


#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.
