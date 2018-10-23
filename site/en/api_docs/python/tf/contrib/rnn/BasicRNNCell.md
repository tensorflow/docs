

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.rnn.BasicRNNCell

### `class tf.contrib.rnn.BasicRNNCell`
### `class tf.contrib.rnn.core_rnn_cell.BasicRNNCell`



Defined in [`tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py).

See the guide: [RNN and Cells (contrib) > Core RNN Cells for use with TensorFlow's core RNN methods](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cells_for_use_with_TensorFlow_s_core_RNN_methods)

The most basic RNN cell.

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    num_units,
    input_size=None,
    activation=tf.tanh,
    reuse=None
)
```



<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    inputs,
    state,
    scope=None
)
```

Most basic RNN: output = new_state = act(W * input + U * state + B).

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



