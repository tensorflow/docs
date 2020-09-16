description: Computes the 1D [Discrete Cosine Transform (DCT)][dct] of input.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal.dct" />
<meta itemprop="path" content="Stable" />
</div>

# tf.signal.dct

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/signal/dct_ops.py#L52-L179">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the 1D [Discrete Cosine Transform (DCT)][dct] of `input`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.signal.dct`, `tf.compat.v1.spectral.dct`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.signal.dct(
    input, type=2, n=None, axis=-1, norm=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Types I, II, III and IV are supported.
Type I is implemented using a length `2N` padded <a href="../../tf/signal/rfft.md"><code>tf.signal.rfft</code></a>.
Type II is implemented using a length `2N` padded <a href="../../tf/signal/rfft.md"><code>tf.signal.rfft</code></a>, as
 described here: [Type 2 DCT using 2N FFT padded (Makhoul)]
 (https://dsp.stackexchange.com/a/10606).
Type III is a fairly straightforward inverse of Type II
 (i.e. using a length `2N` padded <a href="../../tf/signal/irfft.md"><code>tf.signal.irfft</code></a>).
 Type IV is calculated through 2N length DCT2 of padded signal and
picking the odd indices.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `[..., samples]` `float32`/`float64` `Tensor` containing the
signals to take the DCT of.
</td>
</tr><tr>
<td>
`type`
</td>
<td>
The DCT type to perform. Must be 1, 2, 3 or 4.
</td>
</tr><tr>
<td>
`n`
</td>
<td>
The length of the transform. If length is less than sequence length,
only the first n elements of the sequence are considered for the DCT.
If n is greater than the sequence length, zeros are padded and then
the DCT is computed as usual.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
For future expansion. The axis to compute the DCT along. Must be `-1`.
</td>
</tr><tr>
<td>
`norm`
</td>
<td>
The normalization to apply. `None` for no normalization or `'ortho'`
for orthonormal normalization.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
An optional name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `[..., samples]` `float32`/`float64` `Tensor` containing the DCT of
`input`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `type` is not `1`, `2`, `3` or `4`, `axis` is
not `-1`, `n` is not `None` or greater than 0,
or `norm` is not `None` or `'ortho'`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `type` is `1` and `norm` is `ortho`.
</td>
</tr>
</table>


[dct]: https://en.wikipedia.org/wiki/Discrete_cosine_transform

#### Scipy Compatibility
Equivalent to [scipy.fftpack.dct]
 (https://docs.scipy.org/doc/scipy-1.4.0/reference/generated/scipy.fftpack.dct.html)
 for Type-I, Type-II, Type-III and Type-IV DCT.

