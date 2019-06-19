page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.rnn

``` python
tf.keras.backend.rnn(
    step_function,
    inputs,
    initial_states,
    go_backwards=False,
    mask=None,
    constants=None,
    unroll=False,
    input_length=None
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/backend.py).

Iterates over the time dimension of a tensor.

#### Arguments:

* <b>`step_function`</b>: RNN step function.
        Parameters;
            input; tensor with shape `(samples, ...)` (no time dimension),
                representing input for the batch of samples at a certain
                time step.
            states; list of tensors.
        Returns;
            output; tensor with shape `(samples, output_dim)`
                (no time dimension).
            new_states; list of tensors, same length and shapes
                as 'states'. The first state in the list must be the
                output tensor at the previous timestep.
* <b>`inputs`</b>: tensor of temporal data of shape `(samples, time, ...)`
        (at least 3D).
* <b>`initial_states`</b>: tensor with shape (samples, output_dim)
        (no time dimension),
        containing the initial values for the states used in
        the step function.
* <b>`go_backwards`</b>: boolean. If True, do the iteration over the time
        dimension in reverse order and return the reversed sequence.
* <b>`mask`</b>: binary tensor with shape `(samples, time, 1)`,
        with a zero for every element that is masked.
* <b>`constants`</b>: a list of constant values passed at each step.
* <b>`unroll`</b>: whether to unroll the RNN or to use a symbolic loop
        (`while_loop` or `scan` depending on backend).
* <b>`input_length`</b>: If specified, assume time dimension is of this length.


#### Returns:

A tuple, `(last_output, outputs, new_states)`.
    last_output: the latest output of the rnn, of shape `(samples, ...)`
    outputs: tensor with shape `(samples, time, ...)` where each
        entry `outputs[s, t]` is the output of the step function
        at time `t` for sample `s`.
    new_states: list of tensors, latest states returned by
        the step function, of shape `(samples, ...)`.


#### Raises:

* <b>`ValueError`</b>: if input dimension is less than 3.
* <b>`ValueError`</b>: if `unroll` is `True` but input timestep is not a fixed
    number.
* <b>`ValueError`</b>: if `mask` is provided (not `None`) but states is not provided
        (`len(states)` == 0).