page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.KLD


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/losses/KLD">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/losses.py#L992-L1027">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes Kullback-Leibler divergence loss between `y_true` and `y_pred`.

### Aliases:

* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v1.keras.losses.KLD</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v1.keras.losses.kld</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v1.keras.losses.kullback_leibler_divergence</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v1.keras.metrics.KLD</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v1.keras.metrics.kld</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v1.keras.metrics.kullback_leibler_divergence</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v2.keras.losses.KLD</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v2.keras.losses.kld</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v2.keras.losses.kullback_leibler_divergence</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v2.keras.metrics.KLD</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v2.keras.metrics.kld</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v2.keras.metrics.kullback_leibler_divergence</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v2.losses.KLD</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v2.losses.kld</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v2.losses.kullback_leibler_divergence</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v2.metrics.KLD</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v2.metrics.kld</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.compat.v2.metrics.kullback_leibler_divergence</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.keras.losses.kld</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.keras.losses.kullback_leibler_divergence</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.keras.metrics.KLD</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.keras.metrics.kld</code></a>
* <a href="/api_docs/python/tf/keras/losses/KLD"><code>tf.keras.metrics.kullback_leibler_divergence</code></a>


``` python
tf.keras.losses.KLD(
    y_true,
    y_pred
)
```



<!-- Placeholder for "Used in" -->

`loss = y_true * log(y_true / y_pred)`

See: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence

#### Usage:



```python
loss = tf.keras.losses.KLD([.4, .9, .2], [.5, .8, .12])
print('Loss: ', loss.numpy())  # Loss: 0.11891246
```

#### Args:


* <b>`y_true`</b>: Tensor of true targets.
* <b>`y_pred`</b>: Tensor of predicted targets.


#### Returns:

A `Tensor` with loss.



#### Raises:


* <b>`TypeError`</b>: If `y_true` cannot be cast to the `y_pred.dtype`.
