description: A transformation that groups elements and performs a reduction.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.group_by_reducer" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.group_by_reducer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/experimental/ops/grouping.py#L37-L64">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A transformation that groups elements and performs a reduction.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.group_by_reducer`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.group_by_reducer(
    key_func, reducer
)
</code></pre>



<!-- Placeholder for "Used in" -->

This transformation maps element of a dataset to a key using `key_func` and
groups the elements by key. The `reducer` is used to process each group; its
`init_func` is used to initialize state for each group when it is created, the
`reduce_func` is used to update the state every time an element is mapped to
the matching group, and the `finalize_func` is used to map the final state to
an output value.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`key_func`
</td>
<td>
A function mapping a nested structure of tensors
(having shapes and types defined by `self.output_shapes` and
`self.output_types`) to a scalar <a href="../../../tf.md#int64"><code>tf.int64</code></a> tensor.
</td>
</tr><tr>
<td>
`reducer`
</td>
<td>
An instance of `Reducer`, which captures the reduction logic using
the `init_func`, `reduce_func`, and `finalize_func` functions.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset.md#apply"><code>tf.data.Dataset.apply</code></a>.
</td>
</tr>

</table>

