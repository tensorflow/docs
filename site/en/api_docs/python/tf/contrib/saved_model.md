page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.saved_model

SavedModel contrib support.



Defined in [`contrib/saved_model/__init__.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/saved_model/__init__.py).

<!-- Placeholder for "Used in" -->

SavedModel provides a language-neutral format to save machine-learned models
that is recoverable and hermetic. It enables higher-level systems and tools to
produce, consume and transform TensorFlow models.

## Functions

[`load_keras_model(...)`](../../tf/keras/experimental/load_from_saved_model): Loads a keras Model from a SavedModel created by `export_saved_model()`.

[`save_keras_model(...)`](../../tf/keras/experimental/export_saved_model): Exports a <a href="../../tf/keras/Model"><code>tf.keras.Model</code></a> as a Tensorflow SavedModel.

