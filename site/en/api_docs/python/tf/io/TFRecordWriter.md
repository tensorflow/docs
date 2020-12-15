description: A class to write records to a TFRecords file.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.TFRecordWriter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__enter__"/>
<meta itemprop="property" content="__exit__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="close"/>
<meta itemprop="property" content="flush"/>
<meta itemprop="property" content="write"/>
</div>

# tf.io.TFRecordWriter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/lib/io/tf_record.py#L218-L321">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A class to write records to a TFRecords file.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.io.TFRecordWriter`, `tf.compat.v1.python_io.TFRecordWriter`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.TFRecordWriter(
    path, options=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

[TFRecords tutorial](https://www.tensorflow.org/tutorials/load_data/tfrecord)

TFRecords is a binary format which is optimized for high throughput data
retrieval, generally in conjunction with <a href="../../tf/data.md"><code>tf.data</code></a>. `TFRecordWriter` is used
to write serialized examples to a file for later consumption. The key steps
are:

 Ahead of time:

 - [Convert data into a serialized format](
 https://www.tensorflow.org/tutorials/load_data/tfrecord#tfexample)
 - [Write the serialized data to one or more files](
 https://www.tensorflow.org/tutorials/load_data/tfrecord#tfrecord_files_in_python)

 During training or evaluation:

 - [Read serialized examples into memory](
 https://www.tensorflow.org/tutorials/load_data/tfrecord#reading_a_tfrecord_file)
 - [Parse (deserialize) examples](
 https://www.tensorflow.org/tutorials/load_data/tfrecord#reading_a_tfrecord_file)

A minimal example is given below:

```
>>> import tempfile
>>> example_path = os.path.join(tempfile.gettempdir(), "example.tfrecords")
>>> np.random.seed(0)
```

```
>>> # Write the records to a file.
... with tf.io.TFRecordWriter(example_path) as file_writer:
...   for _ in range(4):
...     x, y = np.random.random(), np.random.random()
...
...     record_bytes = tf.train.Example(features=tf.train.Features(feature={
...         "x": tf.train.Feature(float_list=tf.train.FloatList(value=[x])),
...         "y": tf.train.Feature(float_list=tf.train.FloatList(value=[y])),
...     })).SerializeToString()
...     file_writer.write(record_bytes)
```

```
>>> # Read the data back out.
>>> def decode_fn(record_bytes):
...   return tf.io.parse_single_example(
...       # Data
...       record_bytes,
...
...       # Schema
...       {"x": tf.io.FixedLenFeature([], dtype=tf.float32),
...        "y": tf.io.FixedLenFeature([], dtype=tf.float32)}
...   )
```

```
>>> for batch in tf.data.TFRecordDataset([example_path]).map(decode_fn):
...   print("x = {x:.4f},  y = {y:.4f}".format(**batch))
x = 0.5488,  y = 0.7152
x = 0.6028,  y = 0.5449
x = 0.4237,  y = 0.6459
x = 0.4376,  y = 0.8918
```

This class implements `__enter__` and `__exit__`, and can be used
in `with` blocks like a normal file. (See the usage example above.)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`path`
</td>
<td>
The path to the TFRecords file.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
(optional) String specifying compression type,
`TFRecordCompressionType`, or `TFRecordOptions` object.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`IOError`
</td>
<td>
If `path` cannot be opened for writing.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If valid compression_type can't be determined from `options`.
</td>
</tr>
</table>



## Methods

<h3 id="close"><code>close</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/lib/io/tf_record.py#L319-L321">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>close()
</code></pre>

Close the file.


<h3 id="flush"><code>flush</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/lib/io/tf_record.py#L315-L317">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>flush()
</code></pre>

Flush the file.


<h3 id="write"><code>write</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/lib/io/tf_record.py#L307-L313">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>write(
    record
)
</code></pre>

Write a string record to the file.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`record`
</td>
<td>
str
</td>
</tr>
</table>



<h3 id="__enter__"><code>__enter__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__enter__()
</code></pre>

__enter__(self: object) -> object


<h3 id="__exit__"><code>__exit__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__exit__()
</code></pre>

__exit__(self: tensorflow.python._pywrap_record_io.RecordWriter, *args) -> None




