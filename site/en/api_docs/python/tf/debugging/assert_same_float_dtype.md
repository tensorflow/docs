page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_same_float_dtype

### Aliases:

* `tf.assert_same_float_dtype`
* `tf.contrib.framework.assert_same_float_dtype`
* `tf.debugging.assert_same_float_dtype`

``` python
tf.debugging.assert_same_float_dtype(
    tensors=None,
    dtype=None
)
```



Defined in [`tensorflow/python/ops/check_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/check_ops.py).

Validate and return float type based on `tensors` and `dtype`.

For ops such as matrix multiplication, inputs and weights must be of the
same float type. This function validates that all `tensors` are the same type,
validates that type is `dtype` (if supplied), and returns the type. Type must
be a floating point type. If neither `tensors` nor `dtype` is supplied,
the function will return `dtypes.float32`.

#### Args:

* <b>`tensors`</b>: Tensors of input values. Can include `None` elements, which will be
      ignored.
* <b>`dtype`</b>: Expected type.

#### Returns:

Validated type.

#### Raises:

* <b>`ValueError`</b>: if neither `tensors` nor `dtype` is supplied, or result is not
      float, or the common type of the inputs is not a floating point type.