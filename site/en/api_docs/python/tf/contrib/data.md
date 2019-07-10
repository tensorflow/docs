page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.data



Defined in [`tensorflow/contrib/data/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/data/__init__.py).

Experimental API for building input pipelines.

This module contains experimental `Dataset` sources and transformations that can
be used in conjunction with the <a href="../../tf/data/Dataset"><code>tf.data.Dataset</code></a> API. Note that the
<a href="../../tf/contrib/data"><code>tf.contrib.data</code></a> API is not subject to the same backwards compatibility
guarantees as <a href="../../tf/data"><code>tf.data</code></a>, but we will provide deprecation advice in advance of
removing existing functionality.

See <a href="../../../../guide/datasets">Importing Data</a> for an overview.





## Classes

[`class CheckpointInputPipelineHook`](../../tf/contrib/data/CheckpointInputPipelineHook): Checkpoints input pipeline state every N steps or seconds.

[`class CsvDataset`](../../tf/contrib/data/CsvDataset): A Dataset comprising lines from one or more CSV files.

[`class RandomDataset`](../../tf/contrib/data/RandomDataset): A `Dataset` of pseudorandom values.

[`class Reducer`](../../tf/contrib/data/Reducer): A reducer is used for reducing a set of elements.

[`class SqlDataset`](../../tf/contrib/data/SqlDataset): A `Dataset` consisting of the results from a SQL query.

[`class TFRecordWriter`](../../tf/contrib/data/TFRecordWriter): Writes data to a TFRecord file.

## Functions

[`Counter(...)`](../../tf/contrib/data/Counter): Creates a `Dataset` that counts from `start` in steps of size `step`.

[`assert_element_shape(...)`](../../tf/contrib/data/assert_element_shape): Assert the shape of this `Dataset`.

[`batch_and_drop_remainder(...)`](../../tf/contrib/data/batch_and_drop_remainder): A batching transformation that omits the final small batch (if present). (deprecated)

[`bucket_by_sequence_length(...)`](../../tf/contrib/data/bucket_by_sequence_length): A transformation that buckets elements in a `Dataset` by length.

[`choose_from_datasets(...)`](../../tf/contrib/data/choose_from_datasets): Creates a dataset that deterministically chooses elements from `datasets`.

[`copy_to_device(...)`](../../tf/contrib/data/copy_to_device): A transformation that copies dataset elements to the given `target_device`.

[`dense_to_sparse_batch(...)`](../../tf/contrib/data/dense_to_sparse_batch): A transformation that batches ragged elements into <a href="../../tf/SparseTensor"><code>tf.SparseTensor</code></a>s.

[`enumerate_dataset(...)`](../../tf/contrib/data/enumerate_dataset): A transformation that enumerate the elements of a dataset.

[`get_single_element(...)`](../../tf/contrib/data/get_single_element): Returns the single element in `dataset` as a nested structure of tensors.

[`group_by_reducer(...)`](../../tf/contrib/data/group_by_reducer): A transformation that groups elements and performs a reduction.

[`group_by_window(...)`](../../tf/contrib/data/group_by_window): A transformation that groups windows of elements by key and reduces them.

[`ignore_errors(...)`](../../tf/contrib/data/ignore_errors): Creates a `Dataset` from another `Dataset` and silently ignores any errors.

[`make_batched_features_dataset(...)`](../../tf/contrib/data/make_batched_features_dataset): Returns a `Dataset` of feature dictionaries from `Example` protos.

[`make_csv_dataset(...)`](../../tf/contrib/data/make_csv_dataset): Reads CSV files into a dataset.

[`make_saveable_from_iterator(...)`](../../tf/contrib/data/make_saveable_from_iterator): Returns a SaveableObject for saving/restore iterator state using Saver.

[`map_and_batch(...)`](../../tf/contrib/data/map_and_batch): Fused implementation of `map` and `batch`.

[`padded_batch_and_drop_remainder(...)`](../../tf/contrib/data/padded_batch_and_drop_remainder): A batching and padding transformation that omits the final small batch. (deprecated)

[`parallel_interleave(...)`](../../tf/contrib/data/parallel_interleave): A parallel version of the `Dataset.interleave()` transformation.

[`prefetch_to_device(...)`](../../tf/contrib/data/prefetch_to_device): A transformation that prefetches dataset values to the given `device`.

[`read_batch_features(...)`](../../tf/contrib/data/read_batch_features): Reads batches of Examples. (deprecated)

[`rejection_resample(...)`](../../tf/contrib/data/rejection_resample): A transformation that resamples a dataset to achieve a target distribution.

[`sample_from_datasets(...)`](../../tf/contrib/data/sample_from_datasets): Samples elements at random from the datasets in `datasets`.

[`scan(...)`](../../tf/contrib/data/scan): A transformation that scans a function across an input dataset.

[`shuffle_and_repeat(...)`](../../tf/contrib/data/shuffle_and_repeat): Shuffles and repeats a Dataset returning a new permutation for each epoch.

[`sliding_window_batch(...)`](../../tf/contrib/data/sliding_window_batch): A sliding window with size of `window_size` and step of `stride`.

[`sloppy_interleave(...)`](../../tf/contrib/data/sloppy_interleave): A non-deterministic version of the `Dataset.interleave()` transformation. (deprecated)

[`unbatch(...)`](../../tf/contrib/data/unbatch): Splits elements of a dataset into multiple elements on the batch dimension.

[`unique(...)`](../../tf/contrib/data/unique): Creates a `Dataset` from another `Dataset`, discarding duplicates.

## Other Members

`AUTOTUNE`

