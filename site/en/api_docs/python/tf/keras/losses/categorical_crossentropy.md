page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.categorical_crossentropy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/losses/categorical_crossentropy">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/losses.py#L938-L966">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the categorical crossentropy loss.

### Aliases:

* <a href="/api_docs/python/tf/keras/losses/categorical_crossentropy"><code>tf.compat.v1.keras.losses.categorical_crossentropy</code></a>
* <a href="/api_docs/python/tf/keras/losses/categorical_crossentropy"><code>tf.compat.v1.keras.metrics.categorical_crossentropy</code></a>
* <a href="/api_docs/python/tf/keras/losses/categorical_crossentropy"><code>tf.compat.v2.keras.losses.categorical_crossentropy</code></a>
* <a href="/api_docs/python/tf/keras/losses/categorical_crossentropy"><code>tf.compat.v2.keras.metrics.categorical_crossentropy</code></a>
* <a href="/api_docs/python/tf/keras/losses/categorical_crossentropy"><code>tf.compat.v2.losses.categorical_crossentropy</code></a>
* <a href="/api_docs/python/tf/keras/losses/categorical_crossentropy"><code>tf.compat.v2.metrics.categorical_crossentropy</code></a>
* <a href="/api_docs/python/tf/keras/losses/categorical_crossentropy"><code>tf.keras.metrics.categorical_crossentropy</code></a>


``` python
tf.keras.losses.categorical_crossentropy(
    y_true,
    y_pred,
    from_logits=False,
    label_smoothing=0
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`y_true`</b>: tensor of true targets.
* <b>`y_pred`</b>: tensor of predicted targets.
* <b>`from_logits`</b>: Whether `y_pred` is expected to be a logits tensor. By default,
  we assume that `y_pred` encodes a probability distribution.
* <b>`label_smoothing`</b>: Float in [0, 1]. If > `0` then smooth the labels.


#### Returns:

Categorical crossentropy loss value.
