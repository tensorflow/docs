page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.glob


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/gfile/glob">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/lib/io/file_io.py#L366-L393">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a list of files that match the given pattern(s).

### Aliases:

* <a href="/api_docs/python/tf/io/gfile/glob"><code>tf.compat.v1.io.gfile.glob</code></a>
* <a href="/api_docs/python/tf/io/gfile/glob"><code>tf.compat.v2.io.gfile.glob</code></a>


``` python
tf.io.gfile.glob(pattern)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`pattern`</b>: string or iterable of strings. The glob pattern(s).


#### Returns:

A list of strings containing filenames that match the given pattern(s).



#### Raises:


* <b><a href="/api_docs/python/tf/errors/OpError"><code>errors.OpError</code></a></b>: If there are filesystem / directory listing errors.
