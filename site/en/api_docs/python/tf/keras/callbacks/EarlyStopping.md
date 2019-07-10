page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.callbacks.EarlyStopping

## Class `EarlyStopping`

Inherits From: [`Callback`](../../../tf/keras/callbacks/Callback)



Defined in [`tensorflow/python/keras/callbacks.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/keras/callbacks.py).

Stop training when a monitored quantity has stopped improving.

#### Arguments:

* <b>`monitor`</b>: Quantity to be monitored.
* <b>`min_delta`</b>: Minimum change in the monitored quantity
        to qualify as an improvement, i.e. an absolute
        change of less than min_delta, will count as no
        improvement.
* <b>`patience`</b>: Number of epochs with no improvement
        after which training will be stopped.
* <b>`verbose`</b>: verbosity mode.
* <b>`mode`</b>: One of `{"auto", "min", "max"}`. In `min` mode,
        training will stop when the quantity
        monitored has stopped decreasing; in `max`
        mode it will stop when the quantity
        monitored has stopped increasing; in `auto`
        mode, the direction is automatically inferred
        from the name of the monitored quantity.
* <b>`baseline`</b>: Baseline value for the monitored quantity.
        Training will stop if the model doesn't show improvement over the
        baseline.
* <b>`restore_best_weights`</b>: Whether to restore model weights from
        the epoch with the best value of the monitored quantity.
        If False, the model weights obtained at the last step of
        training are used.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    monitor='val_loss',
    min_delta=0,
    patience=0,
    verbose=0,
    mode='auto',
    baseline=None,
    restore_best_weights=False
)
```

Initialize self.  See help(type(self)) for accurate signature.



## Methods

<h3 id="get_monitor_value"><code>get_monitor_value</code></h3>

``` python
get_monitor_value(logs)
```



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

A backwards compatibility alias for `on_train_batch_end`.

<h3 id="on_epoch_begin"><code>on_epoch_begin</code></h3>

``` python
on_epoch_begin(
    epoch,
    logs=None,
    mode='train'
)
```

Called at the start of an epoch.

Subclasses should override for any actions to run.

#### Arguments:

* <b>`epoch`</b>: integer, index of epoch.
* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
      but that may change in the future.
* <b>`mode`</b>: One of 'train'/'test'/'predict'

<h3 id="on_epoch_end"><code>on_epoch_end</code></h3>

``` python
on_epoch_end(
    epoch,
    logs=None
)
```

Called at the end of an epoch.

Subclasses should override for any actions to run.

#### Arguments:

* <b>`epoch`</b>: integer, index of epoch.
* <b>`logs`</b>: dict, metric results for this training epoch, and for the
      validation epoch if validation is performed. Validation result keys
      are prefixed with `val_`.
* <b>`mode`</b>: One of 'train'/'test'/'predict'

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

Called at the beginning of training.

Subclasses should override for any actions to run.

#### Arguments:

* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
      but that may change in the future.

<h3 id="on_train_end"><code>on_train_end</code></h3>

``` python
on_train_end(logs=None)
```

Called at the end of training.

Subclasses should override for any actions to run.

#### Arguments:

* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
      but that may change in the future.

<h3 id="set_model"><code>set_model</code></h3>

``` python
set_model(model)
```



<h3 id="set_params"><code>set_params</code></h3>

``` python
set_params(params)
```





