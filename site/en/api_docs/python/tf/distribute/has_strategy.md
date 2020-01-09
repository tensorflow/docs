page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.has_strategy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/distribute/has_strategy">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribution_strategy_context.py#L199-L212">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Return if there is a current non-default <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>.

### Aliases:

* <a href="/api_docs/python/tf/distribute/has_strategy"><code>tf.compat.v1.distribute.has_strategy</code></a>
* <a href="/api_docs/python/tf/distribute/has_strategy"><code>tf.compat.v2.distribute.has_strategy</code></a>
* <a href="/api_docs/python/tf/distribute/has_strategy"><code>tf.contrib.distribute.has_distribution_strategy</code></a>
* <a href="/api_docs/python/tf/distribute/has_strategy"><code>tf.contrib.distribute.has_strategy</code></a>


``` python
tf.distribute.has_strategy()
```



<!-- Placeholder for "Used in" -->

```
assert not tf.distribute.has_strategy()
with strategy.scope():
  assert tf.distribute.has_strategy()
```

#### Returns:

True if inside a `with strategy.scope():`.
