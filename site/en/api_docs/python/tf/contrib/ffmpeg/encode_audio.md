page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.ffmpeg.encode_audio

``` python
tf.contrib.ffmpeg.encode_audio(
    audio,
    file_format=None,
    samples_per_second=None
)
```



Defined in [`tensorflow/contrib/ffmpeg/ffmpeg_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/ffmpeg/ffmpeg_ops.py).

See the guide: [FFmpeg (contrib) > Encoding and decoding audio using FFmpeg](../../../../../api_guides/python/contrib.ffmpeg#Encoding_and_decoding_audio_using_FFmpeg)

Creates an op that encodes an audio file using sampled audio from a tensor.

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