page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.audio.decode_wav


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/audio/decode_wav">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_audio_ops.py`



Decode a 16-bit PCM WAV file to a float tensor.

### Aliases:

* <a href="/api_docs/python/tf/audio/decode_wav"><code>tf.compat.v1.audio.decode_wav</code></a>
* <a href="/api_docs/python/tf/audio/decode_wav"><code>tf.compat.v2.audio.decode_wav</code></a>


``` python
tf.audio.decode_wav(
    contents,
    desired_channels=-1,
    desired_samples=-1,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The -32768 to 32767 signed 16-bit values will be scaled to -1.0 to 1.0 in float.

When desired_channels is set, if the input contains fewer channels than this
then the last channel will be duplicated to give the requested number, else if
the input has more channels than requested then the additional channels will be
ignored.

If desired_samples is set, then the audio will be cropped or padded with zeroes
to the requested length.

The first output contains a Tensor with the content of the audio samples. The
lowest dimension will be the number of channels, and the second will be the
number of samples. For example, a ten-sample-long stereo WAV file should give an
output shape of [10, 2].

#### Args:


* <b>`contents`</b>: A `Tensor` of type `string`.
  The WAV-encoded audio, usually from a file.
* <b>`desired_channels`</b>: An optional `int`. Defaults to `-1`.
  Number of sample channels wanted.
* <b>`desired_samples`</b>: An optional `int`. Defaults to `-1`.
  Length of audio requested.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of `Tensor` objects (audio, sample_rate).


* <b>`audio`</b>: A `Tensor` of type `float32`.
* <b>`sample_rate`</b>: A `Tensor` of type `int32`.
