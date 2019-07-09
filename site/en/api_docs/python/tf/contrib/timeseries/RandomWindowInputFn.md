page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.timeseries.RandomWindowInputFn

## Class `RandomWindowInputFn`





Defined in [`tensorflow/contrib/timeseries/python/timeseries/input_pipeline.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/timeseries/python/timeseries/input_pipeline.py).

Wraps a `TimeSeriesReader` to create random batches of windows.

Tensors are first collected into sequential windows (in a windowing queue
created by <a href="../../../tf/train/batch"><code>tf.train.batch</code></a>, based on the order returned from
`time_series_reader`), then these windows are randomly batched (in a
`RandomShuffleQueue`), the Tensors returned by `create_batch` having shapes
prefixed by [`batch_size`, `window_size`].

This `TimeSeriesInputFn` is useful for both training and quantitative
evaluation (but be sure to run several epochs for sequential models such as
`StructuralEnsembleRegressor` to completely flush stale state left over from
training). For qualitative evaluation or when preparing for predictions, use
`WholeDatasetInputFn`.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    time_series_reader,
    window_size,
    batch_size,
    queue_capacity_multiplier=1000,
    shuffle_min_after_dequeue_multiplier=2,
    discard_out_of_order=True,
    discard_consecutive_batches_limit=1000,
    jitter=True,
    num_threads=2,
    shuffle_seed=None
)
```

Configure the RandomWindowInputFn.

#### Args:

* <b>`time_series_reader`</b>: A TimeSeriesReader object.
* <b>`window_size`</b>: The number of examples to keep together sequentially. This
    controls the length of truncated backpropagation: smaller values mean
    less sequential computation, which can lead to faster training, but
    create a coarser approximation to the gradient (which would ideally be
    computed by a forward pass over the entire sequence in order).
* <b>`batch_size`</b>: The number of windows to place together in a batch. Larger
    values will lead to more stable gradients during training.
* <b>`queue_capacity_multiplier`</b>: The capacity for the queues used to create
    batches, specified as a multiple of `batch_size` (for
    RandomShuffleQueue) and `batch_size * window_size` (for the
    FIFOQueue). Controls the maximum number of windows stored. Should be
    greater than `shuffle_min_after_dequeue_multiplier`.
* <b>`shuffle_min_after_dequeue_multiplier`</b>: The minimum number of windows in the
    RandomShuffleQueue after a dequeue, which controls the amount of entropy
    introduced during batching. Specified as a multiple of `batch_size`.
* <b>`discard_out_of_order`</b>: If True, windows of data which have times which
    decrease (a higher time followed by a lower time) are discarded. If
    False, the window and associated features are instead sorted so that
    times are non-decreasing. Discarding is typically faster, as models do
    not have to deal with artificial gaps in the data. However, discarding
    does create a bias where the beginnings and endings of files are
    under-sampled.
* <b>`discard_consecutive_batches_limit`</b>: Raise an OutOfRangeError if more than
    this number of batches are discarded without a single non-discarded
    window (prevents infinite looping when the dataset is too small).
* <b>`jitter`</b>: If True, randomly discards examples between some windows in order
    to avoid deterministic chunking patterns. This is important for models
    like AR which may otherwise overfit a fixed chunking.
* <b>`num_threads`</b>: Use this number of threads for queues. Setting a value of 1
    removes one source of non-determinism (and in combination with
    shuffle_seed should provide deterministic windowing).
* <b>`shuffle_seed`</b>: A seed for window shuffling. The default value of None
    provides random behavior. With `shuffle_seed` set and
    `num_threads=1`, provides deterministic behavior.

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__()
```



<h3 id="create_batch"><code>create_batch</code></h3>

``` python
create_batch()
```

Create queues to window and batch time series data.

#### Returns:

A dictionary of Tensors corresponding to the output of `self._reader`
(from the `time_series_reader` constructor argument), each with shapes
prefixed by [`batch_size`, `window_size`].



