description: Converts a Python entity into a TensorFlow graph.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.autograph.to_graph" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.autograph.to_graph

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/autograph/impl/api.py#L756-L824">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts a Python entity into a TensorFlow graph.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.autograph.to_graph(
    entity, recursive=(True), arg_values=None, arg_types=None,
    experimental_optional_features=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Also see: <a href="../../../../tf/autograph/to_code.md"><code>tf.autograph.to_code</code></a>, <a href="../../../../tf/function.md"><code>tf.function</code></a>.

Unlike <a href="../../../../tf/function.md"><code>tf.function</code></a>, `to_graph` is a low-level transpiler that converts
Python code to TensorFlow graph code. It does not implement any caching,
variable management or create any actual ops, and is best used where greater
control over the generated TensorFlow graph is desired. Another difference
from <a href="../../../../tf/function.md"><code>tf.function</code></a> is that `to_graph` will not wrap the graph into a
TensorFlow function or a Python callable. Internally, <a href="../../../../tf/function.md"><code>tf.function</code></a> uses
`to_graph`.

_Example Usage_

```python
  def foo(x):
    if x > 0:
      y = x * x
    else:
      y = -x
    return y

  converted_foo = to_graph(foo)

  x = tf.constant(1)
  y = converted_foo(x)  # converted_foo is a TensorFlow Op-like.
  assert is_tensor(y)
```

Supported Python entities include:
  * functions
  * classes
  * object methods

Functions are converted into new functions with converted code.

Classes are converted by generating a new class whose methods use converted
code.

Methods are converted into unbound function that have an additional first
argument called `self`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`entity`
</td>
<td>
Python callable or class to convert.
</td>
</tr><tr>
<td>
`recursive`
</td>
<td>
Whether to recursively convert any functions that the converted
function may call.
</td>
</tr><tr>
<td>
`arg_values`
</td>
<td>
Deprecated.
</td>
</tr><tr>
<td>
`arg_types`
</td>
<td>
Deprecated.
</td>
</tr><tr>
<td>
`experimental_optional_features`
</td>
<td>
`None`, a tuple of, or a single
<a href="../../../../tf/autograph/experimental/Feature.md"><code>tf.autograph.experimental.Feature</code></a> value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Same as `entity`, the converted Python function or class.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If the entity could not be converted.
</td>
</tr>
</table>

