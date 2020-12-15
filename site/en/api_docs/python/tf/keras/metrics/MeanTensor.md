description: Computes the element-wise (weighted) mean of the given tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.metrics.MeanTensor" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="reset_states"/>
<meta itemprop="property" content="result"/>
<meta itemprop="property" content="update_state"/>
</div>

# tf.keras.metrics.MeanTensor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L2854-L2961">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the element-wise (weighted) mean of the given tensors.

Inherits From: [`Metric`](../../../tf/keras/metrics/Metric.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.metrics.MeanTensor`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.metrics.MeanTensor`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.metrics.MeanTensor(
    name='mean_tensor', dtype=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`MeanTensor` returns a tensor with the same shape of the input tensors. The
mean value is updated by keeping local variables `total` and `count`. The
`total` tracks the sum of the weighted values, and `count` stores the sum of
the weighted counts.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
(Optional) string name of the metric instance.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
(Optional) data type of the metric result.
</td>
</tr>
</table>



#### Standalone usage:



```
>>> m = tf.keras.metrics.MeanTensor()
>>> m.update_state([0, 1, 2, 3])
>>> m.update_state([4, 5, 6, 7])
>>> m.result().numpy()
array([2., 3., 4., 5.], dtype=float32)
```

```
>>> m.update_state([12, 10, 8, 6], sample_weight= [0, 0.2, 0.5, 1])
>>> m.result().numpy()
array([2.       , 3.6363635, 4.8      , 5.3333335], dtype=float32)
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`count`
</td>
<td>

</td>
</tr><tr>
<td>
`total`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L2958-L2961">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_states()
</code></pre>

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L2950-L2956">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>result()
</code></pre>

Computes and returns the metric value tensor.

Result computation is an idempotent operation that simply calculates the
metric value using the state variables.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L2907-L2948">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_state(
    values, sample_weight=None
)
</code></pre>

Accumulates statistics for computing the element-wise mean.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`values`
</td>
<td>
Per-example value.
</td>
</tr><tr>
<td>
`sample_weight`
</td>
<td>
Optional weighting of each example. Defaults to 1.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Update op.
</td>
</tr>

</table>





