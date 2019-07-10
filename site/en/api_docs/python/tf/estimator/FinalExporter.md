page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.FinalExporter

## Class `FinalExporter`

This class exports the serving graph and checkpoints at the end.

Inherits From: [`Exporter`](../../tf/estimator/Exporter)

### Aliases:

* Class `tf.compat.v1.estimator.FinalExporter`
* Class `tf.compat.v2.estimator.FinalExporter`
* Class `tf.estimator.FinalExporter`



Defined in [`python/estimator/exporter.py`](https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/exporter.py).

<!-- Placeholder for "Used in" -->

This class performs a single export at the end of training.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    name,
    serving_input_receiver_fn,
    assets_extra=None,
    as_text=False
)
```

Create an `Exporter` to use with <a href="../../tf/estimator/EvalSpec"><code>tf.estimator.EvalSpec</code></a>.


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


#### Raises:


* <b>`ValueError`</b>: if any arguments is invalid.



## Properties

<h3 id="name"><code>name</code></h3>






## Methods

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






