page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.ffmpeg.decode_audio

Create an op that decodes the contents of an audio file. (deprecated)

``` python
tf.contrib.ffmpeg.decode_audio(
    contents,
    file_format=None,
    samples_per_second=None,
    channel_count=None,
    stream=None
)
```



Defined in [`contrib/ffmpeg/ffmpeg_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/ffmpeg/ffmpeg_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2018-09-04.
Instructions for updating:
tf.contrib.ffmpeg will be removed in 2.0, the support for video and audio will continue to be provided in tensorflow-io: https://github.com/tensorflow/io

Note that ffmpeg is free to select the "best" audio track from an mp4.
https://trac.ffmpeg.org/wiki/Map

#### Args:


* <b>`contents`</b>: The binary contents of the audio file to decode. This is a
    scalar.
* <b>`file_format`</b>: A string or scalar string tensor specifying which
    format the contents will conform to. This can be mp3, mp4, ogg,
    or wav.
* <b>`samples_per_second`</b>: The number of samples per second that is
    assumed, as an `int` or scalar `int32` tensor. In some cases,
    resampling will occur to generate the correct sample rate.
* <b>`channel_count`</b>: The number of channels that should be created from the
    audio contents, as an `int` or scalar `int32` tensor. If the
    `contents` have more than this number, then some channels will
    be merged or dropped. If `contents` has fewer than this, then
    additional channels will be created from the existing ones.
* <b>`stream`</b>: A string specifying which stream from the content file
    should be decoded, e.g., '0' means the 0-th stream.
    The default value is '' which leaves the decision to ffmpeg.


#### Returns:

A rank-2 tensor that has time along dimension 0 and channels along
dimension 1. Dimension 0 will be `samples_per_second *
length_in_seconds` wide, and dimension 1 will be `channel_count`
wide. If ffmpeg fails to decode the audio then an empty tensor will
be returned.
