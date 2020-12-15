description: Shuffles and repeats a Dataset, reshuffling with each repetition. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.shuffle_and_repeat" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.shuffle_and_repeat

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/experimental/ops/shuffle_ops.py#L54-L109">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Shuffles and repeats a Dataset, reshuffling with each repetition. (deprecated)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.shuffle_and_repeat`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.shuffle_and_repeat(
    buffer_size, count=None, seed=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/Dataset.md#shuffle"><code>tf.data.Dataset.shuffle(buffer_size, seed)</code></a> followed by <a href="../../../tf/data/Dataset.md#repeat"><code>tf.data.Dataset.repeat(count)</code></a>. Static tf.data optimizations will take care of using the fused implementation.

```
>>> d = tf.data.Dataset.from_tensor_slices([1, 2, 3])
>>> d = d.apply(tf.data.experimental.shuffle_and_repeat(2, count=2))
>>> [elem.numpy() for elem in d] # doctest: +SKIP
[2, 3, 1, 1, 3, 2]
```

```python
dataset.apply(
  tf.data.experimental.shuffle_and_repeat(buffer_size, count, seed))
```

produces the same output as

```python
dataset.shuffle(
  buffer_size, seed=seed, reshuffle_each_iteration=True).repeat(count)
```

In each repetition, this dataset fills a buffer with `buffer_size` elements,
then randomly samples elements from this buffer, replacing the selected
elements with new elements. For perfect shuffling, set the buffer size equal
to the full size of the dataset.

For instance, if your dataset contains 10,000 elements but `buffer_size` is
set to 1,000, then `shuffle` will initially select a random element from
only the first 1,000 elements in the buffer. Once an element is selected,
its space in the buffer is replaced by the next (i.e. 1,001-st) element,
maintaining the 1,000 element buffer.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`buffer_size`
</td>
<td>
A <a href="../../../tf.md#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, representing the maximum
number elements that will be buffered when prefetching.
</td>
</tr><tr>
<td>
`count`
</td>
<td>
(Optional.) A <a href="../../../tf.md#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, representing the number
of times the dataset should be repeated. The default behavior (if `count`
is `None` or `-1`) is for the dataset be repeated indefinitely.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
(Optional.) A <a href="../../../tf.md#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, representing the random
seed that will be used to create the distribution. See
<a href="../../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a> for behavior.
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

