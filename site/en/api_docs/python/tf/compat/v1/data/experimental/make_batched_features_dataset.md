description: Returns a Dataset of feature dictionaries from Example protos.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.data.experimental.make_batched_features_dataset" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.data.experimental.make_batched_features_dataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/experimental/ops/readers.py#L932-L952">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a `Dataset` of feature dictionaries from `Example` protos.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.data.experimental.make_batched_features_dataset(
    file_pattern, batch_size, features, reader=None, label_key=None,
    reader_args=None, num_epochs=None, shuffle=(True), shuffle_buffer_size=10000,
    shuffle_seed=None, prefetch_buffer_size=None, reader_num_threads=None,
    parser_num_threads=None, sloppy_ordering=(False), drop_final_batch=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

If label_key argument is provided, returns a `Dataset` of tuple
comprising of feature dictionaries and label.

#### Example:



```
serialized_examples = [
  features {
    feature { key: "age" value { int64_list { value: [ 0 ] } } }
    feature { key: "gender" value { bytes_list { value: [ "f" ] } } }
    feature { key: "kws" value { bytes_list { value: [ "code", "art" ] } } }
  },
  features {
    feature { key: "age" value { int64_list { value: [] } } }
    feature { key: "gender" value { bytes_list { value: [ "f" ] } } }
    feature { key: "kws" value { bytes_list { value: [ "sports" ] } } }
  }
]
```

#### We can use arguments:



```
features: {
  "age": FixedLenFeature([], dtype=tf.int64, default_value=-1),
  "gender": FixedLenFeature([], dtype=tf.string),
  "kws": VarLenFeature(dtype=tf.string),
}
```

And the expected output is:

```python
{
  "age": [[0], [-1]],
  "gender": [["f"], ["f"]],
  "kws": SparseTensor(
    indices=[[0, 0], [0, 1], [1, 0]],
    values=["code", "art", "sports"]
    dense_shape=[2, 2]),
}
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`file_pattern`
</td>
<td>
List of files or patterns of file paths containing
`Example` records. See <a href="../../../../../tf/io/gfile/glob.md"><code>tf.io.gfile.glob</code></a> for pattern rules.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
An int representing the number of records to combine
in a single batch.
</td>
</tr><tr>
<td>
`features`
</td>
<td>
A `dict` mapping feature keys to `FixedLenFeature` or
`VarLenFeature` values. See <a href="../../../../../tf/io/parse_example.md"><code>tf.io.parse_example</code></a>.
</td>
</tr><tr>
<td>
`reader`
</td>
<td>
A function or class that can be
called with a `filenames` tensor and (optional) `reader_args` and returns
a `Dataset` of `Example` tensors. Defaults to <a href="../../../../../tf/data/TFRecordDataset.md"><code>tf.data.TFRecordDataset</code></a>.
</td>
</tr><tr>
<td>
`label_key`
</td>
<td>
(Optional) A string corresponding to the key labels are stored in
`tf.Examples`. If provided, it must be one of the `features` key,
otherwise results in `ValueError`.
</td>
</tr><tr>
<td>
`reader_args`
</td>
<td>
Additional arguments to pass to the reader class.
</td>
</tr><tr>
<td>
`num_epochs`
</td>
<td>
Integer specifying the number of times to read through the
dataset. If None, cycles through the dataset forever. Defaults to `None`.
</td>
</tr><tr>
<td>
`shuffle`
</td>
<td>
A boolean, indicates whether the input should be shuffled. Defaults
to `True`.
</td>
</tr><tr>
<td>
`shuffle_buffer_size`
</td>
<td>
Buffer size of the ShuffleDataset. A large capacity
ensures better shuffling but would increase memory usage and startup time.
</td>
</tr><tr>
<td>
`shuffle_seed`
</td>
<td>
Randomization seed to use for shuffling.
</td>
</tr><tr>
<td>
`prefetch_buffer_size`
</td>
<td>
Number of feature batches to prefetch in order to
improve performance. Recommended value is the number of batches consumed
per training step. Defaults to auto-tune.
</td>
</tr><tr>
<td>
`reader_num_threads`
</td>
<td>
Number of threads used to read `Example` records. If >1,
the results will be interleaved. Defaults to `1`.
</td>
</tr><tr>
<td>
`parser_num_threads`
</td>
<td>
Number of threads to use for parsing `Example` tensors
into a dictionary of `Feature` tensors. Defaults to `2`.
</td>
</tr><tr>
<td>
`sloppy_ordering`
</td>
<td>
If `True`, reading performance will be improved at
the cost of non-deterministic ordering. If `False`, the order of elements
produced is deterministic prior to shuffling (elements are still
randomized if `shuffle=True`. Note that if the seed is set, then order
of elements after shuffling is deterministic). Defaults to `False`.
</td>
</tr><tr>
<td>
`drop_final_batch`
</td>
<td>
If `True`, and the batch size does not evenly divide the
input dataset size, the final smaller batch will be dropped. Defaults to
`False`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A dataset of `dict` elements, (or a tuple of `dict` elements and label).
Each `dict` maps feature keys to `Tensor` or `SparseTensor` objects.
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
If `reader` is of the wrong type.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `label_key` is not one of the `features` keys.
</td>
</tr>
</table>

