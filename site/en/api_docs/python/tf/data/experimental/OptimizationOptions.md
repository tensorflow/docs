description: Represents options for dataset optimizations.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.OptimizationOptions" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__ne__"/>
</div>

# tf.data.experimental.OptimizationOptions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/experimental/ops/optimization_options.py#L70-L262">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents options for dataset optimizations.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.OptimizationOptions`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.OptimizationOptions()
</code></pre>



<!-- Placeholder for "Used in" -->

You can set the optimization options of a dataset through the
`experimental_optimization` property of <a href="../../../tf/data/Options.md"><code>tf.data.Options</code></a>; the property is
an instance of <a href="../../../tf/data/experimental/OptimizationOptions.md"><code>tf.data.experimental.OptimizationOptions</code></a>.

```python
options = tf.data.Options()
options.experimental_optimization.noop_elimination = True
options.experimental_optimization.map_vectorization.enabled = True
options.experimental_optimization.apply_default_optimizations = False
dataset = dataset.with_options(options)
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`apply_default_optimizations`
</td>
<td>
Whether to apply default graph optimizations. If False, only graph optimizations that have been explicitly enabled will be applied.
</td>
</tr><tr>
<td>
`autotune`
</td>
<td>
Whether to automatically tune performance knobs. If None, defaults to True.
</td>
</tr><tr>
<td>
`autotune_buffers`
</td>
<td>
When autotuning is enabled (through `autotune`), determines whether to also autotune buffer sizes for datasets with parallelism. If None, defaults to False.
</td>
</tr><tr>
<td>
`autotune_cpu_budget`
</td>
<td>
When autotuning is enabled (through `autotune`), determines the CPU budget to use. Values greater than the number of schedulable CPU cores are allowed but may result in CPU contention. If None, defaults to the number of schedulable CPU cores.
</td>
</tr><tr>
<td>
`filter_fusion`
</td>
<td>
Whether to fuse filter transformations. If None, defaults to False.
</td>
</tr><tr>
<td>
`filter_with_random_uniform_fusion`
</td>
<td>
Whether to fuse filter dataset that predicts random_uniform < rate into a sampling dataset. If None, defaults to False.
</td>
</tr><tr>
<td>
`hoist_random_uniform`
</td>
<td>
Whether to hoist `tf.random_uniform()` ops out of map transformations. If None, defaults to False.
</td>
</tr><tr>
<td>
`map_and_batch_fusion`
</td>
<td>
Whether to fuse map and batch transformations. If None, defaults to True.
</td>
</tr><tr>
<td>
`map_and_filter_fusion`
</td>
<td>
Whether to fuse map and filter transformations. If None, defaults to False.
</td>
</tr><tr>
<td>
`map_fusion`
</td>
<td>
Whether to fuse map transformations. If None, defaults to False.
</td>
</tr><tr>
<td>
`map_parallelization`
</td>
<td>
Whether to parallelize stateless map transformations. If None, defaults to False.
</td>
</tr><tr>
<td>
`map_vectorization`
</td>
<td>
The map vectorization options associated with the dataset. See <a href="../../../tf/data/experimental/MapVectorizationOptions.md"><code>tf.data.experimental.MapVectorizationOptions</code></a> for more details.
</td>
</tr><tr>
<td>
`noop_elimination`
</td>
<td>
Whether to eliminate no-op transformations. If None, defaults to True.
</td>
</tr><tr>
<td>
`parallel_batch`
</td>
<td>
Whether to parallelize copying of batch elements. If None, defaults to False.
</td>
</tr><tr>
<td>
`shuffle_and_repeat_fusion`
</td>
<td>
Whether to fuse shuffle and repeat transformations. If None, defaults to True.
</td>
</tr>
</table>



## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/util/options.py#L37-L43">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Return self==value.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/util/options.py#L45-L49">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ne__(
    other
)
</code></pre>

Return self!=value.




