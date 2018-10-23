

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.timeseries.ARModel

## Class `ARModel`





Defined in [`tensorflow/contrib/timeseries/python/timeseries/ar_model.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/timeseries/python/timeseries/ar_model.py).

Auto-regressive model, both linear and non-linear.

Features to the model include time and values of input_window_size timesteps,
and times for output_window_size timesteps. These are passed through zero or
more hidden layers, and then fed to a loss function (e.g. squared loss).

Note that this class can also be used to regress against time only by setting
the input_window_size to zero.

## Properties

<h3 id="exogenous_feature_columns"><code>exogenous_feature_columns</code></h3>

`tf.feature_colum`s for features which are not predicted.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    periodicities,
    input_window_size,
    output_window_size,
    num_features,
    num_time_buckets=10,
    loss=NORMAL_LIKELIHOOD_LOSS,
    hidden_layer_sizes=None
)
```

Constructs an auto-regressive model.

#### Args:

* <b>`periodicities`</b>: periodicities of the input data, in the same units as the
    time feature. Note this can be a single value or a list of values for
    multiple periodicities.
* <b>`input_window_size`</b>: Number of past time steps of data to look at when doing
    the regression.
* <b>`output_window_size`</b>: Number of future time steps to predict. Note that
    setting it to > 1 empirically seems to give a better fit.
* <b>`num_features`</b>: number of input features per time step.
* <b>`num_time_buckets`</b>: Number of buckets into which to divide (time %
    periodicity) for generating time based features.
* <b>`loss`</b>: Loss function to use for training. Currently supported values are
    SQUARED_LOSS and NORMAL_LIKELIHOOD_LOSS. Note that for
    NORMAL_LIKELIHOOD_LOSS, we train the covariance term as well. For
    SQUARED_LOSS, the evaluation loss is reported based on un-scaled
    observations and predictions, while the training loss is computed on
    normalized data (if input statistics are available).
* <b>`hidden_layer_sizes`</b>: list of sizes of hidden layers.

<h3 id="define_loss"><code>define_loss</code></h3>

``` python
define_loss(
    features,
    mode
)
```

Default loss definition with state replicated across a batch.

Time series passed to this model have a batch dimension, and each series in
a batch can be operated on in parallel. This loss definition assumes that
each element of the batch represents an independent sample conditioned on
the same initial state (i.e. it is simply replicated across the batch). A
batch size of one provides sequential operations on a single time series.

More complex processing may operate instead on get_start_state() and
get_batch_loss() directly.

#### Args:

* <b>`features`</b>: A dictionary (such as is produced by a chunker) with at minimum
    the following key/value pairs (others corresponding to the
    `exogenous_feature_columns` argument to `__init__` may be included
    representing exogenous regressors):
* <b>`TrainEvalFeatures.TIMES`</b>: A [batch size x window size] integer Tensor
        with times for each observation. If there is no artificial chunking,
        the window size is simply the length of the time series.
* <b>`TrainEvalFeatures.VALUES`</b>: A [batch size x window size x num features]
        Tensor with values for each observation.
* <b>`mode`</b>: The tf.estimator.ModeKeys mode to use (TRAIN, EVAL). For INFER,
    see predict().

#### Returns:

A ModelOutputs object.

<h3 id="generate"><code>generate</code></h3>

``` python
generate(
    number_of_series,
    series_length,
    model_parameters=None,
    seed=None
)
```



<h3 id="get_batch_loss"><code>get_batch_loss</code></h3>

``` python
get_batch_loss(
    features,
    mode,
    state
)
```

Computes predictions and a loss.

#### Args:

* <b>`features`</b>: A dictionary (such as is produced by a chunker) with the
    following key/value pairs (shapes are given as required for training):
      TrainEvalFeatures.TIMES: A [batch size, self.window_size] integer
        Tensor with times for each observation. To train on longer
        sequences, the data should first be chunked.
      TrainEvalFeatures.VALUES: A [batch size, self.window_size,
        self.num_features] Tensor with values for each observation.
    When evaluating, `TIMES` and `VALUES` must have a window size of at
    least self.window_size, but it may be longer, in which case the last
    window_size - self.input_window_size times (or fewer if this is not
    divisible by self.output_window_size) will be evaluated on with
    non-overlapping output windows (and will have associated
    predictions). This is primarily to support qualitative
    evaluation/plotting, and is not a recommended way to compute evaluation
    losses (since there is no overlap in the output windows, which for
    window-based models is an undesirable bias).
* <b>`mode`</b>: The tf.estimator.ModeKeys mode to use (TRAIN or EVAL).
* <b>`state`</b>: Unused

#### Returns:

A model.ModelOutputs object.

#### Raises:

* <b>`ValueError`</b>: If `mode` is not TRAIN or EVAL, or if static shape information
  is incorrect.

<h3 id="get_start_state"><code>get_start_state</code></h3>

``` python
get_start_state()
```



<h3 id="initialize_graph"><code>initialize_graph</code></h3>

``` python
initialize_graph(input_statistics=None)
```

Define ops for the model, not depending on any previously defined ops.

#### Args:

* <b>`input_statistics`</b>: A math_utils.InputStatistics object containing input
      statistics. If None, data-independent defaults are used, which may
      result in longer or unstable training.

<h3 id="loss_op"><code>loss_op</code></h3>

``` python
loss_op(
    targets,
    prediction_ops
)
```

Create loss_op.

<h3 id="predict"><code>predict</code></h3>

``` python
predict(features)
```

Computes predictions multiple steps into the future.

#### Args:

* <b>`features`</b>: A dictionary with the following key/value pairs:
* <b>`PredictionFeatures.TIMES`</b>: A [batch size, predict window size]
      integer Tensor of times, after the window of data indicated by
      `STATE_TUPLE`, to make predictions for.
* <b>`PredictionFeatures.STATE_TUPLE`</b>: A tuple of (times, values), times with
      shape [batch size, self.input_window_size], values with shape [batch
      size, self.input_window_size, self.num_features] representing a
      segment of the time series before `TIMES`. This data is used
      to start of the autoregressive computation. This should have data for
      at least self.input_window_size timesteps.

#### Returns:

A dictionary with keys, "mean", "covariance". The
values are Tensors of shape [batch_size, predict window size,
num_features] and correspond to the values passed in `TIMES`.

<h3 id="prediction_ops"><code>prediction_ops</code></h3>

``` python
prediction_ops(
    times,
    values
)
```

Compute model predictions given input data.

#### Args:

* <b>`times`</b>: A [batch size, self.window_size] integer Tensor, the first
      self.input_window_size times in each part of the batch indicating
      input features, and the last self.output_window_size times indicating
      prediction times.
* <b>`values`</b>: A [batch size, self.input_window_size, self.num_features] Tensor
      with input features.

#### Returns:

Tuple (predicted_mean, predicted_covariance), where each element is a
Tensor with shape [batch size, self.output_window_size,
self.num_features].

<h3 id="random_model_parameters"><code>random_model_parameters</code></h3>

``` python
random_model_parameters(seed=None)
```





## Class Members

<h3 id="NORMAL_LIKELIHOOD_LOSS"><code>NORMAL_LIKELIHOOD_LOSS</code></h3>

<h3 id="SQUARED_LOSS"><code>SQUARED_LOSS</code></h3>

