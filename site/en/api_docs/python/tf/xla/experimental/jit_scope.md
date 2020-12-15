description: Enable or disable JIT compilation of operators within the scope.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.xla.experimental.jit_scope" />
<meta itemprop="path" content="Stable" />
</div>

# tf.xla.experimental.jit_scope

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/compiler/xla/jit.py#L40-L160">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Enable or disable JIT compilation of operators within the scope.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.xla.experimental.jit_scope`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@contextlib.contextmanager</code>
<code>tf.xla.experimental.jit_scope(
    compile_ops=(True), separate_compiled_gradients=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

NOTE: This is an experimental feature.

The compilation is a hint and only supported on a best-effort basis.

#### Example usage:


```python
with tf.xla.experimental.jit_scope():
  c = tf.matmul(a, b)  # compiled
with tf.xla.experimental.jit_scope(compile_ops=False):
  d = tf.matmul(a, c)  # not compiled
with tf.xla.experimental.jit_scope(
    compile_ops=lambda node_def: 'matmul' in node_def.op.lower()):
  e = tf.matmul(a, b) + d  # matmul is compiled, the addition is not.
```


Example of `separate_compiled_gradients`:

  ```python
  # In the example below, the computations for f, g and h will all be compiled
  # in separate scopes.
  with tf.xla.experimental.jit_scope(
      separate_compiled_gradients=True):
    f = tf.matmul(a, b)
  g = tf.gradients([f], [a, b], name='mygrads1')
  h = tf.gradients([f], [a, b], name='mygrads2')
  ```

Ops that are not in the scope may be clustered and compiled with ops in
the scope with `compile_ops=True`, while the ops in the scope with
`compile_ops=False` will never be compiled.

#### For example:


```python
# In the example below, x and loss may be clustered and compiled together,
# while y will not be compiled.
with tf.xla.experimental.jit_scope():
  x = tf.matmul(a, b)
with tf.xla.experimental.jit_scope(compile_ops=False):
  y = tf.matmul(c, d)
loss = x + y
```


If you want to only compile the ops in the scope with `compile_ops=True`,
consider adding an outer `jit_scope(compile_ops=False)`:

  ```python
  # In the example below, only x will be compiled.
  with tf.xla.experimental.jit_scope(compile_ops=False):
    with tf.xla.experimental.jit_scope():
      x = tf.matmul(a, b)
    y = tf.matmul(c, d)
    loss = x + y
  ```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`compile_ops`
</td>
<td>
Whether to enable or disable compilation in the scope.
Either a Python bool, or a callable that accepts the parameter
`node_def` and returns a python bool.
</td>
</tr><tr>
<td>
`separate_compiled_gradients`
</td>
<td>
If true put each gradient subgraph into a
separate compilation scope. This gives fine-grained control over which
portions of the graph will be compiled as a single unit. Compiling
gradients separately may yield better performance for some graphs.
The scope is named based on the scope of the forward computation as well
as the name of the gradients. As a result, the gradients will be compiled
in a scope that is separate from both the forward computation, and from
other gradients.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
if called when eager execution is enabled.
</td>
</tr>
</table>



#### Yields:

The current scope, enabling or disabling compilation.
