

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.moving_average_variables

``` python
tf.moving_average_variables(scope=None)
```



Defined in [`tensorflow/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/ops/variables.py).

See the guide: [Variables > Variable helper functions](../../../api_guides/python/state_ops#Variable_helper_functions)

Returns all variables that maintain their moving averages.

If an `ExponentialMovingAverage` object is created and the `apply()`
method is called on a list of variables, these variables will
be added to the `GraphKeys.MOVING_AVERAGE_VARIABLES` collection.
This convenience function returns the contents of that collection.

#### Args:

* <b>`scope`</b>: (Optional.) A string. If supplied, the resulting list is filtered
    to include only items whose `name` attribute matches `scope` using
    `re.match`. Items without a `name` attribute are never returned if a
    scope is supplied. The choice of `re.match` means that a `scope` without
    special tokens filters by prefix.


#### Returns:

A list of Variable objects.