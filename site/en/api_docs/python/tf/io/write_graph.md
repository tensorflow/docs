description: Writes a graph proto to a file.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.write_graph" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.write_graph

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/framework/graph_io.py#L30-L75">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Writes a graph proto to a file.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.io.write_graph`, `tf.compat.v1.train.write_graph`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.write_graph(
    graph_or_graph_def, logdir, name, as_text=(True)
)
</code></pre>



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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`graph_or_graph_def`
</td>
<td>
A `Graph` or a `GraphDef` protocol buffer.
</td>
</tr><tr>
<td>
`logdir`
</td>
<td>
Directory where to write the graph. This can refer to remote
filesystems, such as Google Cloud Storage (GCS).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Filename for the graph.
</td>
</tr><tr>
<td>
`as_text`
</td>
<td>
If `True`, writes the graph as an ASCII proto.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The path of the output proto file.
</td>
</tr>

</table>

