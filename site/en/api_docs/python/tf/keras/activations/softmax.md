page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.softmax


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/activations/softmax">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/activations.py#L43-L72">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



The softmax activation function transforms the outputs so that all values are in

### Aliases:

* <a href="/api_docs/python/tf/keras/activations/softmax"><code>tf.compat.v1.keras.activations.softmax</code></a>
* <a href="/api_docs/python/tf/keras/activations/softmax"><code>tf.compat.v2.keras.activations.softmax</code></a>


``` python
tf.keras.activations.softmax(
    x,
    axis=-1
)
```



<!-- Placeholder for "Used in" -->

range (0, 1) and sum to 1. It is often used as the activation for the last
layer of a classification network because the result could be interpreted as
a probability distribution. The softmax of x is calculated by
exp(x)/tf.reduce_sum(exp(x)).

#### Arguments:


* <b>`x`</b>: Input tensor.
* <b>`axis`</b>: Integer, axis along which the softmax normalization is applied.


#### Returns:

Tensor, output of softmax transformation (all values are non-negative
  and sum to 1).



#### Raises:


* <b>`ValueError`</b>: In case `dim(x) == 1`.
