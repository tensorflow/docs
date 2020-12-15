description: Computes the 1D [Inverse Discrete Cosine Transform (DCT)][idct] of input.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal.idct" />
<meta itemprop="path" content="Stable" />
</div>

# tf.signal.idct

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/signal/dct_ops.py#L185-L228">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the 1D [Inverse Discrete Cosine Transform (DCT)][idct] of `input`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.signal.idct`, `tf.compat.v1.spectral.idct`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.signal.idct(
    input, type=2, n=None, axis=-1, norm=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Currently Types I, II, III, IV are supported. Type III is the inverse of
Type II, and vice versa.

Note that you must re-normalize by 1/(2n) to obtain an inverse if `norm` is
not `'ortho'`. That is:
`signal == idct(dct(signal)) * 0.5 / signal.shape[-1]`.
When `norm='ortho'`, we have:
`signal == idct(dct(signal, norm='ortho'), norm='ortho')`.



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
The IDCT type to perform. Must be 1, 2, 3 or 4.
</td>
</tr><tr>
<td>
`n`
</td>
<td>
For future expansion. The length of the transform. Must be `None`.
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
A `[..., samples]` `float32`/`float64` `Tensor` containing the IDCT of
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
If `type` is not `1`, `2` or `3`, `n` is not `None, `axis` is
not `-1`, or `norm` is not `None` or `'ortho'`.
</td>
</tr>
</table>


[idct]:
https://en.wikipedia.org/wiki/Discrete_cosine_transform#Inverse_transforms

#### Scipy Compatibility
Equivalent to [scipy.fftpack.idct]
 (https://docs.scipy.org/doc/scipy-1.4.0/reference/generated/scipy.fftpack.idct.html)
 for Type-I, Type-II, Type-III and Type-IV DCT.

