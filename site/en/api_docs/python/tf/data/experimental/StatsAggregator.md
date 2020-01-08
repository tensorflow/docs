page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.StatsAggregator

## Class `StatsAggregator`





Defined in [`tensorflow/python/data/experimental/ops/stats_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/data/experimental/ops/stats_ops.py).

A stateful resource that aggregates statistics from one or more iterators.

To record statistics, use one of the custom transformation functions defined
in this module when defining your <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a>. All statistics will be
aggregated by the `StatsAggregator` that is associated with a particular
iterator (see below). For example, to record the latency of producing each
element by iterating over a dataset:

```python
dataset = ...
dataset = dataset.apply(tf.data.experimental.latency_stats("total_bytes"))
```

To associate a `StatsAggregator` with a <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> object, use
the following pattern:

```python
stats_aggregator = stats_ops.StatsAggregator()
dataset = ...

# Apply `set_stats_aggregator` to associate `dataset` with `stats_aggregator`.
dataset = dataset.apply(
    tf.data.experimental.set_stats_aggregator(stats_aggregator))
iterator = dataset.make_one_shot_iterator()
```

To get a protocol buffer summary of the currently aggregated statistics,
use the `StatsAggregator.get_summary()` tensor. The easiest way to do this
is to add the returned tensor to the <a href="../../../tf/GraphKeys#SUMMARIES"><code>tf.GraphKeys.SUMMARIES</code></a> collection,
so that the summaries will be included with any existing summaries.

```python
stats_aggregator = stats_ops.StatsAggregator()
# ...
stats_summary = stats_aggregator.get_summary()
tf.add_to_collection(tf.GraphKeys.SUMMARIES, stats_summary)
```

Note: This interface is experimental and expected to change. In particular,
we expect to add other implementations of `StatsAggregator` that provide
different ways of exporting statistics, and add more types of statistics.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__()
```

Creates a `StatsAggregator`.



## Methods

<h3 id="get_summary"><code>get_summary</code></h3>

``` python
get_summary()
```

Returns a string <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> that summarizes the aggregated statistics.

The returned tensor will contain a serialized <a href="../../../tf/Summary"><code>tf.summary.Summary</code></a> protocol
buffer, which can be used with the standard TensorBoard logging facilities.

#### Returns:

A scalar string <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> that summarizes the aggregated statistics.



