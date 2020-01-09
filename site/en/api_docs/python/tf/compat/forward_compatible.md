page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.forward_compatible


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/compat/forward_compatible">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/compat/compat.py#L63-L120">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Return true if the forward compatibility window has expired.

### Aliases:

* <a href="/api_docs/python/tf/compat/forward_compatible"><code>tf.compat.v1.compat.forward_compatible</code></a>
* <a href="/api_docs/python/tf/compat/forward_compatible"><code>tf.compat.v2.compat.forward_compatible</code></a>


``` python
tf.compat.forward_compatible(
    year,
    month,
    day
)
```



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
wrapper - <a href="../../tf/math/add"><code>tf.add</code></a>.  The Python wrapper implementation should change from
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
  # To maintain forward compatibiltiy, use the old implementation.
  return gen_math_ops.add(inputs, name)
```

Where `year`, `month`, and `day` specify the date beyond which binaries
that consume a model are expected to have been updated to include the
new operations. This date is typically at least 3 weeks beyond the date
the code that adds the new operation is committed.

#### Args:


* <b>`year`</b>:  A year (e.g., 2018). Must be an `int`.
* <b>`month`</b>: A month (1 <= month <= 12) in year. Must be an `int`.
* <b>`day`</b>:   A day (1 <= day <= 31, or 30, or 29, or 28) in month. Must be an
  `int`.


#### Returns:

True if the caller can expect that serialized TensorFlow graphs produced
can be consumed by programs that are compiled with the TensorFlow library
source code after (year, month, day).
