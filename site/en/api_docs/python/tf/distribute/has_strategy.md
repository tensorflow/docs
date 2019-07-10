page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.has_strategy

Return if there is a current non-default <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>.

### Aliases:

* `tf.compat.v1.distribute.has_strategy`
* `tf.compat.v2.distribute.has_strategy`
* `tf.contrib.distribute.has_distribution_strategy`
* `tf.contrib.distribute.has_strategy`
* `tf.distribute.has_strategy`

``` python
tf.distribute.has_strategy()
```



Defined in [`python/distribute/distribution_strategy_context.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/distribute/distribution_strategy_context.py).

<!-- Placeholder for "Used in" -->


#### Returns:

True if inside a `with strategy.scope():`.
