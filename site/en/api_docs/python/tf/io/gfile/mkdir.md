page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.mkdir


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L411-L423">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a directory with the name given by 'path'.

### Aliases:

* `tf.compat.v1.io.gfile.mkdir`
* `tf.compat.v2.io.gfile.mkdir`


``` python
tf.io.gfile.mkdir(path)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`path`</b>: string, name of the directory to be created
Notes: The parent directories need to exist. Use recursive_create_dir instead
  if there is the possibility that the parent dirs don't exist.

#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.
