page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.assign_from_values_fn


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/ops/variables.py#L569-L591">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a function that assigns specific variables from the given values.

``` python
tf.contrib.framework.assign_from_values_fn(var_names_to_values)
```



<!-- Placeholder for "Used in" -->

This function provides a mechanism for performing assignment of variables
to values in a way that does not fill the graph with large assignment values.

#### Args:


* <b>`var_names_to_values`</b>: A map from variable names to values.


#### Returns:

A function that takes a single argument, a <a href="../../../tf/Session"><code>tf.compat.v1.Session</code></a>, that
applies the
assignment operation.



#### Raises:


* <b>`ValueError`</b>: if any of the given variable names were not found.
