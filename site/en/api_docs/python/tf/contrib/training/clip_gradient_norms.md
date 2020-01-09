page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.clip_gradient_norms


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/training/python/training/training.py#L298-L317">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Clips the gradients by the given value.

``` python
tf.contrib.training.clip_gradient_norms(
    gradients_to_variables,
    max_norm
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`gradients_to_variables`</b>: A list of gradient to variable pairs (tuples).
* <b>`max_norm`</b>: the maximum norm value.


#### Returns:

A list of clipped gradient to variable pairs.
