page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ConditionalAccumulatorBase


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/data_flow_ops.py#L1163-L1249">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ConditionalAccumulatorBase`

A conditional accumulator for aggregating gradients.



### Aliases:

* Class <a href="/api_docs/python/tf/ConditionalAccumulatorBase"><code>tf.compat.v1.ConditionalAccumulatorBase</code></a>


<!-- Placeholder for "Used in" -->

Up-to-date gradients (i.e., time step at which gradient was computed is
equal to the accumulator's time step) are added to the accumulator.

Extraction of the average gradient is blocked until the required number of
gradients has been accumulated.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/data_flow_ops.py#L1173-L1191">View source</a>

``` python
__init__(
    dtype,
    shape,
    accumulator_ref
)
```

Creates a new ConditionalAccumulator.


#### Args:


* <b>`dtype`</b>: Datatype of the accumulated gradients.
* <b>`shape`</b>: Shape of the accumulated gradients.
* <b>`accumulator_ref`</b>: A handle to the conditional accumulator, created by sub-
  classes



## Properties

<h3 id="accumulator_ref"><code>accumulator_ref</code></h3>

The underlying accumulator reference.


<h3 id="dtype"><code>dtype</code></h3>

The datatype of the gradients accumulated by this accumulator.


<h3 id="name"><code>name</code></h3>

The name of the underlying accumulator.




## Methods

<h3 id="num_accumulated"><code>num_accumulated</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/data_flow_ops.py#L1208-L1225">View source</a>

``` python
num_accumulated(name=None)
```

Number of gradients that have currently been aggregated in accumulator.


#### Args:


* <b>`name`</b>: Optional name for the operation.


#### Returns:

Number of accumulated gradients currently in accumulator.


<h3 id="set_global_step"><code>set_global_step</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/data_flow_ops.py#L1227-L1249">View source</a>

``` python
set_global_step(
    new_global_step,
    name=None
)
```

Sets the global time step of the accumulator.

The operation logs a warning if we attempt to set to a time step that is
lower than the accumulator's own time step.

#### Args:


* <b>`new_global_step`</b>: Value of new time step. Can be a variable or a constant
* <b>`name`</b>: Optional name for the operation.


#### Returns:

Operation that sets the accumulator's time step.
