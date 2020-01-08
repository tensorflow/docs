page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.arg_scoped_arguments

``` python
tf.contrib.framework.arg_scoped_arguments(func)
```



Defined in [`tensorflow/contrib/framework/python/ops/arg_scope.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/framework/python/ops/arg_scope.py).

Returns the list kwargs that arg_scope can set for a func.

#### Args:

* <b>`func`</b>: function which has been decorated with @add_arg_scope.


#### Returns:

a list of kwargs names.