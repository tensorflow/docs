page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.errstate


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Context manager setting error state.

``` python
tf.contrib.eager.errstate(
    *args,
    **kwds
)
```



<!-- Placeholder for "Used in" -->


#### Example:


```
c = tf.math.log(0.)  # -inf

with errstate(inf_or_nan=ExecutionCallback.RAISE):
  tf.math.log(0.)  # <-- Raises InfOrNanError.
```

#### Args:


* <b>`inf_or_nan`</b>: An `ExecutionCallback` determining the action for infinity
  (`inf`) and NaN (`nan`) values. A value of `None` leads to no change in
  the action of the condition.


#### Yields:

None.



#### Raises:


* <b>`ValueError`</b>: If the value of any keyword arguments is invalid.
