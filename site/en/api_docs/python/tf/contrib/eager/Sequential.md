page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.Sequential


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/network.py#L531-L575">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Sequential`

Represents a linear sequence of Layers or functions.

Inherits From: [`Network`](../../../tf/contrib/eager/Network)

<!-- Placeholder for "Used in" -->

The output of each layer/function is provided as the input to the next.
The inputs passed to `__call__` are passed to the inputs of the first
Layer, and it returns the outputs of the last Layer.

#### Args:


* <b>`layers_funcs`</b>: An optional sequence where each element is either a
  tf.compat.v1.layers.Layer object or a callable.
* <b>`name`</b>: An optional string name to use for this Network.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/network.py#L544-L549">View source</a>

``` python
__init__(
    layers_funcs=None,
    name=None
)
```

Configure the `Network`. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please inherit from <a href="../../../tf/keras/Model"><code>tf.keras.Model</code></a>, and see its documentation for details. <a href="../../../tf/keras/Model"><code>tf.keras.Model</code></a> should be a drop-in replacement for `tfe.Network` in most cases, but note that `track_layer` is no longer necessary or supported. Instead, `Layer` instances are tracked on attribute assignment (see the section of <a href="../../../tf/keras/Model"><code>tf.keras.Model</code></a>'s documentation on subclassing). Since the output of `track_layer` is often assigned to an attribute anyway, most code can be ported by simply removing the `track_layer` calls.

<a href="../../../tf/keras/Model"><code>tf.keras.Model</code></a> works with all TensorFlow `Layer` instances, including those from <a href="../../../tf/layers"><code>tf.layers</code></a>, but switching to the <a href="../../../tf/keras/layers"><code>tf.keras.layers</code></a> versions along with the migration to <a href="../../../tf/keras/Model"><code>tf.keras.Model</code></a> is recommended, since it will preserve variable names. Feel free to import it with an alias to avoid excess typing :).

#### Args:


* <b>`name`</b>: The name to use for this `Network`. If specified, it must be unique
  in the context where this `Network` is first (1) added to another
  `Network` (in which case it must not share a name with other `Layers`
  added to that `Network`), or (2) built/called (in which case no other
  'top-level' `Network`s may share this name). If unspecified or None, the
  `Network` will be named using its class name, with a number appended if
  necessary for uniqueness (e.g. MyNetwork -> 'my_network_1').


#### Raises:


* <b>`ValueError`</b>: If `name` is not valid. Note that some naming errors will
  instead be raised when the `Network` is called.



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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/network.py#L551-L561">View source</a>

``` python
add(layer_func)
```




<h3 id="get_layer"><code>get_layer</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/network.py#L413-L447">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/network.py#L350-L411">View source</a>

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
