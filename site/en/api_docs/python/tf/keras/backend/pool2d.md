page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.pool2d


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L5215-L5271">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



2D Pooling.

### Aliases:

* `tf.compat.v1.keras.backend.pool2d`
* `tf.compat.v2.keras.backend.pool2d`


``` python
tf.keras.backend.pool2d(
    x,
    pool_size,
    strides=(1, 1),
    padding='valid',
    data_format=None,
    pool_mode='max'
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`pool_size`</b>: tuple of 2 integers.
* <b>`strides`</b>: tuple of 2 integers.
* <b>`padding`</b>: string, `"same"` or `"valid"`.
* <b>`data_format`</b>: string, `"channels_last"` or `"channels_first"`.
* <b>`pool_mode`</b>: string, `"max"` or `"avg"`.


#### Returns:

A tensor, result of 2D pooling.



#### Raises:


* <b>`ValueError`</b>: if `data_format` is neither `"channels_last"` or
`"channels_first"`.
* <b>`ValueError`</b>: if `pool_size` is not a tuple of 2 integers.
* <b>`ValueError`</b>: if `strides` is not a tuple of 2 integers.
* <b>`ValueError`</b>: if `pool_mode` is neither `"max"` or `"avg"`.
