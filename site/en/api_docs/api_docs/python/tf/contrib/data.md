

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.data



Defined in [`tensorflow/contrib/data/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/data/__init__.py).

`tf.contrib.data.Dataset` API for input pipelines.

See the [Importing Data](../../../../programmers_guide/datasets) Programmer's Guide for an overview.



## Classes

[`class Dataset`](../../tf/contrib/data/Dataset): Represents a potentially large set of elements.

[`class FixedLengthRecordDataset`](../../tf/contrib/data/FixedLengthRecordDataset): A `Dataset` of fixed-length records from one or more binary files.

[`class Iterator`](../../tf/data/Iterator): Represents the state of iterating through a `Dataset`.

[`class TFRecordDataset`](../../tf/contrib/data/TFRecordDataset): A `Dataset` comprising records from one or more TFRecord files.

[`class TextLineDataset`](../../tf/contrib/data/TextLineDataset): A `Dataset` comprising lines from one or more text files.

## Functions

[`batch_and_drop_remainder(...)`](../../tf/contrib/data/batch_and_drop_remainder): A batching transformation that omits the final small batch (if present).

[`dense_to_sparse_batch(...)`](../../tf/contrib/data/dense_to_sparse_batch): A transformation that batches ragged elements into `tf.SparseTensor`s.

[`enumerate_dataset(...)`](../../tf/contrib/data/enumerate_dataset): A transformation that enumerate the elements of a dataset.

[`group_by_window(...)`](../../tf/contrib/data/group_by_window): A transformation that groups windows of elements by key and reduces them.

[`ignore_errors(...)`](../../tf/contrib/data/ignore_errors): Creates a `Dataset` from another `Dataset` and silently ignores any errors.

[`read_batch_features(...)`](../../tf/contrib/data/read_batch_features): Reads batches of Examples.

[`rejection_resample(...)`](../../tf/contrib/data/rejection_resample): A transformation that resamples a dataset to achieve a target distribution.

[`sloppy_interleave(...)`](../../tf/contrib/data/sloppy_interleave): A non-deterministic version of the `Dataset.interleave()` transformation.

[`unbatch(...)`](../../tf/contrib/data/unbatch): A Transformation which splits the elements of a dataset.

