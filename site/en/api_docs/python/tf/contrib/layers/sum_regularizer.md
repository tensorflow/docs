page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.sum_regularizer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/regularizers.py#L141-L167">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a function that applies the sum of multiple regularizers.

``` python
tf.contrib.layers.sum_regularizer(
    regularizer_list,
    scope=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`regularizer_list`</b>: A list of regularizers to apply.
* <b>`scope`</b>: An optional scope name


#### Returns:

A function with signature `sum_reg(weights)` that applies the
sum of all the input regularizers.
