page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.TFRecordWriter


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/data/experimental/TFRecordWriter">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/experimental/ops/writers.py#L30-L87">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TFRecordWriter`

Writes data to a TFRecord file.



### Aliases:

* Class <a href="/api_docs/python/tf/data/experimental/TFRecordWriter"><code>tf.compat.v1.data.experimental.TFRecordWriter</code></a>
* Class <a href="/api_docs/python/tf/data/experimental/TFRecordWriter"><code>tf.compat.v2.data.experimental.TFRecordWriter</code></a>


<!-- Placeholder for "Used in" -->

To write a `dataset` to a single TFRecord file:

```python
dataset = ... # dataset to be written
writer = tf.data.experimental.TFRecordWriter(PATH)
writer.write(dataset)
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

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/experimental/ops/writers.py#L59-L66">View source</a>

``` python
__init__(
    filename,
    compression_type=None
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="write"><code>write</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/experimental/ops/writers.py#L68-L87">View source</a>

``` python
write(dataset)
```

Returns a <a href="../../../tf/Operation"><code>tf.Operation</code></a> to write a dataset to a file.


#### Args:


* <b>`dataset`</b>: a <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> whose elements are to be written to a file


#### Returns:

A <a href="../../../tf/Operation"><code>tf.Operation</code></a> that, when run, writes contents of `dataset` to a file.
