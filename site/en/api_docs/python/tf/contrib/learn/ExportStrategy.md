

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.ExportStrategy

## Class `ExportStrategy`





Defined in [`tensorflow/contrib/learn/python/learn/export_strategy.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/learn/python/learn/export_strategy.py).

See the guide: [Learn (contrib) > Distributed training utilities](../../../../../api_guides/python/contrib.learn#Distributed_training_utilities)

A class representing a type of model export.

THIS CLASS IS DEPRECATED. See
[contrib/learn/README.md](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/learn/README.md)
for general migration instructions.

Typically constructed by a utility function specific to the exporter, such as
`saved_model_export_utils.make_export_strategy()`.

#### Attributes:

* <b>`name`</b>: The directory name under the export base directory where exports of
    this type will be written.
* <b>`export_fn`</b>: A function that writes an export, given an estimator, a
    destination path, and optionally a checkpoint path and an evaluation
    result for that checkpoint.  This export_fn() may be run repeatedly during
    continuous training, or just once at the end of fixed-length training.
    Note the export_fn() may choose whether or not to export based on the eval
    result or based on an internal timer or any other criterion, if exports
    are not desired for every checkpoint.

  The signature of this function must be one of:

    * `(estimator, export_path) -> export_path`
    * `(estimator, export_path, checkpoint_path) -> export_path`
    * `(estimator, export_path, checkpoint_path, eval_result) -> export_path`
    * `(estimator, export_path, checkpoint_path, eval_result,
        strip_default_attrs) -> export_path`
* <b>`strip_default_attrs`</b>: (Optional) Boolean. If set as True, default attrs in
      the `GraphDef` will be stripped on write. This is recommended for better
      forward compatibility of the resulting `SavedModel`.

## Properties

<h3 id="export_fn"><code>export_fn</code></h3>

Alias for field number 1

<h3 id="name"><code>name</code></h3>

Alias for field number 0

<h3 id="strip_default_attrs"><code>strip_default_attrs</code></h3>

Alias for field number 2



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
@staticmethod
__new__(
    cls,
    name,
    export_fn,
    strip_default_attrs=None
)
```

DEPRECATED FUNCTION

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please switch to tf.estimator.train_and_evaluate, and use tf.estimator.Exporter.

<h3 id="export"><code>export</code></h3>

``` python
export(
    estimator,
    export_path,
    checkpoint_path=None,
    eval_result=None
)
```

Exports the given Estimator to a specific format.

#### Args:

* <b>`estimator`</b>: the Estimator to export.
* <b>`export_path`</b>: A string containing a directory where to write the export.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If None (the default),
    the strategy may locate a checkpoint (e.g. the most recent) by itself.
* <b>`eval_result`</b>: The output of Estimator.evaluate on this checkpoint.  This
    should be set only if checkpoint_path is provided (otherwise it is
    unclear which checkpoint this eval refers to).


#### Returns:

The string path to the exported directory.


#### Raises:

* <b>`ValueError`</b>: if the export_fn does not have the required signature



