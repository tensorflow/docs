page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.summarize_activation


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/summaries.py#L78-L104">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Summarize an activation.

``` python
tf.contrib.layers.summarize_activation(op)
```



<!-- Placeholder for "Used in" -->

This applies the given activation and adds useful summaries specific to the
activation.

#### Args:


* <b>`op`</b>: The tensor to summarize (assumed to be a layer activation).

#### Returns:

The summary op created to summarize `op`.
