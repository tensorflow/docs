page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.std


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L2080-L2097">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Standard deviation of a tensor, alongside the specified axis.

### Aliases:

* `tf.compat.v1.keras.backend.std`
* `tf.compat.v2.keras.backend.std`


``` python
tf.keras.backend.std(
    x,
    axis=None,
    keepdims=False
)
```



### Used in the guide:

* [Train and evaluate with Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate)




#### Arguments:


* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: An integer, the axis to compute the standard deviation.
* <b>`keepdims`</b>: A boolean, whether to keep the dimensions or not.
    If `keepdims` is `False`, the rank of the tensor is reduced
    by 1. If `keepdims` is `True`,
    the reduced dimension is retained with length 1.


#### Returns:

A tensor with the standard deviation of elements of `x`.
