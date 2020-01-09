page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.ControlOutputs


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/util.py#L338-L390">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ControlOutputs`

The control outputs topology.



<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/util.py#L341-L358">View source</a>

``` python
__init__(graph)
```

Create a dictionary of control-output dependencies.


#### Args:


* <b>`graph`</b>: a <a href="../../../tf/Graph"><code>tf.Graph</code></a>.

#### Returns:

A dictionary where a key is a <a href="../../../tf/Operation"><code>tf.Operation</code></a> instance and the
   corresponding value is a list of all the ops which have the key
   as one of their control-input dependencies.


#### Raises:


* <b>`TypeError`</b>: graph is not a <a href="../../../tf/Graph"><code>tf.Graph</code></a>.



## Properties

<h3 id="graph"><code>graph</code></h3>






## Methods

<h3 id="get"><code>get</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/util.py#L381-L386">View source</a>

``` python
get(op)
```

return the control outputs of op.


<h3 id="get_all"><code>get_all</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/util.py#L378-L379">View source</a>

``` python
get_all()
```




<h3 id="update"><code>update</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/util.py#L360-L364">View source</a>

``` python
update()
```

Update the control outputs if the graph has changed.
