page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.InputProjectionWrapper

## Class `InputProjectionWrapper`

Operator adding an input projection to the given cell.

Inherits From: [`RNNCell`](../../../tf/nn/rnn_cell/RNNCell)



Defined in [`contrib/rnn/python/ops/core_rnn_cell.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/core_rnn_cell.py).

<!-- Placeholder for "Used in" -->

Note: in many cases it may be more efficient to not use this wrapper,
but instead concatenate the whole sequence of your inputs in time,
do the projection on this batch-concatenated sequence, then split it.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    cell,
    num_proj,
    activation=None,
    input_size=None,
    reuse=None
)
```

Create a cell with input projection.


#### Args:


* <b>`cell`</b>: an RNNCell, a projection of inputs is added before it.
* <b>`num_proj`</b>: Python integer.  The dimension to project to.
* <b>`activation`</b>: (optional) an optional activation function.
* <b>`input_size`</b>: Deprecated and unused.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
  in an existing scope.  If not `True`, and the existing scope already has
  the given variables, an error is raised.


#### Raises:


* <b>`TypeError`</b>: if cell is not an RNNCell.



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






