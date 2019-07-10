page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_unique_variable

Gets the variable uniquely identified by that var_op_name.

``` python
tf.contrib.framework.get_unique_variable(var_op_name)
```



Defined in [`contrib/framework/python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/ops/variables.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`var_op_name`</b>: the full name of the variable op, including the scope.


#### Returns:

a tensorflow variable.



#### Raises:


* <b>`ValueError`</b>: if no variable uniquely identified by the name exists.