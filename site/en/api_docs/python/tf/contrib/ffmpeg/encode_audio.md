page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.ffmpeg.encode_audio

Creates an op that encodes an audio file using sampled audio from a tensor. (deprecated)

``` python
tf.contrib.ffmpeg.encode_audio(
    audio,
    file_format=None,
    samples_per_second=None
)
```



Defined in [`contrib/ffmpeg/ffmpeg_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/ffmpeg/ffmpeg_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2018-09-04.
Instructions for updating:
tf.contrib.ffmpeg will be removed in 2.0, the support for video and audio will continue to be provided in tensorflow-io: https://github.com/tensorflow/io

#### Args:


* <b>`audio`</b>: A rank-2 `Tensor` that has time along dimension 0 and
    channels along dimension 1. Dimension 0 is `samples_per_second *
    length_in_seconds` long.
* <b>`file_format`</b>: The type of file to encode, as a string or rank-0
    string tensor. "wav" is the only supported format.
* <b>`samples_per_second`</b>: The number of samples in the audio tensor per
    second of audio, as an `int` or rank-0 `int32` tensor.


#### Returns:

A scalar tensor that contains the encoded audio in the specified file
format.
