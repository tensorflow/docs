page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.Options

## Class `Options`

Represents options for tf.data.Dataset.



### Aliases:

* Class `tf.compat.v1.data.Options`
* Class `tf.compat.v2.data.Options`
* Class `tf.data.Options`



Defined in [`python/data/ops/dataset_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/ops/dataset_ops.py).

<!-- Placeholder for "Used in" -->

An `Options` object can be, for instance, used to control which static
optimizations to apply or whether to use performance modeling to dynamically
tune the parallelism of operations such as <a href="../../tf/data/Dataset#map"><code>tf.data.Dataset.map</code></a> or
<a href="../../tf/data/Dataset#interleave"><code>tf.data.Dataset.interleave</code></a>.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__()
```






## Properties

<h3 id="experimental_deterministic"><code>experimental_deterministic</code></h3>

Whether the outputs need to be produced in deterministic order. If None, defaults to True.


<h3 id="experimental_distribute"><code>experimental_distribute</code></h3>

The distribution options associated with the dataset. See <a href="../../tf/data/experimental/DistributeOptions"><code>tf.data.experimental.DistributeOptions</code></a> for more details.


<h3 id="experimental_optimization"><code>experimental_optimization</code></h3>

The optimization options associated with the dataset. See <a href="../../tf/data/experimental/OptimizationOptions"><code>tf.data.experimental.OptimizationOptions</code></a> for more details.


<h3 id="experimental_slack"><code>experimental_slack</code></h3>

Whether to introduce 'slack' in the last `prefetch` of the input pipeline, if it exists. This may reduce CPU contention with accelerator host-side activity at the start of a step. The slack frequency is determined by the number of devices attached to this input pipeline. If None, defaults to False.


<h3 id="experimental_stats"><code>experimental_stats</code></h3>

The statistics options associated with the dataset. See <a href="../../tf/data/experimental/StatsOptions"><code>tf.data.experimental.StatsOptions</code></a> for more details.


<h3 id="experimental_threading"><code>experimental_threading</code></h3>

The threading options associated with the dataset. See <a href="../../tf/data/experimental/ThreadingOptions"><code>tf.data.experimental.ThreadingOptions</code></a> for more details.




## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```




<h3 id="__ne__"><code>__ne__</code></h3>

``` python
__ne__(other)
```




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

New <a href="../../tf/data/Options"><code>tf.data.Options()</code></a> object which is the result of merging self with
the input <a href="../../tf/data/Options"><code>tf.data.Options</code></a>.




