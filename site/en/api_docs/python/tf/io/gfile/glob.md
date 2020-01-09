page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.glob


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L366-L393">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a list of files that match the given pattern(s).

### Aliases:

* `tf.compat.v1.io.gfile.glob`
* `tf.compat.v2.io.gfile.glob`


``` python
tf.io.gfile.glob(pattern)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`pattern`</b>: string or iterable of strings. The glob pattern(s).


#### Returns:

A list of strings containing filenames that match the given pattern(s).



#### Raises:


* <b>`errors.OpError`</b>: If there are filesystem / directory listing errors.
