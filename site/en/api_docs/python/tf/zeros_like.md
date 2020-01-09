page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.zeros_like


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/zeros_like">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L2355-L2383">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a tensor with all elements set to zero.

### Aliases:

* <a href="/api_docs/python/tf/zeros_like"><code>tf.compat.v1.zeros_like</code></a>


``` python
tf.zeros_like(
    tensor,
    dtype=None,
    name=None,
    optimize=True
)
```



<!-- Placeholder for "Used in" -->

Given a single tensor (`tensor`), this operation returns a tensor of the
same type and shape as `tensor` with all elements set to zero. Optionally,
you can use `dtype` to specify a new type for the returned tensor.

#### For example:



```python
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
tf.zeros_like(tensor)  # [[0, 0, 0], [0, 0, 0]]
```

#### Args:


* <b>`tensor`</b>: A `Tensor`.
* <b>`dtype`</b>: A type for the returned `Tensor`. Must be `float16`, `float32`,
  `float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`,
  `complex64`, `complex128`, `bool` or `string`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`optimize`</b>: if true, attempt to statically determine the shape of 'tensor' and
  encode it as a constant.


#### Returns:

A `Tensor` with all elements set to zero.
