

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.optimizers.Adadelta

## Class `Adadelta`

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer)



Defined in [`tensorflow/python/keras/_impl/keras/optimizers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/keras/_impl/keras/optimizers.py).

Adadelta optimizer.

It is recommended to leave the parameters of this optimizer
at their default values.

#### Arguments:

* <b>`lr`</b>: float >= 0. Learning rate.
        It is recommended to leave it at the default value.
* <b>`rho`</b>: float >= 0.
* <b>`epsilon`</b>: float >= 0. Fuzz factor. If `None`, defaults to `K.epsilon()`.
* <b>`decay`</b>: float >= 0. Learning rate decay over each update.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    lr=1.0,
    rho=0.95,
    epsilon=None,
    decay=0.0,
    **kwargs
)
```



<h3 id="from_config"><code>from_config</code></h3>

``` python
from_config(
    cls,
    config
)
```



<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```



<h3 id="get_gradients"><code>get_gradients</code></h3>

``` python
get_gradients(
    loss,
    params
)
```



<h3 id="get_updates"><code>get_updates</code></h3>

``` python
get_updates(
    loss,
    params
)
```



<h3 id="get_weights"><code>get_weights</code></h3>

``` python
get_weights()
```

Returns the current value of the weights of the optimizer.

#### Returns:

A list of numpy arrays.

<h3 id="set_weights"><code>set_weights</code></h3>

``` python
set_weights(weights)
```

Sets the weights of the optimizer, from Numpy arrays.

Should only be called after computing the gradients
(otherwise the optimizer has no weights).

#### Arguments:

* <b>`weights`</b>: a list of Numpy arrays. The number
        of arrays and their shape must match
        number of the dimensions of the weights
        of the optimizer (i.e. it should match the
        output of `get_weights`).


#### Raises:

* <b>`ValueError`</b>: in case of incompatible weight shapes.



