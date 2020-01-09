page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Dense


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L923-L1087">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Dense`

Just your regular densely-connected NN layer.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.Dense`
* Class `tf.compat.v2.keras.layers.Dense`


### Used in the guide:

* [Better performance with tf.function and AutoGraph](https://www.tensorflow.org/guide/function)
* [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training)
* [Eager execution](https://www.tensorflow.org/guide/eager)
* [Estimators](https://www.tensorflow.org/guide/estimator)
* [Keras custom callbacks](https://www.tensorflow.org/guide/keras/custom_callback)
* [Keras overview](https://www.tensorflow.org/guide/keras/overview)
* [Migrate your TensorFlow 1 code to TensorFlow 2](https://www.tensorflow.org/guide/migrate)
* [Recurrent Neural Networks (RNN) with Keras](https://www.tensorflow.org/guide/keras/rnn)
* [Save and serialize models with Keras](https://www.tensorflow.org/guide/keras/save_and_serialize)
* [The Keras functional API in TensorFlow](https://www.tensorflow.org/guide/keras/functional)
* [Train and evaluate with Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate)
* [Training checkpoints](https://www.tensorflow.org/guide/checkpoint)
* [Use a GPU](https://www.tensorflow.org/guide/gpu)
* [Writing custom layers and models with Keras](https://www.tensorflow.org/guide/keras/custom_layers_and_models)
* [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)

### Used in the tutorials:

* [Basic classification: Predict an image of clothing](https://www.tensorflow.org/tutorials/keras/classification)
* [Basic regression: Predict fuel efficiency](https://www.tensorflow.org/tutorials/keras/regression)
* [Classification on imbalanced data](https://www.tensorflow.org/tutorials/structured_data/imbalanced_data)
* [Classify structured data with feature columns](https://www.tensorflow.org/tutorials/structured_data/feature_columns)
* [Convolutional Neural Network (CNN)](https://www.tensorflow.org/tutorials/images/cnn)
* [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)
* [Create an Estimator from a Keras model](https://www.tensorflow.org/tutorials/estimator/keras_model_to_estimator)
* [Custom layers](https://www.tensorflow.org/tutorials/customization/custom_layers)
* [Custom training: walkthrough](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough)
* [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)
* [Distributed training with Keras](https://www.tensorflow.org/tutorials/distribute/keras)
* [Explore overfit and underfit](https://www.tensorflow.org/tutorials/keras/overfit_and_underfit)
* [Image captioning with visual attention](https://www.tensorflow.org/tutorials/text/image_captioning)
* [Image classification](https://www.tensorflow.org/tutorials/images/classification)
* [Load CSV data](https://www.tensorflow.org/tutorials/load_data/csv)
* [Load NumPy data](https://www.tensorflow.org/tutorials/load_data/numpy)
* [Load a pandas.DataFrame](https://www.tensorflow.org/tutorials/load_data/pandas_dataframe)
* [Load text](https://www.tensorflow.org/tutorials/load_data/text)
* [Multi-worker training with Estimator](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_estimator)
* [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras)
* [Neural machine translation with attention](https://www.tensorflow.org/tutorials/text/nmt_with_attention)
* [Save and load a model using a distribution strategy](https://www.tensorflow.org/tutorials/distribute/save_and_load)
* [Save and load models](https://www.tensorflow.org/tutorials/keras/save_and_load)
* [TensorFlow 2.0 quickstart for beginners](https://www.tensorflow.org/tutorials/quickstart/beginner)
* [TensorFlow 2.0 quickstart for experts](https://www.tensorflow.org/tutorials/quickstart/advanced)
* [Text classification with TensorFlow Hub: Movie reviews](https://www.tensorflow.org/tutorials/keras/text_classification_with_hub)
* [Text classification with an RNN](https://www.tensorflow.org/tutorials/text/text_classification_rnn)
* [Text classification with preprocessed text: Movie reviews](https://www.tensorflow.org/tutorials/keras/text_classification)
* [Text generation with an RNN](https://www.tensorflow.org/tutorials/text/text_generation)
* [Time series forecasting](https://www.tensorflow.org/tutorials/structured_data/time_series)
* [Transfer learning with TensorFlow Hub](https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub)
* [Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer)
* [Word embeddings](https://www.tensorflow.org/tutorials/text/word_embeddings)



`Dense` implements the operation:
`output = activation(dot(input, kernel) + bias)`
where `activation` is the element-wise activation function
passed as the `activation` argument, `kernel` is a weights matrix
created by the layer, and `bias` is a bias vector created by the layer
(only applicable if `use_bias` is `True`).

Note: If the input to the layer has a rank greater than 2, then
it is flattened prior to the initial dot product with `kernel`.

#### Example:



```python
# as first layer in a sequential model:
model = Sequential()
model.add(Dense(32, input_shape=(16,)))
# now the model will take as input arrays of shape (*, 16)
# and output arrays of shape (*, 32)

# after the first layer, you don't need to specify
# the size of the input anymore:
model.add(Dense(32))
```

#### Arguments:


* <b>`units`</b>: Positive integer, dimensionality of the output space.
* <b>`activation`</b>: Activation function to use.
  If you don't specify anything, no activation is applied
  (ie. "linear" activation: `a(x) = x`).
* <b>`use_bias`</b>: Boolean, whether the layer uses a bias vector.
* <b>`kernel_initializer`</b>: Initializer for the `kernel` weights matrix.
* <b>`bias_initializer`</b>: Initializer for the bias vector.
* <b>`kernel_regularizer`</b>: Regularizer function applied to
  the `kernel` weights matrix.
* <b>`bias_regularizer`</b>: Regularizer function applied to the bias vector.
* <b>`activity_regularizer`</b>: Regularizer function applied to
  the output of the layer (its "activation")..
* <b>`kernel_constraint`</b>: Constraint function applied to
  the `kernel` weights matrix.
* <b>`bias_constraint`</b>: Constraint function applied to the bias vector.


#### Input shape:

N-D tensor with shape: `(batch_size, ..., input_dim)`.
The most common situation would be
a 2D input with shape `(batch_size, input_dim)`.



#### Output shape:

N-D tensor with shape: `(batch_size, ..., units)`.
For instance, for a 2D input with shape `(batch_size, input_dim)`,
the output would have shape `(batch_size, units)`.


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L978-L1006">View source</a>

``` python
__init__(
    units,
    activation=None,
    use_bias=True,
    kernel_initializer='glorot_uniform',
    bias_initializer='zeros',
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    **kwargs
)
```
