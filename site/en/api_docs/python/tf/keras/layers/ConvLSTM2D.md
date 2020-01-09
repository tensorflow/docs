page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.ConvLSTM2D


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/convolutional_recurrent.py#L758-L1062">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ConvLSTM2D`

Convolutional LSTM.



### Aliases:

* Class `tf.compat.v1.keras.layers.ConvLSTM2D`
* Class `tf.compat.v2.keras.layers.ConvLSTM2D`


<!-- Placeholder for "Used in" -->

It is similar to an LSTM layer, but the input transformations
and recurrent transformations are both convolutional.

#### Arguments:


* <b>`filters`</b>: Integer, the dimensionality of the output space
  (i.e. the number of output filters in the convolution).
* <b>`kernel_size`</b>: An integer or tuple/list of n integers, specifying the
  dimensions of the convolution window.
* <b>`strides`</b>: An integer or tuple/list of n integers,
  specifying the strides of the convolution.
  Specifying any stride value != 1 is incompatible with specifying
  any `dilation_rate` value != 1.
* <b>`padding`</b>: One of `"valid"` or `"same"` (case-insensitive).
* <b>`data_format`</b>: A string,
  one of `channels_last` (default) or `channels_first`.
  The ordering of the dimensions in the inputs.
  `channels_last` corresponds to inputs with shape
  `(batch, time, ..., channels)`
  while `channels_first` corresponds to
  inputs with shape `(batch, time, channels, ...)`.
  It defaults to the `image_data_format` value found in your
  Keras config file at `~/.keras/keras.json`.
  If you never set it, then it will be "channels_last".
* <b>`dilation_rate`</b>: An integer or tuple/list of n integers, specifying
  the dilation rate to use for dilated convolution.
  Currently, specifying any `dilation_rate` value != 1 is
  incompatible with specifying any `strides` value != 1.
* <b>`activation`</b>: Activation function to use.
  By default hyperbolic tangent activation function is applied
  (`tanh(x)`).
* <b>`recurrent_activation`</b>: Activation function to use
  for the recurrent step.
* <b>`use_bias`</b>: Boolean, whether the layer uses a bias vector.
* <b>`kernel_initializer`</b>: Initializer for the `kernel` weights matrix,
  used for the linear transformation of the inputs.
* <b>`recurrent_initializer`</b>: Initializer for the `recurrent_kernel`
  weights matrix,
  used for the linear transformation of the recurrent state.
* <b>`bias_initializer`</b>: Initializer for the bias vector.
* <b>`unit_forget_bias`</b>: Boolean.
  If True, add 1 to the bias of the forget gate at initialization.
  Use in combination with `bias_initializer="zeros"`.
  This is recommended in [Jozefowicz et al.]
  (http://www.jmlr.org/proceedings/papers/v37/jozefowicz15.pdf)
* <b>`kernel_regularizer`</b>: Regularizer function applied to
  the `kernel` weights matrix.
* <b>`recurrent_regularizer`</b>: Regularizer function applied to
  the `recurrent_kernel` weights matrix.
* <b>`bias_regularizer`</b>: Regularizer function applied to the bias vector.
* <b>`activity_regularizer`</b>: Regularizer function applied to.
* <b>`kernel_constraint`</b>: Constraint function applied to
  the `kernel` weights matrix.
* <b>`recurrent_constraint`</b>: Constraint function applied to
  the `recurrent_kernel` weights matrix.
* <b>`bias_constraint`</b>: Constraint function applied to the bias vector.
* <b>`return_sequences`</b>: Boolean. Whether to return the last output
  in the output sequence, or the full sequence.
* <b>`go_backwards`</b>: Boolean (default False).
  If True, process the input sequence backwards.
* <b>`stateful`</b>: Boolean (default False). If True, the last state
  for each sample at index i in a batch will be used as initial
  state for the sample of index i in the following batch.
* <b>`dropout`</b>: Float between 0 and 1.
  Fraction of the units to drop for
  the linear transformation of the inputs.
* <b>`recurrent_dropout`</b>: Float between 0 and 1.
  Fraction of the units to drop for
  the linear transformation of the recurrent state.


#### Call arguments:


* <b>`inputs`</b>: A 5D tensor.
* <b>`mask`</b>: Binary tensor of shape `(samples, timesteps)` indicating whether
  a given timestep should be masked.
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode or in inference mode. This argument is passed to the cell
  when calling it. This is only relevant if `dropout` or `recurrent_dropout`
  are set.
* <b>`initial_state`</b>: List of initial state tensors to be passed to the first
  call of the cell.


#### Input shape:

- If data_format='channels_first'
    5D tensor with shape:
    `(samples, time, channels, rows, cols)`
- If data_format='channels_last'
    5D tensor with shape:
    `(samples, time, rows, cols, channels)`



#### Output shape:

- If `return_sequences`
   - If data_format='channels_first'
      5D tensor with shape:
      `(samples, time, filters, output_row, output_col)`
   - If data_format='channels_last'
      5D tensor with shape:
      `(samples, time, output_row, output_col, filters)`
- Else
  - If data_format ='channels_first'
      4D tensor with shape:
      `(samples, filters, output_row, output_col)`
  - If data_format='channels_last'
      4D tensor with shape:
      `(samples, output_row, output_col, filters)`
  where `o_row` and `o_col` depend on the shape of the filter and
  the padding



#### Raises:


* <b>`ValueError`</b>: in case of invalid constructor arguments.


#### References:

- [Convolutional LSTM Network: A Machine Learning Approach for
Precipitation Nowcasting](http://arxiv.org/abs/1506.04214v1)
The current implementation does not include the feedback loop on the
cells output.


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/convolutional_recurrent.py#L877-L931">View source</a>

``` python
__init__(
    filters,
    kernel_size,
    strides=(1, 1),
    padding='valid',
    data_format=None,
    dilation_rate=(1, 1),
    activation='tanh',
    recurrent_activation='hard_sigmoid',
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
    return_sequences=False,
    go_backwards=False,
    stateful=False,
    dropout=0.0,
    recurrent_dropout=0.0,
    **kwargs
)
```






## Properties

<h3 id="activation"><code>activation</code></h3>




<h3 id="bias_constraint"><code>bias_constraint</code></h3>




<h3 id="bias_initializer"><code>bias_initializer</code></h3>




<h3 id="bias_regularizer"><code>bias_regularizer</code></h3>




<h3 id="data_format"><code>data_format</code></h3>




<h3 id="dilation_rate"><code>dilation_rate</code></h3>




<h3 id="dropout"><code>dropout</code></h3>




<h3 id="filters"><code>filters</code></h3>




<h3 id="kernel_constraint"><code>kernel_constraint</code></h3>




<h3 id="kernel_initializer"><code>kernel_initializer</code></h3>




<h3 id="kernel_regularizer"><code>kernel_regularizer</code></h3>




<h3 id="kernel_size"><code>kernel_size</code></h3>




<h3 id="padding"><code>padding</code></h3>




<h3 id="recurrent_activation"><code>recurrent_activation</code></h3>




<h3 id="recurrent_constraint"><code>recurrent_constraint</code></h3>




<h3 id="recurrent_dropout"><code>recurrent_dropout</code></h3>




<h3 id="recurrent_initializer"><code>recurrent_initializer</code></h3>




<h3 id="recurrent_regularizer"><code>recurrent_regularizer</code></h3>




<h3 id="states"><code>states</code></h3>




<h3 id="strides"><code>strides</code></h3>




<h3 id="unit_forget_bias"><code>unit_forget_bias</code></h3>




<h3 id="use_bias"><code>use_bias</code></h3>






## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/convolutional_recurrent.py#L278-L292">View source</a>

``` python
get_initial_state(inputs)
```




<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/convolutional_recurrent.py#L414-L482">View source</a>

``` python
reset_states(states=None)
```
