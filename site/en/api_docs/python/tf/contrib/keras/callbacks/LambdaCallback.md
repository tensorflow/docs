

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.callbacks.LambdaCallback

### `class tf.contrib.keras.callbacks.LambdaCallback`



Defined in [`tensorflow/contrib/keras/python/keras/callbacks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/callbacks.py).

Callback for creating simple, custom callbacks on-the-fly.

This callback is constructed with anonymous functions that will be called
at the appropriate time. Note that the callbacks expects positional
arguments, as:
 - `on_epoch_begin` and `on_epoch_end` expect two positional arguments:
    `epoch`, `logs`
 - `on_batch_begin` and `on_batch_end` expect two positional arguments:
    `batch`, `logs`
 - `on_train_begin` and `on_train_end` expect one positional argument:
    `logs`

#### Arguments:

    on_epoch_begin: called at the beginning of every epoch.
    on_epoch_end: called at the end of every epoch.
    on_batch_begin: called at the beginning of every batch.
    on_batch_end: called at the end of every batch.
    on_train_begin: called at the beginning of model training.
    on_train_end: called at the end of model training.

Example:

    ```python
    # Print the batch number at the beginning of every batch.
    batch_print_callback = LambdaCallback(
        on_batch_begin=lambda batch,logs: print(batch))

    # Plot the loss after every epoch.
    import numpy as np
    import matplotlib.pyplot as plt
    plot_loss_callback = LambdaCallback(
        on_epoch_end=lambda epoch, logs: plt.plot(np.arange(epoch),
                                                  logs['loss']))

    # Terminate some processes after having finished model training.
    processes = ...
    cleanup_callback = LambdaCallback(
        on_train_end=lambda logs: [
            p.terminate() for p in processes if p.is_alive()])

    model.fit(...,
              callbacks=[batch_print_callback,
                         plot_loss_callback,
                         cleanup_callback])
    ```

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    on_epoch_begin=None,
    on_epoch_end=None,
    on_batch_begin=None,
    on_batch_end=None,
    on_train_begin=None,
    on_train_end=None,
    **kwargs
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





