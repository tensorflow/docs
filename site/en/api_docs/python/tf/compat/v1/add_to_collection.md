page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.add_to_collection


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/ops.py#L6156-L6171">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Wrapper for `Graph.add_to_collection()` using the default graph.

``` python
tf.compat.v1.add_to_collection(
    name,
    value
)
```



<!-- Placeholder for "Used in" -->

See <a href="../../../tf/Graph#add_to_collection"><code>tf.Graph.add_to_collection</code></a>
for more details.

#### Args:


* <b>`name`</b>: The key for the collection. For example, the `GraphKeys` class
  contains many standard names for collections.
* <b>`value`</b>: The value to add to the collection.

#### Eager Compatibility
Collections are only supported in eager when variables are created inside
an EagerVariableStore (e.g. as part of a layer or template).
