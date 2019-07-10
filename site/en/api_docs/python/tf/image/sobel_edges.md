page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.sobel_edges

Returns a tensor holding Sobel edge maps.

### Aliases:

* `tf.compat.v1.image.sobel_edges`
* `tf.compat.v2.image.sobel_edges`
* `tf.image.sobel_edges`

``` python
tf.image.sobel_edges(image)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`image`</b>: Image tensor with shape [batch_size, h, w, d] and type float32 or
  float64.  The image(s) must be 2x2 or larger.


#### Returns:

Tensor holding edge maps for each channel. Returns a tensor with shape
[batch_size, h, w, d, 2] where the last two dimensions hold [[dy[0], dx[0]],
[dy[1], dx[1]], ..., [dy[d-1], dx[d-1]]] calculated using the Sobel filter.
