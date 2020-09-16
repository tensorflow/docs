description: Image ops.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.image

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Image ops.


The <a href="../tf/image.md"><code>tf.image</code></a> module contains various functions for image
processing and decoding-encoding Ops.

Many of the encoding/decoding functions are also available in the
core <a href="../tf/io.md"><code>tf.io</code></a> module.

## Image processing

### Resizing

The resizing Ops accept input images as tensors of several types. They always
output resized images as float32 tensors.

The convenience function <a href="../tf/image/resize.md"><code>tf.image.resize</code></a> supports both 4-D
and 3-D tensors as input and output.  4-D tensors are for batches of images,
3-D tensors for individual images.

Resized images will be distorted if their original aspect ratio is not the
same as size. To avoid distortions see tf.image.resize_with_pad.

*   <a href="../tf/image/resize.md"><code>tf.image.resize</code></a>
*   <a href="../tf/image/resize_with_pad.md"><code>tf.image.resize_with_pad</code></a>
*   <a href="../tf/image/resize_with_crop_or_pad.md"><code>tf.image.resize_with_crop_or_pad</code></a>

The Class <a href="../tf/image/ResizeMethod.md"><code>tf.image.ResizeMethod</code></a> provides various resize methods like
`bilinear`, `nearest_neighbor`.

### Converting Between Colorspaces

Image ops work either on individual images or on batches of images, depending on
the shape of their input Tensor.

If 3-D, the shape is `[height, width, channels]`, and the Tensor represents one
image. If 4-D, the shape is `[batch_size, height, width, channels]`, and the
Tensor represents `batch_size` images.

Currently, `channels` can usefully be 1, 2, 3, or 4. Single-channel images are
grayscale, images with 3 channels are encoded as either RGB or HSV. Images
with 2 or 4 channels include an alpha channel, which has to be stripped from the
image before passing the image to most image processing functions (and can be
re-attached later).

Internally, images are either stored in as one `float32` per channel per pixel
(implicitly, values are assumed to lie in `[0,1)`) or one `uint8` per channel
per pixel (values are assumed to lie in `[0,255]`).

TensorFlow can convert between images in RGB or HSV or YIQ.

*   <a href="../tf/image/rgb_to_grayscale.md"><code>tf.image.rgb_to_grayscale</code></a>, <a href="../tf/image/grayscale_to_rgb.md"><code>tf.image.grayscale_to_rgb</code></a>
*   <a href="../tf/image/rgb_to_hsv.md"><code>tf.image.rgb_to_hsv</code></a>, <a href="../tf/image/hsv_to_rgb.md"><code>tf.image.hsv_to_rgb</code></a>
*   <a href="../tf/image/rgb_to_yiq.md"><code>tf.image.rgb_to_yiq</code></a>, <a href="../tf/image/yiq_to_rgb.md"><code>tf.image.yiq_to_rgb</code></a>
*   <a href="../tf/image/rgb_to_yuv.md"><code>tf.image.rgb_to_yuv</code></a>, <a href="../tf/image/yuv_to_rgb.md"><code>tf.image.yuv_to_rgb</code></a>
*   <a href="../tf/image/image_gradients.md"><code>tf.image.image_gradients</code></a>
*   <a href="../tf/image/convert_image_dtype.md"><code>tf.image.convert_image_dtype</code></a>

### Image Adjustments

TensorFlow provides functions to adjust images in various ways: brightness,
contrast, hue, and saturation.  Each adjustment can be done with predefined
parameters or with random parameters picked from predefined intervals. Random
adjustments are often useful to expand a training set and reduce overfitting.

If several adjustments are chained it is advisable to minimize the number of
redundant conversions by first converting the images to the most natural data
type and representation.

*   <a href="../tf/image/adjust_brightness.md"><code>tf.image.adjust_brightness</code></a>
*   <a href="../tf/image/adjust_contrast.md"><code>tf.image.adjust_contrast</code></a>
*   <a href="../tf/image/adjust_gamma.md"><code>tf.image.adjust_gamma</code></a>
*   <a href="../tf/image/adjust_hue.md"><code>tf.image.adjust_hue</code></a>
*   <a href="../tf/image/adjust_jpeg_quality.md"><code>tf.image.adjust_jpeg_quality</code></a>
*   <a href="../tf/image/adjust_saturation.md"><code>tf.image.adjust_saturation</code></a>
*   <a href="../tf/image/random_brightness.md"><code>tf.image.random_brightness</code></a>
*   <a href="../tf/image/random_contrast.md"><code>tf.image.random_contrast</code></a>
*   <a href="../tf/image/random_hue.md"><code>tf.image.random_hue</code></a>
*   <a href="../tf/image/random_saturation.md"><code>tf.image.random_saturation</code></a>
*   <a href="../tf/image/per_image_standardization.md"><code>tf.image.per_image_standardization</code></a>

### Working with Bounding Boxes

*   <a href="../tf/image/draw_bounding_boxes.md"><code>tf.image.draw_bounding_boxes</code></a>
*   <a href="../tf/image/combined_non_max_suppression.md"><code>tf.image.combined_non_max_suppression</code></a>
*   <a href="../tf/image/generate_bounding_box_proposals.md"><code>tf.image.generate_bounding_box_proposals</code></a>
*   <a href="../tf/image/non_max_suppression.md"><code>tf.image.non_max_suppression</code></a>
*   <a href="../tf/image/non_max_suppression_overlaps.md"><code>tf.image.non_max_suppression_overlaps</code></a>
*   <a href="../tf/image/non_max_suppression_padded.md"><code>tf.image.non_max_suppression_padded</code></a>
*   <a href="../tf/image/non_max_suppression_with_scores.md"><code>tf.image.non_max_suppression_with_scores</code></a>
*   <a href="../tf/image/pad_to_bounding_box.md"><code>tf.image.pad_to_bounding_box</code></a>
*   <a href="../tf/image/sample_distorted_bounding_box.md"><code>tf.image.sample_distorted_bounding_box</code></a>

### Cropping

*   <a href="../tf/image/central_crop.md"><code>tf.image.central_crop</code></a>
*   <a href="../tf/image/crop_and_resize.md"><code>tf.image.crop_and_resize</code></a>
*   <a href="../tf/image/crop_to_bounding_box.md"><code>tf.image.crop_to_bounding_box</code></a>
*   <a href="../tf/io/decode_and_crop_jpeg.md"><code>tf.io.decode_and_crop_jpeg</code></a>
*   <a href="../tf/image/extract_glimpse.md"><code>tf.image.extract_glimpse</code></a>
*   <a href="../tf/image/random_crop.md"><code>tf.image.random_crop</code></a>
*   <a href="../tf/image/resize_with_crop_or_pad.md"><code>tf.image.resize_with_crop_or_pad</code></a>

### Flipping, Rotating and Transposing

*   <a href="../tf/image/flip_left_right.md"><code>tf.image.flip_left_right</code></a>
*   <a href="../tf/image/flip_up_down.md"><code>tf.image.flip_up_down</code></a>
*   <a href="../tf/image/random_flip_left_right.md"><code>tf.image.random_flip_left_right</code></a>
*   <a href="../tf/image/random_flip_up_down.md"><code>tf.image.random_flip_up_down</code></a>
*   <a href="../tf/image/rot90.md"><code>tf.image.rot90</code></a>
*   <a href="../tf/image/transpose.md"><code>tf.image.transpose</code></a>

## Image decoding and encoding

TensorFlow provides Ops to decode and encode JPEG and PNG formats.  Encoded
images are represented by scalar string Tensors, decoded images by 3-D uint8
tensors of shape `[height, width, channels]`. (PNG also supports uint16.)

Note: `decode_gif` returns a 4-D array `[num_frames, height, width, 3]`

The encode and decode Ops apply to one image at a time.  Their input and output
are all of variable size.  If you need fixed size images, pass the output of
the decode Ops to one of the cropping and resizing Ops.

*   <a href="../tf/io/decode_bmp.md"><code>tf.io.decode_bmp</code></a>
*   <a href="../tf/io/decode_gif.md"><code>tf.io.decode_gif</code></a>
*   <a href="../tf/io/decode_image.md"><code>tf.io.decode_image</code></a>
*   <a href="../tf/io/decode_jpeg.md"><code>tf.io.decode_jpeg</code></a>
*   <a href="../tf/io/decode_and_crop_jpeg.md"><code>tf.io.decode_and_crop_jpeg</code></a>
*   <a href="../tf/io/decode_png.md"><code>tf.io.decode_png</code></a>
*   <a href="../tf/io/encode_jpeg.md"><code>tf.io.encode_jpeg</code></a>
*   <a href="../tf/image/encode_png.md"><code>tf.image.encode_png</code></a>

## Classes

[`class ResizeMethod`](../tf/image/ResizeMethod.md): See <a href="../tf/image/resize.md"><code>tf.image.resize</code></a> for details.

## Functions

[`adjust_brightness(...)`](../tf/image/adjust_brightness.md): Adjust the brightness of RGB or Grayscale images.

[`adjust_contrast(...)`](../tf/image/adjust_contrast.md): Adjust contrast of RGB or grayscale images.

[`adjust_gamma(...)`](../tf/image/adjust_gamma.md): Performs [Gamma Correction](http://en.wikipedia.org/wiki/Gamma_correction).

[`adjust_hue(...)`](../tf/image/adjust_hue.md): Adjust hue of RGB images.

[`adjust_jpeg_quality(...)`](../tf/image/adjust_jpeg_quality.md): Adjust jpeg encoding quality of an image.

[`adjust_saturation(...)`](../tf/image/adjust_saturation.md): Adjust saturation of RGB images.

[`central_crop(...)`](../tf/image/central_crop.md): Crop the central region of the image(s).

[`combined_non_max_suppression(...)`](../tf/image/combined_non_max_suppression.md): Greedily selects a subset of bounding boxes in descending order of score.

[`convert_image_dtype(...)`](../tf/image/convert_image_dtype.md): Convert `image` to `dtype`, scaling its values if needed.

[`crop_and_resize(...)`](../tf/image/crop_and_resize.md): Extracts crops from the input image tensor and resizes them.

[`crop_to_bounding_box(...)`](../tf/image/crop_to_bounding_box.md): Crops an image to a specified bounding box.

[`decode_and_crop_jpeg(...)`](../tf/io/decode_and_crop_jpeg.md): Decode and Crop a JPEG-encoded image to a uint8 tensor.

[`decode_bmp(...)`](../tf/io/decode_bmp.md): Decode the first frame of a BMP-encoded image to a uint8 tensor.

[`decode_gif(...)`](../tf/io/decode_gif.md): Decode the frame(s) of a GIF-encoded image to a uint8 tensor.

[`decode_image(...)`](../tf/io/decode_image.md): Function for `decode_bmp`, `decode_gif`, `decode_jpeg`, and `decode_png`.

[`decode_jpeg(...)`](../tf/io/decode_jpeg.md): Decode a JPEG-encoded image to a uint8 tensor.

[`decode_png(...)`](../tf/io/decode_png.md): Decode a PNG-encoded image to a uint8 or uint16 tensor.

[`draw_bounding_boxes(...)`](../tf/image/draw_bounding_boxes.md): Draw bounding boxes on a batch of images.

[`encode_jpeg(...)`](../tf/io/encode_jpeg.md): JPEG-encode an image.

[`encode_png(...)`](../tf/image/encode_png.md): PNG-encode an image.

[`extract_glimpse(...)`](../tf/image/extract_glimpse.md): Extracts a glimpse from the input tensor.

[`extract_jpeg_shape(...)`](../tf/io/extract_jpeg_shape.md): Extract the shape information of a JPEG-encoded image.

[`extract_patches(...)`](../tf/image/extract_patches.md): Extract `patches` from `images`.

[`flip_left_right(...)`](../tf/image/flip_left_right.md): Flip an image horizontally (left to right).

[`flip_up_down(...)`](../tf/image/flip_up_down.md): Flip an image vertically (upside down).

[`generate_bounding_box_proposals(...)`](../tf/image/generate_bounding_box_proposals.md): Generate bounding box proposals from encoded bounding boxes.

[`grayscale_to_rgb(...)`](../tf/image/grayscale_to_rgb.md): Converts one or more images from Grayscale to RGB.

[`hsv_to_rgb(...)`](../tf/image/hsv_to_rgb.md): Convert one or more images from HSV to RGB.

[`image_gradients(...)`](../tf/image/image_gradients.md): Returns image gradients (dy, dx) for each color channel.

[`is_jpeg(...)`](../tf/io/is_jpeg.md): Convenience function to check if the 'contents' encodes a JPEG image.

[`non_max_suppression(...)`](../tf/image/non_max_suppression.md): Greedily selects a subset of bounding boxes in descending order of score.

[`non_max_suppression_overlaps(...)`](../tf/image/non_max_suppression_overlaps.md): Greedily selects a subset of bounding boxes in descending order of score.

[`non_max_suppression_padded(...)`](../tf/image/non_max_suppression_padded.md): Greedily selects a subset of bounding boxes in descending order of score.

[`non_max_suppression_with_scores(...)`](../tf/image/non_max_suppression_with_scores.md): Greedily selects a subset of bounding boxes in descending order of score.

[`pad_to_bounding_box(...)`](../tf/image/pad_to_bounding_box.md): Pad `image` with zeros to the specified `height` and `width`.

[`per_image_standardization(...)`](../tf/image/per_image_standardization.md): Linearly scales each image in `image` to have mean 0 and variance 1.

[`psnr(...)`](../tf/image/psnr.md): Returns the Peak Signal-to-Noise Ratio between a and b.

[`random_brightness(...)`](../tf/image/random_brightness.md): Adjust the brightness of images by a random factor.

[`random_contrast(...)`](../tf/image/random_contrast.md): Adjust the contrast of an image or images by a random factor.

[`random_crop(...)`](../tf/image/random_crop.md): Randomly crops a tensor to a given size.

[`random_flip_left_right(...)`](../tf/image/random_flip_left_right.md): Randomly flip an image horizontally (left to right).

[`random_flip_up_down(...)`](../tf/image/random_flip_up_down.md): Randomly flips an image vertically (upside down).

[`random_hue(...)`](../tf/image/random_hue.md): Adjust the hue of RGB images by a random factor.

[`random_jpeg_quality(...)`](../tf/image/random_jpeg_quality.md): Randomly changes jpeg encoding quality for inducing jpeg noise.

[`random_saturation(...)`](../tf/image/random_saturation.md): Adjust the saturation of RGB images by a random factor.

[`resize(...)`](../tf/image/resize.md): Resize `images` to `size` using the specified `method`.

[`resize_with_crop_or_pad(...)`](../tf/image/resize_with_crop_or_pad.md): Crops and/or pads an image to a target width and height.

[`resize_with_pad(...)`](../tf/image/resize_with_pad.md): Resizes and pads an image to a target width and height.

[`rgb_to_grayscale(...)`](../tf/image/rgb_to_grayscale.md): Converts one or more images from RGB to Grayscale.

[`rgb_to_hsv(...)`](../tf/image/rgb_to_hsv.md): Converts one or more images from RGB to HSV.

[`rgb_to_yiq(...)`](../tf/image/rgb_to_yiq.md): Converts one or more images from RGB to YIQ.

[`rgb_to_yuv(...)`](../tf/image/rgb_to_yuv.md): Converts one or more images from RGB to YUV.

[`rot90(...)`](../tf/image/rot90.md): Rotate image(s) counter-clockwise by 90 degrees.

[`sample_distorted_bounding_box(...)`](../tf/image/sample_distorted_bounding_box.md): Generate a single randomly distorted bounding box for an image.

[`sobel_edges(...)`](../tf/image/sobel_edges.md): Returns a tensor holding Sobel edge maps.

[`ssim(...)`](../tf/image/ssim.md): Computes SSIM index between img1 and img2.

[`ssim_multiscale(...)`](../tf/image/ssim_multiscale.md): Computes the MS-SSIM between img1 and img2.

[`total_variation(...)`](../tf/image/total_variation.md): Calculate and return the total variation for one or more images.

[`transpose(...)`](../tf/image/transpose.md): Transpose image(s) by swapping the height and width dimension.

[`yiq_to_rgb(...)`](../tf/image/yiq_to_rgb.md): Converts one or more images from YIQ to RGB.

[`yuv_to_rgb(...)`](../tf/image/yuv_to_rgb.md): Converts one or more images from YUV to RGB.

