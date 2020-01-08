page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.timeseries.OneShotPredictionHead

## Class `OneShotPredictionHead`





Defined in [`tensorflow/contrib/timeseries/python/timeseries/head.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/timeseries/python/timeseries/head.py).

A time series head which exports a single stateless serving signature.

The serving default signature exported by this head expects `times`, `values`,
and any exogenous features, but no state. `values` has shape `[batch_size,
filter_length, num_features]` and `times` has shape `[batch_size,
total_length]`, where `total_length > filter_length`. Any exogenous features
must have their shapes prefixed by the shape of the `times` feature.

When serving, first performs filtering on the series up to `filter_length`
starting from the default start state for the model, then computes predictions
on the remainder of the series, returning them.

Model state is neither accepted nor returned, so filtering must be performed
each time predictions are requested when using this head.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    model,
    state_manager,
    optimizer,
    input_statistics_generator=None,
    name=None
)
```

Creates a `_Head` for time series regression.

#### Args:

* <b>`model`</b>: A model for time series regression.
* <b>`state_manager`</b>: A state manager.
* <b>`optimizer`</b>: An optimizer.
* <b>`input_statistics_generator`</b>: A input statistics generator.
* <b>`name`</b>: An optional name for the model.



## Properties

<h3 id="logits_dimension"><code>logits_dimension</code></h3>

See `_Head`.

<h3 id="name"><code>name</code></h3>





## Methods

<h3 id="create_estimator_spec"><code>create_estimator_spec</code></h3>

``` python
create_estimator_spec(
    features,
    mode,
    labels=None
)
```

Performs basic error checking and returns an EstimatorSpec.

<h3 id="create_loss"><code>create_loss</code></h3>

``` python
create_loss(
    features,
    mode,
    logits=None,
    labels=None
)
```

See `_Head`.



