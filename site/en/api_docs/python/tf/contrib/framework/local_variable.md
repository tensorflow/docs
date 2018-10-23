

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.framework.local_variable

### `tf.contrib.framework.local_variable`

``` python
local_variable(
    initial_value,
    validate_shape=True,
    name=None
)
```



Defined in [`tensorflow/contrib/framework/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/framework/python/ops/variables.py).

See the guide: [Framework (contrib) > Variables](../../../../../api_guides/python/contrib.framework#Variables)

Create variable and add it to `GraphKeys.LOCAL_VARIABLES` collection.

#### Args:

* <b>`initial_value`</b>: See variables.Variable.__init__.
* <b>`validate_shape`</b>: See variables.Variable.__init__.
* <b>`name`</b>: See variables.Variable.__init__.
Returns:
  New variable.