page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.Stat


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/lib/io/file_io.py#L714-L727">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns file statistics for a given path.

### Aliases:

* <a href="/api_docs/python/tf/gfile/Stat"><code>tf.compat.v1.gfile.Stat</code></a>


``` python
tf.gfile.Stat(filename)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`filename`</b>: string, path to a file


#### Returns:

FileStatistics struct that contains information about the path



#### Raises:


* <b><a href="/api_docs/python/tf/errors/OpError"><code>errors.OpError</code></a></b>: If the operation fails.
