

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.name_scope

### `tf.contrib.keras.backend.name_scope`
### `tf.name_scope`

``` python
name_scope(
    *args,
    **kwds
)
```

See the guide: [Building Graphs > Utility functions](../../../api_guides/python/framework#Utility_functions)

Returns a context manager for use when defining a Python op.

This context manager validates that the given `values` are from the
same graph, makes that graph the default graph, and pushes a
name scope in that graph (see
[`tf.Graph.name_scope`](../tf/Graph#name_scope)
for more details on that).

For example, to define a new Python op called `my_op`:

```python
def my_op(a, b, c, name=None):
  with tf.name_scope(name, "MyOp", [a, b, c]) as scope:
    a = tf.convert_to_tensor(a, name="a")
    b = tf.convert_to_tensor(b, name="b")
    c = tf.convert_to_tensor(c, name="c")
    # Define some computation that uses `a`, `b`, and `c`.
    return foo_op(..., name=scope)
```

#### Args:

* <b>`name`</b>: The name argument that is passed to the op function.
* <b>`default_name`</b>: The default name to use if the `name` argument is `None`.
* <b>`values`</b>: The list of `Tensor` arguments that are passed to the op function.


#### Returns:

  A context manager for use in defining Python ops. Yields the name scope.


#### Raises:

* <b>`ValueError`</b>: if neither `name` nor `default_name` is provided
    but `values` are.