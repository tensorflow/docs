description: Transforms a spectrogram into a form that's useful for speech recognition.

robots: noindex

# tf.raw_ops.Mfcc

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Transforms a spectrogram into a form that's useful for speech recognition.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Mfcc`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Mfcc(
    spectrogram, sample_rate, upper_frequency_limit=4000, lower_frequency_limit=20,
    filterbank_channel_count=40, dct_coefficient_count=13, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Mel Frequency Cepstral Coefficients are a way of representing audio data that's
been effective as an input feature for machine learning. They are created by
taking the spectrum of a spectrogram (a 'cepstrum'), and discarding some of the
higher frequencies that are less significant to the human ear. They have a long
history in the speech recognition world, and https://en.wikipedia.org/wiki/Mel-frequency_cepstrum
is a good resource to learn more.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`spectrogram`
</td>
<td>
A `Tensor` of type `float32`.
Typically produced by the Spectrogram op, with magnitude_squared
set to true.
</td>
</tr><tr>
<td>
`sample_rate`
</td>
<td>
A `Tensor` of type `int32`.
How many samples per second the source audio used.
</td>
</tr><tr>
<td>
`upper_frequency_limit`
</td>
<td>
An optional `float`. Defaults to `4000`.
The highest frequency to use when calculating the
ceptstrum.
</td>
</tr><tr>
<td>
`lower_frequency_limit`
</td>
<td>
An optional `float`. Defaults to `20`.
The lowest frequency to use when calculating the
ceptstrum.
</td>
</tr><tr>
<td>
`filterbank_channel_count`
</td>
<td>
An optional `int`. Defaults to `40`.
Resolution of the Mel bank used internally.
</td>
</tr><tr>
<td>
`dct_coefficient_count`
</td>
<td>
An optional `int`. Defaults to `13`.
How many output channels to produce per time slice.
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

