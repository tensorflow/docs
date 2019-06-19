page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lite.freeze_saved_model

``` python
tf.contrib.lite.freeze_saved_model(
    saved_model_dir,
    input_arrays,
    input_shapes,
    output_arrays,
    tag_set,
    signature_key
)
```



Defined in [`tensorflow/contrib/lite/python/convert_saved_model.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/lite/python/convert_saved_model.py).

Converts a SavedModel to a frozen graph.

#### Args:

* <b>`saved_model_dir`</b>: SavedModel directory to convert.
* <b>`input_arrays`</b>: List of input tensors to freeze graph with. Uses input arrays
    from SignatureDef when none are provided.
* <b>`input_shapes`</b>: Dict of strings representing input tensor names to list of
    integers representing input shapes (e.g., {"foo": : [1, 16, 16, 3]}).
    Automatically determined when input shapes is None (e.g., {"foo" : None}).
* <b>`output_arrays`</b>: List of output tensors to freeze graph with. Uses output
    arrays from SignatureDef when none are provided.
* <b>`tag_set`</b>: Set of tags identifying the MetaGraphDef within the SavedModel to
    analyze. All tags in the tag set must be present.
* <b>`signature_key`</b>: Key identifying SignatureDef containing inputs and outputs.


#### Returns:

* <b>`frozen_graph_def`</b>: Frozen GraphDef.
* <b>`in_tensors`</b>: List of input tensors for the graph.
* <b>`out_tensors`</b>: List of output tensors for the graph.


#### Raises:

* <b>`ValueError`</b>:     SavedModel doesn't contain a MetaGraphDef identified by tag_set.
    signature_key is not in the MetaGraphDef.
    input_shapes does not match the length of input_arrays.
    input_arrays or output_arrays are not valid.