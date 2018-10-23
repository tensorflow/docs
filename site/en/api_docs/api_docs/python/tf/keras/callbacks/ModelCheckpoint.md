

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.callbacks.ModelCheckpoint

## Class `ModelCheckpoint`

Inherits From: [`Callback`](../../../tf/keras/callbacks/Callback)



Defined in [`tensorflow/python/keras/_impl/keras/callbacks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/callbacks.py).

Save the model after every epoch.

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
* <b>`save_best_only`</b>: if `save_best_only=True`,
        the latest best model according to
        the quantity monitored will not be overwritten.
* <b>`mode`</b>: one of {auto, min, max}.
        If `save_best_only=True`, the decision
        to overwrite the current save file is made
        based on either the maximization or the
        minimization of the monitored quantity. For `val_acc`,
        this should be `max`, for `val_loss` this should
        be `min`, etc. In `auto` mode, the direction is
        automatically inferred from the name of the monitored quantity.
* <b>`save_weights_only`</b>: if True, then only the model's weights will be
        saved (`model.save_weights(filepath)`), else the full model
        is saved (`model.save(filepath)`).
* <b>`period`</b>: Interval (number of epochs) between checkpoints.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    filepath,
    monitor='val_loss',
    verbose=0,
    save_best_only=False,
    save_weights_only=False,
    mode='auto',
    period=1
)
```



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





