description: Produces a visualization of audio data over time.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.AudioSpectrogram" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.AudioSpectrogram

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Produces a visualization of audio data over time.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.AudioSpectrogram`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.AudioSpectrogram(
    input, window_size, stride, magnitude_squared=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Spectrograms are a standard way of representing audio information as a series of
slices of frequency information, one slice for each window of time. By joining
these together into a sequence, they form a distinctive fingerprint of the sound
over time.

This op expects to receive audio data as an input, stored as floats in the range
-1 to 1, together with a window width in samples, and a stride specifying how
far to move the window between slices. From this it generates a three
dimensional output. The first dimension is for the channels in the input, so a
stereo audio input would have two here for example. The second dimension is time,
with successive frequency slices. The third dimension has an amplitude value for
each frequency during that time slice.

This means the layout when converted and saved as an image is rotated 90 degrees
clockwise from a typical spectrogram. Time is descending down the Y axis, and
the frequency decreases from left to right.

Each value in the result represents the square root of the sum of the real and
imaginary parts of an FFT on the current window of samples. In this way, the
lowest dimension represents the power of each frequency in the current window,
and adjacent windows are concatenated in the next dimension.

To get a more intuitive and visual look at what this operation does, you can run
tensorflow/examples/wav_to_spectrogram to read in an audio file and save out the
resulting spectrogram as a PNG image.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor` of type `float32`. Float representation of audio data.
</td>
</tr><tr>
<td>
`window_size`
</td>
<td>
An `int`.
How wide the input window is in samples. For the highest efficiency
this should be a power of two, but other values are accepted.
</td>
</tr><tr>
<td>
`stride`
</td>
<td>
An `int`.
How widely apart the center of adjacent sample windows should be.
</td>
</tr><tr>
<td>
`magnitude_squared`
</td>
<td>
An optional `bool`. Defaults to `False`.
Whether to return the squared magnitude or just the
magnitude. Using squared magnitude can avoid extra calculations.
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
A `Tensor` of type `float32`.
</td>
</tr>

</table>

