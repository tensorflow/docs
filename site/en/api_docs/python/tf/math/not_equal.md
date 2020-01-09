page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.not_equal


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/math_ops.py#L1309-L1325">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the truth value of (x != y) element-wise.

### Aliases:

* `tf.compat.v1.math.not_equal`
* `tf.compat.v1.not_equal`
* `tf.compat.v2.math.not_equal`
* `tf.compat.v2.not_equal`
* `tf.not_equal`


``` python
tf.math.not_equal(
    x,
    y,
    name=None
)
```



### Used in the guide:

* [Masking and padding with Keras](https://www.tensorflow.org/guide/keras/masking_and_padding)
* [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)

### Used in the tutorials:

* [Unicode strings](https://www.tensorflow.org/tutorials/load_data/unicode)



**NOTE**: `NotEqual` supports broadcasting. More about broadcasting [here](
https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor` or `SparseTensor` or `IndexedSlices`.
* <b>`y`</b>: A `Tensor` or `SparseTensor` or `IndexedSlices`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type bool with the same size as that of x or y.
