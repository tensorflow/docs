page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.data

Experimental API for building input pipelines.



Defined in [`contrib/data/__init__.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/data/__init__.py).

<!-- Placeholder for "Used in" -->

This module contains experimental `Dataset` sources and transformations that can
be used in conjunction with the <a href="../../tf/data/Dataset"><code>tf.data.Dataset</code></a> API. Note that the
<a href="../../tf/contrib/data"><code>tf.contrib.data</code></a> API is not subject to the same backwards compatibility
guarantees as <a href="../../tf/data"><code>tf.data</code></a>, but we will provide deprecation advice in advance of
removing existing functionality.

See [Importing Data](https://tensorflow.org/guide/datasets) for an overview.




## Classes

[`class CheckpointInputPipelineHook`](../../tf/contrib/data/CheckpointInputPipelineHook): Checkpoints input pipeline state every N steps or seconds.

[`class CsvDataset`](../../tf/contrib/data/CsvDataset): A Dataset comprising lines from one or more CSV files.

[`class LMDBDataset`](../../tf/contrib/data/LMDBDataset): A LMDB Dataset that reads the lmdb file.

[`class Optional`](../../tf/data/experimental/Optional): Wraps a nested structure of tensors that may/may not be present at runtime.

[`class RandomDataset`](../../tf/contrib/data/RandomDataset): A `Dataset` of pseudorandom values.

[`class Reducer`](../../tf/contrib/data/Reducer): A reducer is used for reducing a set of elements.

[`class SqlDataset`](../../tf/contrib/data/SqlDataset): A `Dataset` consisting of the results from a SQL query.

[`class TFRecordWriter`](../../tf/contrib/data/TFRecordWriter): Writes data to a TFRecord file.

## Functions

[`Counter(...)`](../../tf/contrib/data/Counter): Creates a `Dataset` that counts from `start` in steps of size `step`. (deprecated)

[`assert_element_shape(...)`](../../tf/contrib/data/assert_element_shape): Assert the shape of this `Dataset`.

[`batch_and_drop_remainder(...)`](../../tf/contrib/data/batch_and_drop_remainder): A batching transformation that omits the final small batch (if present). (deprecated)

[`bucket_by_sequence_length(...)`](../../tf/contrib/data/bucket_by_sequence_length): A transformation that buckets elements in a `Dataset` by length. (deprecated)

[`choose_from_datasets(...)`](../../tf/contrib/data/choose_from_datasets): Creates a dataset that deterministically chooses elements from `datasets`. (deprecated)

[`copy_to_device(...)`](../../tf/contrib/data/copy_to_device): A transformation that copies dataset elements to the given `target_device`. (deprecated)

[`dense_to_sparse_batch(...)`](../../tf/contrib/data/dense_to_sparse_batch): A transformation that batches ragged elements into <a href="../../tf/sparse/SparseTensor"><code>tf.SparseTensor</code></a>s. (deprecated)

[`enumerate_dataset(...)`](../../tf/contrib/data/enumerate_dataset): A transformation that enumerate the elements of a dataset. (deprecated)

[`get_next_as_optional(...)`](../../tf/data/experimental/get_next_as_optional): Returns an `Optional` that contains the next value from the iterator.

[`get_single_element(...)`](../../tf/contrib/data/get_single_element): Returns the single element in `dataset` as a nested structure of tensors. (deprecated)

[`group_by_reducer(...)`](../../tf/contrib/data/group_by_reducer): A transformation that groups elements and performs a reduction. (deprecated)

[`group_by_window(...)`](../../tf/contrib/data/group_by_window): A transformation that groups windows of elements by key and reduces them. (deprecated)

[`ignore_errors(...)`](../../tf/contrib/data/ignore_errors): Creates a `Dataset` from another `Dataset` and silently ignores any errors. (deprecated)

[`make_batched_features_dataset(...)`](../../tf/contrib/data/make_batched_features_dataset): Returns a `Dataset` of feature dictionaries from `Example` protos. (deprecated)

[`make_csv_dataset(...)`](../../tf/contrib/data/make_csv_dataset): Reads CSV files into a dataset. (deprecated)

[`make_saveable_from_iterator(...)`](../../tf/contrib/data/make_saveable_from_iterator): Returns a SaveableObject for saving/restore iterator state using Saver. (deprecated)

[`map_and_batch(...)`](../../tf/contrib/data/map_and_batch): Fused implementation of `map` and `batch`. (deprecated)

[`padded_batch_and_drop_remainder(...)`](../../tf/contrib/data/padded_batch_and_drop_remainder): A batching and padding transformation that omits the final small batch. (deprecated)

[`parallel_interleave(...)`](../../tf/contrib/data/parallel_interleave): A parallel version of the `Dataset.interleave()` transformation. (deprecated)

[`parse_example_dataset(...)`](../../tf/contrib/data/parse_example_dataset): A transformation that parses `Example` protos into a `dict` of tensors. (deprecated)

[`prefetch_to_device(...)`](../../tf/contrib/data/prefetch_to_device): A transformation that prefetches dataset values to the given `device`. (deprecated)

[`read_batch_features(...)`](../../tf/contrib/data/read_batch_features): Reads batches of Examples. (deprecated)

[`reduce_dataset(...)`](../../tf/contrib/data/reduce_dataset): Returns the result of reducing the `dataset` using `reducer`. (deprecated)

[`rejection_resample(...)`](../../tf/contrib/data/rejection_resample): A transformation that resamples a dataset to achieve a target distribution. (deprecated)

[`sample_from_datasets(...)`](../../tf/contrib/data/sample_from_datasets): Samples elements at random from the datasets in `datasets`. (deprecated)

[`scan(...)`](../../tf/contrib/data/scan): A transformation that scans a function across an input dataset. (deprecated)

[`shuffle_and_repeat(...)`](../../tf/contrib/data/shuffle_and_repeat): Shuffles and repeats a Dataset returning a new permutation for each epoch. (deprecated)

[`sliding_window_batch(...)`](../../tf/contrib/data/sliding_window_batch): A sliding window over a dataset. (deprecated) (deprecated arguments)

[`sloppy_interleave(...)`](../../tf/contrib/data/sloppy_interleave): A non-deterministic version of the `Dataset.interleave()` transformation. (deprecated)

[`unbatch(...)`](../../tf/contrib/data/unbatch): Splits elements of a dataset into multiple elements on the batch dimension. (deprecated)

[`unique(...)`](../../tf/contrib/data/unique): Creates a `Dataset` from another `Dataset`, discarding duplicates. (deprecated)

## Other Members

* `AUTOTUNE = -1` <a id="AUTOTUNE"></a>
