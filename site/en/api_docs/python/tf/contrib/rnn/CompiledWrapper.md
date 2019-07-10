page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.CompiledWrapper

## Class `CompiledWrapper`

Wraps step execution in an XLA JIT scope.

Inherits From: [`RNNCell`](../../../tf/nn/rnn_cell/RNNCell)



Defined in [`contrib/rnn/python/ops/rnn_cell.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/rnn_cell.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    cell,
    compile_stateful=False
)
```

Create CompiledWrapper cell.


#### Args:


* <b>`cell`</b>: Instance of `RNNCell`.
* <b>`compile_stateful`</b>: Whether to compile stateful ops like initializers
  and random number generators (default: False).



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






