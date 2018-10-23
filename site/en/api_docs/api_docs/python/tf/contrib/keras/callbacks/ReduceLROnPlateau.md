

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.callbacks.ReduceLROnPlateau

## Class `ReduceLROnPlateau`

Inherits From: [`Callback`](../../../../tf/contrib/keras/callbacks/Callback)



Defined in [`tensorflow/contrib/keras/python/keras/callbacks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/callbacks.py).

Reduce learning rate when a metric has stopped improving.

Models often benefit from reducing the learning rate by a factor
of 2-10 once learning stagnates. This callback monitors a
quantity and if no improvement is seen for a 'patience' number
of epochs, the learning rate is reduced.

Example:

```python
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                              patience=5, min_lr=0.001)
model.fit(X_train, Y_train, callbacks=[reduce_lr])
```

#### Arguments:

    monitor: quantity to be monitored.
    factor: factor by which the learning rate will
        be reduced. new_lr = lr * factor
    patience: number of epochs with no improvement
        after which learning rate will be reduced.
    verbose: int. 0: quiet, 1: update messages.
    mode: one of {auto, min, max}. In `min` mode,
        lr will be reduced when the quantity
        monitored has stopped decreasing; in `max`
        mode it will be reduced when the quantity
        monitored has stopped increasing; in `auto`
        mode, the direction is automatically inferred
        from the name of the monitored quantity.
    epsilon: threshold for measuring the new optimum,
        to only focus on significant changes.
    cooldown: number of epochs to wait before resuming
        normal operation after lr has been reduced.
    min_lr: lower bound on the learning rate.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    monitor='val_loss',
    factor=0.1,
    patience=10,
    verbose=0,
    mode='auto',
    epsilon=0.0001,
    cooldown=0,
    min_lr=0
)
```



<h3 id="in_cooldown"><code>in_cooldown</code></h3>

``` python
in_cooldown()
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





