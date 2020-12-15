description: Scales per-example losses with sample_weights and computes their average.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.compute_average_loss" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.compute_average_loss

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/nn_impl.py#L391-L446">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Scales per-example losses with sample_weights and computes their average.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.compute_average_loss`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.compute_average_loss(
    per_example_loss, sample_weight=None, global_batch_size=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Usage with distribution strategy and custom training loop:

```python
with strategy.scope():
  def compute_loss(labels, predictions, sample_weight=None):

    # If you are using a `Loss` class instead, set reduction to `NONE` so that
    # we can do the reduction afterwards and divide by global batch size.
    per_example_loss = tf.keras.losses.sparse_categorical_crossentropy(
        labels, predictions)

    # Compute loss that is scaled by sample_weight and by global batch size.
    return tf.nn.compute_average_loss(
        per_example_loss,
        sample_weight=sample_weight,
        global_batch_size=GLOBAL_BATCH_SIZE)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`per_example_loss`
</td>
<td>
Per-example loss.
</td>
</tr><tr>
<td>
`sample_weight`
</td>
<td>
Optional weighting for each example.
</td>
</tr><tr>
<td>
`global_batch_size`
</td>
<td>
Optional global batch size value. Defaults to (size of
first dimension of `losses`) * (number of replicas).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Scalar loss value.
</td>
</tr>

</table>

