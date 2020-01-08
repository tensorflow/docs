page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.build_raw_supervised_input_receiver_fn

``` python
tf.contrib.estimator.build_raw_supervised_input_receiver_fn(
    features,
    labels,
    default_batch_size=None
)
```



Defined in [`tensorflow/python/estimator/export/export.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/estimator/export/export.py).

Build a supervised_input_receiver_fn for raw features and labels.

This function wraps tensor placeholders in a supervised_receiver_fn
with the expectation that the features and labels appear precisely as
the model_fn expects them. Features and labels can therefore be dicts of
tensors, or raw tensors.

#### Args:

* <b>`features`</b>: a dict of string to `Tensor` or `Tensor`.
* <b>`labels`</b>: a dict of string to `Tensor` or `Tensor`.
* <b>`default_batch_size`</b>: the number of query examples expected per batch.
      Leave unset for variable batch size (recommended).


#### Returns:

A supervised_input_receiver_fn.


#### Raises:

* <b>`ValueError`</b>: if features and labels have overlapping keys.