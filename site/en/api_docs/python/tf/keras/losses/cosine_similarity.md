page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.cosine_similarity


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/losses.py#L1064-L1093">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the cosine similarity between labels and predictions.

### Aliases:

* `tf.compat.v1.keras.losses.cosine`
* `tf.compat.v1.keras.losses.cosine_proximity`
* `tf.compat.v1.keras.losses.cosine_similarity`
* `tf.compat.v1.keras.metrics.cosine`
* `tf.compat.v1.keras.metrics.cosine_proximity`
* `tf.compat.v2.keras.losses.cosine_similarity`
* `tf.compat.v2.losses.cosine_similarity`
* `tf.losses.cosine_similarity`


``` python
tf.keras.losses.cosine_similarity(
    y_true,
    y_pred,
    axis=-1
)
```



<!-- Placeholder for "Used in" -->

Note that it is a negative quantity between -1 and 0, where 0 indicates
orthogonality and values closer to -1 indicate greater similarity. This makes
it usable as a loss function in a setting where you try to maximize the
proximity between predictions and targets.

`loss = -sum(y_true * y_pred)`

#### Args:


* <b>`y_true`</b>: Tensor of true targets.
* <b>`y_pred`</b>: Tensor of predicted targets.
* <b>`axis`</b>: Axis along which to determine similarity.


#### Returns:

Cosine similarity tensor.
