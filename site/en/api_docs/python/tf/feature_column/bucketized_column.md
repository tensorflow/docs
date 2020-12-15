description: Represents discretized dense input bucketed by boundaries.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.feature_column.bucketized_column" />
<meta itemprop="path" content="Stable" />
</div>

# tf.feature_column.bucketized_column

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/feature_column/feature_column_v2.py#L1040-L1123">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents discretized dense input bucketed by `boundaries`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.feature_column.bucketized_column`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.feature_column.bucketized_column(
    source_column, boundaries
)
</code></pre>



<!-- Placeholder for "Used in" -->

Buckets include the left boundary, and exclude the right boundary. Namely,
`boundaries=[0., 1., 2.]` generates buckets `(-inf, 0.)`, `[0., 1.)`,
`[1., 2.)`, and `[2., +inf)`.

For example, if the inputs are

```python
boundaries = [0, 10, 100]
input tensor = [[-5, 10000]
                [150,   10]
                [5,    100]]
```

then the output will be

```python
output = [[0, 3]
          [3, 2]
          [1, 3]]
```

#### Example:



```python
price = tf.feature_column.numeric_column('price')
bucketized_price = tf.feature_column.bucketized_column(
    price, boundaries=[...])
columns = [bucketized_price, ...]
features = tf.io.parse_example(
    ..., features=tf.feature_column.make_parse_example_spec(columns))
dense_tensor = tf.keras.layers.DenseFeatures(columns)(features)
```

A `bucketized_column` can also be crossed with another categorical column
using `crossed_column`:

```python
price = tf.feature_column.numeric_column('price')
# bucketized_column converts numerical feature to a categorical one.
bucketized_price = tf.feature_column.bucketized_column(
    price, boundaries=[...])
# 'keywords' is a string feature.
price_x_keywords = tf.feature_column.crossed_column(
    [bucketized_price, 'keywords'], 50K)
columns = [price_x_keywords, ...]
features = tf.io.parse_example(
    ..., features=tf.feature_column.make_parse_example_spec(columns))
dense_tensor = tf.keras.layers.DenseFeatures(columns)(features)
linear_model = tf.keras.experimental.LinearModel(units=...)(dense_tensor)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`source_column`
</td>
<td>
A one-dimensional dense column which is generated with
`numeric_column`.
</td>
</tr><tr>
<td>
`boundaries`
</td>
<td>
A sorted list or tuple of floats specifying the boundaries.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `BucketizedColumn`.
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
If `source_column` is not a numeric column, or if it is not
one-dimensional.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `boundaries` is not a sorted list or tuple.
</td>
</tr>
</table>

