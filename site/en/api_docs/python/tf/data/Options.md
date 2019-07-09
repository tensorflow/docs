page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.Options

## Class `Options`





Defined in [`tensorflow/python/data/ops/dataset_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/data/ops/dataset_ops.py).

Represents options for tf.data.Dataset.

An `Options` object can be, for instance, used to control which static
optimizations to apply or whether to use performance modeling to dynamically
tune the parallelism of operations such as <a href="../../tf/data/Dataset#map"><code>tf.data.Dataset.map</code></a> or
<a href="../../tf/data/Dataset#interleave"><code>tf.data.Dataset.interleave</code></a>.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__()
```

Initialize self.  See help(type(self)) for accurate signature.



## Properties

<h3 id="experimental_autotune"><code>experimental_autotune</code></h3>

Whether to dynamically adjust the values of tunable parameters (e.g. degrees of parallelism). If None, defaults to True.

<h3 id="experimental_deterministic"><code>experimental_deterministic</code></h3>

Whether the outputs need to be produced in deterministic order. If None, defaults to True.

<h3 id="experimental_numa_aware"><code>experimental_numa_aware</code></h3>

Whether to use NUMA-aware operations. If None, defaults to False.

<h3 id="experimental_optimization"><code>experimental_optimization</code></h3>

The optimization options associated with the dataset. See <a href="../../tf/data/experimental/OptimizationOptions"><code>tf.data.experimental.OptimizationOptions</code></a> for more details.

<h3 id="experimental_stats"><code>experimental_stats</code></h3>

The statistics options associated with the dataset. See <a href="../../tf/data/experimental/StatsOptions"><code>tf.data.experimental.StatsOptions</code></a> for more details.

<h3 id="experimental_threading"><code>experimental_threading</code></h3>

The threading options associated with the dataset. See <a href="../../tf/data/experimental/ThreadingOptions"><code>tf.data.experimental.ThreadingOptions</code></a> for more details.



## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```

Return self==value.

<h3 id="__ne__"><code>__ne__</code></h3>

``` python
__ne__(other)
```

Return self!=value.

<h3 id="__setattr__"><code>__setattr__</code></h3>

``` python
__setattr__(
    name,
    value
)
```

Implement setattr(self, name, value).

<h3 id="merge"><code>merge</code></h3>

``` python
merge(options)
```

Merges itself with the given <a href="../../tf/data/Options"><code>tf.data.Options</code></a>.

The given <a href="../../tf/data/Options"><code>tf.data.Options</code></a> can be merged as long as there does not exist an
attribute that is set to different values in `self` and `options`.

#### Args:

* <b>`options`</b>: a <a href="../../tf/data/Options"><code>tf.data.Options</code></a> to merge with


#### Raises:

* <b>`ValueError`</b>: if the given <a href="../../tf/data/Options"><code>tf.data.Options</code></a> cannot be merged


#### Returns:

New `tf.data.Options()` object which is the result of merging self with
the input <a href="../../tf/data/Options"><code>tf.data.Options</code></a>.



