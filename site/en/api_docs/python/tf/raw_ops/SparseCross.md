description: Generates sparse cross from a list of sparse and dense tensors.

robots: noindex

# tf.raw_ops.SparseCross

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Generates sparse cross from a list of sparse and dense tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseCross`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseCross(
    indices, values, shapes, dense_inputs, hashed_output, num_buckets, hash_key,
    out_type, internal_type, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The op takes two lists, one of 2D `SparseTensor` and one of 2D `Tensor`, each
representing features of one feature column. It outputs a 2D `SparseTensor` with
the batchwise crosses of these features.

For example, if the inputs are

    inputs[0]: SparseTensor with shape = [2, 2]
    [0, 0]: "a"
    [1, 0]: "b"
    [1, 1]: "c"

    inputs[1]: SparseTensor with shape = [2, 1]
    [0, 0]: "d"
    [1, 0]: "e"

    inputs[2]: Tensor [["f"], ["g"]]

then the output will be

    shape = [2, 2]
    [0, 0]: "a_X_d_X_f"
    [1, 0]: "b_X_e_X_g"
    [1, 1]: "c_X_e_X_g"

if hashed_output=true then the output will be

    shape = [2, 2]
    [0, 0]: FingerprintCat64(
                Fingerprint64("f"), FingerprintCat64(
                    Fingerprint64("d"), Fingerprint64("a")))
    [1, 0]: FingerprintCat64(
                Fingerprint64("g"), FingerprintCat64(
                    Fingerprint64("e"), Fingerprint64("b")))
    [1, 1]: FingerprintCat64(
                Fingerprint64("g"), FingerprintCat64(
                    Fingerprint64("e"), Fingerprint64("c")))

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`indices`
</td>
<td>
A list of `Tensor` objects with type `int64`.
2-D.  Indices of each input `SparseTensor`.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A list of `Tensor` objects with types from: `int64`, `string`.
1-D.   values of each `SparseTensor`.
</td>
</tr><tr>
<td>
`shapes`
</td>
<td>
A list with the same length as `indices` of `Tensor` objects with type `int64`.
1-D.   Shapes of each `SparseTensor`.
</td>
</tr><tr>
<td>
`dense_inputs`
</td>
<td>
A list of `Tensor` objects with types from: `int64`, `string`.
2-D.    Columns represented by dense `Tensor`.
</td>
</tr><tr>
<td>
`hashed_output`
</td>
<td>
A `bool`.
If true, returns the hash of the cross instead of the string.
This will allow us avoiding string manipulations.
</td>
</tr><tr>
<td>
`num_buckets`
</td>
<td>
An `int` that is `>= 0`. It is used if hashed_output is true.
output = hashed_value%num_buckets if num_buckets > 0 else hashed_value.
</td>
</tr><tr>
<td>
`hash_key`
</td>
<td>
An `int`.
Specify the hash_key that will be used by the `FingerprintCat64`
function to combine the crosses fingerprints.
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int64, tf.string`.
</td>
</tr><tr>
<td>
`internal_type`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int64, tf.string`.
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
A tuple of `Tensor` objects (output_indices, output_values, output_shape).
</td>
</tr>
<tr>
<td>
`output_indices`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`output_values`
</td>
<td>
A `Tensor` of type `out_type`.
</td>
</tr><tr>
<td>
`output_shape`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr>
</table>

