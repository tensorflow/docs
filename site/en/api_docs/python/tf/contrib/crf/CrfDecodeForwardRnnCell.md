page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.crf.CrfDecodeForwardRnnCell

## Class `CrfDecodeForwardRnnCell`

Computes the forward decoding in a linear-chain CRF.

Inherits From: [`RNNCell`](../../../tf/nn/rnn_cell/RNNCell)



Defined in [`contrib/crf/python/ops/crf.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/crf/python/ops/crf.py).

<!-- Placeholder for "Used in" -->
  

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(transition_params)
```

Initialize the CrfDecodeForwardRnnCell.


#### Args:


* <b>`transition_params`</b>: A [num_tags, num_tags] matrix of binary
  potentials. This matrix is expanded into a
  [1, num_tags, num_tags] in preparation for the broadcast
  summation occurring within the cell.



## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="output_size"><code>output_size</code></h3>




<h3 id="scope_name"><code>scope_name</code></h3>




<h3 id="state_size"><code>state_size</code></h3>






## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

``` python
get_initial_state(
    inputs=None,
    batch_size=None,
    dtype=None
)
```




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
`N-D` tensor of shape `[batch_size, state_size]` filled with zeros.

If `state_size` is a nested list or tuple, then the return value is
a nested list or tuple (of the same structure) of `2-D` tensors with
the shapes `[batch_size, s]` for each s in `state_size`.




