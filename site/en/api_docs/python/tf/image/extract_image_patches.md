page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.extract_image_patches

Extract `patches` from `images` and put them in the "depth" output dimension.

### Aliases:

* `tf.compat.v1.extract_image_patches`
* `tf.compat.v1.image.extract_image_patches`
* `tf.extract_image_patches`
* `tf.image.extract_image_patches`

``` python
tf.image.extract_image_patches(
    images,
    ksizes=None,
    strides=None,
    rates=None,
    padding=None,
    name=None,
    sizes=None
)
```



Defined in [`python/ops/array_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/array_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`images`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
  4-D Tensor with shape `[batch, in_rows, in_cols, depth]`.
* <b>`ksizes`</b>: A list of `ints` that has length `>= 4`.
  The size of the sliding window for each dimension of `images`.
* <b>`strides`</b>: A list of `ints` that has length `>= 4`.
  1-D of length 4. How far the centers of two consecutive patches are in
  the images. Must be: `[1, stride_rows, stride_cols, 1]`.
* <b>`rates`</b>: A list of `ints` that has length `>= 4`.
  1-D of length 4. Must be: `[1, rate_rows, rate_cols, 1]`. This is the
  input stride, specifying how far two consecutive patch samples are in the
  input. Equivalent to extracting patches with
  `patch_sizes_eff = patch_sizes + (patch_sizes - 1) * (rates - 1)`, followed by
  subsampling them spatially by a factor of `rates`. This is equivalent to
  `rate` in dilated (a.k.a. Atrous) convolutions.
* <b>`padding`</b>: A `string` from: `"SAME", "VALID"`.
  The type of padding algorithm to use.

  We specify the size-related attributes as:

>           ksizes = [1, ksize_rows, ksize_cols, 1]
>           strides = [1, strides_rows, strides_cols, 1]
>           rates = [1, rates_rows, rates_cols, 1]
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `images`.
