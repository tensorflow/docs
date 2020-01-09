page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.scale_regularization_loss


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/nn/scale_regularization_loss">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_impl.py#L441-L476">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Scales the sum of the given regularization losses by number of replicas.

### Aliases:

* <a href="/api_docs/python/tf/nn/scale_regularization_loss"><code>tf.compat.v1.nn.scale_regularization_loss</code></a>
* <a href="/api_docs/python/tf/nn/scale_regularization_loss"><code>tf.compat.v2.nn.scale_regularization_loss</code></a>


``` python
tf.nn.scale_regularization_loss(regularization_loss)
```



<!-- Placeholder for "Used in" -->

Usage with distribution strategy and custom training loop:

```python
with strategy.scope():
  def compute_loss(self, label, predictions):
    per_example_loss = tf.keras.losses.sparse_categorical_crossentropy(
        labels, predictions)

    # Compute loss that is scaled by sample_weight and by global batch size.
    loss = tf.compute_average_loss(
        per_example_loss,
        sample_weight=sample_weight,
        global_batch_size=GLOBAL_BATCH_SIZE)

    # Add scaled regularization losses.
    loss += tf.scale_regularization_loss(tf.nn.l2_loss(weights))
    return loss
```

#### Args:


* <b>`regularization_loss`</b>: Regularization loss.


#### Returns:

Scalar loss value.
