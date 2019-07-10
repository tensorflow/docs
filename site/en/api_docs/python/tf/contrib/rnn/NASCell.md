page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.NASCell

## Class `NASCell`

Neural Architecture Search (NAS) recurrent network cell.

Inherits From: [`LayerRNNCell`](../../../tf/contrib/rnn/LayerRNNCell)



Defined in [`contrib/rnn/python/ops/rnn_cell.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/rnn_cell.py).

<!-- Placeholder for "Used in" -->

This implements the recurrent cell from the paper:

  https://arxiv.org/abs/1611.01578

Barret Zoph and Quoc V. Le.
"Neural Architecture Search with Reinforcement Learning" Proc. ICLR 2017.

The class uses an optional projection layer.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units,
    num_proj=None,
    use_bias=False,
    reuse=None,
    **kwargs
)
```

Initialize the parameters for a NAS cell.


#### Args:


* <b>`num_units`</b>: int, The number of units in the NAS cell.
* <b>`num_proj`</b>: (optional) int, The output dimensionality for the projection
  matrices.  If None, no projection is performed.
* <b>`use_bias`</b>: (optional) bool, If True then use biases within the cell. This
  is False by default.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
  in an existing scope.  If not `True`, and the existing scope already has
  the given variables, an error is raised.
* <b>`**kwargs`</b>: Additional keyword arguments.



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




