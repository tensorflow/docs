

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.get_collection

``` python
get_collection(
    key,
    scope=None
)
```



Defined in [`tensorflow/python/framework/ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/framework/ops.py).

See the guide: [Building Graphs > Graph collections](../../../api_guides/python/framework#Graph_collections)

Wrapper for `Graph.get_collection()` using the default graph.

See [`tf.Graph.get_collection`](../tf/Graph#get_collection)
for more details.

#### Args:

* <b>`key`</b>: The key for the collection. For example, the `GraphKeys` class
    contains many standard names for collections.
* <b>`scope`</b>: (Optional.) If supplied, the resulting list is filtered to include
    only items whose `name` attribute matches using `re.match`. Items
    without a `name` attribute are never returned if a scope is supplied and
    the choice or `re.match` means that a `scope` without special tokens
    filters by prefix.


#### Returns:

The list of values in the collection with the given `name`, or
an empty list if no value has been added to that collection. The
list contains the values in the order under which they were
collected.