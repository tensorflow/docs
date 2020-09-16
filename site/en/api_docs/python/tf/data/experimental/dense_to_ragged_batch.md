description: A transformation that batches ragged elements into <a href="../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>s.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.dense_to_ragged_batch" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.dense_to_ragged_batch

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/experimental/ops/batching.py#L35-L86">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A transformation that batches ragged elements into <a href="../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>s.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.dense_to_ragged_batch`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.dense_to_ragged_batch(
    batch_size, drop_remainder=(False), row_splits_dtype=tf.dtypes.int64
)
</code></pre>



<!-- Placeholder for "Used in" -->

This transformation combines multiple consecutive elements of the input
dataset into a single element.

Like <a href="../../../tf/data/Dataset.md#batch"><code>tf.data.Dataset.batch</code></a>, the components of the resulting element will
have an additional outer dimension, which will be `batch_size` (or
`N % batch_size` for the last element if `batch_size` does not divide the
number of input elements `N` evenly and `drop_remainder` is `False`). If
your program depends on the batches having the same outer dimension, you
should set the `drop_remainder` argument to `True` to prevent the smaller
batch from being produced.

Unlike <a href="../../../tf/data/Dataset.md#batch"><code>tf.data.Dataset.batch</code></a>, the input elements to be batched may have
different shapes, and each batch will be encoded as a <a href="../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>.
Example:

```
>>> dataset = tf.data.Dataset.from_tensor_slices(np.arange(6))
>>> dataset = dataset.map(lambda x: tf.range(x))
>>> dataset = dataset.apply(
...     tf.data.experimental.dense_to_ragged_batch(batch_size=2))
>>> for batch in dataset:
...   print(batch)
<tf.RaggedTensor [[], [0]]>
<tf.RaggedTensor [[0, 1], [0, 1, 2]]>
<tf.RaggedTensor [[0, 1, 2, 3], [0, 1, 2, 3, 4]]>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`batch_size`
</td>
<td>
A <a href="../../../tf.md#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, representing the number of
consecutive elements of this dataset to combine in a single batch.
</td>
</tr><tr>
<td>
`drop_remainder`
</td>
<td>
(Optional.) A <a href="../../../tf.md#bool"><code>tf.bool</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, representing
whether the last batch should be dropped in the case it has fewer than
`batch_size` elements; the default behavior is not to drop the smaller
batch.
</td>
</tr><tr>
<td>
`row_splits_dtype`
</td>
<td>
The dtype that should be used for the `row_splits` of any
new ragged tensors.  Existing <a href="../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a> elements do not have their
row_splits dtype changed.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`Dataset`
</td>
<td>
A `Dataset`.
</td>
</tr>
</table>

