page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.GRUCell


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/GRUCell">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent.py#L1496-L1762">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `GRUCell`

Cell class for the GRU layer.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/GRUCell"><code>tf.compat.v1.keras.layers.GRUCell</code></a>


<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`units`</b>: Positive integer, dimensionality of the output space.
* <b>`activation`</b>: Activation function to use.
  Default: hyperbolic tangent (`tanh`).
  If you pass None, no activation is applied
  (ie. "linear" activation: `a(x) = x`).
* <b>`recurrent_activation`</b>: Activation function to use
  for the recurrent step.
  Default: hard sigmoid (`hard_sigmoid`).
  If you pass `None`, no activation is applied
  (ie. "linear" activation: `a(x) = x`).
* <b>`use_bias`</b>: Boolean, whether the layer uses a bias vector.
* <b>`kernel_initializer`</b>: Initializer for the `kernel` weights matrix,
  used for the linear transformation of the inputs.
* <b>`recurrent_initializer`</b>: Initializer for the `recurrent_kernel`
  weights matrix,
  used for the linear transformation of the recurrent state.
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
  Fraction of the units to drop for the linear transformation of the inputs.
* <b>`recurrent_dropout`</b>: Float between 0 and 1.
  Fraction of the units to drop for
  the linear transformation of the recurrent state.
* <b>`implementation`</b>: Implementation mode, either 1 or 2.
  Mode 1 will structure its operations as a larger number of
  smaller dot products and additions, whereas mode 2 will
  batch them into fewer, larger operations. These modes will
  have different performance profiles on different hardware and
  for different applications.
* <b>`reset_after`</b>: GRU convention (whether to apply reset gate after or
  before matrix multiplication). False = "before" (default),
  True = "after" (CuDNN compatible).


#### Call arguments:


* <b>`inputs`</b>: A 2D tensor.
* <b>`states`</b>: List of state tensors corresponding to the previous timestep.
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode or in inference mode. Only relevant when `dropout` or
  `recurrent_dropout` is used.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent.py#L1550-L1592">View source</a>

``` python
__init__(
    units,
    activation='tanh',
    recurrent_activation='hard_sigmoid',
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
    implementation=1,
    reset_after=False,
    **kwargs
)
```






## Methods

<h3 id="get_dropout_mask_for_cell"><code>get_dropout_mask_for_cell</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent.py#L1033-L1067">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent.py#L1761-L1762">View source</a>

``` python
get_initial_state(
    inputs=None,
    batch_size=None,
    dtype=None
)
```




<h3 id="get_recurrent_dropout_mask_for_cell"><code>get_recurrent_dropout_mask_for_cell</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent.py#L1069-L1105">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent.py#L1009-L1019">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent.py#L1021-L1031">View source</a>

``` python
reset_recurrent_dropout_mask()
```

Reset the cached recurrent dropout masks if any.

This is important for the RNN layer to invoke this in it call() method so
that the cached mask is cleared before calling the cell.call(). The mask
should be cached across the timestep within the same batch, but shouldn't
be cached between batches. Otherwise it will introduce unreasonable bias
against certain index of data within the batch.
