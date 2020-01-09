page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.poisson


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/losses/poisson">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/losses.py#L1030-L1056">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the Poisson loss between y_true and y_pred.

### Aliases:

* <a href="/api_docs/python/tf/keras/losses/poisson"><code>tf.compat.v1.keras.losses.poisson</code></a>
* <a href="/api_docs/python/tf/keras/losses/poisson"><code>tf.compat.v1.keras.metrics.poisson</code></a>
* <a href="/api_docs/python/tf/keras/losses/poisson"><code>tf.compat.v2.keras.losses.poisson</code></a>
* <a href="/api_docs/python/tf/keras/losses/poisson"><code>tf.compat.v2.keras.metrics.poisson</code></a>
* <a href="/api_docs/python/tf/keras/losses/poisson"><code>tf.compat.v2.losses.poisson</code></a>
* <a href="/api_docs/python/tf/keras/losses/poisson"><code>tf.compat.v2.metrics.poisson</code></a>
* <a href="/api_docs/python/tf/keras/losses/poisson"><code>tf.keras.metrics.poisson</code></a>


``` python
tf.keras.losses.poisson(
    y_true,
    y_pred
)
```



<!-- Placeholder for "Used in" -->

The Poisson loss is the mean of the elements of the `Tensor`
`y_pred - y_true * log(y_pred)`.

#### Usage:



```python
loss = tf.keras.losses.poisson([1.4, 9.3, 2.2], [4.3, 8.2, 12.2])
print('Loss: ', loss.numpy())  # Loss: -0.8045559
```

#### Args:


* <b>`y_true`</b>: Tensor of true targets.
* <b>`y_pred`</b>: Tensor of predicted targets.


#### Returns:

A `Tensor` with the mean Poisson loss.



#### Raises:


* <b>`InvalidArgumentError`</b>: If `y_true` and `y_pred` have incompatible shapes.
