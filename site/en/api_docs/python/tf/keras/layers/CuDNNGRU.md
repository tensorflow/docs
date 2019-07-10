page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.CuDNNGRU

## Class `CuDNNGRU`

Fast GRU implementation backed by cuDNN.



### Aliases:

* Class `tf.compat.v1.keras.layers.CuDNNGRU`
* Class `tf.keras.layers.CuDNNGRU`



Defined in [`python/keras/layers/cudnn_recurrent.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/cudnn_recurrent.py).

<!-- Placeholder for "Used in" -->

More information about cuDNN can be found on the [NVIDIA
developer website](https://developer.nvidia.com/cudnn).
Can only be run on GPU.

#### Arguments:


* <b>`units`</b>: Positive integer, dimensionality of the output space.
* <b>`kernel_initializer`</b>: Initializer for the `kernel` weights matrix, used for
  the linear transformation of the inputs.
* <b>`recurrent_initializer`</b>: Initializer for the `recurrent_kernel` weights
  matrix, used for the linear transformation of the recurrent state.
* <b>`bias_initializer`</b>: Initializer for the bias vector.
* <b>`kernel_regularizer`</b>: Regularizer function applied to the `kernel` weights
  matrix.
* <b>`recurrent_regularizer`</b>: Regularizer function applied to the
  `recurrent_kernel` weights matrix.
* <b>`bias_regularizer`</b>: Regularizer function applied to the bias vector.
* <b>`activity_regularizer`</b>: Regularizer function applied to the output of the
  layer (its "activation").
* <b>`kernel_constraint`</b>: Constraint function applied to the `kernel` weights
  matrix.
* <b>`recurrent_constraint`</b>: Constraint function applied to the
  `recurrent_kernel` weights matrix.
* <b>`bias_constraint`</b>: Constraint function applied to the bias vector.
* <b>`return_sequences`</b>: Boolean. Whether to return the last output in the output
  sequence, or the full sequence.
* <b>`return_state`</b>: Boolean. Whether to return the last state in addition to the
  output.
* <b>`go_backwards`</b>: Boolean (default False). If True, process the input sequence
  backwards and return the reversed sequence.
* <b>`stateful`</b>: Boolean (default False). If True, the last state for each sample
  at index i in a batch will be used as initial state for the sample of
  index i in the following batch.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    units,
    kernel_initializer='glorot_uniform',
    recurrent_initializer='orthogonal',
    bias_initializer='zeros',
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    return_sequences=False,
    return_state=False,
    go_backwards=False,
    stateful=False,
    **kwargs
)
```






## Properties

<h3 id="cell"><code>cell</code></h3>




<h3 id="states"><code>states</code></h3>






## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

``` python
get_initial_state(inputs)
```




<h3 id="reset_states"><code>reset_states</code></h3>

``` python
reset_states(states=None)
```






