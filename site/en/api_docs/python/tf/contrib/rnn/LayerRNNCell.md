page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.LayerRNNCell

## Class `LayerRNNCell`

Subclass of RNNCells that act like proper `tf.Layer` objects.

Inherits From: [`RNNCell`](../../../tf/nn/rnn_cell/RNNCell)



Defined in [`python/ops/rnn_cell_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/rnn_cell_impl.py).

<!-- Placeholder for "Used in" -->

For backwards compatibility purposes, most `RNNCell` instances allow their
`call` methods to instantiate variables via <a href="../../../tf/get_variable"><code>tf.compat.v1.get_variable</code></a>.  The
underlying
variable scope thus keeps track of any variables, and returning cached
versions.  This is atypical of `tf.layer` objects, which separate this
part of layer building into a `build` method that is only called once.

Here we provide a subclass for `RNNCell` objects that act exactly as
`Layer` objects do.  They must provide a `build` method and their
`call` methods do not access Variables <a href="../../../tf/get_variable"><code>tf.compat.v1.get_variable</code></a>.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    trainable=True,
    name=None,
    dtype=None,
    **kwargs
)
```






## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="output_size"><code>output_size</code></h3>

Integer or TensorShape: size of outputs produced by this cell.


<h3 id="scope_name"><code>scope_name</code></h3>




<h3 id="state_size"><code>state_size</code></h3>

size(s) of state(s) used by this cell.

It can be represented by an Integer, a TensorShape or a tuple of Integers
or TensorShapes.



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




