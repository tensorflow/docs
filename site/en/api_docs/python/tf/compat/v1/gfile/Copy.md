page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.gfile.Copy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L456-L469">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Copies data from `oldpath` to `newpath`.

``` python
tf.compat.v1.gfile.Copy(
    oldpath,
    newpath,
    overwrite=False
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`oldpath`</b>: string, name of the file who's contents need to be copied
* <b>`newpath`</b>: string, name of the file to which to copy to
* <b>`overwrite`</b>: boolean, if false it's an error for `newpath` to be occupied by
  an existing file.


#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.
