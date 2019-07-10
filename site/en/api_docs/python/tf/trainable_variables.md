page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.trainable_variables

Returns all variables created with `trainable=True`.

### Aliases:

* `tf.compat.v1.trainable_variables`
* `tf.trainable_variables`

``` python
tf.trainable_variables(scope=None)
```



Defined in [`python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/variables.py).

<!-- Placeholder for "Used in" -->

When passed `trainable=True`, the `Variable()` constructor automatically
adds new variables to the graph collection
<a href="../tf/GraphKeys#TRAINABLE_VARIABLES"><code>GraphKeys.TRAINABLE_VARIABLES</code></a>. This convenience function returns the
contents of that collection.

#### Args:


* <b>`scope`</b>: (Optional.) A string. If supplied, the resulting list is filtered
  to include only items whose `name` attribute matches `scope` using
  `re.match`. Items without a `name` attribute are never returned if a
  scope is supplied. The choice of `re.match` means that a `scope` without
  special tokens filters by prefix.


#### Returns:

A list of Variable objects.
