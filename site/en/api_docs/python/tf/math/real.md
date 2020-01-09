page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.real

### Aliases:

* `tf.math.real`
* `tf.real`

``` python
tf.math.real(
    input,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/math_ops.py).

Returns the real part of a complex (or real) tensor.

Given a tensor `input`, this operation returns a tensor of type `float` that
is the real part of each element in `input` considered as a complex number.

For example:

```python
x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])
tf.real(x)  # [-2.25, 3.25]
```

If `input` is already real, it is returned unchanged.

#### Args:

* <b>`input`</b>: A `Tensor`. Must have numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float32` or `float64`.