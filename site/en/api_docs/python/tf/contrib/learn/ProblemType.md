page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.ProblemType

## Class `ProblemType`

Enum-like values for the type of problem that the model solves.





Defined in [`contrib/learn/python/learn/estimators/constants.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/learn/python/learn/estimators/constants.py).

<!-- Placeholder for "Used in" -->

THIS CLASS IS DEPRECATED.

These values are used when exporting the model to produce the appropriate
signature function for serving.

The following values are supported:
  UNSPECIFIED: Produces a predict signature_fn.
  CLASSIFICATION: Produces a classify signature_fn.
  LINEAR_REGRESSION: Produces a regression signature_fn.
  LOGISTIC_REGRESSION: Produces a classify signature_fn.

## Class Members

* `CLASSIFICATION = 1` <a id="CLASSIFICATION"></a>
* `LINEAR_REGRESSION = 2` <a id="LINEAR_REGRESSION"></a>
* `LOGISTIC_REGRESSION = 3` <a id="LOGISTIC_REGRESSION"></a>
* `UNSPECIFIED = 0` <a id="UNSPECIFIED"></a>
