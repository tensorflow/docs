page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.keras.layers.LSTM


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent_v2.py#L755-L1000">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `LSTM`

Long Short-Term Memory layer - Hochreiter 1997.

Inherits From: [`LSTM`](../../../../../tf/keras/layers/LSTM)

<!-- Placeholder for "Used in" -->

Based on available runtime hardware and constraints, this layer
will choose different implementations (cuDNN-based or pure-TensorFlow)
to maximize the performance. If a GPU is available and all
the arguments to the layer meet the requirement of the CuDNN kernel
(see below for details), the layer will use a fast cuDNN implementation.

The requirements to use the cuDNN implementation are:

1. `activation` == 'tanh'
2. `recurrent_activation` == 'sigmoid'
3. `recurrent_dropout` == 0
4. `unroll` is False
5. `use_bias` is True
6. Inputs are not masked or strictly right padded.

#### Arguments:


* <b>`units`</b>: Positive integer, dimensionality of the output space.
* <b>`activation`</b>: Activation function to use.
  Default: hyperbolic tangent (`tanh`). If you pass `None`, no activation
  is applied (ie. "linear" activation: `a(x) = x`).
* <b>`recurrent_activation`</b>: Activation function to use for the recurrent step.
  Default: sigmoid (`sigmoid`). If you pass `None`, no activation is
  applied (ie. "linear" activation: `a(x) = x`).
* <b>`use_bias`</b>: Boolean, whether the layer uses a bias vector.
* <b>`kernel_initializer`</b>: Initializer for the `kernel` weights matrix, used for
  the linear transformation of the inputs..
* <b>`recurrent_initializer`</b>: Initializer for the `recurrent_kernel` weights
  matrix, used for the linear transformation of the recurrent state..
* <b>`bias_initializer`</b>: Initializer for the bias vector.
* <b>`unit_forget_bias`</b>: Boolean. If True, add 1 to the bias of the forget gate at
  initialization. Setting it to true will also force
  `bias_initializer="zeros"`. This is recommended in [Jozefowicz et
      al.](http://www.jmlr.org/proceedings/papers/v37/jozefowicz15.pdf).
* <b>`kernel_regularizer`</b>: Regularizer function applied to the `kernel` weights
  matrix.
* <b>`recurrent_regularizer`</b>: Regularizer function applied to the
  `recurrent_kernel` weights matrix.
* <b>`bias_regularizer`</b>: Regularizer function applied to the bias vector.
* <b>`activity_regularizer`</b>: Regularizer function applied to the output of the
  layer (its "activation")..
* <b>`kernel_constraint`</b>: Constraint function applied to the `kernel` weights
  matrix.
* <b>`recurrent_constraint`</b>: Constraint function applied to the `recurrent_kernel`
  weights matrix.
* <b>`bias_constraint`</b>: Constraint function applied to the bias vector.
* <b>`dropout`</b>: Float between 0 and 1. Fraction of the units to drop for the linear
  transformation of the inputs.
* <b>`recurrent_dropout`</b>: Float between 0 and 1. Fraction of the units to drop for
  the linear transformation of the recurrent state.
* <b>`implementation`</b>: Implementation mode, either 1 or 2. Mode 1 will structure
  its operations as a larger number of smaller dot products and additions,
  whereas mode 2 will batch them into fewer, larger operations. These modes
  will have different performance profiles on different hardware and for
  different applications.
* <b>`return_sequences`</b>: Boolean. Whether to return the last output. in the output
  sequence, or the full sequence.
* <b>`return_state`</b>: Boolean. Whether to return the last state in addition to the
  output.
* <b>`go_backwards`</b>: Boolean (default False). If True, process the input sequence
  backwards and return the reversed sequence.
* <b>`stateful`</b>: Boolean (default False). If True, the last state for each sample
  at index i in a batch will be used as initial state for the sample of
  index i in the following batch.
* <b>`unroll`</b>: Boolean (default False). If True, the network will be unrolled, else
  a symbolic loop will be used. Unrolling can speed-up a RNN, although it
  tends to be more memory-intensive. Unrolling is only suitable for short
  sequences.


#### Call arguments:


* <b>`inputs`</b>: A 3D tensor.
* <b>`mask`</b>: Binary tensor of shape `(samples, timesteps)` indicating whether
  a given timestep should be masked (optional, defaults to `None`).
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode or in inference mode. This argument is passed to the cell
  when calling it. This is only relevant if `dropout` or
  `recurrent_dropout` is used (optional, defaults to `None`).
* <b>`initial_state`</b>: List of initial state tensors to be passed to the first
  call of the cell (optional, defaults to `None` which causes creation
  of zero-filled initial state tensors).

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent_v2.py#L839-L902">View source</a>

``` python
__init__(
    units,
    activation='tanh',
    recurrent_activation='sigmoid',
    use_bias=True,
    kernel_initializer='glorot_uniform',
    recurrent_initializer='orthogonal',
    bias_initializer='zeros',
    unit_forget_bias=True,
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    implementation=2,
    return_sequences=False,
    return_state=False,
    go_backwards=False,
    stateful=False,
    time_major=False,
    unroll=False,
    **kwargs
)
```






## Properties

<h3 id="activation"><code>activation</code></h3>




<h3 id="bias_constraint"><code>bias_constraint</code></h3>




<h3 id="bias_initializer"><code>bias_initializer</code></h3>




<h3 id="bias_regularizer"><code>bias_regularizer</code></h3>




<h3 id="dropout"><code>dropout</code></h3>




<h3 id="implementation"><code>implementation</code></h3>




<h3 id="kernel_constraint"><code>kernel_constraint</code></h3>




<h3 id="kernel_initializer"><code>kernel_initializer</code></h3>




<h3 id="kernel_regularizer"><code>kernel_regularizer</code></h3>




<h3 id="recurrent_activation"><code>recurrent_activation</code></h3>




<h3 id="recurrent_constraint"><code>recurrent_constraint</code></h3>




<h3 id="recurrent_dropout"><code>recurrent_dropout</code></h3>




<h3 id="recurrent_initializer"><code>recurrent_initializer</code></h3>




<h3 id="recurrent_regularizer"><code>recurrent_regularizer</code></h3>




<h3 id="states"><code>states</code></h3>




<h3 id="unit_forget_bias"><code>unit_forget_bias</code></h3>




<h3 id="units"><code>units</code></h3>




<h3 id="use_bias"><code>use_bias</code></h3>






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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent.py#L593-L614">View source</a>

``` python
get_initial_state(inputs)
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

<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent.py#L806-L858">View source</a>

``` python
reset_states(states=None)
```
