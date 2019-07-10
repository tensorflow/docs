page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.autograph.to_graph

### Aliases:

* `tf.autograph.to_graph`
* `tf.contrib.autograph.to_graph`

``` python
tf.autograph.to_graph(
    entity,
    recursive=True,
    arg_values=None,
    arg_types=None,
    experimental_optional_features=tf.autograph.experimental.Feature.ALL,
    experimental_strip_decorators=None,
    experimental_verbose=converter.Verbosity.BRIEF,
    experimental_partial_types=None
)
```



Defined in [`tensorflow/python/autograph/impl/api.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/autograph/impl/api.py).

Converts a Python entity into a TensorFlow graph.

Also see: <a href="../../tf/autograph/to_code"><code>tf.autograph.to_code</code></a>, `tf.function`.

Unlike `tf.function`, `to_graph` is a low-level transpiler that converts
Python code to TensorFlow graph code. It does not implement any caching,
variable management or create any actual ops, and is best used where greater
control over the generated TensorFlow graph is desired. Another difference
from `tf.function` is that `to_graph` will not wrap the graph into a
TensorFlow function or a Python callable. Internally, `tf.function` uses
`to_graph`.

_Example Usage_

```python
  def foo(x):
    if x > 0:
      y = x * x
    else:
      y = -x
    return y

  converted_foo = to_graph(foo)

  x = tf.constant(1)
  y = converted_foo(x)  # converted_foo is a TensorFlow Op-like.
  assert is_tensor(y)
```

Supported Python entities include:
  * functions
  * classes
  * object methods

Functions are converted into new functions with converted code.

Classes are converted by generating a new class whose methods use converted
code.

Methods are converted into unbound function that have an additional first
argument called `self`.

#### Args:

* <b>`entity`</b>: Python callable or class to convert.
* <b>`recursive`</b>: Whether to recursively convert any functions that the
    converted function may call.
* <b>`arg_values`</b>: Optional dict of value hints for symbols including
    function arguments mapping string names to actual values. For example,
    `arg_values={'a': 1}` will map the variable `a` to the value `1`.
* <b>`arg_types`</b>: Optional dict of type hints for symbols including function
    arguments. Type hints allow specifying just the type of a variable, rather
    than a specific value.
* <b>`experimental_optional_features`</b>: `None`, a tuple of, or a single
    <a href="../../tf/autograph/experimental/Feature"><code>tf.autograph.experimental.Feature</code></a> value. Controls the use of
    optional features in the conversion process.
* <b>`experimental_strip_decorators`</b>: A tuple specifying decorators that should be
    excluded from the compiled output. By default, when converting a function
    before the decorators are applied, the compiled output will include those
    decorators.
* <b>`experimental_verbose`</b>: The level of printing verbosity to use, as a
    <a href="../../tf/autograph/experimental/Verbosity"><code>tf.autograph.experimental.Verbosity</code></a> value.
* <b>`experimental_partial_types`</b>: A `set` of `type` values, reserved for internal
    use.


#### Returns:

Same as `entity`, the converted Python function or class.


#### Raises:

* <b>`ValueError`</b>: If the entity could not be converted.