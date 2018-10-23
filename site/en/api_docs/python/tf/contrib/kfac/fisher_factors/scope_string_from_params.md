

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.fisher_factors.scope_string_from_params

``` python
tf.contrib.kfac.fisher_factors.scope_string_from_params(params)
```



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_factors.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/kfac/python/ops/fisher_factors.py).

Builds a variable scope string name from the given parameters.

Supported parameters are:
  * tensors
  * booleans
  * ints
  * strings
  * depth-1 tuples/lists of ints
  * any depth tuples/lists of tensors
Other parameter types will throw an error.

#### Args:

* <b>`params`</b>: A parameter or list of parameters.


#### Returns:

A string to use for the variable scope.


#### Raises:

* <b>`ValueError`</b>: if params includes an unsupported type.