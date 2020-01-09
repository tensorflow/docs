page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.zeros_like


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L2386-L2424">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a tensor with all elements set to zero.

``` python
tf.compat.v2.zeros_like(
    input,
    dtype=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Given a single tensor (`tensor`), this operation returns a tensor of the
same type and shape as `tensor` with all elements set to zero. Optionally,
you can use `dtype` to specify a new type for the returned tensor.

#### For example:



```python
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
tf.zeros_like(tensor)  # [[0, 0, 0], [0, 0, 0]] with dtype=int32

If dtype of input `tensor` is `float32`, then the output is also of `float32`
tensor = tf.constant([[1.0, 2.0, 3.0], [4, 5, 6]])
tf.zeros_like(tensor)  # [[0., 0., 0.], [0., 0., 0.]] with dtype=floa32

If you want to specify desired dtype of output `tensor`, then specify it in
the op tensor = tf.constant([[1.0, 2.0, 3.0], [4, 5, 6]])
tf.zeros_like(tensor,dtype=tf.int32)  # [[0, 0, 0], [0, 0, 0]] with
dtype=int32
```

#### Args:


* <b>`input`</b>: A `Tensor`.
* <b>`dtype`</b>: A type for the returned `Tensor`. Must be `float16`, `float32`,
  `float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`,
  `complex64`, `complex128`, `bool` or `string`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` with all elements set to zero.
