page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.imag

Returns the imaginary part of a complex (or real) tensor.

### Aliases:

* `tf.compat.v1.imag`
* `tf.compat.v1.math.imag`
* `tf.compat.v2.math.imag`
* `tf.imag`
* `tf.math.imag`

``` python
tf.math.imag(
    input,
    name=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

Given a tensor `input`, this operation returns a tensor of type `float` that
is the imaginary part of each element in `input` considered as a complex
number. If `input` is real, a tensor of all zeros is returned.

#### For example:



```python
x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])
tf.math.imag(x)  # [4.75, 5.75]
```

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float`, `double`,
  `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float32` or `float64`.
