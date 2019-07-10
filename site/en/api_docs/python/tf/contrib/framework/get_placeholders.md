page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_placeholders

``` python
tf.contrib.framework.get_placeholders(graph)
```



Defined in [`tensorflow/contrib/framework/python/framework/graph_util.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/framework/python/framework/graph_util.py).

Get placeholders of a graph.

For example:

```python
a = tf.placeholder(dtype=tf.float32, shape=[2, 2], name='a')
a = tf.placeholder(dtype=tf.int32, shape=[3, 2], name='b')

tf.contrib.framework.get_placeholders(tf.get_default_graph())
# Returns:
#  [<tf.Tensor 'a:0' shape=(2, 2) dtype=float32>,
#   <tf.Tensor 'b:0' shape=(3, 2) dtype=int32>]
```

#### Args:

* <b>`graph`</b>: A tf.Graph.

#### Returns:

A list contains all placeholders of given graph.


#### Raises:

* <b>`TypeError`</b>: If `graph` is not a tensorflow graph.