page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.write_graph


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/write_graph">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/graph_io.py#L30-L75">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Writes a graph proto to a file.

### Aliases:

* <a href="/api_docs/python/tf/io/write_graph"><code>tf.compat.v1.io.write_graph</code></a>
* <a href="/api_docs/python/tf/io/write_graph"><code>tf.compat.v1.train.write_graph</code></a>
* <a href="/api_docs/python/tf/io/write_graph"><code>tf.compat.v2.io.write_graph</code></a>
* <a href="/api_docs/python/tf/io/write_graph"><code>tf.train.write_graph</code></a>


``` python
tf.io.write_graph(
    graph_or_graph_def,
    logdir,
    name,
    as_text=True
)
```



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
