page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.experimental_set_strategy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/distribution_strategy_context.py#L220-L266">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Set a <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> as current without `with strategy.scope()`.

### Aliases:

* `tf.compat.v1.distribute.experimental_set_strategy`
* `tf.compat.v2.distribute.experimental_set_strategy`


``` python
tf.distribute.experimental_set_strategy(strategy)
```



<!-- Placeholder for "Used in" -->

```
tf.distribute.experimental_set_strategy(strategy1)
f()
tf.distribute.experimental_set_strategy(strategy2)
g()
tf.distribute.experimental_set_strategy(None)
h()
```

is equivalent to:

```
with strategy1.scope():
  f()
with strategy2.scope():
  g()
h()
```

In general, you should use the `with strategy.scope():` API, but this
alternative may be convenient in notebooks where you would have to put
each cell in a `with strategy.scope():` block.

Note: This should only be called outside of any TensorFlow scope to
avoid improper nesting.

#### Args:


* <b>`strategy`</b>: A <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object or None.


#### Raises:


* <b>`RuntimeError`</b>: If called inside a `with strategy.scope():`.
