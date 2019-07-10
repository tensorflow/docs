page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.SimpleRNNCell

## Class `SimpleRNNCell`

Cell class for SimpleRNN.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.SimpleRNNCell`
* Class `tf.compat.v2.keras.layers.SimpleRNNCell`
* Class `tf.keras.layers.SimpleRNNCell`



Defined in [`python/keras/layers/recurrent.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/recurrent.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`units`</b>: Positive integer, dimensionality of the output space.
* <b>`activation`</b>: Activation function to use.
  Default: hyperbolic tangent (`tanh`).
  If you pass `None`, no activation is applied
  (ie. "linear" activation: `a(x) = x`).
* <b>`use_bias`</b>: Boolean, whether the layer uses a bias vector.
* <b>`kernel_initializer`</b>: Initializer for the `kernel` weights matrix,
  used for the linear transformation of the inputs.
* <b>`recurrent_initializer`</b>: Initializer for the `recurrent_kernel`
  weights matrix, used for the linear transformation of the recurrent state.
* <b>`bias_initializer`</b>: Initializer for the bias vector.
* <b>`kernel_regularizer`</b>: Regularizer function applied to
  the `kernel` weights matrix.
* <b>`recurrent_regularizer`</b>: Regularizer function applied to
  the `recurrent_kernel` weights matrix.
* <b>`bias_regularizer`</b>: Regularizer function applied to the bias vector.
* <b>`kernel_constraint`</b>: Constraint function applied to
  the `kernel` weights matrix.
* <b>`recurrent_constraint`</b>: Constraint function applied to
  the `recurrent_kernel` weights matrix.
* <b>`bias_constraint`</b>: Constraint function applied to the bias vector.
* <b>`dropout`</b>: Float between 0 and 1.
  Fraction of the units to drop for
  the linear transformation of the inputs.
* <b>`recurrent_dropout`</b>: Float between 0 and 1.
  Fraction of the units to drop for
  the linear transformation of the recurrent state.


#### Call arguments:


* <b>`inputs`</b>: A 2D tensor.
* <b>`states`</b>: List of state tensors corresponding to the previous timestep.
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode or in inference mode. Only relevant when `dropout` or
  `recurrent_dropout` is used.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    units,
    activation='tanh',
    use_bias=True,
    kernel_initializer='glorot_uniform',
    recurrent_initializer='orthogonal',
    bias_initializer='zeros',
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    **kwargs
)
```






## Methods

<h3 id="get_dropout_mask_for_cell"><code>get_dropout_mask_for_cell</code></h3>

``` python
get_dropout_mask_for_cell(
    inputs,
    training,
    count=1
)
```

Get the dropout mask for RNN cell's input.

It will create mask based on context if there isn't any existing cached
mask. If a new mask is generated, it will update the cache in the cell.

#### Args:


* <b>`inputs`</b>: the input tensor whose shape will be used to generate dropout
  mask.
* <b>`training`</b>: boolean tensor, whether its in training mode, dropout will be
  ignored in non-training mode.
* <b>`count`</b>: int, how many dropout mask will be generated. It is useful for cell
  that has internal weights fused together.

#### Returns:

List of mask tensor, generated or cached mask based on context.


<h3 id="get_initial_state"><code>get_initial_state</code></h3>

``` python
get_initial_state(
    inputs=None,
    batch_size=None,
    dtype=None
)
```




<h3 id="get_recurrent_dropout_mask_for_cell"><code>get_recurrent_dropout_mask_for_cell</code></h3>

``` python
get_recurrent_dropout_mask_for_cell(
    inputs,
    training,
    count=1
)
```

Get the recurrent dropout mask for RNN cell.

It will create mask based on context if there isn't any existing cached
mask. If a new mask is generated, it will update the cache in the cell.

#### Args:


* <b>`inputs`</b>: the input tensor whose shape will be used to generate dropout
  mask.
* <b>`training`</b>: boolean tensor, whether its in training mode, dropout will be
  ignored in non-training mode.
* <b>`count`</b>: int, how many dropout mask will be generated. It is useful for cell
  that has internal weights fused together.

#### Returns:

List of mask tensor, generated or cached mask based on context.


<h3 id="reset_dropout_mask"><code>reset_dropout_mask</code></h3>

``` python
reset_dropout_mask()
```

Reset the cached dropout masks if any.

This is important for the RNN layer to invoke this in it call() method so
that the cached mask is cleared before calling the cell.call(). The mask
should be cached across the timestep within the same batch, but shouldn't
be cached between batches. Otherwise it will introduce unreasonable bias
against certain index of data within the batch.

<h3 id="reset_recurrent_dropout_mask"><code>reset_recurrent_dropout_mask</code></h3>

``` python
reset_recurrent_dropout_mask()
```

Reset the cached recurrent dropout masks if any.

This is important for the RNN layer to invoke this in it call() method so
that the cached mask is cleared before calling the cell.call(). The mask
should be cached across the timestep within the same batch, but shouldn't
be cached between batches. Otherwise it will introduce unreasonable bias
against certain index of data within the batch.



