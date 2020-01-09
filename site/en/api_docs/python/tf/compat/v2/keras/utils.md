page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v2.keras.utils


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/compat/v2/keras/utils">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Keras utilities.

<!-- Placeholder for "Used in" -->


## Classes

[`class CustomObjectScope`](../../../../tf/keras/utils/CustomObjectScope): Provides a scope that changes to `_GLOBAL_CUSTOM_OBJECTS` cannot escape.

[`class GeneratorEnqueuer`](../../../../tf/keras/utils/GeneratorEnqueuer): Builds a queue out of a data generator.

[`class HDF5Matrix`](../../../../tf/keras/utils/HDF5Matrix): Representation of HDF5 dataset to be used instead of a Numpy array.

[`class OrderedEnqueuer`](../../../../tf/keras/utils/OrderedEnqueuer): Builds a Enqueuer from a Sequence.

[`class Progbar`](../../../../tf/keras/utils/Progbar): Displays a progress bar.

[`class Sequence`](../../../../tf/keras/utils/Sequence): Base object for fitting to a sequence of data, such as a dataset.

[`class SequenceEnqueuer`](../../../../tf/keras/utils/SequenceEnqueuer): Base class to enqueue inputs.

## Functions

[`convert_all_kernels_in_model(...)`](../../../../tf/keras/utils/convert_all_kernels_in_model): Converts all convolution kernels in a model from Theano to TensorFlow.

[`custom_object_scope(...)`](../../../../tf/keras/utils/custom_object_scope): Provides a scope that changes to `_GLOBAL_CUSTOM_OBJECTS` cannot escape.

[`deserialize_keras_object(...)`](../../../../tf/keras/utils/deserialize_keras_object)

[`get_custom_objects(...)`](../../../../tf/keras/utils/get_custom_objects): Retrieves a live reference to the global dictionary of custom objects.

[`get_file(...)`](../../../../tf/keras/utils/get_file): Downloads a file from a URL if it not already in the cache.

[`get_source_inputs(...)`](../../../../tf/keras/utils/get_source_inputs): Returns the list of input tensors necessary to compute `tensor`.

[`model_to_dot(...)`](../../../../tf/keras/utils/model_to_dot): Convert a Keras model to dot format.

[`multi_gpu_model(...)`](../../../../tf/keras/utils/multi_gpu_model): Replicates a model on different GPUs.

[`normalize(...)`](../../../../tf/keras/utils/normalize): Normalizes a Numpy array.

[`plot_model(...)`](../../../../tf/keras/utils/plot_model): Converts a Keras model to dot format and save to a file.

[`serialize_keras_object(...)`](../../../../tf/keras/utils/serialize_keras_object)

[`to_categorical(...)`](../../../../tf/keras/utils/to_categorical): Converts a class vector (integers) to binary class matrix.
