description: Writes a dataset to a TFRecord file.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.TFRecordWriter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="write"/>
</div>

# tf.data.experimental.TFRecordWriter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/experimental/ops/writers.py#L30-L115">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Writes a dataset to a TFRecord file.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.TFRecordWriter`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.TFRecordWriter(
    filename, compression_type=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The elements of the dataset must be scalar strings. To serialize dataset
elements as strings, you can use the <a href="../../../tf/io/serialize_tensor.md"><code>tf.io.serialize_tensor</code></a> function.

```python
dataset = tf.data.Dataset.range(3)
dataset = dataset.map(tf.io.serialize_tensor)
writer = tf.data.experimental.TFRecordWriter("/path/to/file.tfrecord")
writer.write(dataset)
```

To read back the elements, use `TFRecordDataset`.

```python
dataset = tf.data.TFRecordDataset("/path/to/file.tfrecord")
dataset = dataset.map(lambda x: tf.io.parse_tensor(x, tf.int64))
```

To shard a `dataset` across multiple TFRecord files:

```python
dataset = ... # dataset to be written

def reduce_func(key, dataset):
  filename = tf.strings.join([PATH_PREFIX, tf.strings.as_string(key)])
  writer = tf.data.experimental.TFRecordWriter(filename)
  writer.write(dataset.map(lambda _, x: x))
  return tf.data.Dataset.from_tensors(filename)

dataset = dataset.enumerate()
dataset = dataset.apply(tf.data.experimental.group_by_window(
  lambda i, _: i % NUM_SHARDS, reduce_func, tf.int64.max
))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`filename`
</td>
<td>
a string path indicating where to write the TFRecord data.
</td>
</tr><tr>
<td>
`compression_type`
</td>
<td>
(Optional.) a string indicating what type of compression
to use when writing the file. See `tf.io.TFRecordCompressionType` for
what types of compression are available. Defaults to `None`.
</td>
</tr>
</table>



## Methods

<h3 id="write"><code>write</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/experimental/ops/writers.py#L85-L115">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>write(
    dataset
)
</code></pre>

Writes a dataset to a TFRecord file.

An operation that writes the content of the specified dataset to the file
specified in the constructor.

If the file exists, it will be overwritten.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`dataset`
</td>
<td>
a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> whose elements are to be written to a file
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
In graph mode, this returns an operation which when executed performs the
write. In eager mode, the write is performed by the method itself and
there is no return value.
</td>
</tr>

</table>


Raises
  TypeError: if `dataset` is not a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.
  TypeError: if the elements produced by the dataset are not scalar strings.



