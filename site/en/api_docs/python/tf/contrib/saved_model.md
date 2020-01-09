page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.saved_model


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/saved_model/__init__.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



SavedModel contrib support.

<!-- Placeholder for "Used in" -->

SavedModel provides a language-neutral format to save machine-learned models
that is recoverable and hermetic. It enables higher-level systems and tools to
produce, consume and transform TensorFlow models.

## Functions

[`load_keras_model(...)`](../../tf/keras/experimental/load_from_saved_model): Loads a keras Model from a SavedModel created by `export_saved_model()`. (deprecated)

[`save_keras_model(...)`](../../tf/keras/experimental/export_saved_model): Exports a <a href="../../tf/keras/Model"><code>tf.keras.Model</code></a> as a Tensorflow SavedModel. (deprecated)
