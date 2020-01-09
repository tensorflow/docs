page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.MkDir


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/lib/io/file_io.py#L396-L408">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a directory with the name 'dirname'.

### Aliases:

* <a href="/api_docs/python/tf/gfile/MkDir"><code>tf.compat.v1.gfile.MkDir</code></a>


``` python
tf.gfile.MkDir(dirname)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`dirname`</b>: string, name of the directory to be created
Notes: The parent directories need to exist. Use recursive_create_dir instead
  if there is the possibility that the parent dirs don't exist.

#### Raises:


* <b><a href="/api_docs/python/tf/errors/OpError"><code>errors.OpError</code></a></b>: If the operation fails.
