page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.DistributeOptions


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/data/experimental/DistributeOptions">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/experimental/ops/distribute_options.py#L25-L63">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `DistributeOptions`

Represents options for distributed data processing.



### Aliases:

* Class <a href="/api_docs/python/tf/data/experimental/DistributeOptions"><code>tf.compat.v1.data.experimental.DistributeOptions</code></a>
* Class <a href="/api_docs/python/tf/data/experimental/DistributeOptions"><code>tf.compat.v2.data.experimental.DistributeOptions</code></a>


<!-- Placeholder for "Used in" -->

You can set the distribution options of a dataset through the
`experimental_distribute` property of <a href="../../../tf/data/Options"><code>tf.data.Options</code></a>; the property is
an instance of <a href="../../../tf/data/experimental/DistributeOptions"><code>tf.data.experimental.DistributeOptions</code></a>.

```python
options = tf.data.Options()
options.experimental_distribute.auto_shard = False
dataset = dataset.with_options(options)
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/util/options.py#L33-L35">View source</a>

``` python
__init__()
```

Initialize self.  See help(type(self)) for accurate signature.




## Properties

<h3 id="auto_shard"><code>auto_shard</code></h3>

Whether the dataset should be automatically sharded when processedin a distributed fashion. This is applicable when using Keras with multi-worker/TPU distribution strategy, and by using strategy.experimental_distribute_dataset(). In other cases, this option does nothing. If None, defaults to True.


<h3 id="num_devices"><code>num_devices</code></h3>

The number of devices attached to this input pipeline. This will be automatically set by MultiDeviceIterator.




## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/util/options.py#L37-L43">View source</a>

``` python
__eq__(other)
```

Return self==value.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/util/options.py#L45-L49">View source</a>

``` python
__ne__(other)
```

Return self!=value.
