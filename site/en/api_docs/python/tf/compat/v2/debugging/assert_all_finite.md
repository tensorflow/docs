page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.debugging.assert_all_finite

Assert that the tensor does not contain any NaN's or Inf's.

``` python
tf.compat.v2.debugging.assert_all_finite(
    x,
    message,
    name=None
)
```



Defined in [`python/ops/numerics.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/numerics.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: Tensor to check.
* <b>`message`</b>: Message to log on failure.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

Same tensor as `x`.
