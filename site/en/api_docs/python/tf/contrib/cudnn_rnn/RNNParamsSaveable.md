

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.cudnn_rnn.RNNParamsSaveable

### `class tf.contrib.cudnn_rnn.RNNParamsSaveable`



Defined in [`tensorflow/contrib/cudnn_rnn/python/ops/cudnn_rnn_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/cudnn_rnn/python/ops/cudnn_rnn_ops.py).

SaveableObject implementation that handles the RNN params variable.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    params_to_canonical,
    canonical_to_params,
    param_variables,
    name='params_canonical'
)
```

Creates a RNNParamsSaveable object.

   RNNParamsSaveable is saveable/restorable in a checkpoint file and is used
   to save/restore the weights and biases parameters in a canonical
   format, where parameters are saved as tensors layer by layer. For each
   layer, the bias tensors are saved following the weight tensors. When
   restoring, a user could name param_variables as desired, and restore
   weight and bias tensors to these variables.

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

* <b>`params_to_canonical`</b>: a function to convert params from a specific format
      for cuDNN or other RNN ops to the canonical format.
      _CudnnRNN.params_to_canonical() should be provided here.
* <b>`canonical_to_params`</b>: a function to convert params from the canonical
      format to a specific format for cuDNN or other RNN ops. The function
      must return a scalar (e.g. in the case of cuDNN) or a tuple. This
      function could be _CudnnRNN.canonical_to_params() or a
      user-defined function.
* <b>`param_variables`</b>: a list of Variables for parameters in a specific form.
      For cuDNN RNN ops, this is a single merged variable for both weights
      and biases; for other RNN ops, this might be multiple unmerged or
      partially merged variables respectively for weights and biases.
* <b>`name`</b>: the name of the RNNParamsSaveable object.

<h3 id="restore"><code>restore</code></h3>

``` python
restore(
    restored_tensors,
    restored_shapes
)
```





