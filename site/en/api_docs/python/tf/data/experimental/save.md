description: Saves the content of the given dataset.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.save" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.save

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/experimental/ops/io.py#L33-L104">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Saves the content of the given dataset.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.save(
    dataset, path, compression=None, shard_func=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example usage:



```
>>> import tempfile
>>> path = os.path.join(tempfile.gettempdir(), "saved_data")
>>> # Save a dataset
>>> dataset = tf.data.Dataset.range(2)
>>> tf.data.experimental.save(dataset, path)
>>> new_dataset = tf.data.experimental.load(path,
...     tf.TensorSpec(shape=(), dtype=tf.int64))
>>> for elem in new_dataset:
...   print(elem)
tf.Tensor(0, shape=(), dtype=int64)
tf.Tensor(1, shape=(), dtype=int64)
```

The saved dataset is saved in multiple file "shards". By default, the dataset
output is divided to shards in a round-robin fashion but custom sharding can
be specified via the `shard_func` function. For example, you can save the
dataset to using a single shard as follows:

```python
dataset = make_dataset()
def custom_shard_func(element):
  return 0
dataset = tf.data.experimental.save(
    path="/path/to/data", ..., shard_func=custom_shard_func)
```

NOTE: The directory layout and file format used for saving the dataset is
considered an implementation detail and may change. For this reason, datasets
saved through <a href="../../../tf/data/experimental/save.md"><code>tf.data.experimental.save</code></a> should only be consumed through
<a href="../../../tf/data/experimental/load.md"><code>tf.data.experimental.load</code></a>, which is guaranteed to be backwards compatible.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dataset`
</td>
<td>
The dataset to save.
</td>
</tr><tr>
<td>
`path`
</td>
<td>
Required. A directory to use for saving the dataset.
</td>
</tr><tr>
<td>
`compression`
</td>
<td>
Optional. The algorithm to use to compress data when writing
it. Supported options are `GZIP` and `NONE`. Defaults to `NONE`.
</td>
</tr><tr>
<td>
`shard_func`
</td>
<td>
Optional. A function to control the mapping of dataset elements
to file shards. The function is expected to map elements of the input
dataset to int64 shard IDs. If present, the function will be traced and
executed as graph computation.
</td>
</tr>
</table>

