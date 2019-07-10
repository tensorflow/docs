page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.rnn_cell.ResidualWrapper

## Class `ResidualWrapper`

RNNCell wrapper that ensures cell inputs are added to the outputs.



### Aliases:

* Class `tf.compat.v1.nn.rnn_cell.ResidualWrapper`
* Class `tf.contrib.rnn.ResidualWrapper`
* Class `tf.nn.rnn_cell.ResidualWrapper`



Defined in [`python/ops/rnn_cell_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/rnn_cell_impl.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    *args,
    **kwargs
)
```

Constructs a `ResidualWrapper` for `cell`.


#### Args:


* <b>`cell`</b>: An instance of `RNNCell`.
* <b>`residual_fn`</b>: (Optional) The function to map raw cell inputs and raw cell
  outputs to the actual cell outputs of the residual network.
  Defaults to calling nest.map_structure on (lambda i, o: i + o), inputs
    and outputs.



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






