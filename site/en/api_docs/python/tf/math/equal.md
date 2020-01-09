page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.equal


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/math_ops.py#L1278-L1306">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the truth value of (x == y) element-wise.

### Aliases:

* `tf.compat.v1.equal`
* `tf.compat.v1.math.equal`
* `tf.compat.v2.equal`
* `tf.compat.v2.math.equal`
* `tf.equal`


``` python
tf.math.equal(
    x,
    y,
    name=None
)
```



### Used in the tutorials:

* [Better performance with tf.function](https://www.tensorflow.org/tutorials/customization/performance)
* [Image captioning with visual attention](https://www.tensorflow.org/tutorials/text/image_captioning)
* [Neural machine translation with attention](https://www.tensorflow.org/tutorials/text/nmt_with_attention)
* [Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer)




#### Usage:



```python
x = tf.constant([2, 4])
y = tf.constant(2)
tf.math.equal(x, y) ==> array([True, False])

x = tf.constant([2, 4])
y = tf.constant([2, 4])
tf.math.equal(x, y) ==> array([True,  True])
```

**NOTE**: `Equal` supports broadcasting. More about broadcasting [here](
https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor` or `SparseTensor` or `IndexedSlices`.
* <b>`y`</b>: A `Tensor` or `SparseTensor` or `IndexedSlices`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type bool with the same size as that of x or y.
