page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.latency_stats

``` python
tf.data.experimental.latency_stats(tag)
```



Defined in [`tensorflow/python/data/experimental/ops/stats_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/data/experimental/ops/stats_ops.py).

Records the latency of producing each element of the input dataset.

To consume the statistics, associate a `StatsAggregator` with the output
dataset.

#### Args:

* <b>`tag`</b>: String. All statistics recorded by the returned transformation will
    be associated with the given `tag`.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.