page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.RevBlock

## Class `RevBlock`

Block of reversible layers. See rev_block.

Inherits From: [`Layer`](../../../tf/layers/Layer)



Defined in [`contrib/layers/python/layers/rev_block_lib.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/rev_block_lib.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    f,
    g,
    num_layers=1,
    f_side_input=None,
    g_side_input=None,
    use_efficient_backprop=True,
    name='revblock',
    **kwargs
)
```






## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="scope_name"><code>scope_name</code></h3>






## Methods

<h3 id="backward"><code>backward</code></h3>

``` python
backward(
    y1,
    y2
)
```




<h3 id="forward"><code>forward</code></h3>

``` python
forward(
    x1,
    x2
)
```






