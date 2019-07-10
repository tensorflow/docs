page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.callbacks.RemoteMonitor

## Class `RemoteMonitor`

Inherits From: [`Callback`](../../../tf/keras/callbacks/Callback)



Defined in [`tensorflow/python/keras/callbacks.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/keras/callbacks.py).

Callback used to stream events to a server.

Requires the `requests` library.
Events are sent to `root + '/publish/epoch/end/'` by default. Calls are
HTTP POST, with a `data` argument which is a
JSON-encoded dictionary of event data.
If send_as_json is set to True, the content type of the request will be
application/json. Otherwise the serialized JSON will be sent within a form.

#### Arguments:

* <b>`root`</b>: String; root url of the target server.
* <b>`path`</b>: String; path relative to `root` to which the events will be sent.
* <b>`field`</b>: String; JSON field under which the data will be stored.
        The field is used only if the payload is sent within a form
        (i.e. send_as_json is set to False).
* <b>`headers`</b>: Dictionary; optional custom HTTP headers.
* <b>`send_as_json`</b>: Boolean; whether the request should be
        sent as application/json.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    root='http://localhost:9000',
    path='/publish/epoch/end/',
    field='data',
    headers=None,
    send_as_json=False
)
```

Initialize self.  See help(type(self)) for accurate signature.



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





