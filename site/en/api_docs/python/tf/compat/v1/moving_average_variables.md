page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.moving_average_variables


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/variables.py#L3173-L3192">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns all variables that maintain their moving averages.

``` python
tf.compat.v1.moving_average_variables(scope=None)
```



<!-- Placeholder for "Used in" -->

If an `ExponentialMovingAverage` object is created and the `apply()`
method is called on a list of variables, these variables will
be added to the `GraphKeys.MOVING_AVERAGE_VARIABLES` collection.
This convenience function returns the contents of that collection.

#### Args:


* <b>`scope`</b>: (Optional.) A string. If supplied, the resulting list is filtered to
  include only items whose `name` attribute matches `scope` using
  `re.match`. Items without a `name` attribute are never returned if a scope
  is supplied. The choice of `re.match` means that a `scope` without special
  tokens filters by prefix.


#### Returns:

A list of Variable objects.
