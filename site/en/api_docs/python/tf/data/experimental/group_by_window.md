description: A transformation that groups windows of elements by key and reduces them.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.group_by_window" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.group_by_window

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/experimental/ops/grouping.py#L67-L124">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A transformation that groups windows of elements by key and reduces them.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.group_by_window`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.group_by_window(
    key_func, reduce_func, window_size=None, window_size_func=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This transformation maps each consecutive element in a dataset to a key
using `key_func` and groups the elements by key. It then applies
`reduce_func` to at most `window_size_func(key)` elements matching the same
key. All except the final window for each key will contain
`window_size_func(key)` elements; the final window may be smaller.

You may provide either a constant `window_size` or a window size determined by
the key through `window_size_func`.

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
`reduce_func`
</td>
<td>
A function mapping a key and a dataset of up to `window_size`
consecutive elements matching that key to another dataset.
</td>
</tr><tr>
<td>
`window_size`
</td>
<td>
A <a href="../../../tf.md#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, representing the number of
consecutive elements matching the same key to combine in a single
batch, which will be passed to `reduce_func`. Mutually exclusive with
`window_size_func`.
</td>
</tr><tr>
<td>
`window_size_func`
</td>
<td>
A function mapping a key to a <a href="../../../tf.md#int64"><code>tf.int64</code></a> scalar
<a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, representing the number of consecutive elements matching
the same key to combine in a single batch, which will be passed to
`reduce_func`. Mutually exclusive with `window_size`.
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



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if neither or both of {`window_size`, `window_size_func`} are
passed.
</td>
</tr>
</table>

