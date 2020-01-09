page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Dropout


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L110-L179">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Dropout`

Applies Dropout to the input.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.Dropout`
* Class `tf.compat.v2.keras.layers.Dropout`


### Used in the guide:

* [Migrate your TensorFlow 1 code to TensorFlow 2](https://www.tensorflow.org/guide/migrate)
* [The Keras functional API in TensorFlow](https://www.tensorflow.org/guide/keras/functional)

### Used in the tutorials:

* [Basic classification: Predict an image of clothing](https://www.tensorflow.org/tutorials/keras/classification)
* [Classification on imbalanced data](https://www.tensorflow.org/tutorials/structured_data/imbalanced_data)
* [Create an Estimator from a Keras model](https://www.tensorflow.org/tutorials/estimator/keras_model_to_estimator)
* [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)
* [Explore overfit and underfit](https://www.tensorflow.org/tutorials/keras/overfit_and_underfit)
* [Image classification](https://www.tensorflow.org/tutorials/images/classification)
* [Pix2Pix](https://www.tensorflow.org/tutorials/generative/pix2pix)
* [TensorFlow 2.0 quickstart for beginners](https://www.tensorflow.org/tutorials/quickstart/beginner)
* [Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer)



Dropout consists in randomly setting
a fraction `rate` of input units to 0 at each update during training time,
which helps prevent overfitting.

#### Arguments:


* <b>`rate`</b>: Float between 0 and 1. Fraction of the input units to drop.
* <b>`noise_shape`</b>: 1D integer tensor representing the shape of the
  binary dropout mask that will be multiplied with the input.
  For instance, if your inputs have shape
  `(batch_size, timesteps, features)` and
  you want the dropout mask to be the same for all timesteps,
  you can use `noise_shape=(batch_size, 1, features)`.
* <b>`seed`</b>: A Python integer to use as random seed.


#### Call arguments:


* <b>`inputs`</b>: Input tensor (of any rank).
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode (adding dropout) or in inference mode (doing nothing).

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L133-L138">View source</a>

``` python
__init__(
    rate,
    noise_shape=None,
    seed=None,
    **kwargs
)
```
