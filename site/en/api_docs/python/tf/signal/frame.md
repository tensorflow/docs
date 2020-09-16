description: Expands signal's axis dimension into frames of frame_length.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal.frame" />
<meta itemprop="path" content="Stable" />
</div>

# tf.signal.frame

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/signal/shape_ops.py#L58-L216">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Expands `signal`'s `axis` dimension into frames of `frame_length`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.signal.frame`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.signal.frame(
    signal, frame_length, frame_step, pad_end=(False), pad_value=0, axis=-1,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Slides a window of size `frame_length` over `signal`'s `axis` dimension
with a stride of `frame_step`, replacing the `axis` dimension with
`[frames, frame_length]` frames.

If `pad_end` is True, window positions that are past the end of the `axis`
dimension are padded with `pad_value` until the window moves fully past the
end of the dimension. Otherwise, only window positions that fully overlap the
`axis` dimension are produced.

#### For example:



```python
# A batch size 3 tensor of 9152 audio samples.
audio = tf.random.normal([3, 9152])

# Compute overlapping frames of length 512 with a step of 180 (frames overlap
# by 332 samples). By default, only 50 frames are generated since the last
# 152 samples do not form a full frame.
frames = tf.signal.frame(audio, 512, 180)
frames.shape.assert_is_compatible_with([3, 50, 512])

# When pad_end is enabled, the final frame is kept (padded with zeros).
frames = tf.signal.frame(audio, 512, 180, pad_end=True)
frames.shape.assert_is_compatible_with([3, 51, 512])
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`signal`
</td>
<td>
A `[..., samples, ...]` `Tensor`. The rank and dimensions
may be unknown. Rank must be at least 1.
</td>
</tr><tr>
<td>
`frame_length`
</td>
<td>
The frame length in samples. An integer or scalar `Tensor`.
</td>
</tr><tr>
<td>
`frame_step`
</td>
<td>
The frame hop size in samples. An integer or scalar `Tensor`.
</td>
</tr><tr>
<td>
`pad_end`
</td>
<td>
Whether to pad the end of `signal` with `pad_value`.
</td>
</tr><tr>
<td>
`pad_value`
</td>
<td>
An optional scalar `Tensor` to use where the input signal
does not exist when `pad_end` is True.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
A scalar integer `Tensor` indicating the axis to frame. Defaults to
the last axis. Supports negative values for indexing from the end.
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
A `Tensor` of frames with shape `[..., frames, frame_length, ...]`.
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
If `frame_length`, `frame_step`, `pad_value`, or `axis` are not
scalar.
</td>
</tr>
</table>

