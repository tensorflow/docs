page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cudnn_rnn.CudnnRNNRelu


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/cudnn_rnn/python/layers/cudnn_rnn.py#L612-L616">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `CudnnRNNRelu`

Cudnn implementation of the RNN-relu layer.



<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/cudnn_rnn/python/layers/cudnn_rnn.py#L159-L219">View source</a>

``` python
__init__(
    num_layers,
    num_units,
    input_mode=CUDNN_INPUT_LINEAR_MODE,
    direction=CUDNN_RNN_UNIDIRECTION,
    dropout=0.0,
    seed=None,
    dtype=tf.dtypes.float32,
    kernel_initializer=None,
    bias_initializer=None,
    name=None
)
```

Creates a CudnnRNN model from model spec.


#### Args:


* <b>`num_layers`</b>: the number of layers for the RNN model.
* <b>`num_units`</b>: the number of units within the RNN model.
* <b>`input_mode`</b>: indicate whether there is a linear projection between the
  input and the actual computation before the first layer. It can be
  'linear_input', 'skip_input' or 'auto_select'. 'linear_input' (default)
  always applies a linear projection of input onto RNN hidden state.
  (standard RNN behavior). 'skip_input' is only allowed when input_size ==
  num_units; 'auto_select' implies 'skip_input' when input_size ==
  num_units; otherwise, it implies 'linear_input'.
* <b>`direction`</b>: the direction model that the model operates. Can be either
  'unidirectional' or 'bidirectional'
* <b>`dropout`</b>: dropout rate, a number between [0, 1]. Dropout is applied between
  each layer (no dropout is applied for a model with a single layer). When
  set to 0, dropout is disabled.
* <b>`seed`</b>: the op seed used for initializing dropout. See
  <a href="../../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.
* <b>`dtype`</b>: tf.float16, tf.float32 or tf.float64
* <b>`kernel_initializer`</b>: starting value to initialize the weight.
* <b>`bias_initializer`</b>: starting value to initialize the bias (default is all
  zeros).
* <b>`name`</b>: VariableScope for the created subgraph; defaults to class name. This
  only serves the default scope if later no scope is specified when
  invoking __call__().


#### Raises:


* <b>`ValueError`</b>: if direction is invalid. Or dtype is not supported.



## Properties

<h3 id="canonical_bias_shapes"><code>canonical_bias_shapes</code></h3>

Shapes of Cudnn canonical bias tensors.


<h3 id="canonical_weight_shapes"><code>canonical_weight_shapes</code></h3>

Shapes of Cudnn canonical weight tensors.


<h3 id="direction"><code>direction</code></h3>

Returns `unidirectional` or `bidirectional`.


<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="input_mode"><code>input_mode</code></h3>

Input mode of first layer.

Indicates whether there is a linear projection between the input and the
actual computation before the first layer. It can be
* 'linear_input': (default) always applies a linear projection of input
  onto RNN hidden state. (standard RNN behavior)
* 'skip_input': 'skip_input' is only allowed when input_size == num_units.
* 'auto_select'. implies 'skip_input' when input_size == num_units;
  otherwise, it implies 'linear_input'.

#### Returns:

'linear_input', 'skip_input' or 'auto_select'.


<h3 id="input_size"><code>input_size</code></h3>




<h3 id="num_dirs"><code>num_dirs</code></h3>




<h3 id="num_layers"><code>num_layers</code></h3>




<h3 id="num_units"><code>num_units</code></h3>




<h3 id="rnn_mode"><code>rnn_mode</code></h3>

Type of RNN cell used.


#### Returns:

`lstm`, `gru`, `rnn_relu` or `rnn_tanh`.


<h3 id="saveable"><code>saveable</code></h3>




<h3 id="scope_name"><code>scope_name</code></h3>






## Methods

<h3 id="state_shape"><code>state_shape</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/cudnn_rnn/python/layers/cudnn_rnn.py#L582-L595">View source</a>

``` python
state_shape(batch_size)
```

Shape of the state of Cudnn RNN cells w/o.

input_c.

Shape is a 1-element tuple,
[num_layers * num_dirs, batch_size, num_units]
Args:
  batch_size: an int

#### Returns:

a tuple of python arrays.
