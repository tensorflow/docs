page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.timeseries.predict_continuation_input_fn

``` python
tf.contrib.timeseries.predict_continuation_input_fn(
    evaluation,
    steps=None,
    times=None,
    exogenous_features=None
)
```



Defined in [`tensorflow/contrib/timeseries/python/timeseries/input_pipeline.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/timeseries/python/timeseries/input_pipeline.py).

An Estimator input_fn for running predict() after evaluate().

If the call to evaluate() we are making predictions based on had a batch_size
greater than one, predictions will start after each of these windows
(i.e. will have the same batch dimension).

#### Args:

* <b>`evaluation`</b>: The dictionary returned by `Estimator.evaluate`, with keys
    FilteringResults.STATE_TUPLE and FilteringResults.TIMES.
* <b>`steps`</b>: The number of steps to predict (scalar), starting after the
    evaluation. If `times` is specified, `steps` must not be; one is required.
* <b>`times`</b>: A [batch_size x window_size] array of integers (not a Tensor)
    indicating times to make predictions for. These times must be after the
    corresponding evaluation. If `steps` is specified, `times` must not be;
    one is required. If the batch dimension is omitted, it is assumed to be 1.
* <b>`exogenous_features`</b>: Optional dictionary. If specified, indicates exogenous
    features for the model to use while making the predictions. Values must
    have shape [batch_size x window_size x ...], where `batch_size` matches
    the batch dimension used when creating `evaluation`, and `window_size` is
    either the `steps` argument or the `window_size` of the `times` argument
    (depending on which was specified).

#### Returns:

An `input_fn` suitable for passing to the `predict` function of a time
series `Estimator`.

#### Raises:

* <b>`ValueError`</b>: If `times` or `steps` are misspecified.