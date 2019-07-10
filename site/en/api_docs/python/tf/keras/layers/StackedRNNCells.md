page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.StackedRNNCells

## Class `StackedRNNCells`

Wrapper allowing a stack of RNN cells to behave as a single cell.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.StackedRNNCells`
* Class `tf.compat.v2.keras.layers.StackedRNNCells`
* Class `tf.keras.layers.StackedRNNCells`



Defined in [`python/keras/layers/recurrent.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/recurrent.py).

<!-- Placeholder for "Used in" -->

Used to implement efficient stacked RNNs.

#### Arguments:


* <b>`cells`</b>: List of RNN cell instances.


#### Examples:



```python
cells = [
    keras.layers.LSTMCell(output_dim),
    keras.layers.LSTMCell(output_dim),
    keras.layers.LSTMCell(output_dim),
]

inputs = keras.Input((timesteps, input_dim))
x = keras.layers.RNN(cells)(inputs)
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    cells,
    **kwargs
)
```






## Properties

<h3 id="output_size"><code>output_size</code></h3>




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






