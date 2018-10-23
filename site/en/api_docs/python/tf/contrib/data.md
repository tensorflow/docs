

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.data



Defined in [`tensorflow/contrib/data/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/data/__init__.py).

Experimental API for building input pipelines.

This module contains experimental `Dataset` sources and transformations that can
be used in conjunction with the <a href="../../tf/data/Dataset"><code>tf.data.Dataset</code></a> API. Note that the
`tf.contrib.data` API is not subject to the same backwards compatibility
guarantees as `tf.data`, but we will provide deprecation advice in advance of
removing existing functionality.

See the <a href="../../../../programmers_guide/datasets">Importing Data</a> Programmer's Guide for an overview.




## Classes

[`class SqlDataset`](../../tf/contrib/data/SqlDataset): A `Dataset` consisting of the results from a SQL query.

## Functions

[`Counter(...)`](../../tf/contrib/data/Counter): Creates a `Dataset` of a `step`-separated count startin from `start`.

[`batch_and_drop_remainder(...)`](../../tf/contrib/data/batch_and_drop_remainder): A batching transformation that omits the final small batch (if present).

[`bucket_by_sequence_length(...)`](../../tf/contrib/data/bucket_by_sequence_length): A transformation that buckets elements in a `Dataset` by length.

[`dense_to_sparse_batch(...)`](../../tf/contrib/data/dense_to_sparse_batch): A transformation that batches ragged elements into `tf.SparseTensor`s.

[`enumerate_dataset(...)`](../../tf/contrib/data/enumerate_dataset): A transformation that enumerate the elements of a dataset.

[`get_single_element(...)`](../../tf/contrib/data/get_single_element): Returns the single element in `dataset` as a nested structure of tensors.

[`group_by_window(...)`](../../tf/contrib/data/group_by_window): A transformation that groups windows of elements by key and reduces them.

[`ignore_errors(...)`](../../tf/contrib/data/ignore_errors): Creates a `Dataset` from another `Dataset` and silently ignores any errors.

[`make_batched_features_dataset(...)`](../../tf/contrib/data/make_batched_features_dataset): Returns a `Dataset` of feature dictionaries from `Example` protos.

[`make_saveable_from_iterator(...)`](../../tf/contrib/data/make_saveable_from_iterator): Returns a SaveableObject for saving/restore iterator state using Saver.

[`map_and_batch(...)`](../../tf/contrib/data/map_and_batch): Fused implementation of `map` and `batch`.

[`padded_batch_and_drop_remainder(...)`](../../tf/contrib/data/padded_batch_and_drop_remainder): A batching and padding transformation that omits the final small batch.

[`parallel_interleave(...)`](../../tf/contrib/data/parallel_interleave): A parallel version of the `Dataset.interleave()` transformation.

[`read_batch_features(...)`](../../tf/contrib/data/read_batch_features): Reads batches of Examples. (deprecated)

[`rejection_resample(...)`](../../tf/contrib/data/rejection_resample): A transformation that resamples a dataset to achieve a target distribution.

[`scan(...)`](../../tf/contrib/data/scan): A transformation that scans a function across an input dataset.

[`shuffle_and_repeat(...)`](../../tf/contrib/data/shuffle_and_repeat): Shuffles and repeats a Dataset returning a new permutation for each epoch.

[`sliding_window_batch(...)`](../../tf/contrib/data/sliding_window_batch): A sliding window with size of `window_size` and step of `stride`.

[`sloppy_interleave(...)`](../../tf/contrib/data/sloppy_interleave): A non-deterministic version of the `Dataset.interleave()` transformation. (deprecated)

[`unbatch(...)`](../../tf/contrib/data/unbatch): A Transformation which splits the elements of a dataset.

