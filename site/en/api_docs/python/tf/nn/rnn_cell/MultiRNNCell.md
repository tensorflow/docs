page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.rnn_cell.MultiRNNCell

## Class `MultiRNNCell`

RNN cell composed sequentially of multiple simple cells.

Inherits From: [`RNNCell`](../../../tf/nn/rnn_cell/RNNCell)

### Aliases:

* Class `tf.compat.v1.nn.rnn_cell.MultiRNNCell`
* Class `tf.contrib.rnn.MultiRNNCell`
* Class `tf.nn.rnn_cell.MultiRNNCell`



Defined in [`python/ops/rnn_cell_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/rnn_cell_impl.py).

<!-- Placeholder for "Used in" -->


#### Example:



```python
num_units = [128, 64]
cells = [BasicLSTMCell(num_units=n) for n in num_units]
stacked_rnn_cell = MultiRNNCell(cells)
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    cells,
    state_is_tuple=True
)
```

Create a RNN cell composed sequentially of a number of RNNCells. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This class is equivalent as tf.keras.layers.StackedRNNCells, and will be replaced by that in Tensorflow 2.0.

#### Args:


* <b>`cells`</b>: list of RNNCells that will be composed in this order.
* <b>`state_is_tuple`</b>: If True, accepted and returned states are n-tuples, where
  `n = len(cells)`.  If False, the states are all concatenated along the
  column axis.  This latter behavior will soon be deprecated.


#### Raises:


* <b>`ValueError`</b>: if cells is empty (not allowed), or at least one of the cells
  returns a state tuple but the flag `state_is_tuple` is `False`.



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






