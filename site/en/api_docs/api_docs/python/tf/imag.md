

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.imag

``` python
imag(
    input,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/ops/math_ops.py).

See the guide: [Math > Complex Number Functions](../../../api_guides/python/math_ops#Complex_Number_Functions)

Returns the imaginary part of a complex number.

Given a tensor `input` of complex numbers, this operation returns a tensor of
type `float` that is the argument of each element in `input`. All elements in
`input` must be complex numbers of the form \\(a + bj\\), where *a*
is the real part and *b* is the imaginary part returned by the operation.

For example:

```python
x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])
tf.imag(x)  # [4.75, 5.75]
```

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `complex64`,
    `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float32` or `float64`.