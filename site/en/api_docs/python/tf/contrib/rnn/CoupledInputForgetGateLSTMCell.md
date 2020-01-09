page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.CoupledInputForgetGateLSTMCell


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/rnn/python/ops/rnn_cell.py#L98-L322">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `CoupledInputForgetGateLSTMCell`

Long short-term memory unit (LSTM) recurrent network cell.

Inherits From: [`RNNCell`](../../../tf/nn/rnn_cell/RNNCell)

<!-- Placeholder for "Used in" -->

The default non-peephole implementation is based on:

  https://pdfs.semanticscholar.org/1154/0131eae85b2e11d53df7f1360eeb6476e7f4.pdf

Felix Gers, Jurgen Schmidhuber, and Fred Cummins.
"Learning to forget: Continual prediction with LSTM." IET, 850-855, 1999.

The peephole implementation is based on:

  https://research.google.com/pubs/archive/43905.pdf

Hasim Sak, Andrew Senior, and Francoise Beaufays.
"Long short-term memory recurrent neural network architectures for
 large scale acoustic modeling." INTERSPEECH, 2014.

The coupling of input and forget gate is based on:

  http://arxiv.org/pdf/1503.04069.pdf

Greff et al. "LSTM: A Search Space Odyssey"

The class uses optional peep-hole connections, and an optional projection
layer.
Layer normalization implementation is based on:

  https://arxiv.org/abs/1607.06450.

"Layer Normalization"
Jimmy Lei Ba, Jamie Ryan Kiros, Geoffrey E. Hinton

and is applied before the internal nonlinearities.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/rnn/python/ops/rnn_cell.py#L135-L210">View source</a>

``` python
__init__(
    num_units,
    use_peepholes=False,
    initializer=None,
    num_proj=None,
    proj_clip=None,
    num_unit_shards=1,
    num_proj_shards=1,
    forget_bias=1.0,
    state_is_tuple=True,
    activation=tf.math.tanh,
    reuse=None,
    layer_norm=False,
    norm_gain=1.0,
    norm_shift=0.0
)
```

Initialize the parameters for an LSTM cell.


#### Args:


* <b>`num_units`</b>: int, The number of units in the LSTM cell
* <b>`use_peepholes`</b>: bool, set True to enable diagonal/peephole connections.
* <b>`initializer`</b>: (optional) The initializer to use for the weight and
  projection matrices.
* <b>`num_proj`</b>: (optional) int, The output dimensionality for the projection
  matrices.  If None, no projection is performed.
* <b>`proj_clip`</b>: (optional) A float value.  If `num_proj > 0` and `proj_clip` is
provided, then the projected values are clipped elementwise to within
`[-proj_clip, proj_clip]`.
* <b>`num_unit_shards`</b>: How to split the weight matrix.  If >1, the weight
  matrix is stored across num_unit_shards.
* <b>`num_proj_shards`</b>: How to split the projection matrix.  If >1, the
  projection matrix is stored across num_proj_shards.
* <b>`forget_bias`</b>: Biases of the forget gate are initialized by default to 1
  in order to reduce the scale of forgetting at the beginning of
  the training.
* <b>`state_is_tuple`</b>: If True, accepted and returned states are 2-tuples of
  the `c_state` and `m_state`.  By default (False), they are concatenated
  along the column axis.  This default behavior will soon be deprecated.
* <b>`activation`</b>: Activation function of the inner states.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
  in an existing scope.  If not `True`, and the existing scope already has
  the given variables, an error is raised.
* <b>`layer_norm`</b>: If `True`, layer normalization will be applied.
* <b>`norm_gain`</b>: float, The layer normalization gain initial value. If
  `layer_norm` has been set to `False`, this argument will be ignored.
* <b>`norm_shift`</b>: float, The layer normalization shift initial value. If
  `layer_norm` has been set to `False`, this argument will be ignored.



## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="output_size"><code>output_size</code></h3>

Integer or TensorShape: size of outputs produced by this cell.


<h3 id="scope_name"><code>scope_name</code></h3>




<h3 id="state_size"><code>state_size</code></h3>

size(s) of state(s) used by this cell.

It can be represented by an Integer, a TensorShape or a tuple of Integers
or TensorShapes.



## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/rnn_cell_impl.py#L281-L309">View source</a>

``` python
get_initial_state(
    inputs=None,
    batch_size=None,
    dtype=None
)
```




<h3 id="zero_state"><code>zero_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/rnn_cell_impl.py#L311-L340">View source</a>

``` python
zero_state(
    batch_size,
    dtype
)
```

Return zero-filled state tensor(s).


#### Args:


* <b>`batch_size`</b>: int, float, or unit Tensor representing the batch size.
* <b>`dtype`</b>: the data type to use for the state.


#### Returns:

If `state_size` is an int or TensorShape, then the return value is a
`N-D` tensor of shape `[batch_size, state_size]` filled with zeros.

If `state_size` is a nested list or tuple, then the return value is
a nested list or tuple (of the same structure) of `2-D` tensors with
the shapes `[batch_size, s]` for each s in `state_size`.
