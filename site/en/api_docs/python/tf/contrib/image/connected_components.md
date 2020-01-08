page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.image.connected_components

``` python
tf.contrib.image.connected_components(images)
```



Defined in [`tensorflow/contrib/image/python/ops/image_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/image/python/ops/image_ops.py).

Labels the connected components in a batch of images.

A component is a set of pixels in a single input image, which are all adjacent
and all have the same non-zero value. The components using a squared
connectivity of one (all True entries are joined with their neighbors above,
below, left, and right). Components across all images have consecutive ids 1
through n. Components are labeled according to the first pixel of the
component appearing in row-major order (lexicographic order by
image_index_in_batch, row, col). Zero entries all have an output id of 0.

This op is equivalent with `scipy.ndimage.measurements.label` on a 2D array
with the default structuring element (which is the connectivity used here).

#### Args:

* <b>`images`</b>: A 2D (H, W) or 3D (N, H, W) Tensor of boolean image(s).


#### Returns:

Components with the same shape as `images`. False entries in `images` have
value 0, and all True entries map to a component id > 0.


#### Raises:

* <b>`TypeError`</b>: if `images` is not 2D or 3D.