page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.callbacks.TensorBoard


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L1362-L1726">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TensorBoard`

Enable visualizations for TensorBoard.

Inherits From: [`Callback`](../../../tf/keras/callbacks/Callback)

### Aliases:

* Class `tf.compat.v2.keras.callbacks.TensorBoard`


### Used in the guide:

* [Keras overview](https://www.tensorflow.org/guide/keras/overview)

### Used in the tutorials:

* [Distributed training with Keras](https://www.tensorflow.org/tutorials/distribute/keras)



TensorBoard is a visualization tool provided with TensorFlow.

This callback logs events for TensorBoard, including:
* Metrics summary plots
* Training graph visualization
* Activation histograms
* Sampled profiling

If you have installed TensorFlow with pip, you should be able
to launch TensorBoard from the command line:

```sh
tensorboard --logdir=path_to_your_logs
```

You can find more information about TensorBoard
[here](https://www.tensorflow.org/get_started/summaries_and_tensorboard).

#### Arguments:


* <b>`log_dir`</b>: the path of the directory where to save the log files to be
  parsed by TensorBoard.
* <b>`histogram_freq`</b>: frequency (in epochs) at which to compute activation and
  weight histograms for the layers of the model. If set to 0, histograms
  won't be computed. Validation data (or split) must be specified for
  histogram visualizations.
* <b>`write_graph`</b>: whether to visualize the graph in TensorBoard. The log file
  can become quite large when write_graph is set to True.
* <b>`write_images`</b>: whether to write model weights to visualize as image in
  TensorBoard.
* <b>`update_freq`</b>: `'batch'` or `'epoch'` or integer. When using `'batch'`,
  writes the losses and metrics to TensorBoard after each batch. The same
  applies for `'epoch'`. If using an integer, let's say `1000`, the
  callback will write the metrics and losses to TensorBoard every 1000
  samples. Note that writing too frequently to TensorBoard can slow down
  your training.
* <b>`profile_batch`</b>: Profile the batch to sample compute characteristics. By
  default, it will profile the second batch. Set profile_batch=0 to
  disable profiling. Must run in TensorFlow eager mode.
* <b>`embeddings_freq`</b>: frequency (in epochs) at which embedding layers will
  be visualized. If set to 0, embeddings won't be visualized.
* <b>`embeddings_metadata`</b>: a dictionary which maps layer name to a file name in
  which metadata for this embedding layer is saved. See the
  [details](
    https://www.tensorflow.org/how_tos/embedding_viz/#metadata_optional)
  about metadata files format. In case if the same metadata file is
  used for all embedding layers, string can be passed.


#### Raises:


* <b>`ValueError`</b>: If histogram_freq is set and no validation data is provided.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L1419-L1463">View source</a>

``` python
__init__(
    log_dir='logs',
    histogram_freq=0,
    write_graph=True,
    write_images=False,
    update_freq='epoch',
    profile_batch=2,
    embeddings_freq=0,
    embeddings_metadata=None,
    **kwargs
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="on_batch_begin"><code>on_batch_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L464-L465">View source</a>

``` python
on_batch_begin(
    batch,
    logs=None
)
```

A backwards compatibility alias for `on_train_batch_begin`.


<h3 id="on_batch_end"><code>on_batch_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L1585-L1606">View source</a>

``` python
on_batch_end(
    batch,
    logs=None
)
```

Writes scalar summaries for metrics on every training batch.

Performs profiling if current batch is in profiler_batches.

#### Arguments:


* <b>`batch`</b>: Integer, index of batch within the current epoch.
* <b>`logs`</b>: Dict. Metric results for this batch.

<h3 id="on_epoch_begin"><code>on_epoch_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L470-L480">View source</a>

``` python
on_epoch_begin(
    epoch,
    logs=None
)
```

Called at the start of an epoch.

Subclasses should override for any actions to run. This function should only
be called during TRAIN mode.

#### Arguments:


* <b>`epoch`</b>: integer, index of epoch.
* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
  but that may change in the future.

<h3 id="on_epoch_end"><code>on_epoch_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L1608-L1617">View source</a>

``` python
on_epoch_end(
    epoch,
    logs=None
)
```

Runs metrics and histogram summaries at epoch end.


<h3 id="on_predict_batch_begin"><code>on_predict_batch_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L547-L556">View source</a>

``` python
on_predict_batch_begin(
    batch,
    logs=None
)
```

Called at the beginning of a batch in `predict` methods.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`batch`</b>: integer, index of batch within the current epoch.
* <b>`logs`</b>: dict. Has keys `batch` and `size` representing the current batch
  number and the size of the batch.

<h3 id="on_predict_batch_end"><code>on_predict_batch_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L558-L566">View source</a>

``` python
on_predict_batch_end(
    batch,
    logs=None
)
```

Called at the end of a batch in `predict` methods.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`batch`</b>: integer, index of batch within the current epoch.
* <b>`logs`</b>: dict. Metric results for this batch.

<h3 id="on_predict_begin"><code>on_predict_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L608-L616">View source</a>

``` python
on_predict_begin(logs=None)
```

Called at the beginning of prediction.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
  but that may change in the future.

<h3 id="on_predict_end"><code>on_predict_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L618-L626">View source</a>

``` python
on_predict_end(logs=None)
```

Called at the end of prediction.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
  but that may change in the future.

<h3 id="on_test_batch_begin"><code>on_test_batch_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L520-L532">View source</a>

``` python
on_test_batch_begin(
    batch,
    logs=None
)
```

Called at the beginning of a batch in `evaluate` methods.

Also called at the beginning of a validation batch in the `fit`
methods, if validation data is provided.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`batch`</b>: integer, index of batch within the current epoch.
* <b>`logs`</b>: dict. Has keys `batch` and `size` representing the current batch
  number and the size of the batch.

<h3 id="on_test_batch_end"><code>on_test_batch_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L534-L545">View source</a>

``` python
on_test_batch_end(
    batch,
    logs=None
)
```

Called at the end of a batch in `evaluate` methods.

Also called at the end of a validation batch in the `fit`
methods, if validation data is provided.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`batch`</b>: integer, index of batch within the current epoch.
* <b>`logs`</b>: dict. Metric results for this batch.

<h3 id="on_test_begin"><code>on_test_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L588-L596">View source</a>

``` python
on_test_begin(logs=None)
```

Called at the beginning of evaluation or validation.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
  but that may change in the future.

<h3 id="on_test_end"><code>on_test_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L598-L606">View source</a>

``` python
on_test_end(logs=None)
```

Called at the end of evaluation or validation.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
  but that may change in the future.

<h3 id="on_train_batch_begin"><code>on_train_batch_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L495-L506">View source</a>

``` python
on_train_batch_begin(
    batch,
    logs=None
)
```

Called at the beginning of a training batch in `fit` methods.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`batch`</b>: integer, index of batch within the current epoch.
* <b>`logs`</b>: dict. Has keys `batch` and `size` representing the current batch
  number and the size of the batch.

<h3 id="on_train_batch_end"><code>on_train_batch_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L508-L518">View source</a>

``` python
on_train_batch_end(
    batch,
    logs=None
)
```

Called at the end of a training batch in `fit` methods.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`batch`</b>: integer, index of batch within the current epoch.
* <b>`logs`</b>: dict. Metric results for this batch.

<h3 id="on_train_begin"><code>on_train_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L1580-L1583">View source</a>

``` python
on_train_begin(logs=None)
```

Called at the beginning of training.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
  but that may change in the future.

<h3 id="on_train_end"><code>on_train_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L1619-L1622">View source</a>

``` python
on_train_end(logs=None)
```

Called at the end of training.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
  but that may change in the future.

<h3 id="set_model"><code>set_model</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L1492-L1510">View source</a>

``` python
set_model(model)
```

Sets Keras model and writes graph if specified.


<h3 id="set_params"><code>set_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L458-L459">View source</a>

``` python
set_params(params)
```
