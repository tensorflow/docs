page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.get_collection_ref

``` python
tf.get_collection_ref(key)
```



Defined in [`tensorflow/python/framework/ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/framework/ops.py).

Wrapper for `Graph.get_collection_ref()` using the default graph.

See <a href="../tf/Graph#get_collection_ref"><code>tf.Graph.get_collection_ref</code></a>
for more details.

#### Args:

* <b>`key`</b>: The key for the collection. For example, the `GraphKeys` class
    contains many standard names for collections.


#### Returns:

The list of values in the collection with the given `name`, or an empty
list if no value has been added to that collection.  Note that this returns
the collection list itself, which can be modified in place to change the
collection.



#### Eager Compatibility
Collections are not supported when eager execution is enabled.

