page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.reduce_sum


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/math_ops.py#L1530-L1575">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the sum of elements across dimensions of a tensor.

### Aliases:

* `tf.compat.v2.math.reduce_sum`
* `tf.compat.v2.reduce_sum`
* `tf.reduce_sum`


``` python
tf.math.reduce_sum(
    input_tensor,
    axis=None,
    keepdims=False,
    name=None
)
```



### Used in the guide:

* [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training)
* [Eager execution](https://www.tensorflow.org/guide/eager)
* [Train and evaluate with Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate)
* [Writing custom layers and models with Keras](https://www.tensorflow.org/guide/keras/custom_layers_and_models)
* [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)

### Used in the tutorials:

* [Automatic differentiation and gradient tape](https://www.tensorflow.org/tutorials/customization/autodiff)
* [Better performance with tf.function](https://www.tensorflow.org/tutorials/customization/performance)
* [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)
* [Customization basics: tensors and operations](https://www.tensorflow.org/tutorials/customization/basics)
* [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)
* [Image captioning with visual attention](https://www.tensorflow.org/tutorials/text/image_captioning)
* [Multi-worker training with Estimator](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_estimator)
* [Neural machine translation with attention](https://www.tensorflow.org/tutorials/text/nmt_with_attention)
* [Unicode strings](https://www.tensorflow.org/tutorials/load_data/unicode)



Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
entry in `axis`. If `keepdims` is true, the reduced dimensions
are retained with length 1.

If `axis` is None, all dimensions are reduced, and a
tensor with a single element is returned.

#### For example:



```python
x = tf.constant([[1, 1, 1], [1, 1, 1]])
tf.reduce_sum(x)  # 6
tf.reduce_sum(x, 0)  # [2, 2, 2]
tf.reduce_sum(x, 1)  # [3, 3]
tf.reduce_sum(x, 1, keepdims=True)  # [[3], [3]]
tf.reduce_sum(x, [0, 1])  # 6
```

#### Args:


* <b>`input_tensor`</b>: The tensor to reduce. Should have numeric type.
* <b>`axis`</b>: The dimensions to reduce. If `None` (the default), reduces all
  dimensions. Must be in the range `[-rank(input_tensor),
  rank(input_tensor))`.
* <b>`keepdims`</b>: If true, retains reduced dimensions with length 1.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The reduced tensor, of the same dtype as the input_tensor.




#### Numpy Compatibility
Equivalent to np.sum apart the fact that numpy upcast uint8 and int32 to
int64 while tensorflow returns the same dtype as the input.
