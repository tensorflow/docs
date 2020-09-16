description: Generates hashed sparse cross from a list of sparse and dense tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.cross_hashed" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.cross_hashed

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/sparse_ops.py#L556-L600">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generates hashed sparse cross from a list of sparse and dense tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.cross_hashed`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.cross_hashed(
    inputs, num_buckets=0, hash_key=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

For example, if the inputs are

    * inputs[0]: SparseTensor with shape = [2, 2]
      [0, 0]: "a"
      [1, 0]: "b"
      [1, 1]: "c"
    * inputs[1]: SparseTensor with shape = [2, 1]
      [0, 0]: "d"
      [1, 0]: "e"
    * inputs[2]: Tensor [["f"], ["g"]]

then the output will be:

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
`inputs`
</td>
<td>
An iterable of `Tensor` or `SparseTensor`.
</td>
</tr><tr>
<td>
`num_buckets`
</td>
<td>
An `int` that is `>= 0`.
output = hashed_value%num_buckets if num_buckets > 0 else hashed_value.
</td>
</tr><tr>
<td>
`hash_key`
</td>
<td>
Integer hash_key that will be used by the `FingerprintCat64`
function. If not given, will use a default key.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the op.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `SparseTensor` of type `int64`.
</td>
</tr>

</table>

