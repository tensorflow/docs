

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_unique_variable

``` python
tf.contrib.framework.get_unique_variable(var_op_name)
```



Defined in [`tensorflow/contrib/framework/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/framework/python/ops/variables.py).

See the guide: [Framework (contrib) > Variables](../../../../../api_guides/python/contrib.framework#Variables)

Gets the variable uniquely identified by that var_op_name.

#### Args:

* <b>`var_op_name`</b>: the full name of the variable op, including the scope.


#### Returns:

a tensorflow variable.


#### Raises:

* <b>`ValueError`</b>: if no variable uniquely identified by the name exists.