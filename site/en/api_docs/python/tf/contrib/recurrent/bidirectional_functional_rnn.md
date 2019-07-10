page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.recurrent.bidirectional_functional_rnn

``` python
tf.contrib.recurrent.bidirectional_functional_rnn(
    cell_fw,
    cell_bw,
    inputs,
    initial_state_fw=None,
    initial_state_bw=None,
    dtype=None,
    sequence_length=None,
    time_major=False,
    use_tpu=False,
    fast_reverse=False,
    scope=None
)
```



Defined in [`tensorflow/contrib/recurrent/python/ops/functional_rnn.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/recurrent/python/ops/functional_rnn.py).

Creates a bidirectional recurrent neural network.

Performs fully dynamic unrolling of inputs in both directions. Built to be API
compatible with <a href="../../../tf/nn/bidirectional_dynamic_rnn"><code>tf.nn.bidirectional_dynamic_rnn</code></a>, but implemented with
functional control flow for TPU compatibility.

#### Args:

* <b>`cell_fw`</b>: An instance of <a href="../../../tf/nn/rnn_cell/RNNCell"><code>tf.contrib.rnn.RNNCell</code></a>.
* <b>`cell_bw`</b>: An instance of <a href="../../../tf/nn/rnn_cell/RNNCell"><code>tf.contrib.rnn.RNNCell</code></a>.
* <b>`inputs`</b>: The RNN inputs. If time_major == False (default), this must be a
    Tensor (or hierarchical structure of Tensors) of shape
    [batch_size, max_time, ...]. If time_major == True, this must be a Tensor
    (or hierarchical structure of Tensors) of shape:
    [max_time, batch_size, ...]. The first two dimensions must match across
    all the inputs, but otherwise the ranks and other shape components may
    differ.
* <b>`initial_state_fw`</b>: An optional initial state for `cell_fw`. Should match
    `cell_fw.zero_state` in structure and type.
* <b>`initial_state_bw`</b>: An optional initial state for `cell_bw`. Should match
    `cell_bw.zero_state` in structure and type.
* <b>`dtype`</b>: (optional) The data type for the initial state and expected output.
    Required if initial_states are not provided or RNN state has a
    heterogeneous dtype.
* <b>`sequence_length`</b>: An optional int32/int64 vector sized [batch_size]. Used to
    copy-through state and zero-out outputs when past a batch element's
    sequence length. So it's more for correctness than performance.
* <b>`time_major`</b>: Whether the `inputs` tensor is in "time major" format.
* <b>`use_tpu`</b>: Whether to enable TPU-compatible operation. If True, does not truly
    reverse `inputs` in the backwards RNN. Once b/69305369 is fixed, we can
    remove this flag.
* <b>`fast_reverse`</b>: Whether to use fast tf.reverse to replace tf.reverse_sequence.
    This is only possible when either all sequence lengths are the same inside
    the batch, or when the cell function does not change the state on padded
    input.
* <b>`scope`</b>: An optional scope name for the dynamic RNN.


#### Returns:

* <b>`outputs`</b>: A tuple of `(output_fw, output_bw)`. The output of the forward and
    backward RNN. If time_major == False (default), these will
    be Tensors shaped: [batch_size, max_time, cell.output_size]. If
    time_major == True, these will be Tensors shaped:
    [max_time, batch_size, cell.output_size]. Note, if cell.output_size is a
    (possibly nested) tuple of integers or TensorShape objects, then the
    output for that direction will be a tuple having the same structure as
    cell.output_size, containing Tensors having shapes corresponding to the
    shape data in cell.output_size.
* <b>`final_states`</b>: A tuple of `(final_state_fw, final_state_bw)`. A Tensor or
    hierarchical structure of Tensors indicating the final cell state in each
    direction. Must have the same structure and shape as cell.zero_state.


#### Raises:

* <b>`ValueError`</b>: If `initial_state_fw` is None or `initial_state_bw` is None and
    `dtype` is not provided.