description: Return true if the forward compatibility window has expired.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.forward_compatible" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.forward_compatible

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/compat/compat.py#L63-L120">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Return true if the forward compatibility window has expired.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.compat.forward_compatible`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.forward_compatible(
    year, month, day
)
</code></pre>



<!-- Placeholder for "Used in" -->

See [Version
compatibility](https://tensorflow.org/guide/version_compat#backward_forward).

Forward-compatibility refers to scenarios where the producer of a TensorFlow
model (a GraphDef or SavedModel) is compiled against a version of the
TensorFlow library newer than what the consumer was compiled against. The
"producer" is typically a Python program that constructs and trains a model
while the "consumer" is typically another program that loads and serves the
model.

TensorFlow has been supporting a 3 week forward-compatibility window for
programs compiled from source at HEAD.

For example, consider the case where a new operation `MyNewAwesomeAdd` is
created with the intent of replacing the implementation of an existing Python
wrapper - <a href="../../tf/math/add.md"><code>tf.add</code></a>.  The Python wrapper implementation should change from
something like:

```python
def add(inputs, name=None):
  return gen_math_ops.add(inputs, name)
```

to:

```python
from tensorflow.python.compat import compat

def add(inputs, name=None):
  if compat.forward_compatible(year, month, day):
    # Can use the awesome new implementation.
    return gen_math_ops.my_new_awesome_add(inputs, name)
  # To maintain forward compatibility, use the old implementation.
  return gen_math_ops.add(inputs, name)
```

Where `year`, `month`, and `day` specify the date beyond which binaries
that consume a model are expected to have been updated to include the
new operations. This date is typically at least 3 weeks beyond the date
the code that adds the new operation is committed.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`year`
</td>
<td>
A year (e.g., 2018). Must be an `int`.
</td>
</tr><tr>
<td>
`month`
</td>
<td>
A month (1 <= month <= 12) in year. Must be an `int`.
</td>
</tr><tr>
<td>
`day`
</td>
<td>
A day (1 <= day <= 31, or 30, or 29, or 28) in month. Must be an
`int`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
True if the caller can expect that serialized TensorFlow graphs produced
can be consumed by programs that are compiled with the TensorFlow library
source code after (year, month, day).
</td>
</tr>

</table>

