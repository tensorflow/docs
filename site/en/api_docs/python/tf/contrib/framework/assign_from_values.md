page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.assign_from_values


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/ops/variables.py#L514-L566">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates an assignment operation from a given mapping.

``` python
tf.contrib.framework.assign_from_values(var_names_to_values)
```



<!-- Placeholder for "Used in" -->

This function provides a mechanism for performing assignment of variables
to values in a way that does not fill the graph with large assignment values.

#### Args:


* <b>`var_names_to_values`</b>: A map from variable names to values.


#### Returns:


* <b>`assign_op`</b>: An `Operation` that assigns each of the given variables to the
  requested values.
* <b>`feed_dict`</b>: The feed dictionary to use when evaluating `assign_op`.


#### Raises:


* <b>`ValueError`</b>: if any of the given variable names were not found.
