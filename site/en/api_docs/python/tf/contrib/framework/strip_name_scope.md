page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.strip_name_scope


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L6454-L6479">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Removes name scope from a name.

``` python
tf.contrib.framework.strip_name_scope(
    name,
    export_scope
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`name`</b>: A `string` name.
* <b>`export_scope`</b>: Optional `string`. Name scope to remove.


#### Returns:

Name with name scope removed, or the original name if export_scope
is None.
