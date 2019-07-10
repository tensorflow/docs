page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.SparseConditionalAccumulator

## Class `SparseConditionalAccumulator`

A conditional accumulator for aggregating sparse gradients.

Inherits From: [`ConditionalAccumulatorBase`](../../tf/ConditionalAccumulatorBase)

### Aliases:

* Class `tf.SparseConditionalAccumulator`
* Class `tf.compat.v1.SparseConditionalAccumulator`
* Class `tf.compat.v1.sparse.SparseConditionalAccumulator`
* Class `tf.sparse.SparseConditionalAccumulator`



Defined in [`python/ops/data_flow_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/data_flow_ops.py).

<!-- Placeholder for "Used in" -->

Sparse gradients are represented by `IndexedSlices`.

Up-to-date gradients (i.e., time step at which gradient was computed is
equal to the accumulator's time step) are added to the accumulator.

Extraction of the average gradient is blocked until the required number of
gradients has been accumulated.

#### Args:


* <b>`dtype`</b>: Datatype of the accumulated gradients.
* <b>`shape`</b>: Shape of the accumulated gradients.
* <b>`shared_name`</b>: Optional. If non-empty, this accumulator will be shared under
  the given name across multiple sessions.
* <b>`name`</b>: Optional name for the accumulator.
* <b>`reduction_type`</b>: Reduction type to use when taking the gradient.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    dtype,
    shape=None,
    shared_name=None,
    name='sparse_conditional_accumulator',
    reduction_type='MEAN'
)
```






## Properties

<h3 id="accumulator_ref"><code>accumulator_ref</code></h3>

The underlying accumulator reference.


<h3 id="dtype"><code>dtype</code></h3>

The datatype of the gradients accumulated by this accumulator.


<h3 id="name"><code>name</code></h3>

The name of the underlying accumulator.




## Methods

<h3 id="apply_grad"><code>apply_grad</code></h3>

``` python
apply_grad(
    grad_indices,
    grad_values,
    grad_shape=None,
    local_step=0,
    name=None
)
```

Attempts to apply a sparse gradient to the accumulator.

The attempt is silently dropped if the gradient is stale, i.e., `local_step`
is less than the accumulator's global time step.

A sparse gradient is represented by its indices, values and possibly empty
or None shape. Indices must be a vector representing the locations of
non-zero entries in the tensor. Values are the non-zero slices of the
gradient, and must have the same first dimension as indices, i.e., the nnz
represented by indices and values must be consistent. Shape, if not empty or
None, must be consistent with the accumulator's shape (if also provided).

#### Example:

A tensor [[0, 0], [0, 1], [2, 3]] can be represented
  indices: [1,2]
  values: [[0,1],[2,3]]
  shape: [3, 2]



#### Args:


* <b>`grad_indices`</b>: Indices of the sparse gradient to be applied.
* <b>`grad_values`</b>: Values of the sparse gradient to be applied.
* <b>`grad_shape`</b>: Shape of the sparse gradient to be applied.
* <b>`local_step`</b>: Time step at which the gradient was computed.
* <b>`name`</b>: Optional name for the operation.


#### Returns:

The operation that (conditionally) applies a gradient to the accumulator.



#### Raises:


* <b>`InvalidArgumentError`</b>: If grad is of the wrong shape

<h3 id="apply_indexed_slices_grad"><code>apply_indexed_slices_grad</code></h3>

``` python
apply_indexed_slices_grad(
    grad,
    local_step=0,
    name=None
)
```

Attempts to apply a gradient to the accumulator.

The attempt is silently dropped if the gradient is stale, i.e., `local_step`
is less than the accumulator's global time step.

#### Args:


* <b>`grad`</b>: The gradient `IndexedSlices` to be applied.
* <b>`local_step`</b>: Time step at which the gradient was computed.
* <b>`name`</b>: Optional name for the operation.


#### Returns:

The operation that (conditionally) applies a gradient to the accumulator.



#### Raises:


* <b>`InvalidArgumentError`</b>: If grad is of the wrong shape

<h3 id="num_accumulated"><code>num_accumulated</code></h3>

``` python
num_accumulated(name=None)
```

Number of gradients that have currently been aggregated in accumulator.


#### Args:


* <b>`name`</b>: Optional name for the operation.


#### Returns:

Number of accumulated gradients currently in accumulator.


<h3 id="set_global_step"><code>set_global_step</code></h3>

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


<h3 id="take_grad"><code>take_grad</code></h3>

``` python
take_grad(
    num_required,
    name=None
)
```

Attempts to extract the average gradient from the accumulator.

The operation blocks until sufficient number of gradients have been
successfully applied to the accumulator.

Once successful, the following actions are also triggered:
- Counter of accumulated gradients is reset to 0.
- Aggregated gradient is reset to 0 tensor.
- Accumulator's internal time step is incremented by 1.

#### Args:


* <b>`num_required`</b>: Number of gradients that needs to have been aggregated
* <b>`name`</b>: Optional name for the operation


#### Returns:

A tuple of indices, values, and shape representing the average gradient.



#### Raises:


* <b>`InvalidArgumentError`</b>: If `num_required` < 1

<h3 id="take_indexed_slices_grad"><code>take_indexed_slices_grad</code></h3>

``` python
take_indexed_slices_grad(
    num_required,
    name=None
)
```

Attempts to extract the average gradient from the accumulator.

The operation blocks until sufficient number of gradients have been
successfully applied to the accumulator.

Once successful, the following actions are also triggered:
- Counter of accumulated gradients is reset to 0.
- Aggregated gradient is reset to 0 tensor.
- Accumulator's internal time step is incremented by 1.

#### Args:


* <b>`num_required`</b>: Number of gradients that needs to have been aggregated
* <b>`name`</b>: Optional name for the operation


#### Returns:

An `IndexedSlices` holding the value of the average gradient.



#### Raises:


* <b>`InvalidArgumentError`</b>: If `num_required` < 1



