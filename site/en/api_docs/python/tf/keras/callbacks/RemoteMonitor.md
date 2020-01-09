page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.callbacks.RemoteMonitor

## Class `RemoteMonitor`

Inherits From: [`Callback`](../../../tf/keras/callbacks/Callback)



Defined in [`tensorflow/python/keras/callbacks.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/keras/callbacks.py).

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





## Methods

<h3 id="on_batch_begin"><code>on_batch_begin</code></h3>

``` python
on_batch_begin(
    batch,
    logs=None
)
```



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





