page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.latency_stats


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/experimental/ops/stats_ops.py#L74-L94">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Records the latency of producing each element of the input dataset.

### Aliases:

* `tf.compat.v1.data.experimental.latency_stats`
* `tf.compat.v2.data.experimental.latency_stats`


``` python
tf.data.experimental.latency_stats(tag)
```



<!-- Placeholder for "Used in" -->

To consume the statistics, associate a `StatsAggregator` with the output
dataset.

#### Args:


* <b>`tag`</b>: String. All statistics recorded by the returned transformation will
  be associated with the given `tag`.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.
