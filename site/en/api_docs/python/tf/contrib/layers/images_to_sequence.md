page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.images_to_sequence


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/layers.py#L2336-L2368">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Convert a batch of images into a batch of sequences.

``` python
tf.contrib.layers.images_to_sequence(
    inputs,
    data_format=DATA_FORMAT_NHWC,
    outputs_collections=None,
    scope=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`inputs`</b>: a (num_images, height, width, depth) tensor
* <b>`data_format`</b>: A string. `NHWC` (default) and `NCHW` are supported.
* <b>`outputs_collections`</b>: The collections to which the outputs are added.
* <b>`scope`</b>: Optional scope for name_scope.


#### Raises:


* <b>`ValueError`</b>: If `data_format` is not either NCHW or NHWC.


#### Returns:

(width, num_images*height, depth) sequence tensor
