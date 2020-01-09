page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.optimizers.Adam


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/optimizers/Adam">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/adam.py#L32-L274">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Adam`

Optimizer that implements the Adam algorithm.

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/optimizers/Adam"><code>tf.compat.v1.keras.optimizers.Adam</code></a>
* Class <a href="/api_docs/python/tf/keras/optimizers/Adam"><code>tf.compat.v2.keras.optimizers.Adam</code></a>
* Class <a href="/api_docs/python/tf/keras/optimizers/Adam"><code>tf.compat.v2.optimizers.Adam</code></a>


<!-- Placeholder for "Used in" -->

Adam optimization is a stochastic gradient descent method that is based on
adaptive estimation of first-order and second-order moments.
According to the paper
[Adam: A Method for Stochastic Optimization. Kingma et al.,
2014](http://arxiv.org/abs/1412.6980),
 the method is "*computationally efficient, has little memory
requirement, invariant to diagonal rescaling of gradients, and is well suited
for problems that are large in terms of data/parameters*".

For AMSGrad see [On The Convergence Of Adam And Beyond.
Reddi et al., 5-8](https://openreview.net/pdf?id=ryQu7f-RZ).

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/adam.py#L48-L143">View source</a>

``` python
__init__(
    learning_rate=0.001,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-07,
    amsgrad=False,
    name='Adam',
    **kwargs
)
```

Construct a new Adam optimizer.

If amsgrad = False:
  Initialization:

  <div> $$m_0 := 0 \text{(Initialize initial 1st moment vector)}$$ </div>
  <div> $$v_0 := 0 \text{(Initialize initial 2nd moment vector)}$$ </div>
  <div> $$t := 0 \text{(Initialize timestep)}$$ </div>

  The update rule for `variable` with gradient `g` uses an optimization
  described at the end of section 2 of the paper:

  <div> $$t := t + 1$$ </div>
  <div> $$lr_t := \text{learning\_rate} * \sqrt{1 - beta_2^t} / (1 - beta_1^t)$$ </div>

  <div> $$m_t := beta_1 * m_{t-1} + (1 - beta_1) * g$$ </div>
  <div> $$v_t := beta_2 * v_{t-1} + (1 - beta_2) * g * g$$ </div>
  <div> $$variable := variable - lr_t * m_t / (\sqrt{v_t} + \epsilon)$$ </div>

If amsgrad = True:
  Initialization:

  <div> $$m_0 := 0 \text{(Initialize initial 1st moment vector)}$$ </div>
  <div> $$v_0 := 0 \text{(Initialize initial 2nd moment vector)}$$ </div>
  <div> $$v_hat_0 := 0 \text{(Initialize initial 2nd moment vector)}$$ </div>
  <div> $$t := 0 \text{(Initialize timestep)}$$ </div>

  The update rule for `variable` with gradient `g` uses an optimization
  described at the end of section 2 of the paper:

  <div> $$t := t + 1$$ </div>
  <div> $$lr_t := \text{learning\_rate} * \sqrt{1 - beta_2^t} / (1 - beta_1^t)$$ </div>

  <div> $$m_t := beta_1 * m_{t-1} + (1 - beta_1) * g$$ </div>
  <div> $$v_t := beta_2 * v_{t-1} + (1 - beta_2) * g * g$$ </div>
  <div> $$v_hat_t := max(v_hat_{t-1}, v_t)$$ </div>
  <div> $$variable := variable - lr_t * m_t / (\sqrt{v_hat_t} + \epsilon)$$ </div>

The default value of 1e-7 for epsilon might not be a good default in
general. For example, when training an Inception network on ImageNet a
current good choice is 1.0 or 0.1. Note that since AdamOptimizer uses the
formulation just before Section 2.1 of the Kingma and Ba paper rather than
the formulation in Algorithm 1, the "epsilon" referred to here is "epsilon
hat" in the paper.

The sparse implementation of this algorithm (used when the gradient is an
IndexedSlices object, typically because of <a href="../../../tf/gather"><code>tf.gather</code></a> or an embedding
lookup in the forward pass) does apply momentum to variable slices even if
they were not used in the forward pass (meaning they have a gradient equal
to zero). Momentum decay (beta1) is also applied to the entire momentum
accumulator. This means that the sparse behavior is equivalent to the dense
behavior (in contrast to some momentum implementations which ignore momentum
unless a variable slice was actually used).

#### Args:


* <b>`learning_rate`</b>: A Tensor or a floating point value.  The learning rate.
* <b>`beta_1`</b>: A float value or a constant float tensor. The exponential decay
  rate for the 1st moment estimates.
* <b>`beta_2`</b>: A float value or a constant float tensor. The exponential decay
  rate for the 2nd moment estimates.
* <b>`epsilon`</b>: A small constant for numerical stability. This epsilon is
  "epsilon hat" in the Kingma and Ba paper (in the formula just before
  Section 2.1), not the epsilon in Algorithm 1 of the paper.
* <b>`amsgrad`</b>: boolean. Whether to apply AMSGrad variant of this algorithm from
  the paper "On the Convergence of Adam and beyond".
* <b>`name`</b>: Optional name for the operations created when applying gradients.
  Defaults to "Adam".
* <b>`**kwargs`</b>: keyword arguments. Allowed to be {`clipnorm`, `clipvalue`, `lr`,
  `decay`}. `clipnorm` is clip gradients by norm; `clipvalue` is clip
  gradients by value, `decay` is included for backward compatibility to
  allow time inverse decay of learning rate. `lr` is included for backward
  compatibility, recommended to use `learning_rate` instead.



#### Eager Compatibility
When eager execution is enabled, `learning_rate`, `beta_1`, `beta_2`,
and `epsilon` can each be a callable that takes no arguments and
returns the actual value to use. This can be useful for changing these
values across different invocations of optimizer functions.





## Properties

<h3 id="iterations"><code>iterations</code></h3>

Variable. The number of training steps this Optimizer has run.


<h3 id="weights"><code>weights</code></h3>

Returns variables of this Optimizer based on the order created.




## Methods

<h3 id="add_slot"><code>add_slot</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L565-L592">View source</a>

``` python
add_slot(
    var,
    slot_name,
    initializer='zeros'
)
```

Add a new slot variable for `var`.


<h3 id="add_weight"><code>add_weight</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L766-L806">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L406-L439">View source</a>

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

An `Operation` that applies the specified gradients. The `iterations`
  will be automatically increased by 1.



#### Raises:


* <b>`TypeError`</b>: If `grads_and_vars` is malformed.
* <b>`ValueError`</b>: If none of the variables have gradients.

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L696-L719">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/adam.py#L264-L274">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L372-L404">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L594-L597">View source</a>

``` python
get_slot(
    var,
    slot_name
)
```




<h3 id="get_slot_names"><code>get_slot_names</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L561-L563">View source</a>

``` python
get_slot_names()
```

A list of names for this optimizer's slots.


<h3 id="get_updates"><code>get_updates</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L497-L504">View source</a>

``` python
get_updates(
    loss,
    params
)
```




<h3 id="get_weights"><code>get_weights</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L741-L743">View source</a>

``` python
get_weights()
```




<h3 id="minimize"><code>minimize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L288-L317">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/adam.py#L177-L185">View source</a>

``` python
set_weights(weights)
```




<h3 id="variables"><code>variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/optimizer_v2.py#L732-L734">View source</a>

``` python
variables()
```

Returns variables of this Optimizer based on the order created.
