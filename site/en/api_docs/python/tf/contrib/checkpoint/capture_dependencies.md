page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.capture_dependencies


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/tracking/util.py#L519-L607">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Capture variables created within this scope as `Template` dependencies.

``` python
tf.contrib.checkpoint.capture_dependencies(template)
```



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
