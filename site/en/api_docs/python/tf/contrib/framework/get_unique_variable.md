page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_unique_variable


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/ops/variables.py#L491-L511">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Gets the variable uniquely identified by that var_op_name.

``` python
tf.contrib.framework.get_unique_variable(var_op_name)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`var_op_name`</b>: the full name of the variable op, including the scope.


#### Returns:

a tensorflow variable.



#### Raises:


* <b>`ValueError`</b>: if no variable uniquely identified by the name exists.
