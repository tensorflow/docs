description: API to persist the output of the input dataset.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.snapshot" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.snapshot

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/experimental/ops/snapshot.py#L257-L356">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



API to persist the output of the input dataset.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.snapshot`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.snapshot(
    path, compression='AUTO', reader_func=None, shard_func=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The snapshot API allows users to transparently persist the output of their
preprocessing pipeline to disk, and materialize the pre-processed data on a
different training run.

This API enables repeated preprocessing steps to be consolidated, and allows
re-use of already processed data, trading off disk storage and network
bandwidth for freeing up more valuable CPU resources and accelerator compute
time.

https://github.com/tensorflow/community/blob/master/rfcs/20200107-tf-data-snapshot.md
has detailed design documentation of this feature.

Users can specify various options to control the behavior of snapshot,
including how snapshots are read from and written to by passing in
user-defined functions to the `reader_func` and `shard_func` parameters.

`shard_func` is a user specified function that maps input elements to snapshot
shards.

Users may want to specify this function to control how snapshot files should
be written to disk. Below is an example of how a potential shard_func could
be written.

```python
dataset = ...
dataset = dataset.enumerate()
dataset = dataset.apply(tf.data.experimental.snapshot("/path/to/snapshot/dir",
    shard_func=lambda x, y: x % NUM_SHARDS, ...))
dataset = dataset.map(lambda x, y: y)
```

`reader_func` is a user specified function that accepts a single argument:
(1) a Dataset of Datasets, each representing a "split" of elements of the
original dataset. The cardinality of the input dataset matches the
number of the shards specified in the `shard_func` (see above). The function
should return a Dataset of elements of the original dataset.

Users may want specify this function to control how snapshot files should be
read from disk, including the amount of shuffling and parallelism.

Here is an example of a standard reader function a user can define. This
function enables both dataset shuffling and parallel reading of datasets:

```python
def user_reader_func(datasets):
  # shuffle the datasets splits
  datasets = datasets.shuffle(NUM_CORES)
  # read datasets in parallel and interleave their elements
  return datasets.interleave(lambda x: x, num_parallel_calls=AUTOTUNE)

dataset = dataset.apply(tf.data.experimental.snapshot("/path/to/snapshot/dir",
    reader_func=user_reader_func))
```

By default, snapshot parallelize reads by the number of cores available on
the system, but will not attempt to shuffle the data.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`path`
</td>
<td>
Required. A directory to use for storing / loading the snapshot to /
from.
</td>
</tr><tr>
<td>
`compression`
</td>
<td>
Optional. The type of compression to apply to the snapshot
written to disk. Supported options are `GZIP`, `SNAPPY`, `AUTO` or None.
Defaults to AUTO, which attempts to pick an appropriate compression
algorithm for the dataset.
</td>
</tr><tr>
<td>
`reader_func`
</td>
<td>
Optional. A function to control how to read data from snapshot
shards.
</td>
</tr><tr>
<td>
`shard_func`
</td>
<td>
Optional. A function to control how to shard data when writing a
snapshot.
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

