page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.capture_dependencies

``` python
tf.contrib.checkpoint.capture_dependencies(template)
```



Defined in [`tensorflow/python/training/checkpointable/util.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/training/checkpointable/util.py).

Capture variables created within this scope as `Template` dependencies.

Requires that `template.variable_scope` is active.

This scope is intended as a compatibility measure, allowing a checkpointable
object to add dependencies on variables created in a block of code which is
not aware of object-based saving (and instead uses variable names
heavily). This is how `Template` objects add dependencies on variables and
sub-`Template`s. Where possible, use <a href="../../../tf/make_template"><code>tf.make_template</code></a> directly.

#### Args:

* <b>`template`</b>: The `Template` object to register dependencies with.


#### Yields:

None (when used as a context manager).