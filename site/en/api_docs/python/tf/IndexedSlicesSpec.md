description: Type specification for a <a href="../tf/IndexedSlices.md"><code>tf.IndexedSlices</code></a>.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.IndexedSlicesSpec" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__ne__"/>
<meta itemprop="property" content="is_compatible_with"/>
<meta itemprop="property" content="most_specific_compatible_type"/>
</div>

# tf.IndexedSlicesSpec

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/indexed_slices.py#L193-L256">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Type specification for a <a href="../tf/IndexedSlices.md"><code>tf.IndexedSlices</code></a>.

Inherits From: [`TypeSpec`](../tf/TypeSpec.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.IndexedSlicesSpec`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.IndexedSlicesSpec(
    shape=None, dtype=tf.dtypes.float32, indices_dtype=tf.dtypes.int64,
    dense_shape_dtype=None, indices_shape=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
The dense shape of the `IndexedSlices`, or `None` to allow any
dense shape.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
<a href="../tf/dtypes/DType.md"><code>tf.DType</code></a> of values in the `IndexedSlices`.
</td>
</tr><tr>
<td>
`indices_dtype`
</td>
<td>
<a href="../tf/dtypes/DType.md"><code>tf.DType</code></a> of the `indices` in the `IndexedSlices`.  One
of <a href="../tf.md#int32"><code>tf.int32</code></a> or <a href="../tf.md#int64"><code>tf.int64</code></a>.
</td>
</tr><tr>
<td>
`dense_shape_dtype`
</td>
<td>
<a href="../tf/dtypes/DType.md"><code>tf.DType</code></a> of the `dense_shape` in the `IndexedSlices`.
One of <a href="../tf.md#int32"><code>tf.int32</code></a>, <a href="../tf.md#int64"><code>tf.int64</code></a>, or `None` (if the `IndexedSlices` has
no `dense_shape` tensor).
</td>
</tr><tr>
<td>
`indices_shape`
</td>
<td>
The shape of the `indices` component, which indicates
how many slices are in the `IndexedSlices`.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`value_type`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="is_compatible_with"><code>is_compatible_with</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/type_spec.py#L93-L108">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_compatible_with(
    spec_or_value
)
</code></pre>

Returns true if `spec_or_value` is compatible with this TypeSpec.


<h3 id="most_specific_compatible_type"><code>most_specific_compatible_type</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/type_spec.py#L110-L132">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>most_specific_compatible_type(
    other
)
</code></pre>

Returns the most specific TypeSpec compatible with `self` and `other`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`other`
</td>
<td>
A `TypeSpec`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If there is no TypeSpec that is compatible with both `self`
and `other`.
</td>
</tr>
</table>



<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/type_spec.py#L293-L296">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Return self==value.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/type_spec.py#L298-L299">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ne__(
    other
)
</code></pre>

Return self!=value.




