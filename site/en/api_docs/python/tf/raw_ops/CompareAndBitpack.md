description: Compare values of input to threshold and pack resulting bits into a uint8.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.CompareAndBitpack" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.CompareAndBitpack

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Compare values of `input` to `threshold` and pack resulting bits into a `uint8`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CompareAndBitpack`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CompareAndBitpack(
    input, threshold, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Each comparison returns a boolean `true` (if `input_value > threshold`)
or and `false` otherwise.

This operation is useful for Locality-Sensitive-Hashing (LSH) and other
algorithms that use hashing approximations of cosine and `L2` distances;
codes can be generated from an input via:

```python
codebook_size = 50
codebook_bits = codebook_size * 32
codebook = tf.get_variable('codebook', [x.shape[-1].value, codebook_bits],
                           dtype=x.dtype,
                           initializer=tf.orthogonal_initializer())
codes = compare_and_threshold(tf.matmul(x, codebook), threshold=0.)
codes = tf.bitcast(codes, tf.int32)  # go from uint8 to int32
# now codes has shape x.shape[:-1] + [codebook_size]
```

**NOTE**: Currently, the innermost dimension of the tensor must be divisible
by 8.

Given an `input` shaped `[s0, s1, ..., s_n]`, the output is
a `uint8` tensor shaped `[s0, s1, ..., s_n / 8]`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `bool`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`.
Values to compare against `threshold` and bitpack.
</td>
</tr><tr>
<td>
`threshold`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
Threshold to compare against.
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
A `Tensor` of type `uint8`.
</td>
</tr>

</table>

