page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.report_uninitialized_variables


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/variables.py#L3331-L3376">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adds ops to list the names of uninitialized variables.

``` python
tf.compat.v1.report_uninitialized_variables(
    var_list=None,
    name='report_uninitialized_variables'
)
```



<!-- Placeholder for "Used in" -->

When run, it returns a 1-D tensor containing the names of uninitialized
variables if there are any, or an empty array if there are none.

#### Args:


* <b>`var_list`</b>: List of `Variable` objects to check. Defaults to the value of
  `global_variables() + local_variables()`
* <b>`name`</b>: Optional name of the `Operation`.


#### Returns:

A 1-D tensor containing names of the uninitialized variables, or an empty
1-D tensor if there are no variables or no uninitialized variables.



**NOTE** The output of this function should be used.  If it is not, a warning will be logged.  To mark the output as used, call its .mark_used() method.
