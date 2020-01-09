page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.pool3d


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L5274-L5324">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



3D Pooling.

### Aliases:

* `tf.compat.v1.keras.backend.pool3d`
* `tf.compat.v2.keras.backend.pool3d`


``` python
tf.keras.backend.pool3d(
    x,
    pool_size,
    strides=(1, 1, 1),
    padding='valid',
    data_format=None,
    pool_mode='max'
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`pool_size`</b>: tuple of 3 integers.
* <b>`strides`</b>: tuple of 3 integers.
* <b>`padding`</b>: string, `"same"` or `"valid"`.
* <b>`data_format`</b>: string, `"channels_last"` or `"channels_first"`.
* <b>`pool_mode`</b>: string, `"max"` or `"avg"`.


#### Returns:

A tensor, result of 3D pooling.



#### Raises:


* <b>`ValueError`</b>: if `data_format` is neither `"channels_last"` or
`"channels_first"`.
* <b>`ValueError`</b>: if `pool_mode` is neither `"max"` or `"avg"`.
