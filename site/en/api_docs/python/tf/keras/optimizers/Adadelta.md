page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.optimizers.Adadelta

## Class `Adadelta`

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer)



Defined in [`tensorflow/python/keras/optimizers.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/keras/optimizers.py).

Adadelta optimizer.

Adadelta is a more robust extension of Adagrad
that adapts learning rates based on a moving window of gradient updates,
instead of accumulating all past gradients. This way, Adadelta continues
learning even when many updates have been done. Compared to Adagrad, in the
original version of Adadelta you don't have to set an initial learning
rate. In this version, initial learning rate and decay factor can
be set, as in most other Keras optimizers.

It is recommended to leave the parameters of this optimizer
at their default values.

# Arguments
    lr: float >= 0. Initial learning rate, defaults to 1.
        It is recommended to leave it at the default value.
    rho: float >= 0. Adadelta decay factor, corresponding to fraction of
        gradient to keep at each time step.
    epsilon: float >= 0. Fuzz factor. If `None`, defaults to `K.epsilon()`.
    decay: float >= 0. Initial learning rate decay.

# References
    - [Adadelta - an adaptive learning rate method](http://arxiv.org/abs/1212.5701)

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    lr=1.0,
    rho=0.95,
    epsilon=None,
    decay=0.0,
    **kwargs
)
```

Initialize self.  See help(type(self)) for accurate signature.



## Methods

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



