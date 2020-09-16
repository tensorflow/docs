description: Creates a dataset of sliding windows over a timeseries provided as array.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.timeseries_dataset_from_array" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.preprocessing.timeseries_dataset_from_array

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/preprocessing/timeseries.py#L29-L199">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a dataset of sliding windows over a timeseries provided as array.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.timeseries_dataset_from_array(
    data, targets, sequence_length, sequence_stride=1, sampling_rate=1,
    batch_size=128, shuffle=(False), seed=None, start_index=None, end_index=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function takes in a sequence of data-points gathered at
equal intervals, along with time series parameters such as
length of the sequences/windows, spacing between two sequence/windows, etc.,
to produce batches of timeseries inputs and targets.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`data`
</td>
<td>
Numpy array or eager tensor
containing consecutive data points (timesteps).
Axis 0 is expected to be the time dimension.
</td>
</tr><tr>
<td>
`targets`
</td>
<td>
Targets corresponding to timesteps in `data`.
It should have same length as `data`. `targets[i]` should be the target
corresponding to the window that starts at index `i`
(see example 2 below).
Pass None if you don't have target data (in this case the dataset will
only yield the input data).
</td>
</tr><tr>
<td>
`sequence_length`
</td>
<td>
Length of the output sequences (in number of timesteps).
</td>
</tr><tr>
<td>
`sequence_stride`
</td>
<td>
Period between successive output sequences.
For stride `s`, output samples would
start at index `data[i]`, `data[i + s]`, `data[i + 2 * s]`, etc.
</td>
</tr><tr>
<td>
`sampling_rate`
</td>
<td>
Period between successive individual timesteps
within sequences. For rate `r`, timesteps
`data[i], data[i + r], ... data[i + sequence_length]`
are used for create a sample sequence.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
Number of timeseries samples in each batch
(except maybe the last one).
</td>
</tr><tr>
<td>
`shuffle`
</td>
<td>
Whether to shuffle output samples,
or instead draw them in chronological order.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
Optional int; random seed for shuffling.
</td>
</tr><tr>
<td>
`start_index`
</td>
<td>
Optional int; data points earlier (exclusive)
than `start_index` will not be used
in the output sequences. This is useful to reserve part of the
data for test or validation.
</td>
</tr><tr>
<td>
`end_index`
</td>
<td>
Optional int; data points later (exclusive) than `end_index`
will not be used in the output sequences.
This is useful to reserve part of the data for test or validation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tf.data.Dataset instance. If `targets` was passed, the dataset yields
tuple `(batch_of_sequences, batch_of_targets)`. If not, the dataset yields
only `batch_of_sequences`.
</td>
</tr>

</table>



#### Example 1:

Consider indices `[0, 1, ... 99]`.
With `sequence_length=10,  sampling_rate=2, sequence_stride=3`,
`shuffle=False`, the dataset will yield batches of sequences
composed of the following indices:


```
First sequence:  [0  2  4  6  8 10 12 14 16 18]
Second sequence: [3  5  7  9 11 13 15 17 19 21]
Third sequence:  [6  8 10 12 14 16 18 20 22 24]
...
Last sequence:   [78 80 82 84 86 88 90 92 94 96]
```

In this case the last 3 data points are discarded since no full sequence
can be generated to include them (the next sequence would have started
at index 81, and thus its last step would have gone over 99).

Example 2: temporal regression. Consider an array `data` of scalar
values, of shape `(steps,)`. To generate a dataset that uses the past 10
timesteps to predict the next timestep, you would use:

```python
input_data = data[:-10]
targets = data[10:]
dataset = tf.keras.preprocessing.timeseries_dataset_from_array(
    input_data, targets, sequence_length=10)
for batch in dataset:
  inputs, targets = batch
  assert np.array_equal(inputs[0], data[:10])  # First sequence: steps [0-9]
  assert np.array_equal(targets[0], data[10])  # Corresponding target: step 10
  break
```