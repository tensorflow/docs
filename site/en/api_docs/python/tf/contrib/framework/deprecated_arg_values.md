page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.deprecated_arg_values

Decorator for marking specific function argument values as deprecated.

``` python
tf.contrib.framework.deprecated_arg_values(
    date,
    instructions,
    warn_once=True,
    **deprecated_kwargs
)
```



Defined in [`python/util/deprecation.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/util/deprecation.py).

<!-- Placeholder for "Used in" -->

This decorator logs a deprecation warning whenever the decorated function is
called with the deprecated argument values. It has the following format:

  Calling <function> (from <module>) with <arg>=<value> is deprecated and
  will be removed after <date>. Instructions for updating:
    <instructions>

If `date` is None, 'after <date>' is replaced with 'in a future version'.
<function> will include the class name if it is a method.

It also edits the docstring of the function: ' (deprecated arguments)' is
appended to the first line of the docstring and a deprecation notice is
prepended to the rest of the docstring.

#### Args:


* <b>`date`</b>: String or None. The date the function is scheduled to be removed.
  Must be ISO 8601 (YYYY-MM-DD), or None
* <b>`instructions`</b>: String. Instructions on how to update code using the
  deprecated function.
* <b>`warn_once`</b>: If `True`, warn only the first time this function is called with
  deprecated argument values. Otherwise, every call (with a deprecated
  argument value) will log a warning.
* <b>`**deprecated_kwargs`</b>: The deprecated argument values.


#### Returns:

Decorated function or method.



#### Raises:


* <b>`ValueError`</b>: If date is not None or in ISO 8601 format, or instructions are
  empty.