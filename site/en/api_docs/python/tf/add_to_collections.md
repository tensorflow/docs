

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.add_to_collections

``` python
tf.add_to_collections(
    names,
    value
)
```



Defined in [`tensorflow/python/framework/ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/framework/ops.py).

Wrapper for `Graph.add_to_collections()` using the default graph.

See <a href="../tf/Graph#add_to_collections"><code>tf.Graph.add_to_collections</code></a>
for more details.

#### Args:

* <b>`names`</b>: The key for the collections. The `GraphKeys` class
    contains many standard names for collections.
* <b>`value`</b>: The value to add to the collections.



#### Eager Compatibility
Collections are not supported when eager execution is enabled.

