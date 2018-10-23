

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.data



Defined in [`tensorflow/contrib/data/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/data/__init__.py).

`tf.contrib.data.Dataset` API for input pipelines.

See the <a href="../../../../programmers_guide/datasets">Importing Data</a> Programmer's Guide for an overview.




## Classes

[`class Dataset`](../../tf/contrib/data/Dataset): Represents a potentially large set of elements.

[`class FixedLengthRecordDataset`](../../tf/contrib/data/FixedLengthRecordDataset): A `Dataset` of fixed-length records from one or more binary files.

[`class Iterator`](../../tf/data/Iterator): Represents the state of iterating through a `Dataset`.

[`class TFRecordDataset`](../../tf/contrib/data/TFRecordDataset): A `Dataset` comprising records from one or more TFRecord files.

[`class TextLineDataset`](../../tf/contrib/data/TextLineDataset): A `Dataset` comprising lines from one or more text files.

## Functions

[`Counter(...)`](../../tf/contrib/data/Counter): Creates a `Dataset` of a `step`-separated count startin from `start`.

[`batch_and_drop_remainder(...)`](../../tf/contrib/data/batch_and_drop_remainder): A batching transformation that omits the final small batch (if present).

[`dense_to_sparse_batch(...)`](../../tf/contrib/data/dense_to_sparse_batch): A transformation that batches ragged elements into `tf.SparseTensor`s.

[`enumerate_dataset(...)`](../../tf/contrib/data/enumerate_dataset): A transformation that enumerate the elements of a dataset.

[`get_single_element(...)`](../../tf/contrib/data/get_single_element): Returns the single element in `dataset` as a nested structure of tensors.

[`group_by_window(...)`](../../tf/contrib/data/group_by_window): A transformation that groups windows of elements by key and reduces them.

[`ignore_errors(...)`](../../tf/contrib/data/ignore_errors): Creates a `Dataset` from another `Dataset` and silently ignores any errors.

[`make_saveable_from_iterator(...)`](../../tf/contrib/data/make_saveable_from_iterator): Returns a SaveableObject for saving/restore iterator state using Saver.

[`padded_batch_and_drop_remainder(...)`](../../tf/contrib/data/padded_batch_and_drop_remainder): A batching and padding transformation that omits the final small batch.

[`parallel_interleave(...)`](../../tf/contrib/data/parallel_interleave): A parallel version of the `Dataset.interleave()` transformation.

[`read_batch_features(...)`](../../tf/contrib/data/read_batch_features): Reads batches of Examples.

[`rejection_resample(...)`](../../tf/contrib/data/rejection_resample): A transformation that resamples a dataset to achieve a target distribution.

[`scan(...)`](../../tf/contrib/data/scan): A transformation that scans a function across an input dataset.

[`sloppy_interleave(...)`](../../tf/contrib/data/sloppy_interleave): A non-deterministic version of the `Dataset.interleave()` transformation. (deprecated)

[`unbatch(...)`](../../tf/contrib/data/unbatch): A Transformation which splits the elements of a dataset.

