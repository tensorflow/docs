page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.GRU


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/GRU">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent.py#L1766-L2039">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `GRU`

Gated Recurrent Unit - Cho et al. 2014.

Inherits From: [`RNN`](../../../tf/keras/layers/RNN)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/GRU"><code>tf.compat.v1.keras.layers.GRU</code></a>


<!-- Placeholder for "Used in" -->

There are two variants. The default one is based on 1406.1078v3 and
has reset gate applied to hidden state before matrix multiplication. The
other one is based on original 1406.1078v1 and has the order reversed.

The second variant is compatible with CuDNNGRU (GPU-only) and allows
inference on CPU. Thus it has separate biases for `kernel` and
`recurrent_kernel`. Use `'reset_after'=True` and
`recurrent_activation='sigmoid'`.

#### Arguments:


* <b>`units`</b>: Positive integer, dimensionality of the output space.
* <b>`activation`</b>: Activation function to use.
  Default: hyperbolic tangent (`tanh`).
  If you pass `None`, no activation is applied
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
  weights matrix, used for the linear transformation of the recurrent state.
* <b>`bias_initializer`</b>: Initializer for the bias vector.
* <b>`kernel_regularizer`</b>: Regularizer function applied to
  the `kernel` weights matrix.
* <b>`recurrent_regularizer`</b>: Regularizer function applied to
  the `recurrent_kernel` weights matrix.
* <b>`bias_regularizer`</b>: Regularizer function applied to the bias vector.
* <b>`activity_regularizer`</b>: Regularizer function applied to
  the output of the layer (its "activation")..
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
* <b>`implementation`</b>: Implementation mode, either 1 or 2.
  Mode 1 will structure its operations as a larger number of
  smaller dot products and additions, whereas mode 2 will
  batch them into fewer, larger operations. These modes will
  have different performance profiles on different hardware and
  for different applications.
* <b>`return_sequences`</b>: Boolean. Whether to return the last output
  in the output sequence, or the full sequence.
* <b>`return_state`</b>: Boolean. Whether to return the last state
  in addition to the output.
* <b>`go_backwards`</b>: Boolean (default False).
  If True, process the input sequence backwards and return the
  reversed sequence.
* <b>`stateful`</b>: Boolean (default False). If True, the last state
  for each sample at index i in a batch will be used as initial
  state for the sample of index i in the following batch.
* <b>`unroll`</b>: Boolean (default False).
  If True, the network will be unrolled,
  else a symbolic loop will be used.
  Unrolling can speed-up a RNN,
  although it tends to be more memory-intensive.
  Unrolling is only suitable for short sequences.
* <b>`time_major`</b>: The shape format of the `inputs` and `outputs` tensors.
  If True, the inputs and outputs will be in shape
  `(timesteps, batch, ...)`, whereas in the False case, it will be
  `(batch, timesteps, ...)`. Using `time_major = True` is a bit more
  efficient because it avoids transposes at the beginning and end of the
  RNN calculation. However, most TensorFlow data is batch-major, so by
  default this function accepts input and emits output in batch-major
  form. 
* <b>`reset_after`</b>: GRU convention (whether to apply reset gate after or
  before matrix multiplication). False = "before" (default),
  True = "after" (CuDNN compatible).


#### Call arguments:


* <b>`inputs`</b>: A 3D tensor.
* <b>`mask`</b>: Binary tensor of shape `(samples, timesteps)` indicating whether
  a given timestep should be masked.
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode or in inference mode. This argument is passed to the cell
  when calling it. This is only relevant if `dropout` or
  `recurrent_dropout` is used.
* <b>`initial_state`</b>: List of initial state tensors to be passed to the first
  call of the cell.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent.py#L1859-L1916">View source</a>

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
    activity_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    implementation=1,
    return_sequences=False,
    return_state=False,
    go_backwards=False,
    stateful=False,
    unroll=False,
    reset_after=False,
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




<h3 id="reset_after"><code>reset_after</code></h3>




<h3 id="states"><code>states</code></h3>




<h3 id="units"><code>units</code></h3>




<h3 id="use_bias"><code>use_bias</code></h3>






## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent.py#L593-L614">View source</a>

``` python
get_initial_state(inputs)
```




<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/recurrent.py#L806-L858">View source</a>

``` python
reset_states(states=None)
```
