page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.autograph.to_code

### Aliases:

* `tf.autograph.to_code`
* `tf.contrib.autograph.to_code`

``` python
tf.autograph.to_code(
    entity,
    recursive=True,
    arg_values=None,
    arg_types=None,
    indentation='  ',
    experimental_optional_features=tf.autograph.experimental.Feature.ALL,
    experimental_partial_types=None
)
```



Defined in [`tensorflow/python/autograph/impl/api.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/autograph/impl/api.py).

Similar to `to_graph`, but returns Python source code as a string.

Also see: <a href="../../tf/autograph/to_graph"><code>tf.autograph.to_graph</code></a>.

`to_graph` returns the Python source code that can be used to generate a
TensorFlow graph that is functionally identical to the input Python code.

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
* <b>`indentation`</b>: The string to use for indenting. Typically two or four spaces,
    or just the tab character.
* <b>`experimental_optional_features`</b>: `None`, a tuple of, or a single
    <a href="../../tf/autograph/experimental/Feature"><code>tf.autograph.experimental.Feature</code></a> value. Controls the use of
    optional features in the conversion process.
* <b>`experimental_partial_types`</b>: A `set` of `type` values, reserved for internal
    use.


#### Returns:

The converted code as string.