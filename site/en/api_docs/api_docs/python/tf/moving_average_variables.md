

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.moving_average_variables

``` python
moving_average_variables()
```



Defined in [`tensorflow/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/variables.py).

See the guide: [Variables > Variable helper functions](../../../api_guides/python/state_ops#Variable_helper_functions)

Returns all variables that maintain their moving averages.

If an `ExponentialMovingAverage` object is created and the `apply()`
method is called on a list of variables, these variables will
be added to the `GraphKeys.MOVING_AVERAGE_VARIABLES` collection.
This convenience function returns the contents of that collection.

#### Returns:

  A list of Variable objects.