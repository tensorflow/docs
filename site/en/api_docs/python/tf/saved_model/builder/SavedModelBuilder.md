

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.saved_model.builder.SavedModelBuilder

## Class `SavedModelBuilder`





Defined in [`tensorflow/python/saved_model/builder_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/saved_model/builder_impl.py).

Builds the `SavedModel` protocol buffer and saves variables and assets.

The `SavedModelBuilder` class provides functionality to build a `SavedModel`
protocol buffer. Specifically, this allows multiple meta graphs to be saved as
part of a single language-neutral `SavedModel`, while sharing variables and
assets.

To build a SavedModel, the first meta graph must be saved with variables.
Subsequent meta graphs will simply be saved with their graph definitions. If
assets need to be saved and written or copied to disk, they can be provided
when the meta graph def is added. If multiple meta graph defs are associated
an asset of the same name, only the first version is retained.

Each meta graph added to the SavedModel must be annotated with tags. The tags
provide a means to identify the specific meta graph to load and restore, along
with the shared set of variables and assets.

Typical usage for the `SavedModelBuilder`:

```python
...
builder = tf.saved_model.builder.SavedModelBuilder(export_dir)

with tf.Session(graph=tf.Graph()) as sess:
  ...
  builder.add_meta_graph_and_variables(sess,
                                  ["foo-tag"],
                                  signature_def_map=foo_signatures,
                                  assets_collection=foo_assets)
...

with tf.Session(graph=tf.Graph()) as sess:
  ...
  builder.add_meta_graph(["bar-tag", "baz-tag"])
...

builder.save()
```

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(export_dir)
```



<h3 id="add_meta_graph"><code>add_meta_graph</code></h3>

``` python
add_meta_graph(
    tags,
    signature_def_map=None,
    assets_collection=None,
    legacy_init_op=None,
    clear_devices=False,
    main_op=None,
    strip_default_attrs=False
)
```

Adds the current meta graph to the SavedModel.

Creates a Saver in the current scope and uses the Saver to export the meta
graph def. Invoking this API requires the `add_meta_graph_and_variables()`
API to have been invoked before.

#### Args:

* <b>`tags`</b>: The set of tags to annotate the meta graph def with.
* <b>`signature_def_map`</b>: The map of signature defs to be added to the meta graph
      def.
* <b>`assets_collection`</b>: Assets collection to be saved with SavedModel. Note
      that this collection should be a subset of the assets saved as part of
      the first meta graph in the SavedModel.
* <b>`legacy_init_op`</b>: Legacy support for op or group of ops to execute after the
      restore op upon a load.
* <b>`clear_devices`</b>: Set to true if the device info on the default graph should
      be cleared.
* <b>`main_op`</b>: Op or group of ops to execute when the graph is loaded. Note
      that when the main_op is specified it is run after the restore op at
      load-time.
* <b>`strip_default_attrs`</b>: Boolean. If `True`, default-valued attributes will be
    removed from the NodeDefs. For a detailed guide, see
    [Stripping Default-Valued Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).


#### Raises:

* <b>`AssertionError`</b>: If the variables for the SavedModel have not been saved
      yet, or if the graph already contains one or more legacy init ops.

<h3 id="add_meta_graph_and_variables"><code>add_meta_graph_and_variables</code></h3>

``` python
add_meta_graph_and_variables(
    sess,
    tags,
    signature_def_map=None,
    assets_collection=None,
    legacy_init_op=None,
    clear_devices=False,
    main_op=None,
    strip_default_attrs=False
)
```

Adds the current meta graph to the SavedModel and saves variables.

Creates a Saver to save the variables from the provided session. Exports the
corresponding meta graph def. This function assumes that the variables to be
saved have been initialized. For a given `SavedModelBuilder`, this API must
be called exactly once and for the first meta graph to save. For subsequent
meta graph defs to be added, the `add_meta_graph()` API must be used.

#### Args:

* <b>`sess`</b>: The TensorFlow session from which to save the meta graph and
    variables.
* <b>`tags`</b>: The set of tags with which to save the meta graph.
* <b>`signature_def_map`</b>: The map of signature def map to add to the meta graph
    def.
* <b>`assets_collection`</b>: Assets collection to be saved with SavedModel.
* <b>`legacy_init_op`</b>: Legacy support for op or group of ops to execute after the
      restore op upon a load.
* <b>`clear_devices`</b>: Set to true if the device info on the default graph should
      be cleared.
* <b>`main_op`</b>: Op or group of ops to execute when the graph is loaded. Note
      that when the main_op is specified it is run after the restore op at
      load-time.
* <b>`strip_default_attrs`</b>: Boolean. If `True`, default-valued attributes will be
    removed from the NodeDefs. For a detailed guide, see
    [Stripping Default-Valued Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).

<h3 id="save"><code>save</code></h3>

``` python
save(as_text=False)
```

Writes a `SavedModel` protocol buffer to disk.

The function writes the SavedModel protocol buffer to the export directory
in serialized format.

#### Args:

* <b>`as_text`</b>: Writes the SavedModel protocol buffer in text format to disk.


#### Returns:

The path to which the SavedModel protocol buffer was written.



