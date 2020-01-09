page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_equal

### Aliases:

* `tf.assert_equal`
* `tf.debugging.assert_equal`

``` python
tf.debugging.assert_equal(
    x,
    y,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/check_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/check_ops.py).

Assert the condition `x == y` holds element-wise.

Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.assert_equal(x, y)]):
  output = tf.reduce_sum(x)
```

This condition holds if for every pair of (possibly broadcast) elements
`x[i]`, `y[i]`, we have `x[i] == y[i]`.
If both `x` and `y` are empty, this is trivially satisfied.

#### Args:

* <b>`x`</b>:  Numeric `Tensor`.
* <b>`y`</b>:  Numeric `Tensor`, same dtype as and broadcastable to `x`.
* <b>`data`</b>:  The tensors to print out if the condition is False.  Defaults to
    error message and first few entries of `x`, `y`.
* <b>`summarize`</b>: Print this many entries of each tensor.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>: A name for this operation (optional).  Defaults to "assert_equal".


#### Returns:

Op that raises `InvalidArgumentError` if `x == y` is False.
@compatibility{eager} returns None


#### Raises:

* <b>`InvalidArgumentError`</b>: if the check can be performed immediately and
    `x == y` is False. The check can be performed immediately during eager
    execution or if `x` and `y` are statically known.