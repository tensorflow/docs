

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.LayerNormBasicLSTMCell

### `class tf.contrib.rnn.LayerNormBasicLSTMCell`



Defined in [`tensorflow/contrib/rnn/python/ops/rnn_cell.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/rnn/python/ops/rnn_cell.py).

See the guide: [RNN and Cells (contrib) > Core RNN Cells for use with TensorFlow's core RNN methods](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cells_for_use_with_TensorFlow_s_core_RNN_methods)

LSTM unit with layer normalization and recurrent dropout.

This class adds layer normalization and recurrent dropout to a
basic LSTM unit. Layer normalization implementation is based on:

  https://arxiv.org/abs/1607.06450.

"Layer Normalization"
Jimmy Lei Ba, Jamie Ryan Kiros, Geoffrey E. Hinton

and is applied before the internal nonlinearities.
Recurrent dropout is base on:

  https://arxiv.org/abs/1603.05118

"Recurrent Dropout without Memory Loss"
Stanislau Semeniuta, Aliaksei Severyn, Erhardt Barth.

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    num_units,
    forget_bias=1.0,
    input_size=None,
    activation=tf.tanh,
    layer_norm=True,
    norm_gain=1.0,
    norm_shift=0.0,
    dropout_keep_prob=1.0,
    dropout_prob_seed=None,
    reuse=None
)
```

Initializes the basic LSTM cell.

#### Args:

* <b>`num_units`</b>: int, The number of units in the LSTM cell.
* <b>`forget_bias`</b>: float, The bias added to forget gates (see above).
* <b>`input_size`</b>: Deprecated and unused.
* <b>`activation`</b>: Activation function of the inner states.
* <b>`layer_norm`</b>: If `True`, layer normalization will be applied.
* <b>`norm_gain`</b>: float, The layer normalization gain initial value. If
    `layer_norm` has been set to `False`, this argument will be ignored.
* <b>`norm_shift`</b>: float, The layer normalization shift initial value. If
    `layer_norm` has been set to `False`, this argument will be ignored.
* <b>`dropout_keep_prob`</b>: unit Tensor or float between 0 and 1 representing the
    recurrent dropout probability value. If float and 1.0, no dropout will
    be applied.
* <b>`dropout_prob_seed`</b>: (optional) integer, the randomness seed.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
    in an existing scope.  If not `True`, and the existing scope already has
    the given variables, an error is raised.

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    inputs,
    state,
    scope=None
)
```

LSTM cell with layer normalization and recurrent dropout.

<h3 id="zero_state"><code>zero_state</code></h3>

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
  `N-D` tensor of shape `[batch_size x state_size]` filled with zeros.

  If `state_size` is a nested list or tuple, then the return value is
  a nested list or tuple (of the same structure) of `2-D` tensors with
the shapes `[batch_size x s]` for each s in `state_size`.



