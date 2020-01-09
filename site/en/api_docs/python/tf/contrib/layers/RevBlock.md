page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.RevBlock


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/rev_block_lib.py#L176-L380">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `RevBlock`

Block of reversible layers. See rev_block.

Inherits From: [`Layer`](../../../tf/layers/Layer)

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/rev_block_lib.py#L179-L210">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/rev_block_lib.py#L237-L238">View source</a>

``` python
backward(
    y1,
    y2
)
```




<h3 id="forward"><code>forward</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/rev_block_lib.py#L234-L235">View source</a>

``` python
forward(
    x1,
    x2
)
```
