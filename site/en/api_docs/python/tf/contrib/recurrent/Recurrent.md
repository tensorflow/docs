page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.recurrent.Recurrent

``` python
tf.contrib.recurrent.Recurrent(
    theta,
    state0,
    inputs,
    cell_fn,
    cell_grad=None,
    extras=None,
    max_input_length=None,
    use_tpu=False
)
```



Defined in [`tensorflow/contrib/recurrent/python/ops/recurrent.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/recurrent/python/ops/recurrent.py).

Compute a recurrent neural net.

Roughly, Recurrent() computes the following:
  state = state0
  for t in inputs' sequence length:
    state = cell_fn(theta, state, inputs[t, :])
    accumulate_state[t, :] = state
  return accumulate_state, state

theta, state, inputs are all structures of tensors.

inputs[t, :] means taking a slice out from every tensor in the inputs.

accumulate_state[t, :] = state means that we stash every tensor in
'state' into a slice of the corresponding tensor in
accumulate_state.

cell_fn is a python callable computing (building up a TensorFlow
graph) the recurrent neural network's one forward step. Two calls of
cell_fn must describe two identical computations.

By construction, Recurrent()'s backward computation does not access
any intermediate values computed by cell_fn during forward
computation. We may extend Recurrent() to support that by taking a
customized backward function of cell_fn.

#### Args:

* <b>`theta`</b>: weights. A structure of tensors.
* <b>`state0`</b>: initial state. A structure of tensors.
* <b>`inputs`</b>: inputs. A structure of tensors.
* <b>`cell_fn`</b>: A python function, which computes:
    state1, extras = cell_fn(theta, state0, inputs[t, :])
* <b>`cell_grad`</b>: A python function which computes:
    dtheta, dstate0, dinputs[t, :] = cell_grad(
      theta, state0, inputs[t, :], extras, dstate1)
* <b>`extras`</b>: A structure of tensors. The 2nd return value of every
    invocation of cell_fn is a structure of tensors with matching keys
    and shapes of  this `extras`.
* <b>`max_input_length`</b>: maximum length of effective input. This is used to
    truncate the computation if the inputs have been allocated to a
    larger size. A scalar tensor.
* <b>`use_tpu`</b>: whether or not we are on TPU.


#### Returns:

accumulate_state and the final state.