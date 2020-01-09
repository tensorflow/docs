page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.forward_compatibility_horizon


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/compat/forward_compatibility_horizon">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/compat/compat.py#L123-L166">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Context manager for testing forward compatibility of generated graphs.

### Aliases:

* <a href="/api_docs/python/tf/compat/forward_compatibility_horizon"><code>tf.compat.v1.compat.forward_compatibility_horizon</code></a>
* <a href="/api_docs/python/tf/compat/forward_compatibility_horizon"><code>tf.compat.v2.compat.forward_compatibility_horizon</code></a>


``` python
tf.compat.forward_compatibility_horizon(
    year,
    month,
    day
)
```



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

#### Args:


* <b>`year`</b>:  A year (e.g., 2018). Must be an `int`.
* <b>`month`</b>: A month (1 <= month <= 12) in year. Must be an `int`.
* <b>`day`</b>:   A day (1 <= day <= 31, or 30, or 29, or 28) in month. Must be an
  `int`.


#### Yields:

Nothing.
