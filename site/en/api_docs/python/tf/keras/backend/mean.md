page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.mean


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L2100-L2117">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Mean of a tensor, alongside the specified axis.

### Aliases:

* `tf.compat.v1.keras.backend.mean`
* `tf.compat.v2.keras.backend.mean`


``` python
tf.keras.backend.mean(
    x,
    axis=None,
    keepdims=False
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: A list of integer. Axes to compute the mean.
* <b>`keepdims`</b>: A boolean, whether to keep the dimensions or not.
    If `keepdims` is `False`, the rank of the tensor is reduced
    by 1 for each entry in `axis`. If `keepdims` is `True`,
    the reduced dimensions are retained with length 1.


#### Returns:

A tensor with the mean of elements of `x`.
