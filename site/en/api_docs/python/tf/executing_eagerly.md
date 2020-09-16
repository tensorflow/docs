description: Checks whether the current thread has eager execution enabled.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.executing_eagerly" />
<meta itemprop="path" content="Stable" />
</div>

# tf.executing_eagerly

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/eager/context.py#L1734-L1793">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Checks whether the current thread has eager execution enabled.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.executing_eagerly()
</code></pre>



<!-- Placeholder for "Used in" -->

Eager execution is enabled by default and this API returns `True`
in most of cases. However, this API might return `False` in the following use
cases.

*  Executing inside <a href="../tf/function.md"><code>tf.function</code></a>, unless under <a href="../tf/init_scope.md"><code>tf.init_scope</code></a> or
   <a href="../tf/config/experimental_run_functions_eagerly.md"><code>tf.config.experimental_run_functions_eagerly(True)</code></a> is previously called.
*  Executing inside a transformation function for `tf.dataset`.
*  <a href="../tf/compat/v1/disable_eager_execution.md"><code>tf.compat.v1.disable_eager_execution()</code></a> is called.

#### General case:



```
>>> print(tf.executing_eagerly())
True
```

Inside <a href="../tf/function.md"><code>tf.function</code></a>:

```
>>> @tf.function
... def fn():
...   with tf.init_scope():
...     print(tf.executing_eagerly())
...   print(tf.executing_eagerly())
>>> fn()
True
False
```

Inside <a href="../tf/function.md"><code>tf.function</code></a> after

<a href="../tf/config/experimental_run_functions_eagerly.md"><code>tf.config.experimental_run_functions_eagerly(True)</code></a> is called:
>>> tf.config.experimental_run_functions_eagerly(True)
>>> @tf.function
... def fn():
...   with tf.init_scope():
...     print(tf.executing_eagerly())
...   print(tf.executing_eagerly())
>>> fn()
True
True
>>> tf.config.experimental_run_functions_eagerly(False)

Inside a transformation function for `tf.dataset`:

```
>>> def data_fn(x):
...   print(tf.executing_eagerly())
...   return x
>>> dataset = tf.data.Dataset.range(100)
>>> dataset = dataset.map(data_fn)
False
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
`True` if the current thread has eager execution enabled.
</td>
</tr>

</table>

