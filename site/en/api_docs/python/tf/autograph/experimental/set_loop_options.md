description: Specifies additional arguments to be passed to the enclosing while_loop.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.autograph.experimental.set_loop_options" />
<meta itemprop="path" content="Stable" />
</div>

# tf.autograph.experimental.set_loop_options

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/autograph/lang/directives.py#L49-L98">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Specifies additional arguments to be passed to the enclosing while_loop.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.autograph.experimental.set_loop_options`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.autograph.experimental.set_loop_options(
    parallel_iterations=UNSPECIFIED, swap_memory=UNSPECIFIED,
    maximum_iterations=UNSPECIFIED, shape_invariants=UNSPECIFIED
)
</code></pre>



<!-- Placeholder for "Used in" -->

The parameters apply to and only to the immediately enclosing loop. It only
has effect if the loop is staged as a TF while_loop; otherwise the parameters
have no effect.

#### Usage:


```
>>> @tf.function(autograph=True)
... def f():
...   n = 0
...   for i in tf.range(10):
...     tf.autograph.experimental.set_loop_options(maximum_iterations=3)
...     n += 1
...   return n
```

```
>>> @tf.function(autograph=True)
... def f():
...   v = tf.constant((0,))
...   for i in tf.range(3):
...     tf.autograph.experimental.set_loop_options(
...         shape_invariants=[(v, tf.TensorShape([None]))]
...     )
...     v = tf.concat((v, [i]), 0)
...   return v
```


Also see tf.while_loop.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`parallel_iterations`
</td>
<td>
The maximum number of iterations allowed to run in
parallel at any given time. Note that this does not guarantee parallel
execution.
</td>
</tr><tr>
<td>
`swap_memory`
</td>
<td>
Whether to store intermediate values needed for
gradients on the CPU instead of GPU.
</td>
</tr><tr>
<td>
`maximum_iterations`
</td>
<td>
Allows limiting the total number of iterations executed
by the loop.
</td>
</tr><tr>
<td>
`shape_invariants`
</td>
<td>
Allows controlling the argument with the same name passed
to tf.while_loop. Unlike tf.while_loop, this is a list of
`(tensor, shape)` pairs.
</td>
</tr>
</table>

