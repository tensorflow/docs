page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.prepend_name_scope


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L6482-L6506">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Prepends name scope to a name.

``` python
tf.contrib.framework.prepend_name_scope(
    name,
    import_scope
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`name`</b>: A `string` name.
* <b>`import_scope`</b>: Optional `string`. Name scope to add.


#### Returns:

Name with name scope added, or the original name if import_scope
is None.
