page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.add_to_collection


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L6153-L6168">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Wrapper for <a href="../tf/Graph#add_to_collection"><code>Graph.add_to_collection()</code></a> using the default graph.

### Aliases:

* <a href="/api_docs/python/tf/add_to_collection"><code>tf.compat.v1.add_to_collection</code></a>


``` python
tf.add_to_collection(
    name,
    value
)
```



<!-- Placeholder for "Used in" -->

See <a href="../tf/Graph#add_to_collection"><code>tf.Graph.add_to_collection</code></a>
for more details.

#### Args:


* <b>`name`</b>: The key for the collection. For example, the `GraphKeys` class
  contains many standard names for collections.
* <b>`value`</b>: The value to add to the collection.

#### Eager Compatibility
Collections are only supported in eager when variables are created inside
an EagerVariableStore (e.g. as part of a layer or template).
