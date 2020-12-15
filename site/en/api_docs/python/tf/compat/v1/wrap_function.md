description: Wraps the TF 1.x function fn into a graph function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.wrap_function" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.wrap_function

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/eager/wrap_function.py#L559-L630">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Wraps the TF 1.x function fn into a graph function.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.wrap_function(
    fn, signature, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The python function `fn` will be called once with symbolic arguments specified
in the `signature`, traced, and turned into a graph function. Any variables
created by `fn` will be owned by the object returned by `wrap_function`. The
resulting graph function can be called with tensors which match the
signature.

```python
def f(x, do_add):
  v = tf.Variable(5.0)
  if do_add:
    op = v.assign_add(x)
  else:
    op = v.assign_sub(x)
  with tf.control_dependencies([op]):
    return v.read_value()

f_add = tf.compat.v1.wrap_function(f, [tf.TensorSpec((), tf.float32), True])

assert float(f_add(1.0)) == 6.0
assert float(f_add(1.0)) == 7.0

# Can call tf.compat.v1.wrap_function again to get a new trace, a new set
# of variables, and possibly different non-template arguments.
f_sub= tf.compat.v1.wrap_function(f, [tf.TensorSpec((), tf.float32), False])

assert float(f_sub(1.0)) == 4.0
assert float(f_sub(1.0)) == 3.0
```

Both <a href="../../../tf/compat/v1/wrap_function.md"><code>tf.compat.v1.wrap_function</code></a> and <a href="../../../tf/function.md"><code>tf.function</code></a> create a callable
TensorFlow graph. But while <a href="../../../tf/function.md"><code>tf.function</code></a> runs all stateful operations
(e.g. <a href="../../../tf/print.md"><code>tf.print</code></a>) and sequences operations to provide the same semantics as
eager execution, `wrap_function` is closer to the behavior of `session.run` in
TensorFlow 1.x. It will not run any operations unless they are required to
compute the function's outputs, either through a data dependency or a control
dependency. Nor will it sequence operations.

Unlike <a href="../../../tf/function.md"><code>tf.function</code></a>, `wrap_function` will only trace the Python function
once. As with placeholders in TF 1.x, shapes and dtypes must be provided to
`wrap_function`'s `signature` argument.

Since it is only traced once, variables and state may be created inside the
function and owned by the function wrapper object.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`fn`
</td>
<td>
python function to be wrapped
</td>
</tr><tr>
<td>
`signature`
</td>
<td>
the placeholder and python arguments to be passed to the wrapped
function
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional. The name of the function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
the wrapped graph function.
</td>
</tr>

</table>

