page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.summary.experimental.summary_scope

Experimental context manager for use when defining a custom summary op.

``` python
tf.compat.v2.summary.experimental.summary_scope(
    name,
    default_name='summary',
    values=None
)
```



Defined in [`python/ops/summary_ops_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/summary_ops_v2.py).

<!-- Placeholder for "Used in" -->

This behaves similarly to <a href="../../../../../tf/name_scope"><code>tf.name_scope</code></a>, except that it returns a generated
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

#### Args:


* <b>`name`</b>: string name for the summary.
* <b>`default_name`</b>: Optional; if provided, used as default name of the summary.
* <b>`values`</b>: Optional; passed as `values` parameter to name_scope.


#### Yields:

A tuple `(tag, scope)` as described above.
