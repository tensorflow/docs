description: Returns True if executing eagerly, even if inside a graph function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.executing_eagerly_outside_functions" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.executing_eagerly_outside_functions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L5744-L5774">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns True if executing eagerly, even if inside a graph function.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.executing_eagerly_outside_functions()
</code></pre>



<!-- Placeholder for "Used in" -->

This function will check the outermost context for the program and see if
it is in eager mode. It is useful comparing to <a href="../../../tf/executing_eagerly.md"><code>tf.executing_eagerly()</code></a>,
which checks the current context and will return `False` within a
<a href="../../../tf/function.md"><code>tf.function</code></a> body. It can be used to build library that behave differently
in eager runtime and v1 session runtime (deprecated).

#### Example:



```
>>> tf.compat.v1.enable_eager_execution()
>>> @tf.function
... def func():
...   # A function constructs TensorFlow graphs, it does not execute eagerly,
...   # but the outer most context is still eager.
...   assert not tf.executing_eagerly()
...   return tf.compat.v1.executing_eagerly_outside_functions()
>>> func()
<tf.Tensor: shape=(), dtype=bool, numpy=True>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
boolean, whether the outermost context is in eager mode.
</td>
</tr>

</table>

