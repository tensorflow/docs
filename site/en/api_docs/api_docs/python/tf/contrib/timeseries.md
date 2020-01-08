

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.timeseries



Defined in [`tensorflow/contrib/timeseries/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/timeseries/__init__.py).

A time series library in TensorFlow (TFTS).





## Modules

[`saved_model_utils`](../../tf/contrib/timeseries/saved_model_utils) module: Convenience functions for working with time series saved_models.

## Classes

[`class ARModel`](../../tf/contrib/timeseries/ARModel): Auto-regressive model, both linear and non-linear.

[`class ARRegressor`](../../tf/contrib/timeseries/ARRegressor): An Estimator for an (optionally non-linear) autoregressive model.

[`class CSVReader`](../../tf/contrib/timeseries/CSVReader): Reads from a collection of CSV-formatted files.

[`class FilteringResults`](../../tf/contrib/timeseries/FilteringResults): Keys returned from evaluation/filtering.

[`class NumpyReader`](../../tf/contrib/timeseries/NumpyReader): A time series parser for feeding Numpy arrays to a `TimeSeriesInputFn`.

[`class RandomWindowInputFn`](../../tf/contrib/timeseries/RandomWindowInputFn): Wraps a `TimeSeriesReader` to create random batches of windows.

[`class StructuralEnsembleRegressor`](../../tf/contrib/timeseries/StructuralEnsembleRegressor): An Estimator for structural time series models.

[`class TrainEvalFeatures`](../../tf/contrib/timeseries/TrainEvalFeatures): Feature names used during training and evaluation.

[`class WholeDatasetInputFn`](../../tf/contrib/timeseries/WholeDatasetInputFn): Supports passing a full time series to a model for evaluation/inference.

## Functions

[`predict_continuation_input_fn(...)`](../../tf/contrib/timeseries/predict_continuation_input_fn): An Estimator input_fn for running predict() after evaluate().

