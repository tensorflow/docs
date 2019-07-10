page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.extract_patches

Extract `patches` from `images` and put them in the \"depth\" output dimension.

### Aliases:

* `tf.compat.v1.image.extract_patches`
* `tf.compat.v2.image.extract_patches`
* `tf.image.extract_patches`

``` python
tf.image.extract_patches(
    images,
    sizes,
    strides,
    rates,
    padding,
    name=None
)
```



Defined in [`python/ops/array_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/array_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`images`</b>: A 4-D Tensor with shape `[batch, in_rows, in_cols, depth]
* <b>`sizes`</b>: The size of the sliding window for each dimension of `images`.
* <b>`strides`</b>: A 1-D Tensor of length 4. How far the centers of two consecutive
  patches are in the images. Must be: `[1, stride_rows, stride_cols, 1]`.
* <b>`rates`</b>: A 1-D Tensor of length 4. Must be: `[1, rate_rows, rate_cols, 1]`.
  This is the input stride, specifying how far two consecutive patch samples
  are in the input. Equivalent to extracting patches with `patch_sizes_eff =
  patch_sizes + (patch_sizes - 1) * (rates - 1)`, followed by subsampling
  them spatially by a factor of `rates`. This is equivalent to `rate` in
  dilated (a.k.a. Atrous) convolutions.
* <b>`padding`</b>: The type of padding algorithm to use.
  We specify the size-related attributes as: ```python ksizes = [1,
    ksize_rows, ksize_cols, 1] strides = [1, strides_rows, strides_cols, 1]
    rates = [1, rates_rows, rates_cols, 1]
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A 4-D Tensor. Has the same type as `images`, and with shape `[batch,
out_rows, out_cols, ksize_rows * ksize_cols * depth]` containing image
patches with size `ksize_rows x ksize_cols x depth` vectorized in the
\"depth\" dimension. Note `out_rows` and `out_cols` are the dimensions of
the output patches.
