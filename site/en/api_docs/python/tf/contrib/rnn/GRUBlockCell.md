


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.GRUBlockCell

### `class tf.contrib.rnn.GRUBlockCell`

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

Block GRU cell implementation.

The implementation is based on:  http://arxiv.org/abs/1406.1078
Computes the LSTM cell forward propagation for 1 time step.

This kernel op implements the following mathematical equations:

Biases are initialized with:

* `b_ru` - constant_initializer(1.0)
* `b_c` - constant_initializer(0.0)

```
x_h_prev = [x, h_prev]

[r_bar u_bar] = x_h_prev * w_ru + b_ru

r = sigmoid(r_bar)
u = sigmoid(u_bar)

h_prevr = h_prev \circ r

x_h_prevr = [x h_prevr]

c_bar = x_h_prevr * w_c + b_c
c = tanh(c_bar)

h = (1-u) \circ c + u \circ h_prev
```

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__(cell_size)</code></h3>

Initialize the Block GRU cell.

#### Args:

* <b>`cell_size`</b>: int, GRU cell size.

<h3 id="zero_state"><code>zero_state(batch_size, dtype)</code></h3>

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





Defined in [`tensorflow/contrib/rnn/python/ops/gru_ops.py`](https://www.tensorflow.org/code/tensorflow/contrib/rnn/python/ops/gru_ops.py).

