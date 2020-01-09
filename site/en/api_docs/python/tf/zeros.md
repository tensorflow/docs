page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.zeros


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/array_ops.py#L2314-L2363">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a tensor with all elements set to zero.

### Aliases:

* `tf.compat.v1.zeros`
* `tf.compat.v2.zeros`


``` python
tf.zeros(
    shape,
    dtype=tf.dtypes.float32,
    name=None
)
```



### Used in the guide:

* [Better performance with tf.function and AutoGraph](https://www.tensorflow.org/guide/function)
* [Migrate your TensorFlow 1 code to TensorFlow 2](https://www.tensorflow.org/guide/migrate)
* [The Keras functional API in TensorFlow](https://www.tensorflow.org/guide/keras/functional)
* [Training checkpoints](https://www.tensorflow.org/guide/checkpoint)
* [Writing custom layers and models with Keras](https://www.tensorflow.org/guide/keras/custom_layers_and_models)

### Used in the tutorials:

* [Better performance with tf.function](https://www.tensorflow.org/tutorials/customization/performance)
* [Custom layers](https://www.tensorflow.org/tutorials/customization/custom_layers)
* [Custom training with tf.distribute.Strategy](https://www.tensorflow.org/tutorials/distribute/custom_training)
* [Custom training: basics](https://www.tensorflow.org/tutorials/customization/custom_training)
* [Image captioning with visual attention](https://www.tensorflow.org/tutorials/text/image_captioning)
* [Neural machine translation with attention](https://www.tensorflow.org/tutorials/text/nmt_with_attention)



This operation returns a tensor of type `dtype` with shape `shape` and
all elements set to zero.

#### For example:



```python
tf.zeros([3, 4], tf.int32)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```

#### Args:


* <b>`shape`</b>: A list of integers, a tuple of integers, or a 1-D `Tensor` of type
  `int32`.
* <b>`dtype`</b>: The type of an element in the resulting `Tensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` with all elements set to zero.
