page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.compute_average_loss


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/nn/compute_average_loss">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_impl.py#L385-L438">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Scales per-example losses with sample_weights and computes their average.

### Aliases:

* <a href="/api_docs/python/tf/nn/compute_average_loss"><code>tf.compat.v1.nn.compute_average_loss</code></a>
* <a href="/api_docs/python/tf/nn/compute_average_loss"><code>tf.compat.v2.nn.compute_average_loss</code></a>


``` python
tf.nn.compute_average_loss(
    per_example_loss,
    sample_weight=None,
    global_batch_size=None
)
```



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
    return tf.compute_average_loss(
        per_example_loss,
        sample_weight=sample_weight,
        global_batch_size=GLOBAL_BATCH_SIZE)
```

#### Args:


* <b>`per_example_loss`</b>: Per-example loss.
* <b>`sample_weight`</b>: Optional weighting for each example.
* <b>`global_batch_size`</b>: Optional global batch size value. Defaults to (size of
  first dimension of `losses`) * (number of replicas).


#### Returns:

Scalar loss value.
