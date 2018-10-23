

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.report_uninitialized_variables

### `tf.report_uninitialized_variables`

``` python
report_uninitialized_variables(
    var_list=None,
    name='report_uninitialized_variables'
)
```



Defined in [`tensorflow/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/variables.py).

See the guide: [Variables > Variable helper functions](../../../api_guides/python/state_ops#Variable_helper_functions)

Adds ops to list the names of uninitialized variables.

When run, it returns a 1-D tensor containing the names of uninitialized
variables if there are any, or an empty array if there are none.

#### Args:

* <b>`var_list`</b>: List of `Variable` objects to check. Defaults to the
    value of `global_variables() + local_variables()`
* <b>`name`</b>: Optional name of the `Operation`.


#### Returns:

  A 1-D tensor containing names of the uninitialized variables, or an empty
  1-D tensor if there are no variables or no uninitialized variables.