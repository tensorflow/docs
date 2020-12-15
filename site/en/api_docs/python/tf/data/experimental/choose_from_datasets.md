description: Creates a dataset that deterministically chooses elements from datasets.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.choose_from_datasets" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.choose_from_datasets

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/experimental/ops/interleave_ops.py#L236-L276">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a dataset that deterministically chooses elements from `datasets`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.choose_from_datasets(
    datasets, choice_dataset
)
</code></pre>



<!-- Placeholder for "Used in" -->

For example, given the following datasets:

```python
datasets = [tf.data.Dataset.from_tensors("foo").repeat(),
            tf.data.Dataset.from_tensors("bar").repeat(),
            tf.data.Dataset.from_tensors("baz").repeat()]

# Define a dataset containing `[0, 1, 2, 0, 1, 2, 0, 1, 2]`.
choice_dataset = tf.data.Dataset.range(3).repeat(3)

result = tf.data.experimental.choose_from_datasets(datasets, choice_dataset)
```

The elements of `result` will be:

```
"foo", "bar", "baz", "foo", "bar", "baz", "foo", "bar", "baz"
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`datasets`
</td>
<td>
A list of <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> objects with compatible structure.
</td>
</tr><tr>
<td>
`choice_dataset`
</td>
<td>
A <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> of scalar <a href="../../../tf.md#int64"><code>tf.int64</code></a> tensors between
`0` and `len(datasets) - 1`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A dataset that interleaves elements from `datasets` according to the values
of `choice_dataset`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If the `datasets` or `choice_dataset` arguments have the wrong
type.
</td>
</tr>
</table>

