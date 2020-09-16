description: Generates fingerprint values.

robots: noindex

# tf.raw_ops.Fingerprint

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Generates fingerprint values.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Fingerprint`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Fingerprint(
    data, method, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Generates fingerprint values of `data`.

Fingerprint op considers the first dimension of `data` as the batch dimension,
and `output[i]` contains the fingerprint value generated from contents in
`data[i, ...]` for all `i`.

Fingerprint op writes fingerprint values as byte arrays. For example, the
default method `farmhash64` generates a 64-bit fingerprint value at a time.
This 8-byte value is written out as an `uint8` array of size 8, in little-endian
order.

For example, suppose that `data` has data type `DT_INT32` and shape (2, 3, 4),
and that the fingerprint method is `farmhash64`. In this case, the output shape
is (2, 8), where 2 is the batch dimension size of `data`, and 8 is the size of
each fingerprint value in bytes. `output[0, :]` is generated from 12 integers in
`data[0, :, :]` and similarly `output[1, :]` is generated from other 12 integers
in `data[1, :, :]`.

Note that this op fingerprints the raw underlying buffer, and it does not
fingerprint Tensor's metadata such as data type and/or shape. For example, the
fingerprint values are invariant under reshapes and bitcasts as long as the
batch dimension remain the same:

```
Fingerprint(data) == Fingerprint(Reshape(data, ...))
Fingerprint(data) == Fingerprint(Bitcast(data, ...))
```

For string data, one should expect `Fingerprint(data) !=
Fingerprint(ReduceJoin(data))` in general.

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
A `Tensor` of type `string`.
Fingerprint method used by this op. Currently available method is
`farmhash::fingerprint64`.
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

