

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.estimator.LatestExporter

## Class `LatestExporter`

Inherits From: [`Exporter`](../../tf/estimator/Exporter)



Defined in [`tensorflow/python/estimator/exporter.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/estimator/exporter.py).

This class regularly exports the serving graph and checkpoints.

In addition to exporting, this class also garbage collects stale exports.

## Properties

<h3 id="name"><code>name</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    name,
    serving_input_receiver_fn,
    assets_extra=None,
    as_text=False,
    exports_to_keep=5
)
```

Create an `Exporter` to use with `tf.estimator.EvalSpec`.

#### Args:

* <b>`name`</b>: unique name of this `Exporter` that is going to be used in the
    export path.
* <b>`serving_input_receiver_fn`</b>: a function that takes no arguments and returns
    a `ServingInputReceiver`.
* <b>`assets_extra`</b>: An optional dict specifying how to populate the assets.extra
    directory within the exported SavedModel.  Each key should give the
    destination path (including the filename) relative to the assets.extra
    directory.  The corresponding value gives the full path of the source
    file to be copied.  For example, the simple case of copying a single
    file without renaming it is specified as
    `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.
* <b>`as_text`</b>: whether to write the SavedModel proto in text format. Defaults to
    `False`.
* <b>`exports_to_keep`</b>: Number of exports to keep.  Older exports will be
    garbage-collected.  Defaults to 5.  Set to `None` to disable garbage
    collection.


#### Raises:

* <b>`ValueError`</b>: if any arguments is invalid.

<h3 id="export"><code>export</code></h3>

``` python
export(
    estimator,
    export_path,
    checkpoint_path,
    eval_result,
    is_the_final_export
)
```





