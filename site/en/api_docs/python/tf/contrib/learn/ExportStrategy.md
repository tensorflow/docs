

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.learn.ExportStrategy

### `class tf.contrib.learn.ExportStrategy`



Defined in [`tensorflow/contrib/learn/python/learn/export_strategy.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/learn/python/learn/export_strategy.py).

See the guide: [Learn (contrib) > Distributed training utilities](../../../../../api_guides/python/contrib.learn#Distributed_training_utilities)

A class representing a type of model export.

Typically constructed by a utility function specific to the exporter, such as
`saved_model_export_utils.make_export_strategy()`.

The fields are:
  name: The directory name under the export base directory where exports of
    this type will be written.
  export_fn: A function that writes an export, given an estimator, a
    destination path, and optionally a checkpoint path and an evaluation
    result for that checkpoint.  This export_fn() may be run repeatedly during
    continuous training, or just once at the end of fixed-length training.
    Note the export_fn() may choose whether or not to export based on the eval
    result or based on an internal timer or any other criterion, if exports
    are not desired for every checkpoint.

    The signature of this function must be one of:
      * (estimator, export_path) -> export_path`
      * (estimator, export_path, checkpoint_path) -> export_path`
      * (estimator, export_path, checkpoint_path, eval_result) -> export_path`

## Properties

<h3 id="export_fn"><code>export_fn</code></h3>

Alias for field number 1

<h3 id="name"><code>name</code></h3>

Alias for field number 0



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
__new__(
    _cls,
    name,
    export_fn
)
```

Create new instance of ExportStrategy(name, export_fn)

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



