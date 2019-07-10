page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.rnn_cell.GRUCell

## Class `GRUCell`

Gated Recurrent Unit cell (cf.

Inherits From: [`LayerRNNCell`](../../../tf/contrib/rnn/LayerRNNCell)

### Aliases:

* Class `tf.compat.v1.nn.rnn_cell.GRUCell`
* Class `tf.contrib.rnn.GRUCell`
* Class `tf.nn.rnn_cell.GRUCell`



Defined in [`python/ops/rnn_cell_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/rnn_cell_impl.py).

<!-- Placeholder for "Used in" -->

http://arxiv.org/abs/1406.1078).

Note that this cell is not optimized for performance. Please use
<a href="../../../tf/contrib/cudnn_rnn/CudnnGRU"><code>tf.contrib.cudnn_rnn.CudnnGRU</code></a> for better performance on GPU, or
<a href="../../../tf/contrib/rnn/GRUBlockCellV2"><code>tf.contrib.rnn.GRUBlockCellV2</code></a> for better performance on CPU.

#### Args:


* <b>`num_units`</b>: int, The number of units in the GRU cell.
* <b>`activation`</b>: Nonlinearity to use.  Default: `tanh`.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables in an
  existing scope.  If not `True`, and the existing scope already has the
  given variables, an error is raised.
* <b>`kernel_initializer`</b>: (optional) The initializer to use for the weight and
  projection matrices.
* <b>`bias_initializer`</b>: (optional) The initializer to use for the bias.
* <b>`name`</b>: String, the name of the layer. Layers with the same name will share
  weights, but to avoid mistakes we require reuse=True in such cases.
* <b>`dtype`</b>: Default dtype of the layer (default of `None` means use the type of
  the first input). Required when `build` is called before `call`.
* <b>`**kwargs`</b>: Dict, keyword named properties for common layer attributes, like
  `trainable` etc when constructing the cell from configs of get_config().

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units,
    activation=None,
    reuse=None,
    kernel_initializer=None,
    bias_initializer=None,
    name=None,
    dtype=None,
    **kwargs
)
```

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This class is equivalent as tf.keras.layers.GRUCell, and will be replaced by that in Tensorflow 2.0.



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




