page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.cumprod


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L2046-L2057">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Cumulative product of the values in a tensor, alongside the specified axis.

### Aliases:

* `tf.compat.v1.keras.backend.cumprod`
* `tf.compat.v2.keras.backend.cumprod`


``` python
tf.keras.backend.cumprod(
    x,
    axis=0
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: An integer, the axis to compute the product.


#### Returns:

A tensor of the cumulative product of values of `x` along `axis`.
