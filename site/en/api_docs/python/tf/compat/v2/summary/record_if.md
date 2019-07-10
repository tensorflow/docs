page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.summary.record_if

Sets summary recording on or off per the provided boolean value.

``` python
tf.compat.v2.summary.record_if(condition)
```



Defined in [`python/ops/summary_ops_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/summary_ops_v2.py).

<!-- Placeholder for "Used in" -->

The provided value can be a python boolean, a scalar boolean Tensor, or
or a callable providing such a value; if a callable is passed it will be
invoked on-demand to determine whether summary writing will occur.

#### Args:


* <b>`condition`</b>: can be True, False, a bool Tensor, or a callable providing such.


#### Yields:

Returns a context manager that sets this value on enter and restores the
previous value on exit.
