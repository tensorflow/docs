page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.callbacks.EarlyStopping


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L1134-L1251">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `EarlyStopping`

Stop training when a monitored quantity has stopped improving.

Inherits From: [`Callback`](../../../tf/keras/callbacks/Callback)

### Aliases:

* Class `tf.compat.v1.keras.callbacks.EarlyStopping`
* Class `tf.compat.v2.keras.callbacks.EarlyStopping`


### Used in the guide:

* [Keras overview](https://www.tensorflow.org/guide/keras/overview)
* [Train and evaluate with Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate)

### Used in the tutorials:

* [Basic regression: Predict fuel efficiency](https://www.tensorflow.org/tutorials/keras/regression)




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


#### Example:



```python
callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)
# This callback will stop the training when there is no improvement in
# the validation loss for three consecutive epochs.
model.fit(data, labels, epochs=100, callbacks=[callback],
    validation_data=(val_data, val_labels))
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L1172-L1210">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L1244-L1251">View source</a>

``` python
get_monitor_value(logs)
```




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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L467-L468">View source</a>

``` python
on_batch_end(
    batch,
    logs=None
)
```

A backwards compatibility alias for `on_train_batch_end`.


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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L1221-L1238">View source</a>

``` python
on_epoch_end(
    epoch,
    logs=None
)
```

Called at the end of an epoch.

Subclasses should override for any actions to run. This function should only
be called during TRAIN mode.

#### Arguments:


* <b>`epoch`</b>: integer, index of epoch.
* <b>`logs`</b>: dict, metric results for this training epoch, and for the
  validation epoch if validation is performed. Validation result keys
  are prefixed with `val_`.

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L1212-L1219">View source</a>

``` python
on_train_begin(logs=None)
```

Called at the beginning of training.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
  but that may change in the future.

<h3 id="on_train_end"><code>on_train_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L1240-L1242">View source</a>

``` python
on_train_end(logs=None)
```

Called at the end of training.

Subclasses should override for any actions to run.

#### Arguments:


* <b>`logs`</b>: dict. Currently no data is passed to this argument for this method
  but that may change in the future.

<h3 id="set_model"><code>set_model</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L461-L462">View source</a>

``` python
set_model(model)
```




<h3 id="set_params"><code>set_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/callbacks.py#L458-L459">View source</a>

``` python
set_params(params)
```
