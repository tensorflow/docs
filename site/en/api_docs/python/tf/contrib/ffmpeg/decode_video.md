page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.ffmpeg.decode_video

Create an op that decodes the contents of a video file. (deprecated)

``` python
tf.contrib.ffmpeg.decode_video(contents)
```



Defined in [`contrib/ffmpeg/ffmpeg_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/ffmpeg/ffmpeg_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2018-09-04.
Instructions for updating:
tf.contrib.ffmpeg will be removed in 2.0, the support for video and audio will continue to be provided in tensorflow-io: https://github.com/tensorflow/io

#### Args:


* <b>`contents`</b>: The binary contents of the video file to decode. This is a scalar.


#### Returns:

A rank-4 `Tensor` that has `[frames, height, width, 3]` RGB as output.
