page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.conv1d


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/conv1d">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L4671-L4718">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



1D convolution.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/conv1d"><code>tf.compat.v1.keras.backend.conv1d</code></a>
* <a href="/api_docs/python/tf/keras/backend/conv1d"><code>tf.compat.v2.keras.backend.conv1d</code></a>


``` python
tf.keras.backend.conv1d(
    x,
    kernel,
    strides=1,
    padding='valid',
    data_format=None,
    dilation_rate=1
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`kernel`</b>: kernel tensor.
* <b>`strides`</b>: stride integer.
* <b>`padding`</b>: string, `"same"`, `"causal"` or `"valid"`.
* <b>`data_format`</b>: string, one of "channels_last", "channels_first".
* <b>`dilation_rate`</b>: integer dilate rate.


#### Returns:

A tensor, result of 1D convolution.



#### Raises:


* <b>`ValueError`</b>: if `data_format` is neither `channels_last` or
`channels_first`.
