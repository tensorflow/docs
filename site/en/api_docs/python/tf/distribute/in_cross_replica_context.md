page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.in_cross_replica_context

Returns True if in a cross-replica context.

### Aliases:

* `tf.compat.v1.distribute.in_cross_replica_context`
* `tf.compat.v2.distribute.in_cross_replica_context`
* `tf.contrib.distribute.in_cross_replica_context`
* `tf.distribute.in_cross_replica_context`

``` python
tf.distribute.in_cross_replica_context()
```



Defined in [`python/distribute/distribution_strategy_context.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/distribute/distribution_strategy_context.py).

<!-- Placeholder for "Used in" -->

See <a href="../../tf/distribute/get_replica_context"><code>tf.distribute.get_replica_context</code></a> for details.

#### Returns:

True if in a cross-replica context (`get_replica_context()` returns
`None`), or False if in a replica context (`get_replica_context()` returns
non-`None`).
