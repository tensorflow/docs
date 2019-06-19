page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.add_to_collection

``` python
tf.add_to_collection(
    name,
    value
)
```



Defined in [`tensorflow/python/framework/ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/framework/ops.py).

See the guide: [Building Graphs > Graph collections](../../../api_guides/python/framework#Graph_collections)

Wrapper for `Graph.add_to_collection()` using the default graph.

See <a href="../tf/Graph#add_to_collection"><code>tf.Graph.add_to_collection</code></a>
for more details.

#### Args:

* <b>`name`</b>: The key for the collection. For example, the `GraphKeys` class
    contains many standard names for collections.
* <b>`value`</b>: The value to add to the collection.



#### Eager Compatibility
Collections are not supported when eager execution is enabled.

