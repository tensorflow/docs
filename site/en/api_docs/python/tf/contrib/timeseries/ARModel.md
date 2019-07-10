page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.timeseries.ARModel

## Class `ARModel`

Auto-regressive model, both linear and non-linear.





Defined in [`contrib/timeseries/python/timeseries/ar_model.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/timeseries/python/timeseries/ar_model.py).

<!-- Placeholder for "Used in" -->

Features to the model include time and values of input_window_size timesteps,
and times for output_window_size timesteps. These are passed through a
configurable prediction model, and then fed to a loss function (e.g. squared
loss).

Note that this class can also be used to regress against time only by setting
the input_window_size to zero.

Each periodicity in the `periodicities` arg is divided by the
`num_time_buckets` into time buckets that are represented as features added
to the model.

A good heuristic for picking an appropriate periodicity for a given data set
would be the length of cycles in the data. For example, energy usage in a
home is typically cyclic each day. If the time feature in a home energy
usage dataset is in the unit of hours, then 24 would be an appropriate
periodicity. Similarly, a good heuristic for `num_time_buckets` is how often
the data is expected to change within the cycle. For the aforementioned home
energy usage dataset and periodicity of 24, then 48 would be a reasonable
value if usage is expected to change every half hour.

Each feature's value for a given example with time t is the difference
between t and the start of the time bucket it falls under. If it doesn't fall
under a feature's associated time bucket, then that feature's value is zero.

For example: if `periodicities` = (9, 12) and `num_time_buckets` = 3, then 6
features would be added to the model, 3 for periodicity 9 and 3 for
periodicity 12.

For an example data point where t = 17:
- It's in the 3rd time bucket for periodicity 9 (2nd period is 9-18 and 3rd
  time bucket is 15-18)
- It's in the 2nd time bucket for periodicity 12 (2nd period is 12-24 and
  2nd time bucket is between 16-20).

Therefore the 6 added features for this row with t = 17 would be:

# Feature name (periodicity#_timebucket#), feature value
P9_T1, 0 # not in first time bucket
P9_T2, 0 # not in second time bucket
P9_T3, 2 # 17 - 15 since 15 is the start of the 3rd time bucket
P12_T1, 0 # not in first time bucket
P12_T2, 1 # 17 - 16 since 16 is the start of the 2nd time bucket
P12_T3, 0 # not in third time bucket

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    periodicities,
    input_window_size,
    output_window_size,
    num_features,
    prediction_model_factory=FlatPredictionModel,
    num_time_buckets=10,
    loss=NORMAL_LIKELIHOOD_LOSS,
    exogenous_feature_columns=None
)
```

Constructs an auto-regressive model.


#### Args:


* <b>`periodicities`</b>: periodicities of the input data, in the same units as the
  time feature (for example 24 if feeding hourly data with a daily
  periodicity, or 60 * 24 if feeding minute-level data with daily
  periodicity). Note this can be a single value or a list of values for
  multiple periodicities.
* <b>`input_window_size`</b>: Number of past time steps of data to look at when doing
  the regression.
* <b>`output_window_size`</b>: Number of future time steps to predict. Note that
  setting it to > 1 empirically seems to give a better fit.
* <b>`num_features`</b>: number of input features per time step.
* <b>`prediction_model_factory`</b>: A callable taking arguments `num_features`,
  `input_window_size`, and `output_window_size` and returning a
  <a href="../../../tf/keras/Model"><code>tf.keras.Model</code></a>. The `Model`'s `call()` takes two arguments: an input
  window and an output window, and returns a dictionary of predictions.
  See `FlatPredictionModel` for an example. Example usage:

>     prediction_model_factory=functools.partial( FlatPredictionModel,
>     hidden_layer_sizes=[10, 10])) ```
>     
>     The default model computes predictions as a linear function of flattened
>     input and output windows.
>     <b>`num_time_buckets`</b>: Number of buckets into which to divide (time %
>     periodicity). This value multiplied by the number of periodicities is
>     the number of time features added to the model.
>     <b>`loss`</b>: Loss function to use for training. Currently supported values are
>     SQUARED_LOSS and NORMAL_LIKELIHOOD_LOSS. Note that for
>     NORMAL_LIKELIHOOD_LOSS, we train the covariance term as well. For
>     SQUARED_LOSS, the evaluation loss is reported based on un-scaled
>     observations and predictions, while the training loss is computed on
>     normalized data (if input statistics are available).
>     <b>`exogenous_feature_columns`</b>: A list of <a href="../../../tf/feature_column"><code>tf.feature_column</code></a>s (for example
>     <a href="../../../tf/feature_column/embedding_column"><code>tf.feature_column.embedding_column</code></a>) corresponding to
>     features which provide extra information to the model but are not part
>     of the series to be predicted.
>     
>     
>     
>      Properties
>     
>     3 id="exogenous_feature_columns"><code>exogenous_feature_columns</code></h3>
>     
>     f.feature_colum`s for features which are not predicted.
>     
>     
>     
>     
>      Methods
>     
>     3 id="define_loss"><code>define_loss</code></h3>
>     
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
  TrainEvalFeatures.TIMES: A [batch size x window size] integer Tensor
      with times for each observation. If there is no artificial chunking,
      the window size is simply the length of the time series.
  TrainEvalFeatures.VALUES: A [batch size x window size x num features]
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
  PredictionFeatures.TIMES: A [batch size, predict window size]
    integer Tensor of times, after the window of data indicated by
    `STATE_TUPLE`, to make predictions for.
  PredictionFeatures.STATE_TUPLE: A tuple of (times, values), times with
    shape [batch size, self.input_window_size], values with shape [batch
    size, self.input_window_size, self.num_features] representing a
    segment of the time series before `TIMES`. This data is used
    to start of the autoregressive computation. This should have data for
    at least self.input_window_size timesteps.
  And any exogenous features, with shapes prefixed by shape of `TIMES`.

#### Returns:

A dictionary with keys, "mean", "covariance". The
values are Tensors of shape [batch_size, predict window size,
num_features] and correspond to the values passed in `TIMES`.


<h3 id="prediction_ops"><code>prediction_ops</code></h3>

``` python
prediction_ops(
    times,
    values,
    exogenous_regressors
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
* <b>`exogenous_regressors`</b>: A [batch size, self.window_size,
    self.exogenous_size] Tensor with exogenous features.

#### Returns:

Tuple (predicted_mean, predicted_covariance), where each element is a
Tensor with shape [batch size, self.output_window_size,
self.num_features].


<h3 id="random_model_parameters"><code>random_model_parameters</code></h3>

``` python
random_model_parameters(seed=None)
```






## Class Members

* `NORMAL_LIKELIHOOD_LOSS = 'normal_likelihood_loss'` <a id="NORMAL_LIKELIHOOD_LOSS"></a>
* `SQUARED_LOSS = 'squared_loss'` <a id="SQUARED_LOSS"></a>
