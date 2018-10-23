

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.smart_constant_value

``` python
tf.contrib.framework.smart_constant_value(pred)
```



Defined in [`tensorflow/python/framework/smart_cond.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/framework/smart_cond.py).

Return the bool value for `pred`, or None if `pred` had a dynamic value.

#### Arguments:

* <b>`pred`</b>: A scalar, either a Python bool or tensor.


#### Returns:

True or False if `pred` has a constant boolean value, None otherwise.


#### Raises:

* <b>`TypeError`</b>: If `pred` is not a Tensor or bool.