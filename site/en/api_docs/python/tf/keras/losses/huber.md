description: Computes Huber loss value.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.huber" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.losses.huber

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/losses.py#L1421-L1456">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes Huber loss value.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.losses.huber`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.losses.huber(
    y_true, y_pred, delta=1.0
)
</code></pre>



<!-- Placeholder for "Used in" -->

For each value x in `error = y_true - y_pred`:

```
loss = 0.5 * x^2                  if |x| <= d
loss = 0.5 * d^2 + d * (|x| - d)  if |x| > d
```
where d is `delta`. See: https://en.wikipedia.org/wiki/Huber_loss

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`y_true`
</td>
<td>
tensor of true targets.
</td>
</tr><tr>
<td>
`y_pred`
</td>
<td>
tensor of predicted targets.
</td>
</tr><tr>
<td>
`delta`
</td>
<td>
A float, the point where the Huber loss function changes from a
quadratic to linear.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Tensor with one scalar loss entry per sample.
</td>
</tr>

</table>

