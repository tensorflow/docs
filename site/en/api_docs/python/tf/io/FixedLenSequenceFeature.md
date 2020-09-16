description: Configuration for parsing a variable-length input feature into a Tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.FixedLenSequenceFeature" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="allow_missing"/>
<meta itemprop="property" content="default_value"/>
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="shape"/>
</div>

# tf.io.FixedLenSequenceFeature

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/parsing_config.py#L329-L359">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Configuration for parsing a variable-length input feature into a `Tensor`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.FixedLenSequenceFeature`, `tf.compat.v1.io.FixedLenSequenceFeature`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.FixedLenSequenceFeature(
    shape, dtype, allow_missing=(False), default_value=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The resulting `Tensor` of parsing a single `SequenceExample` or `Example` has
a static `shape` of `[None] + shape` and the specified `dtype`.
The resulting `Tensor` of parsing a `batch_size` many `Example`s has
a static `shape` of `[batch_size, None] + shape` and the specified `dtype`.
The entries in the `batch` from different `Examples` will be padded with
`default_value` to the maximum length present in the `batch`.

To treat a sparse input as dense, provide `allow_missing=True`; otherwise,
the parse functions will fail on any examples missing this feature.

#### Fields:


* <b>`shape`</b>: Shape of input data for dimension 2 and higher. First dimension is
  of variable length `None`.
* <b>`dtype`</b>: Data type of input.
* <b>`allow_missing`</b>: Whether to allow this feature to be missing from a feature
  list item. Is available only for parsing `SequenceExample` not for
  parsing `Examples`.
* <b>`default_value`</b>: Scalar value to be used to pad multiple `Example`s to their
  maximum length. Irrelevant for parsing a single `Example` or
  `SequenceExample`. Defaults to "" for dtype string and 0 otherwise
  (optional).




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`shape`
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
`allow_missing`
</td>
<td>

</td>
</tr><tr>
<td>
`default_value`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `allow_missing` <a id="allow_missing"></a>
* `default_value` <a id="default_value"></a>
* `dtype` <a id="dtype"></a>
* `shape` <a id="shape"></a>
