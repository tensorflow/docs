page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.normalize_batch_in_training


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/normalize_batch_in_training">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L2470-L2497">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes mean and std for batch then apply batch_normalization on batch.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/normalize_batch_in_training"><code>tf.compat.v1.keras.backend.normalize_batch_in_training</code></a>
* <a href="/api_docs/python/tf/keras/backend/normalize_batch_in_training"><code>tf.compat.v2.keras.backend.normalize_batch_in_training</code></a>


``` python
tf.keras.backend.normalize_batch_in_training(
    x,
    gamma,
    beta,
    reduction_axes,
    epsilon=0.001
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Input tensor or variable.
* <b>`gamma`</b>: Tensor by which to scale the input.
* <b>`beta`</b>: Tensor with which to center the input.
* <b>`reduction_axes`</b>: iterable of integers,
    axes over which to normalize.
* <b>`epsilon`</b>: Fuzz factor.


#### Returns:

A tuple length of 3, `(normalized_tensor, mean, variance)`.
