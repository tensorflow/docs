page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.ProblemType


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/constants.py#L27-L44">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ProblemType`

Enum-like values for the type of problem that the model solves.



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
