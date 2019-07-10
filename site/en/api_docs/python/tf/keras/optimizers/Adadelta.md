page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.optimizers.Adadelta

## Class `Adadelta`

Optimizer that implements the Adadelta algorithm.

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer)

### Aliases:

* Class `tf.compat.v1.keras.optimizers.Adadelta`
* Class `tf.compat.v2.keras.optimizers.Adadelta`
* Class `tf.compat.v2.optimizers.Adadelta`
* Class `tf.keras.optimizers.Adadelta`



Defined in [`python/keras/optimizer_v2/adadelta.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/optimizer_v2/adadelta.py).

<!-- Placeholder for "Used in" -->

Adadelta optimization is a stochastic gradient descent method that is based on
adaptive learning rate per dimension to address two drawbacks:
  1) the continual decay of learning rates throughout training
  2) the need for a manually selected global learning rate

Two accumulation steps are required:
  1) the accumulation of gradients squared,
  2) the accumulation of updates squared.

#### Initialization:



<div> $$E[g^2]_0 := 0 \text{(Initialize gradient 2nd order moment vector)}$$ </div>
<div> $$E[\Delta x^2]_0 := 0 \text{(Initialize 2nd order variable update)}$$ </div>

<div> $$t := t + 1$$ </div>
<div> $$E[g^2]_t := \rho * E[g^2]_{t-1} + (1 - \rho) * g^2$$ </div>
<div> $$\Delta x_t = -RMS[\Delta x]_{t-1} * g_t / RMS[g]_t$$ </div>
<div> $$E[\Delta x^2]_t := \rho * E[\Delta x^2]_{t-1} + (1 - \rho) * \Delta x_t^2$$ </div>
<div> $$x_t := x_{t-1} + \Delta x_{t}

References
  See [M. D. Zeiler](http://arxiv.org/abs/1212.5701)
    ([pdf](http://arxiv.org/pdf/1212.5701v1.pdf))

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    learning_rate=0.001,
    rho=0.95,
    epsilon=1e-07,
    name='Adadelta',
    **kwargs
)
```

Construct a new Adadelta optimizer.

Adadelta is a more robust extension of Adagrad that adapts learning rates
based on a moving window of gradient updates, instead of accumulating all
past gradients. This way, Adadelta continues learning even when many updates
have been done. Compared to Adagrad, in the original version of Adadelta you
don't have to set an initial learning rate. In this version, initial
learning rate can be set, as in most other Keras optimizers.

#### Args:


* <b>`learning_rate`</b>: A `Tensor` or a floating point value. The learning rate.
  To match the exact form in the original paper use 1.0.
* <b>`rho`</b>: A `Tensor` or a floating point value. The decay rate.
* <b>`epsilon`</b>: A `Tensor` or a floating point value.  A constant epsilon used
         to better conditioning the grad update.
* <b>`name`</b>: Optional name prefix for the operations created when applying
  gradients.  Defaults to "Adadelta".
* <b>`**kwargs`</b>: keyword arguments. Allowed to be {`clipnorm`, `clipvalue`, `lr`,
  `decay`}. `clipnorm` is clip gradients by norm; `clipvalue` is clip
  gradients by value, `decay` is included for backward compatibility to
  allow time inverse decay of learning rate. `lr` is included for backward
  compatibility, recommended to use `learning_rate` instead.



#### Eager Compatibility
When eager execution is enabled, `learning_rate`, `rho`, and `epsilon` can
each be a callable that takes no arguments and returns the actual value to
use. This can be useful for changing these values across different
invocations of optimizer functions.





## Properties

<h3 id="iterations"><code>iterations</code></h3>

Variable. The number of training steps this Optimizer has run.


<h3 id="weights"><code>weights</code></h3>

Returns variables of this Optimizer based on the order created.




## Methods

<h3 id="add_slot"><code>add_slot</code></h3>

``` python
add_slot(
    var,
    slot_name,
    initializer='zeros'
)
```

Add a new slot variable for `var`.


<h3 id="add_weight"><code>add_weight</code></h3>

``` python
add_weight(
    name,
    shape,
    dtype=None,
    initializer='zeros',
    trainable=None,
    synchronization=tf.VariableSynchronization.AUTO,
    aggregation=tf.VariableAggregation.NONE
)
```




<h3 id="apply_gradients"><code>apply_gradients</code></h3>

``` python
apply_gradients(
    grads_and_vars,
    name=None
)
```

Apply gradients to variables.

This is the second part of `minimize()`. It returns an `Operation` that
applies gradients.

#### Args:


* <b>`grads_and_vars`</b>: List of (gradient, variable) pairs.
* <b>`name`</b>: Optional name for the returned operation.  Default to the name
  passed to the `Optimizer` constructor.


#### Returns:

An `Operation` that applies the specified gradients. If `global_step`
was not None, that operation also increments `global_step`.



#### Raises:


* <b>`TypeError`</b>: If `grads_and_vars` is malformed.
* <b>`ValueError`</b>: If none of the variables have gradients.

<h3 id="from_config"><code>from_config</code></h3>

``` python
from_config(
    cls,
    config,
    custom_objects=None
)
```

Creates an optimizer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same optimizer from the config
dictionary.

#### Arguments:


* <b>`config`</b>: A Python dictionary, typically the output of get_config.
* <b>`custom_objects`</b>: A Python dictionary mapping names to additional Python
  objects used to create this optimizer, such as a function used for a
  hyperparameter.


#### Returns:

An optimizer instance.


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

<h3 id="get_slot"><code>get_slot</code></h3>

``` python
get_slot(
    var,
    slot_name
)
```




<h3 id="get_slot_names"><code>get_slot_names</code></h3>

``` python
get_slot_names()
```

A list of names for this optimizer's slots.


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




<h3 id="minimize"><code>minimize</code></h3>

``` python
minimize(
    loss,
    var_list,
    grad_loss=None,
    name=None
)
```

Minimize `loss` by updating `var_list`.

This method simply computes gradient using <a href="../../../tf/GradientTape"><code>tf.GradientTape</code></a> and calls
`apply_gradients()`. If you want to process the gradient before applying
then call <a href="../../../tf/GradientTape"><code>tf.GradientTape</code></a> and `apply_gradients()` explicitly instead
of using this function.

#### Args:


* <b>`loss`</b>: A callable taking no arguments which returns the value to minimize.
* <b>`var_list`</b>: list or tuple of `Variable` objects to update to minimize
  `loss`, or a callable returning the list or tuple of `Variable` objects.
  Use callable when the variable list would otherwise be incomplete before
  `minimize` since the variables are created at the first time `loss` is
  called.
* <b>`grad_loss`</b>: Optional. A `Tensor` holding the gradient computed for `loss`.
* <b>`name`</b>: Optional name for the returned operation.


#### Returns:

An Operation that updates the variables in `var_list`.  If `global_step`
was not `None`, that operation also increments `global_step`.



#### Raises:


* <b>`ValueError`</b>: If some of the variables are not `Variable` objects.

<h3 id="set_weights"><code>set_weights</code></h3>

``` python
set_weights(weights)
```




<h3 id="variables"><code>variables</code></h3>

``` python
variables()
```

Returns variables of this Optimizer based on the order created.




