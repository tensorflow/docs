page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.deprecated_args

``` python
tf.contrib.framework.deprecated_args(
    date,
    instructions,
    *deprecated_arg_names_or_tuples,
    **kwargs
)
```



Defined in [`tensorflow/python/util/deprecation.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/util/deprecation.py).

See the guide: [Framework (contrib) > Deprecation](../../../../../api_guides/python/contrib.framework#Deprecation)

Decorator for marking specific function arguments as deprecated.

This decorator logs a deprecation warning whenever the decorated function is
called with the deprecated argument. It has the following format:

  Calling <function> (from <module>) with <arg> is deprecated and will be
  removed after <date>. Instructions for updating:
    <instructions>

If `date` is None, 'after <date>' is replaced with 'in a future version'.
<function> includes the class name if it is a method.

It also edits the docstring of the function: ' (deprecated arguments)' is
appended to the first line of the docstring and a deprecation notice is
prepended to the rest of the docstring.

#### Args:

* <b>`date`</b>: String or None. The date the function is scheduled to be removed.
    Must be ISO 8601 (YYYY-MM-DD), or None.
* <b>`instructions`</b>: String. Instructions on how to update code using the
    deprecated function.
* <b>`*deprecated_arg_names_or_tuples`</b>: String or 2-Tuple(String,
    [ok_vals]).  The string is the deprecated argument name.
    Optionally, an ok-value may be provided.  If the user provided
    argument equals this value, the warning is suppressed.
* <b>`**kwargs`</b>: If `warn_once=False` is passed, every call with a deprecated
    argument will log a warning. The default behavior is to only warn the
    first time the function is called with any given deprecated argument.
    All other kwargs raise `ValueError`.


#### Returns:

Decorated function or method.


#### Raises:

* <b>`ValueError`</b>: If date is not None or in ISO 8601 format, instructions are
    empty, the deprecated arguments are not present in the function
    signature, the second element of a deprecated_tuple is not a
    list, or if a kwarg other than `warn_once` is passed.