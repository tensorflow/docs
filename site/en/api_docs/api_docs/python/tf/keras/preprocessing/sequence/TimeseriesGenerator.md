

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.sequence.TimeseriesGenerator

## Class `TimeseriesGenerator`

Inherits From: [`Sequence`](../../../../tf/keras/utils/Sequence)



Defined in [`tensorflow/python/keras/preprocessing/sequence.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/preprocessing/sequence.py).

Utility class for generating batches of temporal data.

This class takes in a sequence of data-points gathered at
equal intervals, along with time series parameters such as
stride, length of history, etc., to produce batches for
training/validation.

#### Arguments:

* <b>`data`</b>: Indexable generator (such as list or Numpy array)
        containing consecutive data points (timesteps).
        The data should be at 2D, and axis 0 is expected
        to be the time dimension.
* <b>`targets`</b>: Targets corresponding to timesteps in `data`.
        It should have same length as `data`.
* <b>`length`</b>: Length of the output sequences (in number of timesteps).
* <b>`sampling_rate`</b>: Period between successive individual timesteps
        within sequences. For rate `r`, timesteps
        `data[i]`, `data[i-r]`, ... `data[i - length]`
        are used for create a sample sequence.
* <b>`stride`</b>: Period between successive output sequences.
        For stride `s`, consecutive output samples would
        be centered around `data[i]`, `data[i+s]`, `data[i+2*s]`, etc.
    start_index, end_index: Data points earlier than `start_index`
        or later than `end_index` will not be used in the output sequences.
        This is useful to reserve part of the data for test or validation.
* <b>`shuffle`</b>: Whether to shuffle output samples,
        or instead draw them in chronological order.
* <b>`reverse`</b>: Boolean: if `true`, timesteps in each output sample will be
        in reverse chronological order.
* <b>`batch_size`</b>: Number of timeseries samples in each batch
        (except maybe the last one).


#### Returns:

    A [Sequence](/utils/#sequence) instance.

Examples:

```python
from keras.preprocessing.sequence import TimeseriesGenerator
import numpy as np

data = np.array([[i] for i in range(50)])
targets = np.array([[i] for i in range(50)])

data_gen = TimeseriesGenerator(data, targets,
                               length=10, sampling_rate=2,
                               batch_size=2)
assert len(data_gen) == 20

batch_0 = data_gen[0]
x, y = batch_0
assert np.array_equal(x,
                      np.array([[[0], [2], [4], [6], [8]],
                                [[1], [3], [5], [7], [9]]]))
assert np.array_equal(y,
                      np.array([[10], [11]]))
```

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    data,
    targets,
    length,
    sampling_rate=1,
    stride=1,
    start_index=0,
    end_index=None,
    shuffle=False,
    reverse=False,
    batch_size=128
)
```



<h3 id="__getitem__"><code>__getitem__</code></h3>

``` python
__getitem__(index)
```



<h3 id="__iter__"><code>__iter__</code></h3>

``` python
__iter__()
```

Creates an infinite generator that iterate over the Sequence.

#### Yields:

Sequence items.

<h3 id="__len__"><code>__len__</code></h3>

``` python
__len__()
```



<h3 id="on_epoch_end"><code>on_epoch_end</code></h3>

``` python
on_epoch_end()
```

Method called at the end of every epoch.
    



