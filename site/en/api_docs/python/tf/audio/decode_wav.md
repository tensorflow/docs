description: Decode a 16-bit PCM WAV file to a float tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.audio.decode_wav" />
<meta itemprop="path" content="Stable" />
</div>

# tf.audio.decode_wav

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Decode a 16-bit PCM WAV file to a float tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.audio.decode_wav`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.audio.decode_wav(
    contents, desired_channels=-1, desired_samples=-1, name=None
)
</code></pre>



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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`contents`
</td>
<td>
A `Tensor` of type `string`.
The WAV-encoded audio, usually from a file.
</td>
</tr><tr>
<td>
`desired_channels`
</td>
<td>
An optional `int`. Defaults to `-1`.
Number of sample channels wanted.
</td>
</tr><tr>
<td>
`desired_samples`
</td>
<td>
An optional `int`. Defaults to `-1`.
Length of audio requested.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tuple of `Tensor` objects (audio, sample_rate).
</td>
</tr>
<tr>
<td>
`audio`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`sample_rate`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr>
</table>

