page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.OptimizationOptions

## Class `OptimizationOptions`

Represents options for dataset optimizations.



### Aliases:

* Class `tf.compat.v1.data.experimental.OptimizationOptions`
* Class `tf.compat.v2.data.experimental.OptimizationOptions`
* Class `tf.data.experimental.OptimizationOptions`



Defined in [`python/data/experimental/ops/optimization_options.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/experimental/ops/optimization_options.py).

<!-- Placeholder for "Used in" -->

You can set the optimization options of a dataset through the
`experimental_optimization` property of <a href="../../../tf/data/Options"><code>tf.data.Options</code></a>; the property is
an instance of <a href="../../../tf/data/experimental/OptimizationOptions"><code>tf.data.experimental.OptimizationOptions</code></a>.

```python
options = tf.data.Options()
options.experimental_optimization.noop_elimination = True
options.experimental_optimization.map_vectorization.enabled = True
options.experimental_optimization.apply_default_optimizations = False
dataset = dataset.with_options(options)
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__()
```






## Properties

<h3 id="apply_default_optimizations"><code>apply_default_optimizations</code></h3>

Whether to apply default static optimizations. If False, only static optimizations that have been explicitly enabled will be applied.


<h3 id="autotune"><code>autotune</code></h3>

Whether to automatically tune performance knobs. If None, defaults to True.


<h3 id="autotune_cpu_budget"><code>autotune_cpu_budget</code></h3>

When autotuning is enabled (through `autotune`), determines the CPU budget to use. Values greater than the number of schedulable CPU cores are allowed but may result in CPU contention. If None, defaults to the number of schedulable CPU cores.


<h3 id="filter_fusion"><code>filter_fusion</code></h3>

Whether to fuse filter transformations. If None, defaults to False.


<h3 id="filter_with_random_uniform_fusion"><code>filter_with_random_uniform_fusion</code></h3>

Whether to fuse filter dataset that predicts random_uniform < rate into a sampling dataset. If None, defaults to False.


<h3 id="hoist_random_uniform"><code>hoist_random_uniform</code></h3>

Whether to hoist <a href="../../../tf/random/uniform"><code>tf.random_uniform()</code></a> ops out of map transformations. If None, defaults to False.


<h3 id="map_and_batch_fusion"><code>map_and_batch_fusion</code></h3>

Whether to fuse map and batch transformations. If None, defaults to True.


<h3 id="map_and_filter_fusion"><code>map_and_filter_fusion</code></h3>

Whether to fuse map and filter transformations. If None, defaults to False.


<h3 id="map_fusion"><code>map_fusion</code></h3>

Whether to fuse map transformations. If None, defaults to False.


<h3 id="map_parallelization"><code>map_parallelization</code></h3>

Whether to parallelize stateless map transformations. If None, defaults to False.


<h3 id="map_vectorization"><code>map_vectorization</code></h3>

The map vectorization options associated with the dataset. See <a href="../../../tf/data/experimental/MapVectorizationOptions"><code>tf.data.experimental.MapVectorizationOptions</code></a> for more details.


<h3 id="noop_elimination"><code>noop_elimination</code></h3>

Whether to eliminate no-op transformations. If None, defaults to True.


<h3 id="parallel_batch"><code>parallel_batch</code></h3>

Whether to parallelize copying of batch elements. If None, defaults to False.


<h3 id="shuffle_and_repeat_fusion"><code>shuffle_and_repeat_fusion</code></h3>

Whether to fuse shuffle and repeat transformations. If None, defaults to True.




## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```




<h3 id="__ne__"><code>__ne__</code></h3>

``` python
__ne__(other)
```






