page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_all_finite

### Aliases:

* `tf.debugging.assert_all_finite`
* `tf.verify_tensor_all_finite`

``` python
tf.debugging.assert_all_finite(
    t,
    msg,
    name=None
)
```



Defined in [`tensorflow/python/ops/numerics.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/numerics.py).

Assert that the tensor does not contain any NaN's or Inf's.

#### Args:

* <b>`t`</b>: Tensor to check.
* <b>`msg`</b>: Message to log on failure.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

Same tensor as `t`.