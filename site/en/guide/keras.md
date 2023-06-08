# Keras: The high-level API for TensorFlow

Keras is the high-level API of the TensorFlow platform. It provides an
approachable, highly-productive interface for solving machine learning (ML)
problems, with a focus on modern deep learning. Keras covers every step of the
machine learning workflow, from data processing to hyperparameter tuning to
deployment. It was developed with a focus on enabling fast experimentation.

With Keras, you have full access to the scalability and cross-platform
capabilities of TensorFlow. You can run Keras on a TPU Pod or large clusters of
GPUs, and you can export Keras models to run in the browser or on mobile
devices. You can also serve Keras models via a web API.

Keras is designed to reduce cognitive load by achieving the following goals:

* Offer simple, consistent interfaces.
* Minimize the number of actions required for common use cases.
* Provide clear, actionable error messages.
* Follow the principle of progressive disclosure of complexity: It's easy to get
  started, and you can complete advanced workflows by learning as you go.
* Help you write concise, readable code.

## Who should use Keras

The short answer is that every TensorFlow user should use the Keras APIs by
default. Whether you're an engineer, a researcher, or an ML practitioner, you
should start with Keras.

There are a few use cases (for example, building tools on top of TensorFlow or
developing your own high-performance platform) that require the low-level
[TensorFlow Core APIs](https://www.tensorflow.org/guide/core). But if your use
case doesn't fall into one
of the
[Core API applications](https://www.tensorflow.org/guide/core#core_api_applications),
you should prefer Keras.

## Keras API components

The core data structures of Keras are [layers](https://keras.io/api/layers/) and
[models](https://keras.io/api/models/). A layer is a simple input/output
transformation, and a model is a directed acyclic graph (DAG) of layers.

### Layers

The `tf.keras.layers.Layer` class is the fundamental abstraction in Keras. A
`Layer` encapsulates a state (weights) and some computation (defined in the
`tf.keras.layers.Layer.call` method).

Weights created by layers can be trainable or non-trainable. Layers are
recursively composable: If you assign a layer instance as an attribute of
another layer, the outer layer will start tracking the weights created by the
inner layer.

You can also use layers to handle data preprocessing tasks like normalization
and text vectorization. Preprocessing layers can be included directly into a
model, either during or after training, which makes the model portable.

### Models

A model is an object that groups layers together and that can be trained on
data.

The simplest type of model is the
[`Sequential` model](https://www.tensorflow.org/guide/keras/sequential_model),
which is a linear stack of layers. For more complex architectures, you can
either use the
[Keras functional API](https://www.tensorflow.org/guide/keras/functional_api),
which lets you build arbitrary graphs of layers, or
[use subclassing to write models from scratch](https://www.tensorflow.org/guide/keras/making_new_layers_and_models_via_subclassing).

The `tf.keras.Model` class features built-in training and evaluation methods:

* `tf.keras.Model.fit`: Trains the model for a fixed number of epochs.
* `tf.keras.Model.predict`: Generates output predictions for the input samples.
* `tf.keras.Model.evaluate`: Returns the loss and metrics values for the model;
  configured via the `tf.keras.Model.compile` method.

These methods give you access to the following built-in training features:

* [Callbacks](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks).
  You can leverage built-in callbacks for early stopping, model checkpointing,
  and [TensorBoard](https://www.tensorflow.org/tensorboard) monitoring. You can
  also
  [implement custom callbacks](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks).
* [Distributed training](https://www.tensorflow.org/guide/keras/distributed_training).
  You can easily scale up your training to multiple GPUs, TPUs, or devices.
* Step fusing. With the `steps_per_execution` argument in
  `tf.keras.Model.compile`, you can process multiple batches in a single
  `tf.function` call, which greatly improves device utilization on TPUs.

For a detailed overview of how to use `fit`, see the
[training and evaluation guide](https://www.tensorflow.org/guide/keras/training_with_built_in_methods).
To learn how to customize the built-in training and evaluation loops, see
[Customizing what happens in `fit()`](https://www.tensorflow.org/guide/keras/customizing_what_happens_in_fit).

### Other APIs and tools

Keras provides many other APIs and tools for deep learning, including:

* [Optimizers](https://keras.io/api/optimizers/)
* [Metrics](https://keras.io/api/metrics/)
* [Losses](https://keras.io/api/losses/)
* [Data loading utilities](https://keras.io/api/data_loading/)

For a full list of available APIs, see the
[Keras API reference](https://keras.io/api/). To learn more about other Keras
projects and initiatives, see
[The Keras ecosystem](https://keras.io/getting_started/ecosystem/).

## Next steps

To get started using Keras with TensorFlow, check out the following topics:

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
* [Introduction to Keras for Researchers](https://keras.io/getting_started/intro_to_keras_for_researchers/)
* [Keras API reference](https://keras.io/api/)
* [The Keras ecosystem](https://keras.io/getting_started/ecosystem/)