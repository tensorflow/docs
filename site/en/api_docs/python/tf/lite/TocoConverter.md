page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lite.TocoConverter


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/lite/python/lite.py#L1038-L1088">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TocoConverter`

Convert a TensorFlow model into `output_format` using TOCO.



### Aliases:

* Class <a href="/api_docs/python/tf/lite/TocoConverter"><code>tf.compat.v1.lite.TocoConverter</code></a>


<!-- Placeholder for "Used in" -->

This class has been deprecated. Please use <a href="../../tf/lite/TFLiteConverter"><code>lite.TFLiteConverter</code></a> instead.

## Methods

<h3 id="from_frozen_graph"><code>from_frozen_graph</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/lite/python/lite.py#L1051-L1061">View source</a>

``` python
@classmethod
from_frozen_graph(
    cls,
    graph_def_file,
    input_arrays,
    output_arrays,
    input_shapes=None
)
```

Creates a TocoConverter class from a file containing a frozen graph. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../tf/lite/TFLiteConverter#from_frozen_graph"><code>lite.TFLiteConverter.from_frozen_graph</code></a> instead.

<h3 id="from_keras_model_file"><code>from_keras_model_file</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/lite/python/lite.py#L1078-L1088">View source</a>

``` python
@classmethod
from_keras_model_file(
    cls,
    model_file,
    input_arrays=None,
    input_shapes=None,
    output_arrays=None
)
```

Creates a TocoConverter class from a tf.keras model file. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../tf/lite/TFLiteConverter#from_keras_model_file"><code>lite.TFLiteConverter.from_keras_model_file</code></a> instead.

<h3 id="from_saved_model"><code>from_saved_model</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/lite/python/lite.py#L1063-L1076">View source</a>

``` python
@classmethod
from_saved_model(
    cls,
    saved_model_dir,
    input_arrays=None,
    input_shapes=None,
    output_arrays=None,
    tag_set=None,
    signature_key=None
)
```

Creates a TocoConverter class from a SavedModel. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../tf/lite/TFLiteConverter#from_saved_model"><code>lite.TFLiteConverter.from_saved_model</code></a> instead.

<h3 id="from_session"><code>from_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/lite/python/lite.py#L1044-L1049">View source</a>

``` python
@classmethod
from_session(
    cls,
    sess,
    input_tensors,
    output_tensors
)
```

Creates a TocoConverter class from a TensorFlow Session. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../tf/lite/TFLiteConverter#from_session"><code>lite.TFLiteConverter.from_session</code></a> instead.
