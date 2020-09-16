description: Types of loss reduction.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.losses.Reduction" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="all"/>
<meta itemprop="property" content="validate"/>
<meta itemprop="property" content="MEAN"/>
<meta itemprop="property" content="NONE"/>
<meta itemprop="property" content="SUM"/>
<meta itemprop="property" content="SUM_BY_NONZERO_WEIGHTS"/>
<meta itemprop="property" content="SUM_OVER_BATCH_SIZE"/>
<meta itemprop="property" content="SUM_OVER_NONZERO_WEIGHTS"/>
</div>

# tf.compat.v1.losses.Reduction

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/losses/losses_impl.py#L38-L72">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Types of loss reduction.

<!-- Placeholder for "Used in" -->

Contains the following values:

* `NONE`: Un-reduced weighted losses with the same shape as input.
* `SUM`: Scalar sum of weighted losses.
* `MEAN`: Scalar `SUM` divided by sum of weights. DEPRECATED.
* `SUM_OVER_BATCH_SIZE`: Scalar `SUM` divided by number of elements in losses.
* `SUM_OVER_NONZERO_WEIGHTS`: Scalar `SUM` divided by number of non-zero
   weights. DEPRECATED.
* `SUM_BY_NONZERO_WEIGHTS`: Same as `SUM_OVER_NONZERO_WEIGHTS`. DEPRECATED.

## Methods

<h3 id="all"><code>all</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/losses/losses_impl.py#L59-L67">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>all()
</code></pre>




<h3 id="validate"><code>validate</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/losses/losses_impl.py#L69-L72">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>validate(
    key
)
</code></pre>






## Class Variables

* `MEAN = 'weighted_mean'` <a id="MEAN"></a>
* `NONE = 'none'` <a id="NONE"></a>
* `SUM = 'weighted_sum'` <a id="SUM"></a>
* `SUM_BY_NONZERO_WEIGHTS = 'weighted_sum_by_nonzero_weights'` <a id="SUM_BY_NONZERO_WEIGHTS"></a>
* `SUM_OVER_BATCH_SIZE = 'weighted_sum_over_batch_size'` <a id="SUM_OVER_BATCH_SIZE"></a>
* `SUM_OVER_NONZERO_WEIGHTS = 'weighted_sum_by_nonzero_weights'` <a id="SUM_OVER_NONZERO_WEIGHTS"></a>
