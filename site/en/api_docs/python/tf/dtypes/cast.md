page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.dtypes.cast


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/math_ops.py#L646-L707">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Casts a tensor to a new type.

### Aliases:

* `tf.cast`
* `tf.compat.v1.cast`
* `tf.compat.v1.dtypes.cast`
* `tf.compat.v2.cast`
* `tf.compat.v2.dtypes.cast`


``` python
tf.dtypes.cast(
    x,
    dtype,
    name=None
)
```



### Used in the guide:

* [Better performance with tf.function and AutoGraph](https://www.tensorflow.org/guide/function)
* [Eager execution](https://www.tensorflow.org/guide/eager)
* [Estimators](https://www.tensorflow.org/guide/estimator)
* [Keras overview](https://www.tensorflow.org/guide/keras/overview)
* [Masking and padding with Keras](https://www.tensorflow.org/guide/keras/masking_and_padding)
* [Migrate your TensorFlow 1 code to TensorFlow 2](https://www.tensorflow.org/guide/migrate)
* [Train and evaluate with Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate)
* [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)

### Used in the tutorials:

* [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)
* [CycleGAN](https://www.tensorflow.org/tutorials/generative/cyclegan)
* [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)
* [Distributed training with Keras](https://www.tensorflow.org/tutorials/distribute/keras)
* [Image captioning with visual attention](https://www.tensorflow.org/tutorials/text/image_captioning)
* [Image segmentation](https://www.tensorflow.org/tutorials/images/segmentation)
* [Load CSV data](https://www.tensorflow.org/tutorials/load_data/csv)
* [Load text](https://www.tensorflow.org/tutorials/load_data/text)
* [Multi-worker training with Estimator](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_estimator)
* [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras)
* [Neural machine translation with attention](https://www.tensorflow.org/tutorials/text/nmt_with_attention)
* [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)
* [Pix2Pix](https://www.tensorflow.org/tutorials/generative/pix2pix)
* [Save and load a model using a distribution strategy](https://www.tensorflow.org/tutorials/distribute/save_and_load)
* [Save and load models](https://www.tensorflow.org/tutorials/keras/save_and_load)
* [Transfer learning with a pretrained ConvNet](https://www.tensorflow.org/tutorials/images/transfer_learning)
* [Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer)
* [Unicode strings](https://www.tensorflow.org/tutorials/load_data/unicode)



The operation casts `x` (in case of `Tensor`) or `x.values`
(in case of `SparseTensor` or `IndexedSlices`) to `dtype`.

#### For example:



```python
x = tf.constant([1.8, 2.2], dtype=tf.float32)
tf.dtypes.cast(x, tf.int32)  # [1, 2], dtype=tf.int32
```

The operation supports data types (for `x` and `dtype`) of
`uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`, `int64`,
`float16`, `float32`, `float64`, `complex64`, `complex128`, `bfloat16`.
In case of casting from complex types (`complex64`, `complex128`) to real
types, only the real part of `x` is returned. In case of casting from real
types to complex types (`complex64`, `complex128`), the imaginary part of the
returned value is set to `0`. The handling of complex types here matches the
behavior of numpy.

#### Args:


* <b>`x`</b>: A `Tensor` or `SparseTensor` or `IndexedSlices` of numeric type. It could
  be `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`,
  `int64`, `float16`, `float32`, `float64`, `complex64`, `complex128`,
  `bfloat16`.
* <b>`dtype`</b>: The destination type. The list of supported dtypes is the same as
  `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` and
  same type as `dtype`.



#### Raises:


* <b>`TypeError`</b>: If `x` cannot be cast to the `dtype`.
