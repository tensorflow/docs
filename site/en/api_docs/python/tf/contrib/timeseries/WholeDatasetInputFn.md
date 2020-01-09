page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.timeseries.WholeDatasetInputFn


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/timeseries/python/timeseries/input_pipeline.py#L578-L619">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `WholeDatasetInputFn`

Supports passing a full time series to a model for evaluation/inference.



<!-- Placeholder for "Used in" -->

Note that this `TimeSeriesInputFn` is not designed for high throughput, and
should not be used for training. It allows for sequential evaluation on a full
dataset (with sequential in-sample predictions), which then feeds naturally
into `predict_continuation_input_fn` for making out-of-sample
predictions. While this is useful for plotting and interactive use,
`RandomWindowInputFn` is better suited to training and quantitative
evaluation.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/timeseries/python/timeseries/input_pipeline.py#L598-L605">View source</a>

``` python
__init__(time_series_reader)
```

Initialize the `TimeSeriesInputFn`.


#### Args:


* <b>`time_series_reader`</b>: A TimeSeriesReader object.



## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/timeseries/python/timeseries/input_pipeline.py#L573-L575">View source</a>

``` python
__call__()
```

Call self as a function.


<h3 id="create_batch"><code>create_batch</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/timeseries/python/timeseries/input_pipeline.py#L607-L619">View source</a>

``` python
create_batch()
```

A suitable `input_fn` for an `Estimator`'s `evaluate()`.


#### Returns:

A dictionary mapping feature names to `Tensors`, each shape
prefixed by [1, data set size] (i.e. a batch size of 1).
