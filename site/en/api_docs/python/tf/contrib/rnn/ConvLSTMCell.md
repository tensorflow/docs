page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.ConvLSTMCell

## Class `ConvLSTMCell`

Convolutional LSTM recurrent network cell.

Inherits From: [`RNNCell`](../../../tf/nn/rnn_cell/RNNCell)



Defined in [`contrib/rnn/python/ops/rnn_cell.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/rnn_cell.py).

<!-- Placeholder for "Used in" -->

https://arxiv.org/pdf/1506.04214v1.pdf

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    conv_ndims,
    input_shape,
    output_channels,
    kernel_shape,
    use_bias=True,
    skip_connection=False,
    forget_bias=1.0,
    initializers=None,
    name='conv_lstm_cell'
)
```

Construct ConvLSTMCell.


#### Args:


* <b>`conv_ndims`</b>: Convolution dimensionality (1, 2 or 3).
* <b>`input_shape`</b>: Shape of the input as int tuple, excluding the batch size.
* <b>`output_channels`</b>: int, number of output channels of the conv LSTM.
* <b>`kernel_shape`</b>: Shape of kernel as an int tuple (of size 1, 2 or 3).
* <b>`use_bias`</b>: (bool) Use bias in convolutions.
* <b>`skip_connection`</b>: If set to `True`, concatenate the input to the
  output of the conv LSTM. Default: `False`.
* <b>`forget_bias`</b>: Forget bias.
* <b>`initializers`</b>: Unused.
* <b>`name`</b>: Name of the module.


#### Raises:


* <b>`ValueError`</b>: If `skip_connection` is `True` and stride is different from 1
  or if `input_shape` is incompatible with `conv_ndims`.



## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="output_size"><code>output_size</code></h3>




<h3 id="scope_name"><code>scope_name</code></h3>




<h3 id="state_size"><code>state_size</code></h3>






## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

``` python
get_initial_state(
    inputs=None,
    batch_size=None,
    dtype=None
)
```




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
`N-D` tensor of shape `[batch_size, state_size]` filled with zeros.

If `state_size` is a nested list or tuple, then the return value is
a nested list or tuple (of the same structure) of `2-D` tensors with
the shapes `[batch_size, s]` for each s in `state_size`.




