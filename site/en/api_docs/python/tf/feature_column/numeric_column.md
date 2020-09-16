description: Represents real valued or numerical features.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.feature_column.numeric_column" />
<meta itemprop="path" content="Stable" />
</div>

# tf.feature_column.numeric_column

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/feature_column/feature_column_v2.py#L1319-L1393">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents real valued or numerical features.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.feature_column.numeric_column`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.feature_column.numeric_column(
    key, shape=(1,), default_value=None, dtype=tf.dtypes.float32, normalizer_fn=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example:



```python
price = numeric_column('price')
columns = [price, ...]
features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
dense_tensor = input_layer(features, columns)

# or
bucketized_price = bucketized_column(price, boundaries=[...])
columns = [bucketized_price, ...]
features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
linear_prediction = linear_model(features, columns)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`key`
</td>
<td>
A unique string identifying the input feature. It is used as the
column name and the dictionary key for feature parsing configs, feature
`Tensor` objects, and feature columns.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
An iterable of integers specifies the shape of the `Tensor`. An
integer can be given which means a single dimension `Tensor` with given
width. The `Tensor` representing the column will have the shape of
[batch_size] + `shape`.
</td>
</tr><tr>
<td>
`default_value`
</td>
<td>
A single value compatible with `dtype` or an iterable of
values compatible with `dtype` which the column takes on during
`tf.Example` parsing if data is missing. A default value of `None` will
cause <a href="../../tf/io/parse_example.md"><code>tf.io.parse_example</code></a> to fail if an example does not contain this
column. If a single value is provided, the same value will be applied as
the default value for every item. If an iterable of values is provided,
the shape of the `default_value` should be equal to the given `shape`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
defines the type of values. Default value is <a href="../../tf.md#float32"><code>tf.float32</code></a>. Must be a
non-quantized, real integer or floating point type.
</td>
</tr><tr>
<td>
`normalizer_fn`
</td>
<td>
If not `None`, a function that can be used to normalize the
value of the tensor after `default_value` is applied for parsing.
Normalizer function takes the input `Tensor` as its argument, and returns
the output `Tensor`. (e.g. lambda x: (x - 3.0) / 4.2). Please note that
even though the most common use case of this function is normalization, it
can be used for any kind of Tensorflow transformations.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `NumericColumn`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
if any dimension in shape is not an int
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if any dimension in shape is not a positive integer
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
if `default_value` is an iterable but not compatible with `shape`
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
if `default_value` is not compatible with `dtype`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `dtype` is not convertible to <a href="../../tf.md#float32"><code>tf.float32</code></a>.
</td>
</tr>
</table>

