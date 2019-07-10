page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.callbacks.ModelCheckpoint

## Class `ModelCheckpoint`

Save the model after every epoch.

Inherits From: [`Callback`](../../../tf/keras/callbacks/Callback)

### Aliases:

* Class `tf.compat.v1.keras.callbacks.ModelCheckpoint`
* Class `tf.compat.v2.keras.callbacks.ModelCheckpoint`
* Class `tf.keras.callbacks.ModelCheckpoint`



Defined in [`python/keras/callbacks.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/callbacks.py).

<!-- Placeholder for "Used in" -->

`filepath` can contain named formatting options,
which will be filled the value of `epoch` and
keys in `logs` (passed in `on_epoch_end`).

For example: if `filepath` is `weights.{epoch:02d}-{val_loss:.2f}.hdf5`,
then the model checkpoints will be saved with the epoch number and
the validation loss in the filename.

#### Arguments:


* <b>`filepath`</b>: string, path to save the model file.
* <b>`monitor`</b>: quantity to monitor.
* <b>`verbose`</b>: verbosity mode, 0 or 1.
* <b>`save_best_only`</b>: if `save_best_only=True`, the latest best model according
  to the quantity monitored will not be overwritten.
* <b>`mode`</b>: one of {auto, min, max}. If `save_best_only=True`, the decision to
  overwrite the current save file is made based on either the maximization
  or the minimization of the monitored quantity. For `val_acc`, this
  should be `max`, for `val_loss` this should be `min`, etc. In `auto`
  mode, the direction is automatically inferred from the name of the
  monitored quantity.
* <b>`save_weights_only`</b>: if True, then only the model's weights will be saved
  (`model.save_weights(filepath)`), else the full model is saved
  (`model.save(filepath)`).
* <b>`save_freq`</b>: `'epoch'` or integer. When using `'epoch'`, the callback saves
  the model after each epoch. When using integer, the callback saves the
  model at end of a batch at which this many samples have been seen since
  last saving. Note that if the saving isn't aligned to epochs, the
  monitored metric may potentially be less reliable (it could reflect as
  little as 1 batch, since the metrics get reset every epoch). Defaults to
  `'epoch'`
* <b>`load_weights_on_restart`</b>: Whether the training should restore the model. If
  True, the model will attempt to load the checkpoint file from `filepath`
  at the start of `model.fit()`. This saves the need of manually calling
  `model.load_weights()` before `model.fit(). In multi-worker distributed
  training, this provides fault-tolerance and loads the model
  automatically upon recovery of workers. The callback gives up loading if
  the filepath does not exist, and raises ValueError if format does not
  match. Defaults to False.
* <b>`**kwargs`</b>: Additional arguments for backwards compatibility. Possible key
  is `period`.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    filepath,
    monitor='val_loss',
    verbose=0,
    save_best_only=False,
    save_weights_only=False,
    mode='auto',
    save_freq='epoch',
    load_weights_on_restart=False,
    **kwargs
)
```






## Methods

<h3 id="on_batch_begin"><code>on_batch_begin</code></h3>

``` python
on_batch_begin(
    batch,
    logs=None
)
```

A backwards compatibility alias for `on_train_batch_begin`.


<h3 id="on_batch_end"><code>on_batch_end</code></h3>

``` python
on_batch_end(
    batch,
    logs=None
)
```




<h3 id="on_epoch_begin"><code>on_epoch_begin</code></h3>

``` python
on_epoch_begin(
    epoch,
    logs=None
)
```




<h3 id="on_epoch_end"><code>on_epoch_end</code></h3>

``` python
on_epoch_end(
    epoch,
    logs=None
)
```




<h3 id="on_predict_batch_begin"><code>on_predict_batch_begin</code></h3>

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

``` python
on_predict_begin(logs=None)
```

Called at the beginning of prediction.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
  but that may change in the future.

<h3 id="on_predict_end"><code>on_predict_end</code></h3>

``` python
on_predict_end(logs=None)
```

Called at the end of prediction.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
  but that may change in the future.

<h3 id="on_test_batch_begin"><code>on_test_batch_begin</code></h3>

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

``` python
on_test_begin(logs=None)
```

Called at the beginning of evaluation or validation.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
  but that may change in the future.

<h3 id="on_test_end"><code>on_test_end</code></h3>

``` python
on_test_end(logs=None)
```

Called at the end of evaluation or validation.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
  but that may change in the future.

<h3 id="on_train_batch_begin"><code>on_train_batch_begin</code></h3>

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

``` python
on_train_begin(logs=None)
```




<h3 id="on_train_end"><code>on_train_end</code></h3>

``` python
on_train_end(logs=None)
```




<h3 id="set_model"><code>set_model</code></h3>

``` python
set_model(model)
```




<h3 id="set_params"><code>set_params</code></h3>

``` python
set_params(params)
```






