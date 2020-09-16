description: Makes a "one-shot" iterator that can be iterated only once.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.OneShotIterator" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.OneShotIterator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Makes a "one-shot" iterator that can be iterated only once.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.OneShotIterator`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.OneShotIterator(
    dataset_factory, output_types, output_shapes, container='', shared_name='',
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

A one-shot iterator bundles the logic for defining the dataset and
the state of the iterator in a single op, which allows simple input
pipelines to be defined without an additional initialization
("MakeIterator") step.

One-shot iterators have the following limitations:

* They do not support parameterization: all logic for creating the underlying
  dataset must be bundled in the `dataset_factory` function.
* They are not resettable. Once a one-shot iterator reaches the end of its
  underlying dataset, subsequent "IteratorGetNext" operations on that
  iterator will always produce an `OutOfRange` error.

For greater flexibility, use "Iterator" and "MakeIterator" to define
an iterator using an arbitrary subgraph, which may capture tensors
(including fed values) as parameters, and which may be reset multiple
times by rerunning "MakeIterator".

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dataset_factory`
</td>
<td>
A function decorated with @Defun.
A function of type `() -> DT_VARIANT`, where the returned
DT_VARIANT is a dataset.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
</td>
</tr><tr>
<td>
`container`
</td>
<td>
An optional `string`. Defaults to `""`.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
An optional `string`. Defaults to `""`.
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
A `Tensor` of type `resource`.
</td>
</tr>

</table>

