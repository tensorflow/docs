page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.linear_logit_fn_builder


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/canned/linear.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Function builder for a linear logit_fn.

### Aliases:

* <a href="/api_docs/python/tf/contrib/estimator/linear_logit_fn_builder"><code>tf.compat.v1.estimator.experimental.linear_logit_fn_builder</code></a>
* <a href="/api_docs/python/tf/contrib/estimator/linear_logit_fn_builder"><code>tf.estimator.experimental.linear_logit_fn_builder</code></a>


``` python
tf.contrib.estimator.linear_logit_fn_builder(
    units,
    feature_columns,
    sparse_combiner='sum'
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`units`</b>: An int indicating the dimension of the logit layer.
* <b>`feature_columns`</b>: An iterable containing all the feature columns used by
  the model.
* <b>`sparse_combiner`</b>: A string specifying how to reduce if a categorical column
  is multivalent.  One of "mean", "sqrtn", and "sum".


#### Returns:

A logit_fn (see below).
