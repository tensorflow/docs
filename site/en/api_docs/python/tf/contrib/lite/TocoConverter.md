

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lite.TocoConverter

## Class `TocoConverter`





Defined in [`tensorflow/contrib/lite/python/lite.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/lite/python/lite.py).

Convert a TensorFlow model into `output_format` using TOCO.

This is used to convert from a TensorFlow GraphDef or SavedModel into either a
TFLite FlatBuffer or graph visualization.

#### Attributes:


* <b>`inference_type`</b>: Target data type of arrays in the output file. Currently
    must be `{FLOAT, QUANTIZED_UINT8}`.  (default FLOAT)
* <b>`inference_input_type`</b>: Target data type of input arrays. Allows for a
    different type for input arrays in the case of quantization. Currently
    must be `{FLOAT, QUANTIZED_UINT8}`. (default `inference_type`)
* <b>`output_format`</b>: Output file format. Currently must be `{TFLITE,
    GRAPHVIZ_DOT}`. (default TFLITE)
* <b>`quantized_input_stats`</b>: Dict of strings representing input tensor names
    mapped to tuple of integers representing the mean and standard deviation
    of the training data (e.g., {"foo" : (0., 1.)}). Only need if
    `inference_type` is `QUANTIZED_UINT8`. (default {})
* <b>`default_ranges_stats`</b>: Tuple of integers representing (min, max) range values
    for all arrays without a specified range. Intended for experimenting with
    quantization via "dummy quantization". (default None)
* <b>`drop_control_dependency`</b>: Boolean indicating whether to drop control
    dependencies silently. This is due to TFLite not supporting control
    dependencies. (default True)
* <b>`reorder_across_fake_quant`</b>: Boolean indicating whether to reorder FakeQuant
    nodes in unexpected locations. Used when the location of the FakeQuant
    nodes is preventing graph transformations necessary to convert the graph.
    Results in a graph that differs from the quantized training graph,
    potentially causing differing arithmetic behavior. (default False)
* <b>`change_concat_input_ranges`</b>: Boolean to change behavior of min/max ranges for
    inputs and outputs of the concat operator for quantized models. Changes
    the ranges of concat operator overlap when true. (default False)
* <b>`allow_custom_ops`</b>: Boolean indicating whether to allow custom operations.
    When false any unknown operation is an error. When true, custom ops are
    created for any op that is unknown. The developer will need to provide
    these to the TensorFlow Lite runtime with a custom resolver.
    (default False)

Example usage:

  # Converting a GraphDef from session.
  converter = lite.TocoConverter.from_session(sess, in_tensors, out_tensors)
  tflite_model = converter.convert()
  open("converted_model.tflite", "wb").write(tflite_model)

  # Converting a GraphDef from file.
  converter = lite.TocoConverter.from_frozen_graph(
    graph_def_file, input_arrays, output_arrays)
  tflite_model = converter.convert()
  open("converted_model.tflite", "wb").write(tflite_model)

  # Converting a SavedModel.
  converter = lite.TocoConverter.from_saved_model(saved_model_dir)
  tflite_model = converter.convert()

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    graph_def,
    input_tensors,
    output_tensors
)
```

Constructor for TocoConverter.

#### Args:


* <b>`graph_def`</b>: TensorFlow GraphDef.
* <b>`input_tensors`</b>: List of input tensors. Type and shape are computed using
    `foo.get_shape()` and `foo.dtype`.
* <b>`output_tensors`</b>: List of output tensors (only .name is used from this).

<h3 id="convert"><code>convert</code></h3>

``` python
convert()
```

Converts a TensorFlow GraphDef based on instance variables.

#### Returns:

The converted data in serialized format. Either a TFLite Flatbuffer or a
Graphviz graph depending on value in `output_format`.


#### Raises:

* <b>`ValueError`</b>:     None value for dimension in input_tensor.

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

Creates a TocoConverter class from a file containing a frozen GraphDef.

#### Args:

* <b>`graph_def_file`</b>: Full filepath of file containing TensorFlow GraphDef.
* <b>`input_arrays`</b>: List of input tensors to freeze graph with.
* <b>`output_arrays`</b>: List of output tensors to freeze graph with.
* <b>`input_shapes`</b>: Dict of strings representing input tensor names to list of
    integers representing input shapes (e.g., {"foo" : [1, 16, 16, 3]}).
    Automatically determined when input shapes is None (e.g., {"foo" :
    None}). (default None)


#### Returns:

TocoConverter class.


#### Raises:

* <b>`ValueError`</b>:     Unable to parse input file.
    The graph is not frozen.
    input_arrays or output_arrays contains an invalid tensor name.

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

Creates a TocoConverter class from a SavedModel.

#### Args:

* <b>`saved_model_dir`</b>: SavedModel directory to convert.
* <b>`input_arrays`</b>: List of input tensors to freeze graph with. Uses input
    arrays from SignatureDef when none are provided. (default None)
* <b>`input_shapes`</b>: Dict of strings representing input tensor names to list of
    integers representing input shapes (e.g., {"foo" : [1, 16, 16, 3]}).
    Automatically determined when input shapes is None (e.g., {"foo" :
    None}). (default None)
* <b>`output_arrays`</b>: List of output tensors to freeze graph with. Uses output
    arrays from SignatureDef when none are provided. (default None)
* <b>`tag_set`</b>: Set of tags identifying the MetaGraphDef within the SavedModel to
    analyze. All tags in the tag set must be present. (default set("serve"))
* <b>`signature_key`</b>: Key identifying SignatureDef containing inputs and outputs.
    (default DEFAULT_SERVING_SIGNATURE_DEF_KEY)


#### Returns:

TocoConverter class.

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

Creates a TocoConverter class from a TensorFlow Session.

#### Args:

* <b>`sess`</b>: TensorFlow Session.
* <b>`input_tensors`</b>: List of input tensors. Type and shape are computed using
    `foo.get_shape()` and `foo.dtype`.
* <b>`output_tensors`</b>: List of output tensors (only .name is used from this).


#### Returns:

TocoConverter class.



