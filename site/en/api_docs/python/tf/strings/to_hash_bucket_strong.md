description: Converts each string in the input Tensor to its hash mod by a number of buckets.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strings.to_hash_bucket_strong" />
<meta itemprop="path" content="Stable" />
</div>

# tf.strings.to_hash_bucket_strong

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Converts each string in the input Tensor to its hash mod by a number of buckets.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.string_to_hash_bucket_strong`, `tf.compat.v1.strings.to_hash_bucket_strong`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.strings.to_hash_bucket_strong(
    input, num_buckets, key, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The hash function is deterministic on the content of the string within the
process. The hash function is a keyed hash function, where attribute `key`
defines the key of the hash function. `key` is an array of 2 elements.

A strong hash is important when inputs may be malicious, e.g. URLs with
additional components. Adversaries could try to make their inputs hash to the
same bucket for a denial-of-service attack or to skew the results. A strong
hash can be used to make it difficult to find inputs with a skewed hash value
distribution over buckets. This requires that the hash function is
seeded by a high-entropy (random) "key" unknown to the adversary.

The additional robustness comes at a cost of roughly 4x higher compute
time than `tf.string_to_hash_bucket_fast`.

#### Examples:



```
>>> tf.strings.to_hash_bucket_strong(["Hello", "TF"], 3, [1, 2]).numpy()
array([2, 0])
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor` of type `string`. The strings to assign a hash bucket.
</td>
</tr><tr>
<td>
`num_buckets`
</td>
<td>
An `int` that is `>= 1`. The number of buckets.
</td>
</tr><tr>
<td>
`key`
</td>
<td>
A list of `ints`.
The key used to seed the hash function, passed as a list of two uint64
elements.
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
A `Tensor` of type `int64`.
</td>
</tr>

</table>

