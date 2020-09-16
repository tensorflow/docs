description: Outputs a Summary protocol buffer with audio.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.AudioSummary" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.AudioSummary

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Outputs a `Summary` protocol buffer with audio.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.AudioSummary`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.AudioSummary(
    tag, tensor, sample_rate, max_outputs=3, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The summary has up to `max_outputs` summary values containing audio. The
audio is built from `tensor` which must be 3-D with shape `[batch_size,
frames, channels]` or 2-D with shape `[batch_size, frames]`. The values are
assumed to be in the range of `[-1.0, 1.0]` with a sample rate of `sample_rate`.

The `tag` argument is a scalar `Tensor` of type `string`.  It is used to
build the `tag` of the summary values:

*  If `max_outputs` is 1, the summary value tag is '*tag*/audio'.
*  If `max_outputs` is greater than 1, the summary value tags are
   generated sequentially as '*tag*/audio/0', '*tag*/audio/1', etc.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tag`
</td>
<td>
A `Tensor` of type `string`.
Scalar. Used to build the `tag` attribute of the summary values.
</td>
</tr><tr>
<td>
`tensor`
</td>
<td>
A `Tensor` of type `float32`. 2-D of shape `[batch_size, frames]`.
</td>
</tr><tr>
<td>
`sample_rate`
</td>
<td>
A `float`. The sample rate of the signal in hertz.
</td>
</tr><tr>
<td>
`max_outputs`
</td>
<td>
An optional `int` that is `>= 1`. Defaults to `3`.
Max number of batch elements to generate audio for.
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
A `Tensor` of type `string`.
</td>
</tr>

</table>

