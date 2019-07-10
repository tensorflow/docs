page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_integer

Assert that `x` is of integer dtype.

### Aliases:

* `tf.assert_integer`
* `tf.compat.v1.assert_integer`
* `tf.compat.v1.debugging.assert_integer`
* `tf.debugging.assert_integer`

``` python
tf.debugging.assert_integer(
    x,
    message=None,
    name=None
)
```



Defined in [`python/ops/check_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/check_ops.py).

<!-- Placeholder for "Used in" -->

Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.compat.v1.assert_integer(x)]):
  output = tf.reduce_sum(x)
```

#### Args:


* <b>`x`</b>: `Tensor` whose basetype is integer and is not quantized.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>: A name for this operation (optional).  Defaults to "assert_integer".


#### Raises:


* <b>`TypeError`</b>:  If `x.dtype` is anything other than non-quantized integer.


#### Returns:

A `no_op` that does nothing.  Type can be determined statically.
