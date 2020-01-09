page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.model_pruning.apply_mask


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/model_pruning/python/pruning.py#L90-L114">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Apply mask to a given weight tensor.

``` python
tf.contrib.model_pruning.apply_mask(
    x,
    scope=''
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: Input weight tensor
* <b>`scope`</b>: The current variable scope. Defaults to "".

#### Returns:

Tensor representing masked_weights
