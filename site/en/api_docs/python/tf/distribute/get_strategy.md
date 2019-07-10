page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.get_strategy

Returns the current <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object.

### Aliases:

* `tf.compat.v1.distribute.get_strategy`
* `tf.compat.v2.distribute.get_strategy`
* `tf.contrib.distribute.get_distribution_strategy`
* `tf.contrib.distribute.get_strategy`
* `tf.distribute.get_strategy`

``` python
tf.distribute.get_strategy()
```



Defined in [`python/distribute/distribution_strategy_context.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/distribute/distribution_strategy_context.py).

<!-- Placeholder for "Used in" -->

Typically only used in a cross-replica context:

```
if tf.distribute.in_cross_replica_context():
  strategy = tf.distribute.get_strategy()
  ...
```

#### Returns:

A <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object. Inside a `with strategy.scope()` block,
it returns `strategy`, otherwise it returns the default (single-replica)
<a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object.
