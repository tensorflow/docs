page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.get_strategy

### Aliases:

* `tf.contrib.distribute.get_distribution_strategy`
* `tf.distribute.get_strategy`

``` python
tf.distribute.get_strategy()
```



Defined in [`tensorflow/python/distribute/distribution_strategy_context.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/distribution_strategy_context.py).

Returns the current <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object.

Typically only used in a cross-replica context:

```
if tf.distribute.in_cross_replica_context():
  strategy = tf.distribute.get_strategy()
  ...
```

#### Returns:

A <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object. Inside a
`with distribution_strategy.scope()` block, it returns
`distribution_strategy`, otherwise it returns the default
(single-replica) <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object.