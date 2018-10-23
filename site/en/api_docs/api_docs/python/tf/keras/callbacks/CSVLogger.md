

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.callbacks.CSVLogger

## Class `CSVLogger`

Inherits From: [`Callback`](../../../tf/keras/callbacks/Callback)



Defined in [`tensorflow/python/keras/_impl/keras/callbacks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/callbacks.py).

Callback that streams epoch results to a csv file.

Supports all values that can be represented as a string,
including 1D iterables such as np.ndarray.

Example:
    ```python
    csv_logger = CSVLogger('training.log')
    model.fit(X_train, Y_train, callbacks=[csv_logger])
    ```

#### Arguments:

* <b>`filename`</b>: filename of the csv file, e.g. 'run/log.csv'.
* <b>`separator`</b>: string used to separate elements in the csv file.
* <b>`append`</b>: True: append if file exists (useful for continuing
        training). False: overwrite existing file,

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    filename,
    separator=',',
    append=False
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





