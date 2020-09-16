description: Experimental context manager for use when defining a custom summary op.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.summary.experimental.summary_scope" />
<meta itemprop="path" content="Stable" />
</div>

# tf.summary.experimental.summary_scope

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/summary_ops_v2.py#L573-L611">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Experimental context manager for use when defining a custom summary op.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@tf_contextlib.contextmanager</code>
<code>tf.summary.experimental.summary_scope(
    name, default_name='summary', values=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This behaves similarly to <a href="../../../tf/name_scope.md"><code>tf.name_scope</code></a>, except that it returns a generated
summary tag in addition to the scope name. The tag is structurally similar to
the scope name - derived from the user-provided name, prefixed with enclosing
name scopes if any - but we relax the constraint that it be uniquified, as
well as the character set limitation (so the user-provided name can contain
characters not legal for scope names; in the scope name these are removed).

This makes the summary tag more predictable and consistent for the user.

For example, to define a new summary op called `my_op`:

```python
def my_op(name, my_value, step):
  with tf.summary.summary_scope(name, "MyOp", [my_value]) as (tag, scope):
    my_value = tf.convert_to_tensor(my_value)
    return tf.summary.write(tag, my_value, step=step)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
string name for the summary.
</td>
</tr><tr>
<td>
`default_name`
</td>
<td>
Optional; if provided, used as default name of the summary.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
Optional; passed as `values` parameter to name_scope.
</td>
</tr>
</table>



#### Yields:

A tuple `(tag, scope)` as described above.
