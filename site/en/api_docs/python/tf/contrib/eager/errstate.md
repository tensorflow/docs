page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.errstate

``` python
tf.contrib.eager.errstate(
    *args,
    **kwds
)
```

Context manager setting error state.

Example:

```
c = tf.log(0.)  # -inf

with errstate(inf_or_nan=ExecutionCallback.RAISE):
  tf.log(0.)  # <-- Raises InfOrNanError.
```

#### Args:

* <b>`inf_or_nan`</b>: An `ExecutionCallback` determining the action for infinity
    (`inf`) and NaN (`nan`) values. A value of `None` leads to no change in
    the action of the condition.


#### Yields:

None.


#### Raises:

* <b>`ValueError`</b>: If the value of any keyword arguments is invalid.