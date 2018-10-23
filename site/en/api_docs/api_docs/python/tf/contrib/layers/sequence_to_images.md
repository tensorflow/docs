

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.sequence_to_images

``` python
tf.contrib.layers.sequence_to_images(
    inputs,
    height,
    output_data_format='channels_last',
    outputs_collections=None,
    scope=None
)
```



Defined in [`tensorflow/contrib/layers/python/layers/layers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/layers/python/layers/layers.py).

Convert a batch of sequences into a batch of images.

#### Args:

* <b>`inputs`</b>: (num_steps, num_batches, depth) sequence tensor
* <b>`height`</b>: the height of the images
* <b>`output_data_format`</b>: Format of output tensor.
    Currently supports `'channels_first'` and `'channels_last'`.
* <b>`outputs_collections`</b>: The collections to which the outputs are added.
* <b>`scope`</b>: Optional scope for name_scope.


#### Returns:

A tensor representing the output of the operation.