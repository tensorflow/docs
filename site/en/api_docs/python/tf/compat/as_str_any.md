page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.as_str_any


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/compat/as_str_any">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/util/compat.py#L109-L125">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts input to `str` type.

### Aliases:

* <a href="/api_docs/python/tf/compat/as_str_any"><code>tf.compat.v1.compat.as_str_any</code></a>
* <a href="/api_docs/python/tf/compat/as_str_any"><code>tf.compat.v2.compat.as_str_any</code></a>


``` python
tf.compat.as_str_any(value)
```



<!-- Placeholder for "Used in" -->

   Uses `str(value)`, except for `bytes` typed inputs, which are converted
   using `as_str`.

#### Args:


* <b>`value`</b>: A object that can be converted to `str`.


#### Returns:

A `str` object.
