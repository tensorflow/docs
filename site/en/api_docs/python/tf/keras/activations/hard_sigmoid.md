page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.hard_sigmoid


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/activations/hard_sigmoid">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/activations.py#L262-L277">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Hard sigmoid activation function.

### Aliases:

* <a href="/api_docs/python/tf/keras/activations/hard_sigmoid"><code>tf.compat.v1.keras.activations.hard_sigmoid</code></a>
* <a href="/api_docs/python/tf/keras/activations/hard_sigmoid"><code>tf.compat.v2.keras.activations.hard_sigmoid</code></a>


``` python
tf.keras.activations.hard_sigmoid(x)
```



<!-- Placeholder for "Used in" -->

Faster to compute than sigmoid activation.

#### Arguments:


* <b>`x`</b>: Input tensor.


#### Returns:

Hard sigmoid activation:
- `0` if `x < -2.5`
- `1` if `x > 2.5`
- `0.2 * x + 0.5` if `-2.5 <= x <= 2.5`.
