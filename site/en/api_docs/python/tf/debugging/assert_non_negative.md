page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_non_negative

Assert the condition `x >= 0` holds element-wise.

### Aliases:

* `tf.assert_non_negative`
* `tf.compat.v1.assert_non_negative`
* `tf.compat.v1.debugging.assert_non_negative`
* `tf.debugging.assert_non_negative`

``` python
tf.debugging.assert_non_negative(
    x,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```



Defined in [`python/ops/check_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/check_ops.py).

<!-- Placeholder for "Used in" -->

Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.compat.v1.assert_non_negative(x)]):
  output = tf.reduce_sum(x)
```

Non-negative means, for every element `x[i]` of `x`, we have `x[i] >= 0`.
If `x` is empty this is trivially satisfied.

#### Args:


* <b>`x`</b>:  Numeric `Tensor`.
* <b>`data`</b>:  The tensors to print out if the condition is False.  Defaults to
  error message and first few entries of `x`.
* <b>`summarize`</b>: Print this many entries of each tensor.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>: A name for this operation (optional).
  Defaults to "assert_non_negative".


#### Returns:

Op raising `InvalidArgumentError` unless `x` is all non-negative.
