page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.linear_logit_fn_builder

``` python
tf.contrib.estimator.linear_logit_fn_builder(
    units,
    feature_columns,
    sparse_combiner='sum'
)
```



Defined in [`tensorflow/python/estimator/canned/linear.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/estimator/canned/linear.py).

Function builder for a linear logit_fn.

#### Args:

* <b>`units`</b>: An int indicating the dimension of the logit layer.
* <b>`feature_columns`</b>: An iterable containing all the feature columns used by
    the model.
* <b>`sparse_combiner`</b>: A string specifying how to reduce if a categorical column
    is multivalent.  One of "mean", "sqrtn", and "sum".


#### Returns:

A logit_fn (see below).