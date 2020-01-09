page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.sequence_to_images


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/layers.py#L2854-L2885">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Convert a batch of sequences into a batch of images.

``` python
tf.contrib.layers.sequence_to_images(
    inputs,
    height,
    output_data_format='channels_last',
    outputs_collections=None,
    scope=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`inputs`</b>: (num_steps, num_batches, depth) sequence tensor
* <b>`height`</b>: the height of the images
* <b>`output_data_format`</b>: Format of output tensor. Currently supports
  `'channels_first'` and `'channels_last'`.
* <b>`outputs_collections`</b>: The collections to which the outputs are added.
* <b>`scope`</b>: Optional scope for name_scope.


#### Returns:

A tensor representing the output of the operation.
