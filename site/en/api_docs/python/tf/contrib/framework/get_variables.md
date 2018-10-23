

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.framework.get_variables

### `tf.contrib.framework.get_variables`

``` python
get_variables(
    scope=None,
    suffix=None,
    collection=tf.GraphKeys.GLOBAL_VARIABLES
)
```



Defined in [`tensorflow/contrib/framework/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/framework/python/ops/variables.py).

See the guide: [Framework (contrib) > Variables](../../../../../api_guides/python/contrib.framework#Variables)

Gets the list of variables, filtered by scope and/or suffix.

#### Args:

* <b>`scope`</b>: an optional scope for filtering the variables to return. Can be a
    variable scope or a string.
* <b>`suffix`</b>: an optional suffix for filtering the variables to return.
* <b>`collection`</b>: in which collection search for. Defaults to
    `GraphKeys.GLOBAL_VARIABLES`.


#### Returns:

  a list of variables in collection with scope and suffix.