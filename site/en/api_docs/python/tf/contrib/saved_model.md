page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.saved_model



Defined in [`tensorflow/contrib/saved_model/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/saved_model/__init__.py).

SavedModel contrib support.

SavedModel provides a language-neutral format to save machine-learned models
that is recoverable and hermetic. It enables higher-level systems and tools to
produce, consume and transform TensorFlow models.

## Functions

[`get_signature_def_by_key(...)`](../../tf/contrib/saved_model/get_signature_def_by_key): Utility function to get a SignatureDef protocol buffer by its key.

[`load_keras_model(...)`](../../tf/contrib/saved_model/load_keras_model): Load a keras.Model from SavedModel.

[`save_keras_model(...)`](../../tf/contrib/saved_model/save_keras_model): Save a <a href="../../tf/keras/models/Model"><code>tf.keras.Model</code></a> into Tensorflow SavedModel format.

