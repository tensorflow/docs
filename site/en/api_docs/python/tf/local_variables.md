page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.local_variables

Returns local variables.

### Aliases:

* `tf.compat.v1.local_variables`
* `tf.local_variables`

``` python
tf.local_variables(scope=None)
```



Defined in [`python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/variables.py).

<!-- Placeholder for "Used in" -->

Local variables - per process variables, usually not saved/restored to
checkpoint and used for temporary or intermediate values.
For example, they can be used as counters for metrics computation or
number of epochs this machine has read data.
The <a href="../tf/contrib/framework/local_variable"><code>tf.contrib.framework.local_variable()</code></a> function automatically adds the
new variable to <a href="../tf/GraphKeys#LOCAL_VARIABLES"><code>GraphKeys.LOCAL_VARIABLES</code></a>.
This convenience function returns the contents of that collection.

An alternative to local variables are global variables. See
<a href="../tf/global_variables"><code>tf.compat.v1.global_variables</code></a>

#### Args:


* <b>`scope`</b>: (Optional.) A string. If supplied, the resulting list is filtered
  to include only items whose `name` attribute matches `scope` using
  `re.match`. Items without a `name` attribute are never returned if a
  scope is supplied. The choice of `re.match` means that a `scope` without
  special tokens filters by prefix.


#### Returns:

A list of local `Variable` objects.
