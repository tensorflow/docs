description: Clears the default graph stack and resets the global default graph.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.reset_default_graph" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.reset_default_graph

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L5986-L6003">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Clears the default graph stack and resets the global default graph.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.reset_default_graph()
</code></pre>



<!-- Placeholder for "Used in" -->

NOTE: The default graph is a property of the current thread. This
function applies only to the current thread.  Calling this function while
a <a href="../../../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a> or <a href="../../../tf/compat/v1/InteractiveSession.md"><code>tf.compat.v1.InteractiveSession</code></a> is active will
result in undefined
behavior. Using any previously created <a href="../../../tf/Operation.md"><code>tf.Operation</code></a> or <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a> objects
after calling this function will result in undefined behavior.
Raises:
  AssertionError: If this function is called within a nested graph.