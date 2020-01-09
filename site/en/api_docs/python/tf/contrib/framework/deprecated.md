page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.deprecated


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/util/deprecation.py#L274-L329">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Decorator for marking functions or methods deprecated.

``` python
tf.contrib.framework.deprecated(
    date,
    instructions,
    warn_once=True
)
```



<!-- Placeholder for "Used in" -->

This decorator logs a deprecation warning whenever the decorated function is
called. It has the following format:

  <function> (from <module>) is deprecated and will be removed after <date>.
  Instructions for updating:
  <instructions>

If `date` is None, 'after <date>' is replaced with 'in a future version'.
<function> will include the class name if it is a method.

It also edits the docstring of the function: ' (deprecated)' is appended
to the first line of the docstring and a deprecation notice is prepended
to the rest of the docstring.

#### Args:


* <b>`date`</b>: String or None. The date the function is scheduled to be removed.
  Must be ISO 8601 (YYYY-MM-DD), or None.
* <b>`instructions`</b>: String. Instructions on how to update code using the
  deprecated function.
* <b>`warn_once`</b>: Boolean. Set to `True` to warn only the first time the decorated
  function is called. Otherwise, every call will log a warning.


#### Returns:

Decorated function or method.



#### Raises:


* <b>`ValueError`</b>: If date is not None or in ISO 8601 format, or instructions are
  empty.
