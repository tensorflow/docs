


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.seq2seq.dynamic_rnn_decoder

### `tf.contrib.seq2seq.dynamic_rnn_decoder`

```
tf.contrib.seq2seq.dynamic_rnn_decoder(cell, decoder_fn, inputs=None, sequence_length=None, parallel_iterations=None, swap_memory=False, time_major=False, scope=None, name=None)
```


Dynamic RNN decoder for a sequence-to-sequence model specified by
RNNCell and decoder function.

The `dynamic_rnn_decoder` is similar to the `tf.python.ops.rnn.dynamic_rnn`
as the decoder does not make any assumptions of sequence length and batch
size of the input.

The `dynamic_rnn_decoder` has two modes: training or inference and expects
the user to create seperate functions for each.

Under both training and inference, both `cell` and `decoder_fn` are expected,
where `cell` performs computation at every timestep using `raw_rnn`, and
`decoder_fn` allows modeling of early stopping, output, state, and next
input and context.

When training the user is expected to supply `inputs`. At every time step a
slice of the supplied input is fed to the `decoder_fn`, which modifies and
returns the input for the next time step.

`sequence_length` is needed at training time, i.e., when `inputs` is not
None, for dynamic unrolling. At test time, when `inputs` is None,
`sequence_length` is not needed.

Under inference `inputs` is expected to be `None` and the input is inferred
solely from the `decoder_fn`.

#### Args:

* <b>`cell`</b>: An instance of RNNCell.
* <b>`decoder_fn`</b>: A function that takes time, cell state, cell input,
    cell output and context state. It returns a early stopping vector,
    cell state, next input, cell output and context state.
    Examples of decoder_fn can be found in the decoder_fn.py folder.
* <b>`inputs`</b>: The inputs for decoding (embedded format).

    If `time_major == False` (default), this must be a `Tensor` of shape:
      `[batch_size, max_time, ...]`.

    If `time_major == True`, this must be a `Tensor` of shape:
      `[max_time, batch_size, ...]`.

    The input to `cell` at each time step will be a `Tensor` with dimensions
      `[batch_size, ...]`.

* <b>`sequence_length`</b>: (optional) An int32/int64 vector sized `[batch_size]`.
    if `inputs` is not None and `sequence_length` is None it is inferred
    from the `inputs` as the maximal possible sequence length.
* <b>`parallel_iterations`</b>: (Default: 32).  The number of iterations to run in
    parallel.  Those operations which do not have any temporal dependency
    and can be run in parallel, will be.  This parameter trades off
    time for space.  Values >> 1 use more memory but take less time,
    while smaller values use less memory but computations take longer.
* <b>`swap_memory`</b>: Transparently swap the tensors produced in forward inference
    but needed for back prop from GPU to CPU.  This allows training RNNs
    which would typically not fit on a single GPU, with very minimal (or no)
    performance penalty.
* <b>`time_major`</b>: The shape format of the `inputs` and `outputs` Tensors.
    If true, these `Tensors` must be shaped `[max_time, batch_size, depth]`.
    If false, these `Tensors` must be shaped `[batch_size, max_time, depth]`.
    Using `time_major = True` is a bit more efficient because it avoids
    transposes at the beginning and end of the RNN calculation.  However,
    most TensorFlow data is batch-major, so by default this function
    accepts input and emits output in batch-major form.
* <b>`scope`</b>: VariableScope for the `raw_rnn`;
    defaults to None.
* <b>`name`</b>: NameScope for the decoder;
    defaults to "dynamic_rnn_decoder"


#### Returns:

  A tuple (outputs, final_state, final_context_state) where:

    outputs: the RNN output 'Tensor'.

      If time_major == False (default), this will be a `Tensor` shaped:
        `[batch_size, max_time, cell.output_size]`.

      If time_major == True, this will be a `Tensor` shaped:
        `[max_time, batch_size, cell.output_size]`.

    final_state: The final state and will be shaped
      `[batch_size, cell.state_size]`.

    final_context_state: The context state returned by the final call
      to decoder_fn. This is useful if the context state maintains internal
      data which is required after the graph is run.
      For example, one way to diversify the inference output is to use
      a stochastic decoder_fn, in which case one would want to store the
      decoded outputs, not just the RNN outputs. This can be done by
      maintaining a TensorArray in context_state and storing the decoded
      output of each iteration therein.


#### Raises:

* <b>`ValueError`</b>: if inputs is not None and has less than three dimensions.

Defined in [`tensorflow/contrib/seq2seq/python/ops/seq2seq.py`](https://www.tensorflow.org/code/tensorflow/contrib/seq2seq/python/ops/seq2seq.py).

