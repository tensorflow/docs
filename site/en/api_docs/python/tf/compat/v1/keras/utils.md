description: Public API for tf.keras.utils namespace.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.keras.utils" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.keras.utils

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf.keras.utils namespace.



## Classes

[`class CustomObjectScope`](../../../../tf/keras/utils/CustomObjectScope.md): Exposes custom classes/functions to Keras deserialization internals.

[`class GeneratorEnqueuer`](../../../../tf/keras/utils/GeneratorEnqueuer.md): Builds a queue out of a data generator.

[`class HDF5Matrix`](../../../../tf/keras/utils/HDF5Matrix.md): Representation of HDF5 dataset to be used instead of a Numpy array.

[`class OrderedEnqueuer`](../../../../tf/keras/utils/OrderedEnqueuer.md): Builds a Enqueuer from a Sequence.

[`class Progbar`](../../../../tf/keras/utils/Progbar.md): Displays a progress bar.

[`class Sequence`](../../../../tf/keras/utils/Sequence.md): Base object for fitting to a sequence of data, such as a dataset.

[`class SequenceEnqueuer`](../../../../tf/keras/utils/SequenceEnqueuer.md): Base class to enqueue inputs.

[`class custom_object_scope`](../../../../tf/keras/utils/CustomObjectScope.md): Exposes custom classes/functions to Keras deserialization internals.

## Functions

[`convert_all_kernels_in_model(...)`](../../../../tf/keras/utils/convert_all_kernels_in_model.md): Converts all convolution kernels in a model from Theano to TensorFlow. (deprecated)

[`deserialize_keras_object(...)`](../../../../tf/keras/utils/deserialize_keras_object.md): Turns the serialized form of a Keras object back into an actual object.

[`get_custom_objects(...)`](../../../../tf/keras/utils/get_custom_objects.md): Retrieves a live reference to the global dictionary of custom objects.

[`get_file(...)`](../../../../tf/keras/utils/get_file.md): Downloads a file from a URL if it not already in the cache.

[`get_registered_name(...)`](../../../../tf/keras/utils/get_registered_name.md): Returns the name registered to an object within the Keras framework.

[`get_registered_object(...)`](../../../../tf/keras/utils/get_registered_object.md): Returns the class associated with `name` if it is registered with Keras.

[`get_source_inputs(...)`](../../../../tf/keras/utils/get_source_inputs.md): Returns the list of input tensors necessary to compute `tensor`.

[`model_to_dot(...)`](../../../../tf/keras/utils/model_to_dot.md): Convert a Keras model to dot format.

[`multi_gpu_model(...)`](../../../../tf/keras/utils/multi_gpu_model.md): Replicates a model on different GPUs. (deprecated)

[`normalize(...)`](../../../../tf/keras/utils/normalize.md): Normalizes a Numpy array.

[`plot_model(...)`](../../../../tf/keras/utils/plot_model.md): Converts a Keras model to dot format and save to a file.

[`register_keras_serializable(...)`](../../../../tf/keras/utils/register_keras_serializable.md): Registers an object with the Keras serialization framework.

[`serialize_keras_object(...)`](../../../../tf/keras/utils/serialize_keras_object.md): Serialize a Keras object into a JSON-compatible representation.

[`to_categorical(...)`](../../../../tf/keras/utils/to_categorical.md): Converts a class vector (integers) to binary class matrix.

