page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.data.experimental.StatsAggregator

## Class `StatsAggregator`

A stateful resource that aggregates statistics from one or more iterators.





Defined in [`python/data/experimental/ops/stats_aggregator.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/experimental/ops/stats_aggregator.py).

<!-- Placeholder for "Used in" -->

To record statistics, use one of the custom transformation functions defined
in this module when defining your <a href="../../../../../tf/data/Dataset"><code>tf.data.Dataset</code></a>. All statistics will be
aggregated by the `StatsAggregator` that is associated with a particular
iterator (see below). For example, to record the latency of producing each
element by iterating over a dataset:

```python
dataset = ...
dataset = dataset.apply(tf.data.experimental.latency_stats("total_bytes"))
```

To associate a `StatsAggregator` with a <a href="../../../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> object, use
the following pattern:

```python
aggregator = tf.data.experimental.StatsAggregator()
dataset = ...

# Apply `StatsOptions` to associate `dataset` with `aggregator`.
options = tf.data.Options()
options.experimental_stats.aggregator = aggregator
dataset = dataset.with_options(options)
```

Note: This interface is experimental and expected to change. In particular,
we expect to add other implementations of `StatsAggregator` that provide
different ways of exporting statistics, and add more types of statistics.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__()
```






