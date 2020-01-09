page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.summarize_tensor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/summaries.py#L107-L132">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Summarize a tensor using a suitable summary type.

``` python
tf.contrib.layers.summarize_tensor(
    tensor,
    tag=None
)
```



<!-- Placeholder for "Used in" -->

This function adds a summary op for `tensor`. The type of summary depends on
the shape of `tensor`. For scalars, a `scalar_summary` is created, for all
other tensors, `histogram_summary` is used.

#### Args:


* <b>`tensor`</b>: The tensor to summarize
* <b>`tag`</b>: The tag to use, if None then use tensor's op's name.


#### Returns:

The summary op created or None for string tensors.
