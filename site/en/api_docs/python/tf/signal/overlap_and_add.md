description: Reconstructs a signal from a framed representation.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal.overlap_and_add" />
<meta itemprop="path" content="Stable" />
</div>

# tf.signal.overlap_and_add

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/signal/reconstruction_ops.py#L29-L165">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Reconstructs a signal from a framed representation.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.signal.overlap_and_add`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.signal.overlap_and_add(
    signal, frame_step, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Adds potentially overlapping frames of a signal with shape
`[..., frames, frame_length]`, offsetting subsequent frames by `frame_step`.
The resulting tensor has shape `[..., output_size]` where

    output_size = (frames - 1) * frame_step + frame_length

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`signal`
</td>
<td>
A [..., frames, frame_length] `Tensor`. All dimensions may be
unknown, and rank must be at least 2.
</td>
</tr><tr>
<td>
`frame_step`
</td>
<td>
An integer or scalar `Tensor` denoting overlap offsets. Must be
less than or equal to `frame_length`.
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
A `Tensor` with shape `[..., output_size]` containing the overlap-added
frames of `signal`'s inner-most two dimensions.
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
If `signal`'s rank is less than 2, or `frame_step` is not a
scalar integer.
</td>
</tr>
</table>

