page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_variables_by_suffix


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/ops/variables.py#L464-L474">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Gets the list of variables that end with the given suffix.

``` python
tf.contrib.framework.get_variables_by_suffix(
    suffix,
    scope=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`suffix`</b>: suffix for filtering the variables to return.
* <b>`scope`</b>: an optional scope for filtering the variables to return.


#### Returns:

a copied list of variables with the given name and prefix.
