page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ones


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/ones">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L2531-L2574">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a tensor with all elements set to 1.

### Aliases:

* <a href="/api_docs/python/tf/ones"><code>tf.compat.v1.ones</code></a>
* <a href="/api_docs/python/tf/ones"><code>tf.compat.v2.ones</code></a>


``` python
tf.ones(
    shape,
    dtype=tf.dtypes.float32,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This operation returns a tensor of type `dtype` with shape `shape` and all
elements set to 1.

#### For example:



```python
tf.ones([2, 3], tf.int32)  # [[1, 1, 1], [1, 1, 1]]
```

#### Args:


* <b>`shape`</b>: A list of integers, a tuple of integers, or a 1-D `Tensor` of type
  `int32`.
* <b>`dtype`</b>: The type of an element in the resulting `Tensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` with all elements set to 1.
