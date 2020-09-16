description: Configuration for parsing a sparse input feature from an Example.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.SparseFeature" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="already_sorted"/>
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="index_key"/>
<meta itemprop="property" content="size"/>
<meta itemprop="property" content="value_key"/>
</div>

# tf.io.SparseFeature

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/parsing_config.py#L233-L304">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Configuration for parsing a sparse input feature from an `Example`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.SparseFeature`, `tf.compat.v1.io.SparseFeature`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.SparseFeature(
    index_key, value_key, dtype, size, already_sorted=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note, preferably use `VarLenFeature` (possibly in combination with a
`SequenceExample`) in order to parse out `SparseTensor`s instead of
`SparseFeature` due to its simplicity.

Closely mimicking the `SparseTensor` that will be obtained by parsing an
`Example` with a `SparseFeature` config, a `SparseFeature` contains a

* `value_key`: The name of key for a `Feature` in the `Example` whose parsed
  `Tensor` will be the resulting <a href="../../tf/sparse/SparseTensor.md#values"><code>SparseTensor.values</code></a>.

* `index_key`: A list of names - one for each dimension in the resulting
  `SparseTensor` whose `indices[i][dim]` indicating the position of
  the `i`-th value in the `dim` dimension will be equal to the `i`-th value in
  the Feature with key named `index_key[dim]` in the `Example`.

* `size`: A list of ints for the resulting <a href="../../tf/sparse/SparseTensor.md#dense_shape"><code>SparseTensor.dense_shape</code></a>.

For example, we can represent the following 2D `SparseTensor`

```python
SparseTensor(indices=[[3, 1], [20, 0]],
             values=[0.5, -1.0]
             dense_shape=[100, 3])
```

with an `Example` input proto

```python
features {
  feature { key: "val" value { float_list { value: [ 0.5, -1.0 ] } } }
  feature { key: "ix0" value { int64_list { value: [ 3, 20 ] } } }
  feature { key: "ix1" value { int64_list { value: [ 1, 0 ] } } }
}
```

and `SparseFeature` config with 2 `index_key`s

```python
SparseFeature(index_key=["ix0", "ix1"],
              value_key="val",
              dtype=tf.float32,
              size=[100, 3])
```

#### Fields:


* <b>`index_key`</b>: A single string name or a list of string names of index features.
  For each key the underlying feature's type must be `int64` and its length
  must always match that of the `value_key` feature.
  To represent `SparseTensor`s with a `dense_shape` of `rank` higher than 1
  a list of length `rank` should be used.
* <b>`value_key`</b>: Name of value feature.  The underlying feature's type must
  be `dtype` and its length must always match that of all the `index_key`s'
  features.
* <b>`dtype`</b>: Data type of the `value_key` feature.
* <b>`size`</b>: A Python int or list thereof specifying the dense shape. Should be a
  list if and only if `index_key` is a list. In that case the list must be
  equal to the length of `index_key`. Each for each entry `i` all values in
  the `index_key`[i] feature must be in `[0, size[i])`.
* <b>`already_sorted`</b>: A Python boolean to specify whether the values in
  `value_key` are already sorted by their index position. If so skip
  sorting. False by default (optional).




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`index_key`
</td>
<td>

</td>
</tr><tr>
<td>
`value_key`
</td>
<td>

</td>
</tr><tr>
<td>
`dtype`
</td>
<td>

</td>
</tr><tr>
<td>
`size`
</td>
<td>

</td>
</tr><tr>
<td>
`already_sorted`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `already_sorted` <a id="already_sorted"></a>
* `dtype` <a id="dtype"></a>
* `index_key` <a id="index_key"></a>
* `size` <a id="size"></a>
* `value_key` <a id="value_key"></a>
