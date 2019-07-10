page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_placeholders

Get placeholders of a graph.

``` python
tf.contrib.framework.get_placeholders(graph)
```



Defined in [`contrib/framework/python/framework/graph_util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/framework/graph_util.py).

<!-- Placeholder for "Used in" -->


#### For example:



```python
a = tf.compat.v1.placeholder(dtype=tf.float32, shape=[2, 2], name='a')
a = tf.compat.v1.placeholder(dtype=tf.int32, shape=[3, 2], name='b')

tf.contrib.framework.get_placeholders(tf.compat.v1.get_default_graph())
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