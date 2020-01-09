page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.elu


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/activations/elu">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/activations.py#L75-L91">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Exponential linear unit.

### Aliases:

* <a href="/api_docs/python/tf/keras/activations/elu"><code>tf.compat.v1.keras.activations.elu</code></a>
* <a href="/api_docs/python/tf/keras/activations/elu"><code>tf.compat.v2.keras.activations.elu</code></a>


``` python
tf.keras.activations.elu(
    x,
    alpha=1.0
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Input tensor.
* <b>`alpha`</b>: A scalar, slope of negative section.


#### Returns:

The exponential linear activation: `x` if `x > 0` and
  `alpha * (exp(x)-1)` if `x < 0`.



#### Reference:

- [Fast and Accurate Deep Network Learning by Exponential
  Linear Units (ELUs)](https://arxiv.org/abs/1511.07289)
