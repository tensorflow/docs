description: Applies weight values to a CategoricalColumn.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.feature_column.weighted_categorical_column" />
<meta itemprop="path" content="Stable" />
</div>

# tf.feature_column.weighted_categorical_column

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/feature_column/feature_column_v2.py#L1624-L1697">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Applies weight values to a `CategoricalColumn`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.feature_column.weighted_categorical_column`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.feature_column.weighted_categorical_column(
    categorical_column, weight_feature_key, dtype=tf.dtypes.float32
)
</code></pre>



<!-- Placeholder for "Used in" -->

Use this when each of your sparse inputs has both an ID and a value. For
example, if you're representing text documents as a collection of word
frequencies, you can provide 2 parallel sparse input features ('terms' and
'frequencies' below).

#### Example:



Input `tf.Example` objects:

```proto
[
  features {
    feature {
      key: "terms"
      value {bytes_list {value: "very" value: "model"}}
    }
    feature {
      key: "frequencies"
      value {float_list {value: 0.3 value: 0.1}}
    }
  },
  features {
    feature {
      key: "terms"
      value {bytes_list {value: "when" value: "course" value: "human"}}
    }
    feature {
      key: "frequencies"
      value {float_list {value: 0.4 value: 0.1 value: 0.2}}
    }
  }
]
```

```python
categorical_column = categorical_column_with_hash_bucket(
    column_name='terms', hash_bucket_size=1000)
weighted_column = weighted_categorical_column(
    categorical_column=categorical_column, weight_feature_key='frequencies')
columns = [weighted_column, ...]
features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
linear_prediction, _, _ = linear_model(features, columns)
```

This assumes the input dictionary contains a `SparseTensor` for key
'terms', and a `SparseTensor` for key 'frequencies'. These 2 tensors must have
the same indices and dense shape.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`categorical_column`
</td>
<td>
A `CategoricalColumn` created by
`categorical_column_with_*` functions.
</td>
</tr><tr>
<td>
`weight_feature_key`
</td>
<td>
String key for weight values.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Type of weights, such as <a href="../../tf.md#float32"><code>tf.float32</code></a>. Only float and integer weights
are supported.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `CategoricalColumn` composed of two sparse features: one represents id,
the other represents weight (value) of the id feature in that example.
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
if `dtype` is not convertible to float.
</td>
</tr>
</table>

