description: Context manager for testing forward compatibility of generated graphs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.forward_compatibility_horizon" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.forward_compatibility_horizon

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/compat/compat.py#L123-L166">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Context manager for testing forward compatibility of generated graphs.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.compat.forward_compatibility_horizon`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@tf_contextlib.contextmanager</code>
<code>tf.compat.forward_compatibility_horizon(
    year, month, day
)
</code></pre>



<!-- Placeholder for "Used in" -->

See [Version
compatibility](https://tensorflow.org/guide/version_compat#backward_forward).

To ensure forward compatibility of generated graphs (see `forward_compatible`)
with older binaries, new features can be gated with:

```python
if compat.forward_compatible(year=2018, month=08, date=01):
  generate_graph_with_new_features()
else:
  generate_graph_so_older_binaries_can_consume_it()
```

However, when adding new features, one may want to unittest it before
the forward compatibility window expires. This context manager enables
such tests. For example:

```python
from tensorflow.python.compat import compat

def testMyNewFeature(self):
  with compat.forward_compatibility_horizon(2018, 08, 02):
     # Test that generate_graph_with_new_features() has an effect
```

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



#### Yields:

Nothing.
