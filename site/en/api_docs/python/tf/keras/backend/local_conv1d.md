page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.local_conv1d


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L5404-L5436">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Apply 1D conv with un-shared weights.

### Aliases:

* `tf.compat.v1.keras.backend.local_conv1d`
* `tf.compat.v2.keras.backend.local_conv1d`


``` python
tf.keras.backend.local_conv1d(
    inputs,
    kernel,
    kernel_size,
    strides,
    data_format=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`inputs`</b>: 3D tensor with shape:
    (batch_size, steps, input_dim)
    if data_format is "channels_last" or
    (batch_size, input_dim, steps)
    if data_format is "channels_first".
* <b>`kernel`</b>: the unshared weight for convolution,
    with shape (output_length, feature_dim, filters).
* <b>`kernel_size`</b>: a tuple of a single integer,
    specifying the length of the 1D convolution window.
* <b>`strides`</b>: a tuple of a single integer,
    specifying the stride length of the convolution.
* <b>`data_format`</b>: the data format, channels_first or channels_last.


#### Returns:

A 3d tensor with shape:
(batch_size, output_length, filters)
if data_format='channels_first'
or 3D tensor with shape:
(batch_size, filters, output_length)
if data_format='channels_last'.
