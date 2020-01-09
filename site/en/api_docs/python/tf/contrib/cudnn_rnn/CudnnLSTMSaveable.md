page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cudnn_rnn.CudnnLSTMSaveable

## Class `CudnnLSTMSaveable`





Defined in [`tensorflow/contrib/cudnn_rnn/python/ops/cudnn_rnn_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/cudnn_rnn/python/ops/cudnn_rnn_ops.py).

SaveableObject implementation handling Cudnn LSTM opaque params.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    opaque_params,
    num_layers,
    num_units,
    input_size,
    input_mode=CUDNN_INPUT_LINEAR_MODE,
    direction=CUDNN_RNN_UNIDIRECTION,
    scope=None,
    name='cudnn_rnn_saveable'
)
```

Creates a CudnnOpaqueParamsSaveable object.

   CudnnOpaqueParamsSaveable is saveable/restorable in a checkpoint file
   and is used to save/restore the weights and biases parameters in a
   canonical format which is directly consumable by platform-independent tf
   RNN cells. Parameters are saved as tensors layer by layer with weight
   tensors followed by bias tensors, and forward direction followed by
   backward direction (if applicable). When restoring, a user could name
   param_variables as desired, and restore weight and bias tensors to these
   variables.

   For CudnnRNNRelu or CudnnRNNTanh, there are 2 tensors per weight and per
   bias for each layer: tensor 0 is applied to the input from the previous
   layer and tensor 1 to the recurrent input.

   For CudnnLSTM, there are 8 tensors per weight and per bias for each
   layer: tensor 0-3 are applied to the input from the previous layer and
   tensor 4-7 to the recurrent input. Tensor 0 and 4 are for the input gate;
   tensor 1 and 5 the forget gate; tensor 2 and 6 the new memory gate;
   tensor 3 and 7 the output gate.

   For CudnnGRU, there are 6 tensors per weight and per bias for each layer:
   tensor 0-2 are applied to the input from the previous layer and
   tensor 3-5 to the recurrent input. Tensor 0 and 3 are for the reset gate;
   tensor 1 and 4 the update gate; tensor 2 and 5 the new memory gate.

#### Args:

* <b>`opaque_params`</b>: a variable, Cudnn RNN opaque params.
* <b>`num_layers`</b>: the number of layers for the RNN model.
* <b>`num_units`</b>: the number of units within the RNN model.
* <b>`input_size`</b>: the size of the input, it could be different from the
      num_units.
* <b>`input_mode`</b>: indicate whether there is a linear projection between the
      input and the actual computation before the first layer. It could be
      'linear_input', 'skip_input' or 'auto_select'.
      'linear_input' (default) always applies a linear projection of input
      onto RNN hidden state. (standard RNN behavior).
      'skip_input' is only allowed when input_size == num_units;
      'auto_select' implies 'skip_input' when input_size == num_units;
      otherwise, it implies 'linear_input'.
* <b>`direction`</b>: the direction model that the model operates. Could be either
      'unidirectional' or 'bidirectional'
* <b>`scope`</b>: string of VariableScope, the scope of equivalent subgraph
      consisting only platform-independent tf RNN cells.
* <b>`name`</b>: the name of the CudnnOpaqueParamsSaveable object.



## Properties

<h3 id="device"><code>device</code></h3>

The device for SaveSpec Tensors.



## Methods

<h3 id="restore"><code>restore</code></h3>

``` python
restore(
    restored_tensors,
    restored_shapes
)
```





