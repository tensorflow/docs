page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.assign_from_values_fn

Returns a function that assigns specific variables from the given values.

``` python
tf.contrib.framework.assign_from_values_fn(var_names_to_values)
```



Defined in [`contrib/framework/python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/ops/variables.py).

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