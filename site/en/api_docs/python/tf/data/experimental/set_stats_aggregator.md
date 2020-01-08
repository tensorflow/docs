page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.set_stats_aggregator

``` python
tf.data.experimental.set_stats_aggregator(stats_aggregator)
```



Defined in [`tensorflow/python/data/experimental/ops/stats_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/data/experimental/ops/stats_ops.py).

Set the given `stats_aggregator` for aggregating the input dataset stats.

#### Args:

* <b>`stats_aggregator`</b>: A <a href="../../../tf/data/experimental/StatsAggregator"><code>tf.data.experimental.StatsAggregator</code></a> object.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.