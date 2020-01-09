page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.get_collection_ref


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L6189-L6210">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Wrapper for <a href="../tf/Graph#get_collection_ref"><code>Graph.get_collection_ref()</code></a> using the default graph.

### Aliases:

* <a href="/api_docs/python/tf/get_collection_ref"><code>tf.compat.v1.get_collection_ref</code></a>


``` python
tf.get_collection_ref(key)
```



<!-- Placeholder for "Used in" -->

See <a href="../tf/Graph#get_collection_ref"><code>tf.Graph.get_collection_ref</code></a>
for more details.

#### Args:


* <b>`key`</b>: The key for the collection. For example, the `GraphKeys` class contains
  many standard names for collections.


#### Returns:

The list of values in the collection with the given `name`, or an empty
list if no value has been added to that collection.  Note that this returns
the collection list itself, which can be modified in place to change the
collection.




#### Eager Compatibility
Collections are not supported when eager execution is enabled.
