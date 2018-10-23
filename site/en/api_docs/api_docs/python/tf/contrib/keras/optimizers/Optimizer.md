

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.optimizers.Optimizer

## Class `Optimizer`





Defined in [`tensorflow/contrib/keras/python/keras/optimizers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/optimizers.py).

Abstract optimizer base class.

Note: this is the parent class of all optimizers, not an actual optimizer
that can be used for training models.

All Keras optimizers support the following keyword arguments:

    clipnorm: float >= 0. Gradients will be clipped
        when their L2 norm exceeds this value.
    clipvalue: float >= 0. Gradients will be clipped
        when their absolute value exceeds this value.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(**kwargs)
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
    params,
    constraints,
    loss
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

    weights: a list of Numpy arrays. The number
        of arrays and their shape must match
        number of the dimensions of the weights
        of the optimizer (i.e. it should match the
        output of `get_weights`).


#### Raises:

    ValueError: in case of incompatible weight shapes.



