description: Returns the default graph for the current thread.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.get_default_graph" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.get_default_graph

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L6006-L6022">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the default graph for the current thread.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.get_default_graph()
</code></pre>



<!-- Placeholder for "Used in" -->

The returned graph will be the innermost graph on which a
`Graph.as_default()` context has been entered, or a global default
graph if none has been explicitly created.

NOTE: The default graph is a property of the current thread. If you
create a new thread, and wish to use the default graph in that
thread, you must explicitly add a `with g.as_default():` in that
thread's function.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The default `Graph` being used in the current thread.
</td>
</tr>

</table>

