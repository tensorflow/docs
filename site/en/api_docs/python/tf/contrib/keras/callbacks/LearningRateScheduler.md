

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.callbacks.LearningRateScheduler

### `class tf.contrib.keras.callbacks.LearningRateScheduler`



Defined in [`tensorflow/contrib/keras/python/keras/callbacks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/callbacks.py).

Learning rate scheduler.

#### Arguments:

    schedule: a function that takes an epoch index as input
        (integer, indexed from 0) and returns a new
        learning rate as output (float).

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(schedule)
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





