

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.arg_scoped_arguments

``` python
tf.contrib.framework.arg_scoped_arguments(func)
```



Defined in [`tensorflow/contrib/framework/python/ops/arg_scope.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/framework/python/ops/arg_scope.py).

See the guide: [Framework (contrib) > Arg_Scope](../../../../../api_guides/python/contrib.framework#Arg_Scope)

Returns the list kwargs that arg_scope can set for a func.

#### Args:

* <b>`func`</b>: function which has been decorated with @add_arg_scope.


#### Returns:

a list of kwargs names.