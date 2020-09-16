description: Returns a column for performing crosses of categorical features.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.feature_column.crossed_column" />
<meta itemprop="path" content="Stable" />
</div>

# tf.feature_column.crossed_column

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/feature_column/feature_column_v2.py#L2056-L2181">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a column for performing crosses of categorical features.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.feature_column.crossed_column`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.feature_column.crossed_column(
    keys, hash_bucket_size, hash_key=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Crossed features will be hashed according to `hash_bucket_size`. Conceptually,
the transformation can be thought of as:
  Hash(cartesian product of features) % `hash_bucket_size`

For example, if the input features are:

* SparseTensor referred by first key:

  ```python
  shape = [2, 2]
  {
      [0, 0]: "a"
      [1, 0]: "b"
      [1, 1]: "c"
  }
  ```

* SparseTensor referred by second key:

  ```python
  shape = [2, 1]
  {
      [0, 0]: "d"
      [1, 0]: "e"
  }
  ```

then crossed feature will look like:

```python
 shape = [2, 2]
{
    [0, 0]: Hash64("d", Hash64("a")) % hash_bucket_size
    [1, 0]: Hash64("e", Hash64("b")) % hash_bucket_size
    [1, 1]: Hash64("e", Hash64("c")) % hash_bucket_size
}
```

Here is an example to create a linear model with crosses of string features:

```python
keywords_x_doc_terms = crossed_column(['keywords', 'doc_terms'], 50K)
columns = [keywords_x_doc_terms, ...]
features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
linear_prediction = linear_model(features, columns)
```

You could also use vocabulary lookup before crossing:

```python
keywords = categorical_column_with_vocabulary_file(
    'keywords', '/path/to/vocabulary/file', vocabulary_size=1K)
keywords_x_doc_terms = crossed_column([keywords, 'doc_terms'], 50K)
columns = [keywords_x_doc_terms, ...]
features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
linear_prediction = linear_model(features, columns)
```

If an input feature is of numeric type, you can use
`categorical_column_with_identity`, or `bucketized_column`, as in the example:

```python
# vertical_id is an integer categorical feature.
vertical_id = categorical_column_with_identity('vertical_id', 10K)
price = numeric_column('price')
# bucketized_column converts numerical feature to a categorical one.
bucketized_price = bucketized_column(price, boundaries=[...])
vertical_id_x_price = crossed_column([vertical_id, bucketized_price], 50K)
columns = [vertical_id_x_price, ...]
features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
linear_prediction = linear_model(features, columns)
```

To use crossed column in DNN model, you need to add it in an embedding column
as in this example:

```python
vertical_id_x_price = crossed_column([vertical_id, bucketized_price], 50K)
vertical_id_x_price_embedded = embedding_column(vertical_id_x_price, 10)
dense_tensor = input_layer(features, [vertical_id_x_price_embedded, ...])
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`keys`
</td>
<td>
An iterable identifying the features to be crossed. Each element can
be either:
* string: Will use the corresponding feature which must be of string type.
* `CategoricalColumn`: Will use the transformed tensor produced by this
column. Does not support hashed categorical column.
</td>
</tr><tr>
<td>
`hash_bucket_size`
</td>
<td>
An int > 1. The number of buckets.
</td>
</tr><tr>
<td>
`hash_key`
</td>
<td>
Specify the hash_key that will be used by the `FingerprintCat64`
function to combine the crosses fingerprints on SparseCrossOp (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `CrossedColumn`.
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
If `len(keys) < 2`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If any of the keys is neither a string nor `CategoricalColumn`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If any of the keys is `HashedCategoricalColumn`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `hash_bucket_size < 1`.
</td>
</tr>
</table>

