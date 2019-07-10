page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.moving_average_variables

Returns all variables that maintain their moving averages.

### Aliases:

* `tf.compat.v1.moving_average_variables`
* `tf.moving_average_variables`

``` python
tf.moving_average_variables(scope=None)
```



Defined in [`python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/variables.py).

<!-- Placeholder for "Used in" -->

If an `ExponentialMovingAverage` object is created and the `apply()`
method is called on a list of variables, these variables will
be added to the <a href="../tf/GraphKeys#MOVING_AVERAGE_VARIABLES"><code>GraphKeys.MOVING_AVERAGE_VARIABLES</code></a> collection.
This convenience function returns the contents of that collection.

#### Args:


* <b>`scope`</b>: (Optional.) A string. If supplied, the resulting list is filtered
  to include only items whose `name` attribute matches `scope` using
  `re.match`. Items without a `name` attribute are never returned if a
  scope is supplied. The choice of `re.match` means that a `scope` without
  special tokens filters by prefix.


#### Returns:

A list of Variable objects.
