page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.capture_dependencies

Capture variables created within this scope as `Template` dependencies.

``` python
tf.contrib.checkpoint.capture_dependencies(template)
```



Defined in [`python/training/tracking/util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/tracking/util.py).

<!-- Placeholder for "Used in" -->

Requires that `template.variable_scope` is active.

This scope is intended as a compatibility measure, allowing a trackable
object to add dependencies on variables created in a block of code which is
not aware of object-based saving (and instead uses variable names
heavily). This is how `Template` objects add dependencies on variables and
sub-`Template`s. Where possible, use <a href="../../../tf/make_template"><code>tf.compat.v1.make_template</code></a> directly.

#### Args:


* <b>`template`</b>: The `Template` object to register dependencies with.


#### Yields:

None (when used as a context manager).
