page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.get_cross_replica_context


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribution_strategy_context.py#L138-L151">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the current tf.distribute.Strategy if in a cross-replica context.

``` python
tf.contrib.distribute.get_cross_replica_context()
```



<!-- Placeholder for "Used in" -->

DEPRECATED: Please use `in_cross_replica_context()` and
`get_strategy()` instead.

#### Returns:

Returns the current <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object in a cross-replica
context, or `None`.

Exactly one of `get_replica_context()` and `get_cross_replica_context()`
will return `None` in a particular block.
