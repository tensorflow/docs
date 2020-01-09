page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.l1_l2_regularizer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/regularizers.py#L112-L138">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a function that can be used to apply L1 L2 regularizations.

``` python
tf.contrib.layers.l1_l2_regularizer(
    scale_l1=1.0,
    scale_l2=1.0,
    scope=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`scale_l1`</b>: A scalar multiplier `Tensor` for L1 regularization.
* <b>`scale_l2`</b>: A scalar multiplier `Tensor` for L2 regularization.
* <b>`scope`</b>: An optional scope name.


#### Returns:

A function with signature `l1_l2(weights)` that applies a weighted sum of
L1 L2 regularization.



#### Raises:


* <b>`ValueError`</b>: If scale is negative or if scale is not a float.
