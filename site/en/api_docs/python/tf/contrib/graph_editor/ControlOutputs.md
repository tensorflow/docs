

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.graph_editor.ControlOutputs

## Class `ControlOutputs`





Defined in [`tensorflow/contrib/graph_editor/util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/graph_editor/util.py).

See the guide: [Graph Editor (contrib) > Module: util](../../../../../api_guides/python/contrib.graph_editor#Module_util)

The control outputs topology.

## Properties

<h3 id="graph"><code>graph</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(graph)
```

Create a dictionary of control-output dependencies.

#### Args:

* <b>`graph`</b>: a `tf.Graph`.

#### Returns:

A dictionary where a key is a `tf.Operation` instance and the
   corresponding value is a list of all the ops which have the key
   as one of their control-input dependencies.

#### Raises:

* <b>`TypeError`</b>: graph is not a `tf.Graph`.

<h3 id="get"><code>get</code></h3>

``` python
get(op)
```

return the control outputs of op.

<h3 id="get_all"><code>get_all</code></h3>

``` python
get_all()
```



<h3 id="update"><code>update</code></h3>

``` python
update()
```

Update the control outputs if the graph has changed.



