page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.timeseries.NumpyReader


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/timeseries/python/timeseries/input_pipeline.py#L223-L286">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `NumpyReader`

A time series parser for feeding Numpy arrays to a `TimeSeriesInputFn`.



<!-- Placeholder for "Used in" -->

Avoids embedding data in the graph as constants.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/timeseries/python/timeseries/input_pipeline.py#L229-L245">View source</a>

``` python
__init__(
    data,
    read_num_records_hint=4096
)
```

Numpy array input for a `TimeSeriesInputFn`.


#### Args:


* <b>`data`</b>: A dictionary mapping feature names to Numpy arrays, with two
  possible shapes (requires keys `TrainEvalFeatures.TIMES` and
  `TrainEvalFeatures.VALUES`): Univariate; `TIMES` and `VALUES` are both
    vectors of shape [series length] Multivariate; `TIMES` is a vector of
    shape [series length], `VALUES` has shape [series length x number of
    features]. In any case, `VALUES` and any exogenous features must have
    their shapes prefixed by the shape of the value corresponding to the
    `TIMES` key.
* <b>`read_num_records_hint`</b>: The maximum number of samples to read at one time,
  for efficiency.



## Methods

<h3 id="check_dataset_size"><code>check_dataset_size</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/timeseries/python/timeseries/input_pipeline.py#L247-L255">View source</a>

``` python
check_dataset_size(minimum_dataset_size)
```

Raise an error if the dataset is too small.


<h3 id="read"><code>read</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/timeseries/python/timeseries/input_pipeline.py#L257-L272">View source</a>

``` python
read()
```

Returns a large chunk of the Numpy arrays for later re-chunking.


<h3 id="read_full"><code>read_full</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/timeseries/python/timeseries/input_pipeline.py#L274-L286">View source</a>

``` python
read_full()
```

Returns `Tensor` versions of the full Numpy arrays.
