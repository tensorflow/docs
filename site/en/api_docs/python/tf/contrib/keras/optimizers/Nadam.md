

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.optimizers.Nadam

### `class tf.contrib.keras.optimizers.Nadam`



Defined in [`tensorflow/contrib/keras/python/keras/optimizers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/optimizers.py).

Nesterov Adam optimizer.

Much like Adam is essentially RMSprop with momentum,
Nadam is Adam RMSprop with Nesterov momentum.

Default parameters follow those provided in the paper.
It is recommended to leave the parameters of this optimizer
at their default values.

#### Arguments:

    lr: float >= 0. Learning rate.
    beta_1/beta_2: floats, 0 < beta < 1. Generally close to 1.
    epsilon: float >= 0. Fuzz factor.

References:
    - [Nadam report](http://cs229.stanford.edu/proj2015/054_report.pdf)
    - [On the importance of initialization and momentum in deep
      learning](http://www.cs.toronto.edu/~fritz/absps/momentum.pdf)

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    lr=0.002,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-08,
    schedule_decay=0.004,
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



