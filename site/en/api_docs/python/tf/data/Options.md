page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.Options


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/data/Options">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/ops/dataset_ops.py#L2201-L2314">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Options`

Represents options for tf.data.Dataset.



### Aliases:

* Class <a href="/api_docs/python/tf/data/Options"><code>tf.compat.v1.data.Options</code></a>
* Class <a href="/api_docs/python/tf/data/Options"><code>tf.compat.v2.data.Options</code></a>


<!-- Placeholder for "Used in" -->

An `Options` object can be, for instance, used to control which static
optimizations to apply or whether to use performance modeling to dynamically
tune the parallelism of operations such as <a href="../../tf/data/Dataset#map"><code>tf.data.Dataset.map</code></a> or
<a href="../../tf/data/Dataset#interleave"><code>tf.data.Dataset.interleave</code></a>.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/util/options.py#L33-L35">View source</a>

``` python
__init__()
```

Initialize self.  See help(type(self)) for accurate signature.




## Properties

<h3 id="experimental_deterministic"><code>experimental_deterministic</code></h3>

Whether the outputs need to be produced in deterministic order. If None, defaults to True.


<h3 id="experimental_distribute"><code>experimental_distribute</code></h3>

The distribution strategy options associated with the dataset. See <a href="../../tf/data/experimental/DistributeOptions"><code>tf.data.experimental.DistributeOptions</code></a> for more details.


<h3 id="experimental_optimization"><code>experimental_optimization</code></h3>

The optimization options associated with the dataset. See <a href="../../tf/data/experimental/OptimizationOptions"><code>tf.data.experimental.OptimizationOptions</code></a> for more details.


<h3 id="experimental_slack"><code>experimental_slack</code></h3>

Whether to introduce 'slack' in the last `prefetch` of the input pipeline, if it exists. This may reduce CPU contention with accelerator host-side activity at the start of a step. The slack frequency is determined by the number of devices attached to this input pipeline. If None, defaults to False.


<h3 id="experimental_stateful_whitelist"><code>experimental_stateful_whitelist</code></h3>

By default, tf.data will refuse to serialize a dataset or checkpoint its iterator if the dataset contains a stateful op as the serialization / checkpointing won't be able to capture its state. Users can -- at their own risk -- override this restriction by explicitly whitelisting stateful ops by specifying them in this list.


<h3 id="experimental_stats"><code>experimental_stats</code></h3>

The statistics options associated with the dataset. See <a href="../../tf/data/experimental/StatsOptions"><code>tf.data.experimental.StatsOptions</code></a> for more details.


<h3 id="experimental_threading"><code>experimental_threading</code></h3>

The threading options associated with the dataset. See <a href="../../tf/data/experimental/ThreadingOptions"><code>tf.data.experimental.ThreadingOptions</code></a> for more details.




## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/util/options.py#L37-L43">View source</a>

``` python
__eq__(other)
```

Return self==value.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/util/options.py#L45-L49">View source</a>

``` python
__ne__(other)
```

Return self!=value.


<h3 id="merge"><code>merge</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/ops/dataset_ops.py#L2298-L2314">View source</a>

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
