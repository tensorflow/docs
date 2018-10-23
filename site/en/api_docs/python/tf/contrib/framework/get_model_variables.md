

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.framework.get_model_variables

### `tf.contrib.framework.get_model_variables`

``` python
get_model_variables(
    scope=None,
    suffix=None
)
```



Defined in [`tensorflow/contrib/framework/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/framework/python/ops/variables.py).

See the guide: [Framework (contrib) > Variables](../../../../../api_guides/python/contrib.framework#Variables)

Gets the list of model variables, filtered by scope and/or suffix.

#### Args:

* <b>`scope`</b>: an optional scope for filtering the variables to return.
* <b>`suffix`</b>: an optional suffix for filtering the variables to return.


#### Returns:

  a list of variables in collection with scope and suffix.