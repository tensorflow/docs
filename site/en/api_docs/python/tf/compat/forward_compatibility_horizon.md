page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.forward_compatibility_horizon

``` python
tf.compat.forward_compatibility_horizon(
    year,
    month,
    day
)
```



Defined in [`tensorflow/python/compat/compat.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/compat/compat.py).

Context manager for testing forward compatibility of generated graphs.

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

Args :
  year:  A year (e.g. 2018).
  month: A month (1 <= month <= 12) in year.
  day:   A day (1 <= day <= 31, or 30, or 29, or 28) in month.

#### Yields:

Nothing.