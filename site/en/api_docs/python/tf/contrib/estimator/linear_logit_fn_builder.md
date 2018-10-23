

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.estimator.linear_logit_fn_builder

``` python
tf.contrib.estimator.linear_logit_fn_builder(
    units,
    feature_columns
)
```



Defined in [`tensorflow/python/estimator/canned/linear.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/estimator/canned/linear.py).

Function builder for a linear logit_fn.

#### Args:

* <b>`units`</b>: An int indicating the dimension of the logit layer.
* <b>`feature_columns`</b>: An iterable containing all the feature columns used by
    the model.


#### Returns:

A logit_fn (see below).