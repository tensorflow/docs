page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.optimizers.Adagrad


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/adagrad.py#L38-L206">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Adagrad`

Optimizer that implements the Adagrad algorithm.

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer)

### Aliases:

* Class `tf.compat.v1.keras.optimizers.Adagrad`
* Class `tf.compat.v2.keras.optimizers.Adagrad`
* Class `tf.compat.v2.optimizers.Adagrad`
* Class `tf.optimizers.Adagrad`


<!-- Placeholder for "Used in" -->

Adagrad is an optimizer with parameter-specific learning rates,
which are adapted relative to how frequently a parameter gets
updated during training. The more updates a parameter receives,
the smaller the updates.

#### Initialization:


<div> $$accum_{g_0} := \text{initial_accumulator_value}$$ </div>

#### Update step:


<div> $$t := t + 1$$ </div>
<div> $$accum_{g_t} := accum_{g_{t-1}} + g^2$$ </div>
<div> $$\theta_t := \theta_{t-1} - lr * g / (\sqrt{accum_{g_t}} + \epsilon)$$ </div>

#### References:



* [Paper](http://www.jmlr.org/papers/volume12/duchi11a/duchi11a.pdf).
* [Introduction]
  (https://ppasupat.github.io/a9online/uploads/proximal_notes.pdf).

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/adagrad.py#L61-L102">View source</a>

``` python
__init__(
    learning_rate=0.001,
    initial_accumulator_value=0.1,
    epsilon=1e-07,
    name='Adagrad',
    **kwargs
)
```

Construct a new Adagrad optimizer.


#### Args:


* <b>`learning_rate`</b>: A `Tensor` or a floating point value.  The learning rate.
* <b>`initial_accumulator_value`</b>: A floating point value.
  Starting value for the accumulators, must be positive.
* <b>`epsilon`</b>: A floating point value.
  Starting value for the accumulators, must be positive.
* <b>`name`</b>: Optional name prefix for the operations created when applying
  gradients.  Defaults to "Adagrad".
* <b>`**kwargs`</b>: keyword arguments. Allowed to be {`clipnorm`, `clipvalue`, `lr`,
  `decay`}. `clipnorm` is clip gradients by norm; `clipvalue` is clip
  gradients by value, `decay` is included for backward compatibility to
  allow time inverse decay of learning rate. `lr` is included for backward
  compatibility, recommended to use `learning_rate` instead.


#### Raises:


* <b>`ValueError`</b>: If the `initial_accumulator_value` or `epsilon` is invalid.



#### Eager Compatibility
When eager execution is enabled, `learning_rate` can be a callable that
takes no arguments and returns the actual value to use. This can be useful
for changing these values across different invocations of optimizer
functions.





## Properties

<h3 id="iterations"><code>iterations</code></h3>

Variable. The number of training steps this Optimizer has run.


<h3 id="weights"><code>weights</code></h3>

Returns variables of this Optimizer based on the order created.




## Methods

<h3 id="add_slot"><code>add_slot</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L567-L594">View source</a>

``` python
add_slot(
    var,
    slot_name,
    initializer='zeros'
)
```

Add a new slot variable for `var`.


<h3 id="add_weight"><code>add_weight</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L768-L808">View source</a>

``` python
add_weight(
    name,
    shape,
    dtype=None,
    initializer='zeros',
    trainable=None,
    synchronization=tf.VariableSynchronization.AUTO,
    aggregation=tf.compat.v1.VariableAggregation.NONE
)
```




<h3 id="apply_gradients"><code>apply_gradients</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L408-L441">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/adagrad.py#L128-L149">View source</a>

``` python
@classmethod
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/adagrad.py#L198-L206">View source</a>

``` python
get_config()
```

Returns the config of the optimimizer.

An optimizer config is a Python dictionary (serializable)
containing the configuration of an optimizer.
The same optimizer can be reinstantiated later
(without any saved state) from this configuration.

#### Returns:

Python dictionary.


<h3 id="get_gradients"><code>get_gradients</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L374-L406">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L596-L599">View source</a>

``` python
get_slot(
    var,
    slot_name
)
```




<h3 id="get_slot_names"><code>get_slot_names</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L563-L565">View source</a>

``` python
get_slot_names()
```

A list of names for this optimizer's slots.


<h3 id="get_updates"><code>get_updates</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L499-L506">View source</a>

``` python
get_updates(
    loss,
    params
)
```




<h3 id="get_weights"><code>get_weights</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L743-L745">View source</a>

``` python
get_weights()
```




<h3 id="minimize"><code>minimize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L290-L319">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/adagrad.py#L119-L126">View source</a>

``` python
set_weights(weights)
```




<h3 id="variables"><code>variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L734-L736">View source</a>

``` python
variables()
```

Returns variables of this Optimizer based on the order created.
