description: Generates fingerprint values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.fingerprint" />
<meta itemprop="path" content="Stable" />
</div>

# tf.fingerprint

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L6038-L6085">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generates fingerprint values.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.fingerprint`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.fingerprint(
    data, method='farmhash64', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Generates fingerprint values of `data`.

Fingerprint op considers the first dimension of `data` as the batch dimension,
and `output[i]` contains the fingerprint value generated from contents in
`data[i, ...]` for all `i`.

Fingerprint op writes fingerprint values as byte arrays. For example, the
default method `farmhash64` generates a 64-bit fingerprint value at a time.
This 8-byte value is written out as an <a href="../tf.md#uint8"><code>tf.uint8</code></a> array of size 8, in
little-endian order.

For example, suppose that `data` has data type <a href="../tf.md#int32"><code>tf.int32</code></a> and shape (2, 3, 4),
and that the fingerprint method is `farmhash64`. In this case, the output
shape is (2, 8), where 2 is the batch dimension size of `data`, and 8 is the
size of each fingerprint value in bytes. `output[0, :]` is generated from
12 integers in `data[0, :, :]` and similarly `output[1, :]` is generated from
other 12 integers in `data[1, :, :]`.

Note that this op fingerprints the raw underlying buffer, and it does not
fingerprint Tensor's metadata such as data type and/or shape. For example, the
fingerprint values are invariant under reshapes and bitcasts as long as the
batch dimension remain the same:

```python
tf.fingerprint(data) == tf.fingerprint(tf.reshape(data, ...))
tf.fingerprint(data) == tf.fingerprint(tf.bitcast(data, ...))
```

For string data, one should expect `tf.fingerprint(data) !=
tf.fingerprint(tf.string.reduce_join(data))` in general.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`data`
</td>
<td>
A `Tensor`. Must have rank 1 or higher.
</td>
</tr><tr>
<td>
`method`
</td>
<td>
A `Tensor` of type <a href="../tf.md#string"><code>tf.string</code></a>. Fingerprint method used by this op.
Currently available method is `farmhash64`.
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
A two-dimensional `Tensor` of type <a href="../tf.md#uint8"><code>tf.uint8</code></a>. The first dimension equals to
`data`'s first dimension, and the second dimension size depends on the
fingerprint algorithm.
</td>
</tr>

</table>

