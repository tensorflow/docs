page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.image





Image processing and decoding ops.

See the [Images](https://tensorflow.org/api_guides/python/image) guide.

## Classes

[`class ResizeMethod`](../tf/image/ResizeMethod)

## Functions

[`adjust_brightness(...)`](../tf/image/adjust_brightness): Adjust the brightness of RGB or Grayscale images.

[`adjust_contrast(...)`](../tf/image/adjust_contrast): Adjust contrast of RGB or grayscale images.

[`adjust_gamma(...)`](../tf/image/adjust_gamma): Performs Gamma Correction on the input image.

[`adjust_hue(...)`](../tf/image/adjust_hue): Adjust hue of an RGB image.

[`adjust_jpeg_quality(...)`](../tf/image/adjust_jpeg_quality): Adjust jpeg encoding quality of an RGB image.

[`adjust_saturation(...)`](../tf/image/adjust_saturation): Adjust saturation of an RGB image.

[`central_crop(...)`](../tf/image/central_crop): Crop the central region of the image(s).

[`convert_image_dtype(...)`](../tf/image/convert_image_dtype): Convert `image` to `dtype`, scaling its values if needed.

[`crop_and_resize(...)`](../tf/image/crop_and_resize): Extracts crops from the input image tensor and resizes them.

[`crop_to_bounding_box(...)`](../tf/image/crop_to_bounding_box): Crops an image to a specified bounding box.

[`decode_and_crop_jpeg(...)`](../tf/image/decode_and_crop_jpeg): Decode and Crop a JPEG-encoded image to a uint8 tensor.

[`decode_bmp(...)`](../tf/image/decode_bmp): Decode the first frame of a BMP-encoded image to a uint8 tensor.

[`decode_gif(...)`](../tf/image/decode_gif): Decode the first frame of a GIF-encoded image to a uint8 tensor.

[`decode_image(...)`](../tf/image/decode_image): Convenience function for `decode_bmp`, `decode_gif`, `decode_jpeg`,

[`decode_jpeg(...)`](../tf/image/decode_jpeg): Decode a JPEG-encoded image to a uint8 tensor.

[`decode_png(...)`](../tf/image/decode_png): Decode a PNG-encoded image to a uint8 or uint16 tensor.

[`draw_bounding_boxes(...)`](../tf/image/draw_bounding_boxes): Draw bounding boxes on a batch of images.

[`encode_jpeg(...)`](../tf/image/encode_jpeg): JPEG-encode an image.

[`encode_png(...)`](../tf/image/encode_png): PNG-encode an image.

[`extract_glimpse(...)`](../tf/image/extract_glimpse): Extracts a glimpse from the input tensor.

[`extract_image_patches(...)`](../tf/image/extract_image_patches): Extract `patches` from `images` and put them in the "depth" output dimension.

[`extract_jpeg_shape(...)`](../tf/image/extract_jpeg_shape): Extract the shape information of a JPEG-encoded image.

[`flip_left_right(...)`](../tf/image/flip_left_right): Flip an image horizontally (left to right).

[`flip_up_down(...)`](../tf/image/flip_up_down): Flip an image vertically (upside down).

[`grayscale_to_rgb(...)`](../tf/image/grayscale_to_rgb): Converts one or more images from Grayscale to RGB.

[`hsv_to_rgb(...)`](../tf/image/hsv_to_rgb): Convert one or more images from HSV to RGB.

[`image_gradients(...)`](../tf/image/image_gradients): Returns image gradients (dy, dx) for each color channel.

[`is_jpeg(...)`](../tf/image/is_jpeg): Convenience function to check if the 'contents' encodes a JPEG image.

[`non_max_suppression(...)`](../tf/image/non_max_suppression): Greedily selects a subset of bounding boxes in descending order of score.

[`non_max_suppression_overlaps(...)`](../tf/image/non_max_suppression_overlaps): Greedily selects a subset of bounding boxes in descending order of score.

[`non_max_suppression_padded(...)`](../tf/image/non_max_suppression_padded): Greedily selects a subset of bounding boxes in descending order of score.

[`pad_to_bounding_box(...)`](../tf/image/pad_to_bounding_box): Pad `image` with zeros to the specified `height` and `width`.

[`per_image_standardization(...)`](../tf/image/per_image_standardization): Linearly scales `image` to have zero mean and unit variance.

[`psnr(...)`](../tf/image/psnr): Returns the Peak Signal-to-Noise Ratio between a and b.

[`random_brightness(...)`](../tf/image/random_brightness): Adjust the brightness of images by a random factor.

[`random_contrast(...)`](../tf/image/random_contrast): Adjust the contrast of an image by a random factor.

[`random_crop(...)`](../tf/image/random_crop): Randomly crops a tensor to a given size.

[`random_flip_left_right(...)`](../tf/image/random_flip_left_right): Randomly flip an image horizontally (left to right).

[`random_flip_up_down(...)`](../tf/image/random_flip_up_down): Randomly flips an image vertically (upside down).

[`random_hue(...)`](../tf/image/random_hue): Adjust the hue of an RGB image by a random factor.

[`random_jpeg_quality(...)`](../tf/image/random_jpeg_quality): Randomly changes jpeg encoding quality for inducing jpeg noise.

[`random_saturation(...)`](../tf/image/random_saturation): Adjust the saturation of an RGB image by a random factor.

[`resize_area(...)`](../tf/image/resize_area): Resize `images` to `size` using area interpolation.

[`resize_bicubic(...)`](../tf/image/resize_bicubic): Resize `images` to `size` using bicubic interpolation.

[`resize_bilinear(...)`](../tf/image/resize_bilinear): Resize `images` to `size` using bilinear interpolation.

[`resize_image_with_crop_or_pad(...)`](../tf/image/resize_image_with_crop_or_pad): Crops and/or pads an image to a target width and height.

[`resize_image_with_pad(...)`](../tf/image/resize_image_with_pad): Resizes and pads an image to a target width and height.

[`resize_images(...)`](../tf/image/resize_images): Resize `images` to `size` using the specified `method`.

[`resize_nearest_neighbor(...)`](../tf/image/resize_nearest_neighbor): Resize `images` to `size` using nearest neighbor interpolation.

[`rgb_to_grayscale(...)`](../tf/image/rgb_to_grayscale): Converts one or more images from RGB to Grayscale.

[`rgb_to_hsv(...)`](../tf/image/rgb_to_hsv): Converts one or more images from RGB to HSV.

[`rgb_to_yiq(...)`](../tf/image/rgb_to_yiq): Converts one or more images from RGB to YIQ.

[`rgb_to_yuv(...)`](../tf/image/rgb_to_yuv): Converts one or more images from RGB to YUV.

[`rot90(...)`](../tf/image/rot90): Rotate image(s) counter-clockwise by 90 degrees.

[`sample_distorted_bounding_box(...)`](../tf/image/sample_distorted_bounding_box): Generate a single randomly distorted bounding box for an image.

[`sobel_edges(...)`](../tf/image/sobel_edges): Returns a tensor holding Sobel edge maps.

[`ssim(...)`](../tf/image/ssim): Computes SSIM index between img1 and img2.

[`ssim_multiscale(...)`](../tf/image/ssim_multiscale): Computes the MS-SSIM between img1 and img2.

[`total_variation(...)`](../tf/image/total_variation): Calculate and return the total variation for one or more images.

[`transpose_image(...)`](../tf/image/transpose_image): Transpose image(s) by swapping the height and width dimension.

[`yiq_to_rgb(...)`](../tf/image/yiq_to_rgb): Converts one or more images from YIQ to RGB.

[`yuv_to_rgb(...)`](../tf/image/yuv_to_rgb): Converts one or more images from YUV to RGB.

