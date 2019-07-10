page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.report_uninitialized_variables

Adds ops to list the names of uninitialized variables.

### Aliases:

* `tf.compat.v1.report_uninitialized_variables`
* `tf.report_uninitialized_variables`

``` python
tf.report_uninitialized_variables(
    var_list=None,
    name='report_uninitialized_variables'
)
```



Defined in [`python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/variables.py).

<!-- Placeholder for "Used in" -->

When run, it returns a 1-D tensor containing the names of uninitialized
variables if there are any, or an empty array if there are none.

#### Args:


* <b>`var_list`</b>: List of `Variable` objects to check. Defaults to the
  value of `global_variables() + local_variables()`
* <b>`name`</b>: Optional name of the `Operation`.


#### Returns:

A 1-D tensor containing names of the uninitialized variables, or an empty
1-D tensor if there are no variables or no uninitialized variables.



**NOTE** The output of this function should be used.  If it is not, a warning will be logged.  To mark the output as used, call its .mark_used() method.