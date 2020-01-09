page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.makedirs


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L441-L453">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a directory and all parent/intermediate directories.

### Aliases:

* `tf.compat.v1.io.gfile.makedirs`
* `tf.compat.v2.io.gfile.makedirs`


``` python
tf.io.gfile.makedirs(path)
```



<!-- Placeholder for "Used in" -->

It succeeds if path already exists and is writable.

#### Args:


* <b>`path`</b>: string, name of the directory to be created


#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.
