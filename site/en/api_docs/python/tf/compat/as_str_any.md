page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.as_str_any


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/util/compat.py#L109-L125">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts input to `str` type.

### Aliases:

* `tf.compat.v1.compat.as_str_any`
* `tf.compat.v2.compat.as_str_any`


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
