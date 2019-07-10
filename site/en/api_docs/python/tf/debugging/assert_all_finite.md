page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_all_finite

Assert that the tensor does not contain any NaN's or Inf's.

### Aliases:

* `tf.compat.v1.debugging.assert_all_finite`
* `tf.compat.v1.verify_tensor_all_finite`
* `tf.debugging.assert_all_finite`
* `tf.verify_tensor_all_finite`

``` python
tf.debugging.assert_all_finite(
    t=None,
    msg=None,
    name=None,
    x=None,
    message=None
)
```



Defined in [`python/ops/numerics.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/numerics.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`t`</b>: Tensor to check.
* <b>`msg`</b>: Message to log on failure.
* <b>`name`</b>: A name for this operation (optional).
* <b>`x`</b>: Alias for t.
* <b>`message`</b>: Alias for msg.


#### Returns:

Same tensor as `t`.
