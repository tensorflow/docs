page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.smart_constant_value

Return the bool value for `pred`, or None if `pred` had a dynamic value.

``` python
tf.contrib.framework.smart_constant_value(pred)
```



Defined in [`python/framework/smart_cond.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/smart_cond.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`pred`</b>: A scalar, either a Python bool or tensor.


#### Returns:

True or False if `pred` has a constant boolean value, None otherwise.



#### Raises:


* <b>`TypeError`</b>: If `pred` is not a Tensor or bool.