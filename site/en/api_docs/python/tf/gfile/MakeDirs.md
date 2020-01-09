page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.MakeDirs


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/lib/io/file_io.py#L426-L438">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a directory and all parent/intermediate directories.

### Aliases:

* <a href="/api_docs/python/tf/gfile/MakeDirs"><code>tf.compat.v1.gfile.MakeDirs</code></a>


``` python
tf.gfile.MakeDirs(dirname)
```



<!-- Placeholder for "Used in" -->

It succeeds if dirname already exists and is writable.

#### Args:


* <b>`dirname`</b>: string, name of the directory to be created


#### Raises:


* <b><a href="/api_docs/python/tf/errors/OpError"><code>errors.OpError</code></a></b>: If the operation fails.
