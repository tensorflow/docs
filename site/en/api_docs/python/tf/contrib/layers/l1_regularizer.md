page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.l1_regularizer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/regularizers.py#L37-L73">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a function that can be used to apply L1 regularization to weights.

``` python
tf.contrib.layers.l1_regularizer(
    scale,
    scope=None
)
```



<!-- Placeholder for "Used in" -->

L1 regularization encourages sparsity.

#### Args:


* <b>`scale`</b>: A scalar multiplier `Tensor`. 0.0 disables the regularizer.
* <b>`scope`</b>: An optional scope name.


#### Returns:

A function with signature `l1(weights)` that apply L1 regularization.



#### Raises:


* <b>`ValueError`</b>: If scale is negative or if scale is not a float.
