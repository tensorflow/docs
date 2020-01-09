page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.cumsum


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L2032-L2043">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Cumulative sum of the values in a tensor, alongside the specified axis.

### Aliases:

* `tf.compat.v1.keras.backend.cumsum`
* `tf.compat.v2.keras.backend.cumsum`


``` python
tf.keras.backend.cumsum(
    x,
    axis=0
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: An integer, the axis to compute the sum.


#### Returns:

A tensor of the cumulative sum of values of `x` along `axis`.
