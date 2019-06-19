page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.optimizers.Adam

## Class `Adam`

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer)



Defined in [`tensorflow/python/keras/optimizers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/optimizers.py).

Adam optimizer.

Default parameters follow those provided in the original paper.

#### Arguments:

* <b>`lr`</b>: float >= 0. Learning rate.
* <b>`beta_1`</b>: float, 0 < beta < 1. Generally close to 1.
* <b>`beta_2`</b>: float, 0 < beta < 1. Generally close to 1.
* <b>`epsilon`</b>: float >= 0. Fuzz factor. If `None`, defaults to `K.epsilon()`.
* <b>`decay`</b>: float >= 0. Learning rate decay over each update.
* <b>`amsgrad`</b>: boolean. Whether to apply the AMSGrad variant of this
        algorithm from the paper "On the Convergence of Adam and
        Beyond".

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    lr=0.001,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=None,
    decay=0.0,
    amsgrad=False,
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

Returns gradients of `loss` with respect to `params`.

#### Arguments:

* <b>`loss`</b>: Loss tensor.
* <b>`params`</b>: List of variables.


#### Returns:

List of gradient tensors.


#### Raises:

* <b>`ValueError`</b>: In case any gradient cannot be computed (e.g. if gradient
      function not implemented).

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



