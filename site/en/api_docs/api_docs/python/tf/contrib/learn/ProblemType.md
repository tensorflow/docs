

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.ProblemType

## Class `ProblemType`





Defined in [`tensorflow/contrib/learn/python/learn/estimators/constants.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/learn/python/learn/estimators/constants.py).

See the guide: [Learn (contrib) > Input processing](../../../../../api_guides/python/contrib.learn#Input_processing)

Enum-like values for the type of problem that the model solves.

THIS CLASS IS DEPRECATED.

These values are used when exporting the model to produce the appropriate
signature function for serving.

The following values are supported:
  UNSPECIFIED: Produces a predict signature_fn.
  CLASSIFICATION: Produces a classify signature_fn.
  LINEAR_REGRESSION: Produces a regression signature_fn.
  LOGISTIC_REGRESSION: Produces a classify signature_fn.

## Class Members

<h3 id="CLASSIFICATION"><code>CLASSIFICATION</code></h3>

<h3 id="LINEAR_REGRESSION"><code>LINEAR_REGRESSION</code></h3>

<h3 id="LOGISTIC_REGRESSION"><code>LOGISTIC_REGRESSION</code></h3>

<h3 id="UNSPECIFIED"><code>UNSPECIFIED</code></h3>

