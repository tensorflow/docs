page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_local_variables

Gets the list of local variables, filtered by scope and/or suffix.

``` python
tf.contrib.framework.get_local_variables(
    scope=None,
    suffix=None
)
```



Defined in [`contrib/framework/python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/ops/variables.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`scope`</b>: an optional scope for filtering the variables to return.
* <b>`suffix`</b>: an optional suffix for filtering the variables to return.


#### Returns:

a list of variables in collection with scope and suffix.
