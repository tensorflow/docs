description: A sparse representation of a set of tensor slices at given indices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.IndexedSlices" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__neg__"/>
<meta itemprop="property" content="consumers"/>
</div>

# tf.IndexedSlices

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/indexed_slices.py#L60-L184">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A sparse representation of a set of tensor slices at given indices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.IndexedSlices`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.IndexedSlices(
    values, indices, dense_shape=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This class is a simple wrapper for a pair of `Tensor` objects:

* `values`: A `Tensor` of any dtype with shape `[D0, D1, ..., Dn]`.
* `indices`: A 1-D integer `Tensor` with shape `[D0]`.

An `IndexedSlices` is typically used to represent a subset of a larger
tensor `dense` of shape `[LARGE0, D1, .. , DN]` where `LARGE0 >> D0`.
The values in `indices` are the indices in the first dimension of
the slices that have been extracted from the larger tensor.

The dense tensor `dense` represented by an `IndexedSlices` `slices` has

```python
dense[slices.indices[i], :, :, :, ...] = slices.values[i, :, :, :, ...]
```

The `IndexedSlices` class is used principally in the definition of
gradients for operations that have sparse gradients
(e.g. <a href="../tf/gather.md"><code>tf.gather</code></a>).

Contrast this representation with
<a href="../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a>,
which uses multi-dimensional indices and scalar values.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`dense_shape`
</td>
<td>
A 1-D `Tensor` containing the shape of the corresponding dense tensor.
</td>
</tr><tr>
<td>
`device`
</td>
<td>
The name of the device on which `values` will be produced, or `None`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The `DType` of elements in this tensor.
</td>
</tr><tr>
<td>
`graph`
</td>
<td>
The `Graph` that contains the values, indices, and shape tensors.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
A 1-D `Tensor` containing the indices of the slices.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The name of this `IndexedSlices`.
</td>
</tr><tr>
<td>
`op`
</td>
<td>
The `Operation` that produces `values` as an output.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
Gets the <a href="../tf/TensorShape.md"><code>tf.TensorShape</code></a> representing the shape of the dense tensor.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A `Tensor` containing the values of the slices.
</td>
</tr>
</table>



## Methods

<h3 id="consumers"><code>consumers</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/indexed_slices.py#L183-L184">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>consumers()
</code></pre>




<h3 id="__neg__"><code>__neg__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/indexed_slices.py#L152-L153">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__neg__()
</code></pre>






