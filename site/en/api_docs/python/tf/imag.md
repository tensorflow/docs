

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.imag

``` python
tf.imag(
    input,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/ops/math_ops.py).

See the guide: [Math > Complex Number Functions](../../../api_guides/python/math_ops#Complex_Number_Functions)

Returns the imaginary part of a complex (or real) tensor.

Given a tensor `input`, this operation returns a tensor of type `float` that
is the imaginary part of each element in `input` considered as a complex
number. If `input` is real, a tensor of all zeros is returned.

For example:

```python
x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])
tf.imag(x)  # [4.75, 5.75]
```

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float`, `double`,
    `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float32` or `float64`.