description: Unpacks user-provided data tuple.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.utils.unpack_x_y_sample_weight" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.utils.unpack_x_y_sample_weight

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/data_adapter.py#L1412-L1471">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Unpacks user-provided data tuple.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.utils.unpack_x_y_sample_weight(
    data
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a convenience utility to be used when overriding
<a href="../../../tf/keras/Model.md#train_step"><code>Model.train_step</code></a>, <a href="../../../tf/keras/Model.md#test_step"><code>Model.test_step</code></a>, or <a href="../../../tf/keras/Model.md#predict_step"><code>Model.predict_step</code></a>.
This utility makes it easy to support data of the form `(x,)`,
`(x, y)`, or `(x, y, sample_weight)`.

#### Standalone usage:



```
>>> features_batch = tf.ones((10, 5))
>>> labels_batch = tf.zeros((10, 5))
>>> data = (features_batch, labels_batch)
>>> # `y` and `sample_weight` will default to `None` if not provided.
>>> x, y, sample_weight = tf.keras.utils.unpack_x_y_sample_weight(data)
>>> sample_weight is None
True
```

Example in overridden <a href="../../../tf/keras/Model.md#train_step"><code>Model.train_step</code></a>:

```python
class MyModel(tf.keras.Model):

  def train_step(self, data):
    # If `sample_weight` is not provided, all samples will be weighted
    # equally.
    x, y, sample_weight = tf.keras.utils.unpack_x_y_sample_weight(data)

    with tf.GradientTape() as tape:
      y_pred = self(x, training=True)
      loss = self.compiled_loss(
        y, y_pred, sample_weight, regularization_losses=self.losses)
      trainable_variables = self.trainable_variables
      gradients = tape.gradient(loss, trainable_variables)
      self.optimizer.apply_gradients(zip(gradients, trainable_variables))

    self.compiled_metrics.update_state(y, y_pred, sample_weight)
    return {m.name: m.result() for m in self.metrics}
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`data`
</td>
<td>
A tuple of the form `(x,)`, `(x, y)`, or `(x, y, sample_weight)`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The unpacked tuple, with `None`s for `y` and `sample_weight` if they are not
provided.
</td>
</tr>

</table>

