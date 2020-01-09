page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.multiply_gradients


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/training/python/training/training.py#L329-L366">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Multiply specified gradients.

``` python
tf.contrib.training.multiply_gradients(
    grads_and_vars,
    gradient_multipliers
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`grads_and_vars`</b>: A list of gradient to variable pairs (tuples).
* <b>`gradient_multipliers`</b>: A map from either `Variables` or `Variable` op names
  to the coefficient by which the associated gradient should be scaled.


#### Returns:

The updated list of gradient to variable pairs.



#### Raises:


* <b>`ValueError`</b>: If `grads_and_vars` is not a list or if `gradient_multipliers`
is empty or None or if `gradient_multipliers` is not a dictionary.
