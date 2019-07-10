page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.in_cross_replica_context

### Aliases:

* `tf.contrib.distribute.in_cross_replica_context`
* `tf.distribute.in_cross_replica_context`

``` python
tf.distribute.in_cross_replica_context()
```



Defined in [`tensorflow/python/distribute/distribution_strategy_context.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/distribution_strategy_context.py).

Returns True if in a cross-replica context.

See <a href="../../tf/distribute/get_replica_context"><code>tf.distribute.get_replica_context</code></a> for details.

#### Returns:

True if in a cross-replica context (`get_replica_context()` returns
`None`), or False if in a replica context (`get_replica_context()` returns
non-`None`).