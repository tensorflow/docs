page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.bias_add


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/bias_add">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L5376-L5444">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adds a bias vector to a tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/bias_add"><code>tf.compat.v1.keras.backend.bias_add</code></a>
* <a href="/api_docs/python/tf/keras/backend/bias_add"><code>tf.compat.v2.keras.backend.bias_add</code></a>


``` python
tf.keras.backend.bias_add(
    x,
    bias,
    data_format=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`bias`</b>: Bias tensor to add.
* <b>`data_format`</b>: string, `"channels_last"` or `"channels_first"`.


#### Returns:

Output tensor.



#### Raises:


* <b>`ValueError`</b>: In one of the two cases below:
            1. invalid `data_format` argument.
            2. invalid bias shape.
               the bias should be either a vector or
               a tensor with ndim(x) - 1 dimension
