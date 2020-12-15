description: Converts each string in the input Tensor to its hash mod by a number of buckets.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strings.to_hash_bucket" />
<meta itemprop="path" content="Stable" />
</div>

# tf.strings.to_hash_bucket

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/string_ops.py#L496-L523">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts each string in the input Tensor to its hash mod by a number of buckets.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.strings.to_hash_bucket(
    input, num_buckets, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The hash function is deterministic on the content of the string within the
process.

Note that the hash function may change from time to time.
This functionality will be deprecated and it's recommended to use
<a href="../../tf/strings/to_hash_bucket_fast.md"><code>tf.strings.to_hash_bucket_fast()</code></a> or <a href="../../tf/strings/to_hash_bucket_strong.md"><code>tf.strings.to_hash_bucket_strong()</code></a>.

#### Examples:



```
>>> tf.strings.to_hash_bucket(["Hello", "TensorFlow", "2.x"], 3)
<tf.Tensor: shape=(3,), dtype=int64, numpy=array([2, 0, 1])>
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
A `Tensor` of type `string`.
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

