description: Enables / disables eager execution of <a href="../../tf/function.md"><code>tf.function</code></a>s.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.run_functions_eagerly" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.run_functions_eagerly

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/eager/def_function.py#L363-L411">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Enables / disables eager execution of <a href="../../tf/function.md"><code>tf.function</code></a>s.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.run_functions_eagerly`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.run_functions_eagerly(
    run_eagerly
)
</code></pre>



<!-- Placeholder for "Used in" -->

Calling <a href="../../tf/config/run_functions_eagerly.md"><code>tf.config.run_functions_eagerly(True)</code></a> will make all
invocations of <a href="../../tf/function.md"><code>tf.function</code></a> run eagerly instead of running as a traced graph
function.

This can be useful for debugging or profiling. For example, let's say you
implemented a simple iterative sqrt function, and you want to collect the
intermediate values and plot the convergence.  Appending the values to a list
in `@tf.function` normally wouldn't work since it will just record the Tensors
being traced, not the values.  Instead, you can do the following.

```
>>> ys = []
>>>
>>> @tf.function
... def sqrt(x):
...   y = x / 2
...   d = y
...   for _ in range(10):
...     d /= 2
...     if y * y < x:
...       y += d
...     else:
...       y -= d
...     ys.append(y.numpy())
...   return y
>>>
>>> tf.config.run_functions_eagerly(True)
>>> sqrt(tf.constant(2.))
<tf.Tensor: shape=(), dtype=float32, numpy=1.4150391>
>>> ys
[1.5, 1.25, 1.375, 1.4375, 1.40625, 1.421875, 1.4140625, 1.4179688, 1.4160156,
1.4150391]
>>> tf.config.run_functions_eagerly(False)
```

Calling <a href="../../tf/config/run_functions_eagerly.md"><code>tf.config.run_functions_eagerly(False)</code></a> will undo this
behavior.

Note: This flag has no effect on functions passed into tf.data transformations
as arguments. tf.data functions are never executed eagerly and are always
executed as a compiled Tensorflow Graph.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`run_eagerly`
</td>
<td>
Boolean. Whether to run functions eagerly.
</td>
</tr>
</table>

