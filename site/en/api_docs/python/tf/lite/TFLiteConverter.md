page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lite.TFLiteConverter

## Class `TFLiteConverter`

Convert a TensorFlow model into `output_format`.



### Aliases:

* Class `tf.compat.v1.lite.TFLiteConverter`
* Class `tf.lite.TFLiteConverter`



Defined in [`lite/python/lite.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/lite/python/lite.py).

<!-- Placeholder for "Used in" -->

This is used to convert from a TensorFlow GraphDef or SavedModel into either a
TFLite FlatBuffer or graph visualization.

#### Attributes:


* <b>`inference_type`</b>: Target data type of real-number arrays in the output file.
  Must be `{tf.float32, tf.uint8}`. If `optimzations` are provided, this
  parameter is ignored. (default tf.float32)
* <b>`inference_input_type`</b>: Target data type of real-number input arrays. Allows
  for a different type for input arrays.
  If an integer type is provided and `optimizations` are not used,
  `quantized_inputs_stats` must be provided.
  If `inference_type` is tf.uint8, signaling conversion to a fully quantized
  model from a quantization-aware trained input model, then
  `inference_input_type` defaults to tf.uint8.
  In all other cases, `inference_input_type` defaults to tf.float32.
  Must be `{tf.float32, tf.uint8, tf.int8}`
* <b>`inference_output_type`</b>: Target data type of real-number output arrays. Allows
  for a different type for output arrays.
  If `inference_type` is tf.uint8, signaling conversion to a fully quantized
  model from a quantization-aware trained output model, then
  `inference_output_type` defaults to tf.uint8.
  In all other cases, `inference_output_type` must be tf.float32, an error
  will be thrown otherwise.
  Must be `{tf.float32, tf.uint8, tf.int8}`
* <b>`output_format`</b>: Output file format. Currently must be `{TFLITE,
  GRAPHVIZ_DOT}`. (default TFLITE)
* <b>`quantized_input_stats`</b>: Dict of strings representing input tensor names
  mapped to tuple of floats representing the mean and standard deviation
  of the training data (e.g., {"foo" : (0., 1.)}). Only need if
  `inference_input_type` is `QUANTIZED_UINT8`.
  real_input_value = (quantized_input_value - mean_value) / std_dev_value.
  (default {})
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
* <b>`post_training_quantize`</b>: deprecated, please specify
 `[Optimize.DEFAULT]` for `optimizations` instead. Boolean
 indicating whether to quantize the weights of the converted float model.
 Model size will be reduced and there will be latency improvements
 (at the cost of accuracy). (default False)
* <b>`dump_graphviz_dir`</b>: Full filepath of folder to dump the graphs at various
  stages of processing GraphViz .dot files. Preferred over
  --output_format=GRAPHVIZ_DOT in order to keep the requirements of the
  output file. (default None)
* <b>`dump_graphviz_video`</b>: Boolean indicating whether to dump the graph after
  every graph transformation. (default False)
* <b>`target_ops`</b>: Experimental flag, subject to change. Set of OpsSet
  options indicating which converter to use.
  (default set([OpsSet.TFLITE_BUILTINS]))
* <b>`optimizations`</b>: Experimental flag, subject to change. A list of optimizations
  to apply when converting the model. E.g. `[Optimize.DEFAULT]`
* <b>`representative_dataset`</b>: A representative dataset that can be used to
  generate input and output samples for the model. The converter can use
  the dataset to evaluate different optimizations.


#### Example usage:


```python
# Converting a GraphDef from session.
converter = lite.TFLiteConverter.from_session(sess, in_tensors, out_tensors)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)

# Converting a GraphDef from file.
converter = lite.TFLiteConverter.from_frozen_graph(
  graph_def_file, input_arrays, output_arrays)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)

# Converting a SavedModel.
converter = lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()

# Converting a tf.keras model.
converter = lite.TFLiteConverter.from_keras_model_file(keras_model)
tflite_model = converter.convert()
```


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    graph_def,
    input_tensors,
    output_tensors,
    input_arrays_with_shape=None,
    output_arrays=None
)
```

Constructor for TFLiteConverter.


#### Args:


* <b>`graph_def`</b>: Frozen TensorFlow GraphDef.
* <b>`input_tensors`</b>: List of input tensors. Type and shape are computed using
  `foo.shape` and `foo.dtype`.
* <b>`output_tensors`</b>: List of output tensors (only .name is used from this).
* <b>`input_arrays_with_shape`</b>: Tuple of strings representing input tensor names
  and list of integers representing input shapes
  (e.g., [("foo" : [1, 16, 16, 3])]). Use only when graph cannot be loaded
    into TensorFlow and when `input_tensors` and `output_tensors` are
    None. (default None)
* <b>`output_arrays`</b>: List of output tensors to freeze graph with. Use only when
  graph cannot be loaded into TensorFlow and when `input_tensors` and
  `output_tensors` are None. (default None)


#### Raises:


* <b>`ValueError`</b>: Invalid arguments.



## Methods

<h3 id="convert"><code>convert</code></h3>

``` python
convert()
```

Converts a TensorFlow GraphDef based on instance variables.


#### Returns:

The converted data in serialized format. Either a TFLite Flatbuffer or a
Graphviz graph depending on value in `output_format`.



#### Raises:


* <b>`ValueError`</b>:   Input shape is not specified.
  None value for dimension in input_tensor.

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

Creates a TFLiteConverter class from a file containing a frozen GraphDef.


#### Args:


* <b>`graph_def_file`</b>: Full filepath of file containing frozen GraphDef.
* <b>`input_arrays`</b>: List of input tensors to freeze graph with.
* <b>`output_arrays`</b>: List of output tensors to freeze graph with.
* <b>`input_shapes`</b>: Dict of strings representing input tensor names to list of
  integers representing input shapes (e.g., {"foo" : [1, 16, 16, 3]}).
  Automatically determined when input shapes is None (e.g., {"foo" :
    None}). (default None)


#### Returns:

TFLiteConverter class.



#### Raises:


* <b>`IOError`</b>:   File not found.
  Unable to parse input file.
* <b>`ValueError`</b>:   The graph is not frozen.
  input_arrays or output_arrays contains an invalid tensor name.
  input_shapes is not correctly defined when required

<h3 id="from_keras_model_file"><code>from_keras_model_file</code></h3>

``` python
@classmethod
from_keras_model_file(
    cls,
    model_file,
    input_arrays=None,
    input_shapes=None,
    output_arrays=None,
    custom_objects=None
)
```

Creates a TFLiteConverter class from a tf.keras model file.


#### Args:


* <b>`model_file`</b>: Full filepath of HDF5 file containing the tf.keras model.
* <b>`input_arrays`</b>: List of input tensors to freeze graph with. Uses input
  arrays from SignatureDef when none are provided. (default None)
* <b>`input_shapes`</b>: Dict of strings representing input tensor names to list of
  integers representing input shapes (e.g., {"foo" : [1, 16, 16, 3]}).
  Automatically determined when input shapes is None (e.g., {"foo" :
    None}). (default None)
* <b>`output_arrays`</b>: List of output tensors to freeze graph with. Uses output
  arrays from SignatureDef when none are provided. (default None)
* <b>`custom_objects`</b>: Dict mapping names (strings) to custom classes or
  functions to be considered during model deserialization. (default None)


#### Returns:

TFLiteConverter class.


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

Creates a TFLiteConverter class from a SavedModel.


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

TFLiteConverter class.


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

Creates a TFLiteConverter class from a TensorFlow Session.


#### Args:


* <b>`sess`</b>: TensorFlow Session.
* <b>`input_tensors`</b>: List of input tensors. Type and shape are computed using
  `foo.shape` and `foo.dtype`.
* <b>`output_tensors`</b>: List of output tensors (only .name is used from this).


#### Returns:

TFLiteConverter class.


<h3 id="get_input_arrays"><code>get_input_arrays</code></h3>

``` python
get_input_arrays()
```

Returns a list of the names of the input tensors.


#### Returns:

List of strings.




