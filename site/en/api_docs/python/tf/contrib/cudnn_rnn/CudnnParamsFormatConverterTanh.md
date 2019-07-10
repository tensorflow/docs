page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cudnn_rnn.CudnnParamsFormatConverterTanh

## Class `CudnnParamsFormatConverterTanh`

Helper class that converts between params of Cudnn and TF Tanh RNN.





Defined in [`contrib/cudnn_rnn/python/ops/cudnn_rnn_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/cudnn_rnn/python/ops/cudnn_rnn_ops.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_layers,
    num_units,
    input_size,
    input_mode=CUDNN_INPUT_LINEAR_MODE,
    direction=CUDNN_RNN_UNIDIRECTION
)
```

Constructor.


#### Args:


* <b>`num_layers`</b>: the number of layers for the RNN model.
* <b>`num_units`</b>: the number of units within the RNN model.
* <b>`input_size`</b>: the size of the input, it could be different from the
  num_units.
* <b>`input_mode`</b>: indicate whether there is a linear projection between the
  input and the actual computation before the first layer. It could be one
  of 'linear_input', 'skip_input' or 'auto_select'. * 'linear_input'
  (default) always applies a linear projection of input onto RNN hidden
  state. (standard RNN behavior). * 'skip_input' is only allowed when
  input_size == num_units; * 'auto_select' implies 'skip_input' when
  input_size == num_units; otherwise, it implies 'linear_input'.
* <b>`direction`</b>: the direction model that the model operates. Could be either
  'unidirectional' or 'bidirectional'



## Methods

<h3 id="opaque_to_tf_canonical"><code>opaque_to_tf_canonical</code></h3>

``` python
opaque_to_tf_canonical(opaque_param)
```

Converts cudnn opaque param to tf canonical weights.


<h3 id="tf_canonical_to_opaque"><code>tf_canonical_to_opaque</code></h3>

``` python
tf_canonical_to_opaque(tf_canonicals)
```

Converts tf canonical weights to cudnn opaque param.




