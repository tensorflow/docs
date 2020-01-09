page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.Exists


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/lib/io/file_io.py#L248-L262">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Determines whether a path exists or not.

### Aliases:

* <a href="/api_docs/python/tf/gfile/Exists"><code>tf.compat.v1.gfile.Exists</code></a>


``` python
tf.gfile.Exists(filename)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`filename`</b>: string, a path


#### Returns:

True if the path exists, whether it's a file or a directory.
False if the path does not exist and there are no filesystem errors.



#### Raises:


* <b><a href="/api_docs/python/tf/errors/OpError"><code>errors.OpError</code></a></b>: Propagates any errors reported by the FileSystem API.
