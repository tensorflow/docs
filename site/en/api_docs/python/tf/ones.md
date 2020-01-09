page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ones


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/array_ops.py#L2542-L2585">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a tensor with all elements set to 1.

### Aliases:

* `tf.compat.v1.ones`
* `tf.compat.v2.ones`


``` python
tf.ones(
    shape,
    dtype=tf.dtypes.float32,
    name=None
)
```



### Used in the guide:

* [Migrate your TensorFlow 1 code to TensorFlow 2](https://www.tensorflow.org/guide/migrate)
* [Writing custom layers and models with Keras](https://www.tensorflow.org/guide/keras/custom_layers_and_models)

### Used in the tutorials:

* [Automatic differentiation and gradient tape](https://www.tensorflow.org/tutorials/customization/autodiff)
* [Better performance with tf.function](https://www.tensorflow.org/tutorials/customization/performance)
* [Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer)



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
