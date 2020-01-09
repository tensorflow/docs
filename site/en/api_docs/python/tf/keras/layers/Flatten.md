page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Flatten


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L538-L610">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Flatten`

Flattens the input. Does not affect the batch size.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.Flatten`
* Class `tf.compat.v2.keras.layers.Flatten`


### Used in the guide:

* [Estimators](https://www.tensorflow.org/guide/estimator)
* [Migrate your TensorFlow 1 code to TensorFlow 2](https://www.tensorflow.org/guide/migrate)
* [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)

### Used in the tutorials:

* [Basic classification: Predict an image of clothing](https://www.tensorflow.org/tutorials/keras/classification)
* [Convolutional Neural Network (CNN)](https://www.tensorflow.org/tutorials/images/cnn)
* [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)
* [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)
* [Distributed training with Keras](https://www.tensorflow.org/tutorials/distribute/keras)
* [Image classification](https://www.tensorflow.org/tutorials/images/classification)
* [Load NumPy data](https://www.tensorflow.org/tutorials/load_data/numpy)
* [Multi-worker training with Estimator](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_estimator)
* [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras)
* [Save and load a model using a distribution strategy](https://www.tensorflow.org/tutorials/distribute/save_and_load)
* [Save and load models](https://www.tensorflow.org/tutorials/keras/save_and_load)
* [TensorFlow 2.0 quickstart for beginners](https://www.tensorflow.org/tutorials/quickstart/beginner)
* [TensorFlow 2.0 quickstart for experts](https://www.tensorflow.org/tutorials/quickstart/advanced)



If inputs are shaped `(batch,)` without a channel dimension, then flattening
adds an extra channel dimension and output shapes are `(batch, 1)`.

#### Arguments:


* <b>`data_format`</b>: A string,
  one of `channels_last` (default) or `channels_first`.
  The ordering of the dimensions in the inputs.
  `channels_last` corresponds to inputs with shape
  `(batch, ..., channels)` while `channels_first` corresponds to
  inputs with shape `(batch, channels, ...)`.
  It defaults to the `image_data_format` value found in your
  Keras config file at `~/.keras/keras.json`.
  If you never set it, then it will be "channels_last".


#### Example:



```python
model = Sequential()
model.add(Convolution2D(64, 3, 3,
                        border_mode='same',
                        input_shape=(3, 32, 32)))
# now: model.output_shape == (None, 64, 32, 32)

model.add(Flatten())
# now: model.output_shape == (None, 65536)
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L569-L572">View source</a>

``` python
__init__(
    data_format=None,
    **kwargs
)
```
