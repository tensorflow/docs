page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.arg_scoped_arguments


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/ops/arg_scope.py#L201-L211">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the list kwargs that arg_scope can set for a func.

``` python
tf.contrib.framework.arg_scoped_arguments(func)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`func`</b>: function which has been decorated with @add_arg_scope.


#### Returns:

a list of kwargs names.
