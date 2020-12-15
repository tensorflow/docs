description: A transformation that resamples a dataset to achieve a target distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.rejection_resample" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.rejection_resample

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/experimental/ops/resampling.py#L36-L106">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A transformation that resamples a dataset to achieve a target distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.rejection_resample`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.rejection_resample(
    class_func, target_dist, initial_dist=None, seed=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

**NOTE** Resampling is performed via rejection sampling; some fraction
of the input values will be dropped.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`class_func`
</td>
<td>
A function mapping an element of the input dataset to a scalar
<a href="../../../tf.md#int32"><code>tf.int32</code></a> tensor. Values should be in `[0, num_classes)`.
</td>
</tr><tr>
<td>
`target_dist`
</td>
<td>
A floating point type tensor, shaped `[num_classes]`.
</td>
</tr><tr>
<td>
`initial_dist`
</td>
<td>
(Optional.)  A floating point type tensor, shaped
`[num_classes]`.  If not provided, the true class distribution is
estimated live in a streaming fashion.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
(Optional.) Python integer seed for the resampler.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset.md#apply"><code>tf.data.Dataset.apply</code></a>.
</td>
</tr>

</table>

