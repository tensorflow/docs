# Keras: The high-level API for TensorFlow

Keras is the approachable, productive, high-level API for fast 
experimentation on the TensorFlow platform. Keras focuses on modern 
deep learning and lets you fully use TensorFlow's scalability and 
cross-platform features. 

If you use TensorFlow, use Keras APIs by default for 
each step of the machine learning workflow, from data processing to 
hyperparameter tuning to deployment. Otherwise, 
[a few use cases](https://www.tensorflow.org/guide/core#who_should_use_the_core_apis) 
require the low-level [TensorFlow Core APIs](https://www.tensorflow.org/guide/core).

There are multiple ways to run a Keras model:

* Run on a TPU Pod or large clusters of GPUs.
* Export to run in a browser or mobile device.
* Serve via a web API.

Keras makes ML workflows easier:

* Simple, consistent interfaces.
* Few steps for common tasks.
* Clear, helpful error messages.
* Gradual learning curve: easy to start, advanced options later.
* Concise, readable code.

## Keras API components

Keras has two core data structures: 

* [Layers](https://keras.io/api/layers/) - A simple input/output
  transformation.
* [Models](https://keras.io/api/models/) - A directed acyclic graph (DAG) of layers.

### Layers

The `tf.keras.layers.Layer` class is the main abstraction in Keras. A
`Layer` encapsulates a state (weights) and some computation defined in the
`tf.keras.layers.Layer.call` method.

Weights created by layers are trainable or non-trainable. Layers are
recursively composable: for a layer instance assigned as an attribute of
another layer, the outer layer tracks the weights created by the
inner layer.

Layers can also handle data preprocessing tasks like normalization
and text vectorization. Models are made portable by directly including 
preprocessing layers during or after training.

### Models

A model is an object that groups layers and trains on data. There are a few 
main model types:

* [`Sequential` model](https://www.tensorflow.org/guide/keras/sequential_model) - The
  simplest model which is a linear stack of layers.
* [Keras functional API](https://www.tensorflow.org/guide/keras/functional_api) - Lets
  you build arbitrary graphs of layers for more complex architectures.

You can also [use subclassing to write models from scratch](https://www.tensorflow.org/guide/keras/making_new_layers_and_models_via_subclassing).

The `tf.keras.Model` class has built-in training and evaluation methods:

* `tf.keras.Model.fit` - Trains the model for a fixed number of epochs.
* `tf.keras.Model.predict` - Generates output predictions for the input samples.
* `tf.keras.Model.evaluate` - Returns the loss and metrics values for the model and is
  configured via the `tf.keras.Model.compile` method.

These methods provide built-in training features:

* [Callbacks](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks) -
  Leverage built-in callbacks for early stopping, model checkpointing,
  and [TensorBoard](https://www.tensorflow.org/tensorboard) monitoring. You can
  also
  [implement custom callbacks](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks).
* [Distributed training](https://www.tensorflow.org/guide/keras/distributed_training) -
  Easily scale training to multiple GPUs, TPUs, or devices.
* Step fusing - The `steps_per_execution` argument in
  `tf.keras.Model.compile` can process multiple batches in a single
  `tf.function` call, improving device utilization on TPUs.

For details on using `fit`, see the
[training and evaluation guide](https://www.tensorflow.org/guide/keras/training_with_built_in_methods).
To learn how to customize the built-in training and evaluation loops, see
[customizing what happens in `fit()`](https://www.tensorflow.org/guide/keras/customizing_what_happens_in_fit).

### Other APIs and tools

Keras provides many other APIs and tools for deep learning:

* [Optimizers](https://keras.io/api/optimizers/)
* [Metrics](https://keras.io/api/metrics/)
* [Losses](https://keras.io/api/losses/)
* [Data loading utilities](https://keras.io/api/data_loading/)

For a full list of available APIs, see the
[Keras API reference](https://keras.io/api/). See
[the Keras ecosystem](https://keras.io/getting_started/ecosystem/) to learn more 
about other Keras projects.

## Next steps

To get started using Keras with TensorFlow, see the following topics:

* [The Sequential model](https://www.tensorflow.org/guide/keras/sequential_model)
* [The Functional API](https://www.tensorflow.org/guide/keras/functional)
* [Training & evaluation with the built-in methods](https://www.tensorflow.org/guide/keras/training_with_built_in_methods)
* [Making new layers and models via subclassing](https://www.tensorflow.org/guide/keras/custom_layers_and_models)
* [Serialization and saving](https://www.tensorflow.org/guide/keras/save_and_serialize)
* [Working with preprocessing layers](https://www.tensorflow.org/guide/keras/preprocessing_layers)
* [Customizing what happens in fit()](https://www.tensorflow.org/guide/keras/customizing_what_happens_in_fit)
* [Writing a training loop from scratch](https://www.tensorflow.org/guide/keras/writing_a_training_loop_from_scratch)
* [Working with RNNs](https://www.tensorflow.org/guide/keras/rnn)
* [Understanding masking & padding](https://www.tensorflow.org/guide/keras/masking_and_padding)
* [Writing your own callbacks](https://www.tensorflow.org/guide/keras/custom_callback)
* [Transfer learning & fine-tuning](https://www.tensorflow.org/guide/keras/transfer_learning)
* [Multi-GPU and distributed training](https://www.tensorflow.org/guide/keras/distributed_training)

To learn more about Keras, see the following topics at
[keras.io](http://keras.io):

* [About Keras](https://keras.io/about/)
* [Introduction to Keras for Engineers](https://keras.io/getting_started/intro_to_keras_for_engineers/)
* [Keras API reference](https://keras.io/api/)
* [The Keras ecosystem](https://keras.io/getting_started/ecosystem/)
