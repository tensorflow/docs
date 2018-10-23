

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.framework.get_variables_by_name

``` python
get_variables_by_name(
    given_name,
    scope=None
)
```



Defined in [`tensorflow/contrib/framework/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/framework/python/ops/variables.py).

See the guide: [Framework (contrib) > Variables](../../../../../api_guides/python/contrib.framework#Variables)

Gets the list of variables that were given that name.

#### Args:

* <b>`given_name`</b>: name given to the variable without any scope.
* <b>`scope`</b>: an optional scope for filtering the variables to return.


#### Returns:

  a copied list of variables with the given name and scope.