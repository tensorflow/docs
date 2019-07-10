page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.Sequential

## Class `Sequential`

Represents a linear sequence of Layers or functions.

Inherits From: [`Network`](../../../tf/contrib/eager/Network)



Defined in [`contrib/eager/python/network.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/eager/python/network.py).

<!-- Placeholder for "Used in" -->

The output of each layer/function is provided as the input to the next.
The inputs passed to `__call__` are passed to the inputs of the first
Layer, and it returns the outputs of the last Layer.

#### Args:


* <b>`layers_funcs`</b>: An optional sequence where each element is either a
  tf.compat.v1.layers.Layer object or a callable.
* <b>`name`</b>: An optional string name to use for this Network.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    layers_funcs=None,
    name=None
)
```






## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="layers"><code>layers</code></h3>




<h3 id="scope_name"><code>scope_name</code></h3>






## Methods

<h3 id="add"><code>add</code></h3>

``` python
add(layer_func)
```




<h3 id="get_layer"><code>get_layer</code></h3>

``` python
get_layer(
    name=None,
    index=None
)
```

Get a contained <a href="../../../tf/layers/Layer"><code>tf.compat.v1.layers.Layer</code></a> either by name or index.


#### Args:


* <b>`name`</b>: String matching one of the names of a contained `Layer`. Note that
  the names of `Layer`s added to `Network`s may not be unique when doing
  layer sharing (i.e. adding a `Layer` to this `Network` which was already
  added to another `Network`). The lowest index `Layer` with a matching
  name will be returned.
* <b>`index`</b>: Integer in [0, number of layers). Layers are assigned an index by
  the order they are added.


#### Returns:

A <a href="../../../tf/layers/Layer"><code>tf.compat.v1.layers.Layer</code></a> object.



#### Raises:


* <b>`ValueError`</b>: If neither or both of 'index' or 'name' is specified, or the
  lookup failed.

<h3 id="track_layer"><code>track_layer</code></h3>

``` python
track_layer(layer)
```

Track a Layer in this Network.

`Network` requires that all `Layer`s used in `call()` be tracked so that the
`Network` can export a complete list of variables.

#### Args:


* <b>`layer`</b>: A <a href="../../../tf/layers/Layer"><code>tf.compat.v1.layers.Layer</code></a> object.


#### Returns:

The passed in `layer`.



#### Raises:


* <b>`RuntimeError`</b>: If __init__ has not been called.
* <b>`TypeError`</b>: If `layer` is the wrong type.
* <b>`ValueError`</b>: If a `Layer` with the same name has already been added.



