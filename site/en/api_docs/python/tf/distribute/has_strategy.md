page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.has_strategy

### Aliases:

* `tf.contrib.distribute.has_distribution_strategy`
* `tf.distribute.has_strategy`

``` python
tf.distribute.has_strategy()
```



Defined in [`tensorflow/python/distribute/distribution_strategy_context.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/distribution_strategy_context.py).

Return if there is a current non-default <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>.

#### Returns:

True if inside a `with strategy.scope():`.