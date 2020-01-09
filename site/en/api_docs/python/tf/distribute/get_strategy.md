page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.get_strategy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/distribute/get_strategy">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribution_strategy_context.py#L179-L196">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the current <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object.

### Aliases:

* <a href="/api_docs/python/tf/distribute/get_strategy"><code>tf.compat.v1.distribute.get_strategy</code></a>
* <a href="/api_docs/python/tf/distribute/get_strategy"><code>tf.compat.v2.distribute.get_strategy</code></a>
* <a href="/api_docs/python/tf/distribute/get_strategy"><code>tf.contrib.distribute.get_distribution_strategy</code></a>
* <a href="/api_docs/python/tf/distribute/get_strategy"><code>tf.contrib.distribute.get_strategy</code></a>


``` python
tf.distribute.get_strategy()
```



<!-- Placeholder for "Used in" -->

Typically only used in a cross-replica context:

```
if tf.distribute.in_cross_replica_context():
  strategy = tf.distribute.get_strategy()
  ...
```

#### Returns:

A <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object. Inside a `with strategy.scope()` block,
it returns `strategy`, otherwise it returns the default (single-replica)
<a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object.
