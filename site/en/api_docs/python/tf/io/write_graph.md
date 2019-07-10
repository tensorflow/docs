page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.write_graph

Writes a graph proto to a file.

### Aliases:

* `tf.compat.v1.io.write_graph`
* `tf.compat.v1.train.write_graph`
* `tf.compat.v2.io.write_graph`
* `tf.io.write_graph`
* `tf.train.write_graph`

``` python
tf.io.write_graph(
    graph_or_graph_def,
    logdir,
    name,
    as_text=True
)
```



Defined in [`python/framework/graph_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/graph_io.py).

<!-- Placeholder for "Used in" -->

The graph is written as a text proto unless `as_text` is `False`.

```python
v = tf.Variable(0, name='my_variable')
sess = tf.compat.v1.Session()
tf.io.write_graph(sess.graph_def, '/tmp/my-model', 'train.pbtxt')
```

or

```python
v = tf.Variable(0, name='my_variable')
sess = tf.compat.v1.Session()
tf.io.write_graph(sess.graph, '/tmp/my-model', 'train.pbtxt')
```

#### Args:


* <b>`graph_or_graph_def`</b>: A `Graph` or a `GraphDef` protocol buffer.
* <b>`logdir`</b>: Directory where to write the graph. This can refer to remote
  filesystems, such as Google Cloud Storage (GCS).
* <b>`name`</b>: Filename for the graph.
* <b>`as_text`</b>: If `True`, writes the graph as an ASCII proto.


#### Returns:

The path of the output proto file.
