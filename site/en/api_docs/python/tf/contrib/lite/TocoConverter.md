page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lite.TocoConverter

## Class `TocoConverter`





Defined in [`tensorflow/contrib/lite/python/lite.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/lite/python/lite.py).

Convert a TensorFlow model into `output_format` using TOCO.

This class has been deprecated. Please use `lite.TFLiteConverter` instead.

## Methods

<h3 id="from_frozen_graph"><code>from_frozen_graph</code></h3>

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

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `lite.TFLiteConverter.from_frozen_graph` instead.

<h3 id="from_keras_model_file"><code>from_keras_model_file</code></h3>

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

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `lite.TFLiteConverter.from_keras_model_file` instead.

<h3 id="from_saved_model"><code>from_saved_model</code></h3>

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

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `lite.TFLiteConverter.from_saved_model` instead.

<h3 id="from_session"><code>from_session</code></h3>

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

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `lite.TFLiteConverter.from_session` instead.



