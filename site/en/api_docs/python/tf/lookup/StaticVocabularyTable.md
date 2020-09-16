description: String to Id table wrapper that assigns out-of-vocabulary keys to buckets.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.lookup.StaticVocabularyTable" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="lookup"/>
<meta itemprop="property" content="size"/>
</div>

# tf.lookup.StaticVocabularyTable

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/lookup_ops.py#L1098-L1275">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



String to Id table wrapper that assigns out-of-vocabulary keys to buckets.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.lookup.StaticVocabularyTable(
    initializer, num_oov_buckets, lookup_key_dtype=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

For example, if an instance of `StaticVocabularyTable` is initialized with a
string-to-id initializer that maps:

* `emerson -> 0`
* `lake -> 1`
* `palmer -> 2`

The `Vocabulary` object will performs the following mapping:

* `emerson -> 0`
* `lake -> 1`
* `palmer -> 2`
* `<other term> -> bucket_id`, where bucket_id will be between `3` and
`3 + num_oov_buckets - 1`, calculated by:
`hash(<term>) % num_oov_buckets + vocab_size`

If input_tensor is `["emerson", "lake", "palmer", "king", "crimson"]`,
the lookup result is `[0, 1, 2, 4, 7]`.

If `initializer` is None, only out-of-vocabulary buckets are used.

#### Example usage:



```python
num_oov_buckets = 3
input_tensor = tf.constant(["emerson", "lake", "palmer", "king", "crimnson"])
table = tf.lookup.StaticVocabularyTable(
    tf.lookup.TextFileInitializer(
        filename,
        key_dtype=tf.string, key_index=tf.lookup.TextFileIndex.WHOLE_LINE,
        value_dtype=tf.int64, value_index=tf.lookup.TextFileIndex.LINE_NUMBER,
        delimiter="\t"),
    num_oov_buckets)
out = table.lookup(input_tensor).
table.init.run()
print(out.eval())
```

The hash function used for generating out-of-vocabulary buckets ID is
Fingerprint64.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`initializer`
</td>
<td>
A TableInitializerBase object that contains the data used to
initialize the table. If None, then we only use out-of-vocab buckets.
</td>
</tr><tr>
<td>
`num_oov_buckets`
</td>
<td>
Number of buckets to use for out-of-vocabulary keys. Must
be greater than zero.
</td>
</tr><tr>
<td>
`lookup_key_dtype`
</td>
<td>
Data type of keys passed to `lookup`. Defaults to
`initializer.key_dtype` if `initializer` is specified, otherwise
<a href="../../tf.md#string"><code>tf.string</code></a>. Must be string or integer, and must be castable to
`initializer.key_dtype`.
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
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
when `num_oov_buckets` is not positive.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
when lookup_key_dtype or initializer.key_dtype are not
integer or string. Also when initializer.value_dtype != int64.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`key_dtype`
</td>
<td>
The table key dtype.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The name of the table.
</td>
</tr><tr>
<td>
`resource_handle`
</td>
<td>
Returns the resource handle associated with this Resource.
</td>
</tr><tr>
<td>
`value_dtype`
</td>
<td>
The table value dtype.
</td>
</tr>
</table>



## Methods

<h3 id="lookup"><code>lookup</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/lookup_ops.py#L1236-L1275">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>lookup(
    keys, name=None
)
</code></pre>

Looks up `keys` in the table, outputs the corresponding values.

It assigns out-of-vocabulary keys to buckets based in their hashes.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`keys`
</td>
<td>
Keys to look up. May be either a `SparseTensor` or dense `Tensor`.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `SparseTensor` if keys are sparse, otherwise a dense `Tensor`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
when `keys` doesn't match the table key data type.
</td>
</tr>
</table>



<h3 id="size"><code>size</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/lookup_ops.py#L1227-L1234">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>size(
    name=None
)
</code></pre>

Compute the number of elements in this table.




