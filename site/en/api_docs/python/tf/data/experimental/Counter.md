description: Creates a Dataset that counts from start in steps of size step.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.Counter" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.Counter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/experimental/ops/counter.py#L28-L55">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a `Dataset` that counts from `start` in steps of size `step`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.Counter(
    start=0, step=1, dtype=tf.dtypes.int64
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### For example:



```python
Dataset.count() == [0, 1, 2, ...)
Dataset.count(2) == [2, 3, ...)
Dataset.count(2, 5) == [2, 7, 12, ...)
Dataset.count(0, -1) == [0, -1, -2, ...)
Dataset.count(10, -1) == [10, 9, ...)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`start`
</td>
<td>
(Optional.) The starting value for the counter. Defaults to 0.
</td>
</tr><tr>
<td>
`step`
</td>
<td>
(Optional.) The step size for the counter. Defaults to 1.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
(Optional.) The data type for counter elements. Defaults to
<a href="../../../tf.md#int64"><code>tf.int64</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Dataset` of scalar `dtype` elements.
</td>
</tr>

</table>

