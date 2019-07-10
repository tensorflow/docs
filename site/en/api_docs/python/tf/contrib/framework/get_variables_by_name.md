page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_variables_by_name

Gets the list of variables that were given that name.

``` python
tf.contrib.framework.get_variables_by_name(
    given_name,
    scope=None
)
```



Defined in [`contrib/framework/python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/ops/variables.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`given_name`</b>: name given to the variable without any scope.
* <b>`scope`</b>: an optional scope for filtering the variables to return.


#### Returns:

a copied list of variables with the given name and scope.
