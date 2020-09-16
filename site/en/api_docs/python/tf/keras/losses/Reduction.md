description: Types of loss reduction.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.Reduction" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="all"/>
<meta itemprop="property" content="validate"/>
<meta itemprop="property" content="AUTO"/>
<meta itemprop="property" content="NONE"/>
<meta itemprop="property" content="SUM"/>
<meta itemprop="property" content="SUM_OVER_BATCH_SIZE"/>
</div>

# tf.keras.losses.Reduction

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/losses/loss_reduction.py#L21-L68">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Types of loss reduction.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.losses.Reduction`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->

Contains the following values:

* `AUTO`: Indicates that the reduction option will be determined by the usage
   context. For almost all cases this defaults to `SUM_OVER_BATCH_SIZE`. When
   used with <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>, outside of built-in training loops such
   as <a href="../../../tf/keras.md"><code>tf.keras</code></a> `compile` and `fit`, we expect reduction value to be
   `SUM` or `NONE`. Using `AUTO` in that case will raise an error.
* `NONE`: Weighted losses with one dimension reduced (axis=-1, or axis
   specified by loss function). When this reduction type used with built-in
   Keras training loops like `fit`/`evaluate`, the unreduced vector loss is
   passed to the optimizer but the reported loss will be a scalar value.
* `SUM`: Scalar sum of weighted losses.
* `SUM_OVER_BATCH_SIZE`: Scalar `SUM` divided by number of elements in losses.
   This reduction type is not supported when used with
   <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> outside of built-in training loops like <a href="../../../tf/keras.md"><code>tf.keras</code></a>
   `compile`/`fit`.

   You can implement 'SUM_OVER_BATCH_SIZE' using global batch size like:
   ```
   with strategy.scope():
     loss_obj = tf.keras.losses.CategoricalCrossentropy(
         reduction=tf.keras.losses.Reduction.NONE)
     ....
     loss = tf.reduce_sum(loss_object(labels, predictions)) *
         (1. / global_batch_size)
   ```

Please see the
[custom training guide](https://www.tensorflow.org/tutorials/distribute/custom_training)  
for more details on this.

## Methods

<h3 id="all"><code>all</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/losses/loss_reduction.py#L61-L63">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>all()
</code></pre>




<h3 id="validate"><code>validate</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/losses/loss_reduction.py#L65-L68">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>validate(
    key
)
</code></pre>






## Class Variables

* `AUTO = 'auto'` <a id="AUTO"></a>
* `NONE = 'none'` <a id="NONE"></a>
* `SUM = 'sum'` <a id="SUM"></a>
* `SUM_OVER_BATCH_SIZE = 'sum_over_batch_size'` <a id="SUM_OVER_BATCH_SIZE"></a>
