page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.resize


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/image_ops_impl.py#L1190-L1319">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Resize `images` to `size` using the specified `method`.

### Aliases:

* `tf.compat.v2.image.resize`


``` python
tf.image.resize(
    images,
    size,
    method=ResizeMethod.BILINEAR,
    preserve_aspect_ratio=False,
    antialias=False,
    name=None
)
```



### Used in the guide:

* [Estimators](https://www.tensorflow.org/guide/estimator)
* [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)

### Used in the tutorials:

* [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)
* [CycleGAN](https://www.tensorflow.org/tutorials/generative/cyclegan)
* [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)
* [Image captioning with visual attention](https://www.tensorflow.org/tutorials/text/image_captioning)
* [Image segmentation](https://www.tensorflow.org/tutorials/images/segmentation)
* [Load images](https://www.tensorflow.org/tutorials/load_data/images)
* [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)
* [Pix2Pix](https://www.tensorflow.org/tutorials/generative/pix2pix)
* [Transfer learning with a pretrained ConvNet](https://www.tensorflow.org/tutorials/images/transfer_learning)



Resized images will be distorted if their original aspect ratio is not
the same as `size`.  To avoid distortions see
<a href="../../tf/image/resize_with_pad"><code>tf.image.resize_with_pad</code></a>.

When 'antialias' is true, the sampling filter will anti-alias the input image
as well as interpolate.  When downsampling an image with [anti-aliasing](
https://en.wikipedia.org/wiki/Spatial_anti-aliasing) the sampling filter
kernel is scaled in order to properly anti-alias the input image signal.
'antialias' has no effect when upsampling an image.

*   <b>`bilinear`</b>: [Bilinear interpolation.](
  https://en.wikipedia.org/wiki/Bilinear_interpolation) If 'antialias' is
  true, becomes a hat/tent filter function with radius 1 when downsampling.
*   <b>`lanczos3`</b>:  [Lanczos kernel](
  https://en.wikipedia.org/wiki/Lanczos_resampling) with radius 3.
  High-quality practical filter but may have some ringing especially on
  synthetic images.
*   <b>`lanczos5`</b>: [Lanczos kernel] (
  https://en.wikipedia.org/wiki/Lanczos_resampling) with radius 5.
  Very-high-quality filter but may have stronger ringing.
*   <b>`bicubic`</b>: [Cubic interpolant](
  https://en.wikipedia.org/wiki/Bicubic_interpolation) of Keys. Equivalent to
  Catmull-Rom kernel. Reasonably good quality and faster than Lanczos3Kernel,
  particularly when upsampling.
*   <b>`gaussian`</b>: [Gaussian kernel](
  https://en.wikipedia.org/wiki/Gaussian_filter) with radius 3,
  sigma = 1.5 / 3.0.
*   <b>`nearest`</b>: [Nearest neighbor interpolation.](
  https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation)
  'antialias' has no effect when used with nearest neighbor interpolation.
*   <b>`area`</b>: Anti-aliased resampling with area interpolation.
  'antialias' has no effect when used with area interpolation; it
  always anti-aliases.
*   <b>`mitchellcubic`</b>: Mitchell-Netravali Cubic non-interpolating filter.
  For synthetic images (especially those lacking proper prefiltering), less
  ringing than Keys cubic kernel but less sharp.

Note that near image edges the filtering kernel may be partially outside the
image boundaries. For these pixels, only input pixels inside the image will be
included in the filter sum, and the output value will be appropriately
normalized.

The return value has the same type as `images` if `method` is
<a href="../../tf/image/ResizeMethod#NEAREST_NEIGHBOR"><code>ResizeMethod.NEAREST_NEIGHBOR</code></a>. Otherwise, the return value has type
`float32`.

#### Args:


* <b>`images`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
  of shape `[height, width, channels]`.
* <b>`size`</b>: A 1-D int32 Tensor of 2 elements: `new_height, new_width`.  The new
  size for the images.
* <b>`method`</b>: ResizeMethod.  Defaults to `bilinear`.
* <b>`preserve_aspect_ratio`</b>: Whether to preserve the aspect ratio. If this is set,
  then `images` will be resized to a size that fits in `size` while
  preserving the aspect ratio of the original image. Scales up the image if
  `size` is bigger than the current size of the `image`. Defaults to False.
* <b>`antialias`</b>: Whether to use an anti-aliasing filter when downsampling an
  image.
* <b>`name`</b>: A name for this operation (optional).


#### Raises:


* <b>`ValueError`</b>: if the shape of `images` is incompatible with the
  shape arguments to this function
* <b>`ValueError`</b>: if `size` has invalid shape or type.
* <b>`ValueError`</b>: if an unsupported resize method is specified.


#### Returns:

If `images` was 4-D, a 4-D float Tensor of shape
`[batch, new_height, new_width, channels]`.
If `images` was 3-D, a 3-D float Tensor of shape
`[new_height, new_width, channels]`.
