description: Experimental API for building input pipelines.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.data.experimental" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="AUTOTUNE"/>
<meta itemprop="property" content="INFINITE_CARDINALITY"/>
<meta itemprop="property" content="UNKNOWN_CARDINALITY"/>
</div>

# Module: tf.compat.v1.data.experimental

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Experimental API for building input pipelines.


This module contains experimental `Dataset` sources and transformations that can
be used in conjunction with the <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> API. Note that the
<a href="../../../../tf/data/experimental.md"><code>tf.data.experimental</code></a> API is not subject to the same backwards compatibility
guarantees as <a href="../../../../tf/data.md"><code>tf.data</code></a>, but we will provide deprecation advice in advance of
removing existing functionality.

See [Importing Data](https://tensorflow.org/guide/datasets) for an overview.




## Classes

[`class AutoShardPolicy`](../../../../tf/data/experimental/AutoShardPolicy.md): Represents the type of auto-sharding we enable.

[`class CheckpointInputPipelineHook`](../../../../tf/data/experimental/CheckpointInputPipelineHook.md): Checkpoints input pipeline state every N steps or seconds.

[`class CsvDataset`](../../../../tf/compat/v1/data/experimental/CsvDataset.md): A Dataset comprising lines from one or more CSV files.

[`class DatasetStructure`](../../../../tf/data/DatasetSpec.md): Type specification for <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.

[`class DistributeOptions`](../../../../tf/data/experimental/DistributeOptions.md): Represents options for distributed data processing.

[`class MapVectorizationOptions`](../../../../tf/data/experimental/MapVectorizationOptions.md): Represents options for the MapVectorization optimization.

[`class OptimizationOptions`](../../../../tf/data/experimental/OptimizationOptions.md): Represents options for dataset optimizations.

[`class Optional`](../../../../tf/data/experimental/Optional.md): Wraps a value that may/may not be present at runtime.

[`class OptionalStructure`](../../../../tf/OptionalSpec.md): Represents an optional potentially containing a structured value.

[`class RandomDataset`](../../../../tf/compat/v1/data/experimental/RandomDataset.md): A `Dataset` of pseudorandom values.

[`class Reducer`](../../../../tf/data/experimental/Reducer.md): A reducer is used for reducing a set of elements.

[`class SqlDataset`](../../../../tf/compat/v1/data/experimental/SqlDataset.md): A `Dataset` consisting of the results from a SQL query.

[`class StatsAggregator`](../../../../tf/compat/v1/data/experimental/StatsAggregator.md): A stateful resource that aggregates statistics from one or more iterators.

[`class StatsOptions`](../../../../tf/data/experimental/StatsOptions.md): Represents options for collecting dataset stats using `StatsAggregator`.

[`class Structure`](../../../../tf/TypeSpec.md): Specifies a TensorFlow value type.

[`class TFRecordWriter`](../../../../tf/data/experimental/TFRecordWriter.md): Writes a dataset to a TFRecord file.

[`class ThreadingOptions`](../../../../tf/data/experimental/ThreadingOptions.md): Represents options for dataset threading.

## Functions

[`Counter(...)`](../../../../tf/compat/v1/data/experimental/Counter.md): Creates a `Dataset` that counts from `start` in steps of size `step`.

[`RaggedTensorStructure(...)`](../../../../tf/compat/v1/data/experimental/RaggedTensorStructure.md): DEPRECATED FUNCTION

[`SparseTensorStructure(...)`](../../../../tf/compat/v1/data/experimental/SparseTensorStructure.md): DEPRECATED FUNCTION

[`TensorArrayStructure(...)`](../../../../tf/compat/v1/data/experimental/TensorArrayStructure.md): DEPRECATED FUNCTION

[`TensorStructure(...)`](../../../../tf/compat/v1/data/experimental/TensorStructure.md): DEPRECATED FUNCTION

[`assert_cardinality(...)`](../../../../tf/data/experimental/assert_cardinality.md): Asserts the cardinality of the input dataset.

[`bucket_by_sequence_length(...)`](../../../../tf/data/experimental/bucket_by_sequence_length.md): A transformation that buckets elements in a `Dataset` by length.

[`bytes_produced_stats(...)`](../../../../tf/data/experimental/bytes_produced_stats.md): Records the number of bytes produced by each element of the input dataset.

[`cardinality(...)`](../../../../tf/data/experimental/cardinality.md): Returns the cardinality of `dataset`, if known.

[`choose_from_datasets(...)`](../../../../tf/compat/v1/data/experimental/choose_from_datasets.md): Creates a dataset that deterministically chooses elements from `datasets`.

[`copy_to_device(...)`](../../../../tf/data/experimental/copy_to_device.md): A transformation that copies dataset elements to the given `target_device`.

[`dense_to_ragged_batch(...)`](../../../../tf/data/experimental/dense_to_ragged_batch.md): A transformation that batches ragged elements into <a href="../../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>s.

[`dense_to_sparse_batch(...)`](../../../../tf/data/experimental/dense_to_sparse_batch.md): A transformation that batches ragged elements into <a href="../../../../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a>s.

[`enumerate_dataset(...)`](../../../../tf/data/experimental/enumerate_dataset.md): A transformation that enumerates the elements of a dataset. (deprecated)

[`from_variant(...)`](../../../../tf/data/experimental/from_variant.md): Constructs a dataset from the given variant and structure.

[`get_next_as_optional(...)`](../../../../tf/data/experimental/get_next_as_optional.md): Returns an `Optional` that contains the next value from the iterator.

[`get_single_element(...)`](../../../../tf/data/experimental/get_single_element.md): Returns the single element in `dataset` as a nested structure of tensors.

[`get_structure(...)`](../../../../tf/data/experimental/get_structure.md): Returns the type specification of an element of a `Dataset` or `Iterator`.

[`group_by_reducer(...)`](../../../../tf/data/experimental/group_by_reducer.md): A transformation that groups elements and performs a reduction.

[`group_by_window(...)`](../../../../tf/data/experimental/group_by_window.md): A transformation that groups windows of elements by key and reduces them.

[`ignore_errors(...)`](../../../../tf/data/experimental/ignore_errors.md): Creates a `Dataset` from another `Dataset` and silently ignores any errors.

[`latency_stats(...)`](../../../../tf/data/experimental/latency_stats.md): Records the latency of producing each element of the input dataset.

[`make_batched_features_dataset(...)`](../../../../tf/compat/v1/data/experimental/make_batched_features_dataset.md): Returns a `Dataset` of feature dictionaries from `Example` protos.

[`make_csv_dataset(...)`](../../../../tf/compat/v1/data/experimental/make_csv_dataset.md): Reads CSV files into a dataset.

[`make_saveable_from_iterator(...)`](../../../../tf/data/experimental/make_saveable_from_iterator.md): Returns a SaveableObject for saving/restoring iterator state using Saver.

[`map_and_batch(...)`](../../../../tf/data/experimental/map_and_batch.md): Fused implementation of `map` and `batch`. (deprecated)

[`map_and_batch_with_legacy_function(...)`](../../../../tf/compat/v1/data/experimental/map_and_batch_with_legacy_function.md): Fused implementation of `map` and `batch`. (deprecated)

[`parallel_interleave(...)`](../../../../tf/data/experimental/parallel_interleave.md): A parallel version of the `Dataset.interleave()` transformation. (deprecated)

[`parse_example_dataset(...)`](../../../../tf/data/experimental/parse_example_dataset.md): A transformation that parses `Example` protos into a `dict` of tensors.

[`prefetch_to_device(...)`](../../../../tf/data/experimental/prefetch_to_device.md): A transformation that prefetches dataset values to the given `device`.

[`rejection_resample(...)`](../../../../tf/data/experimental/rejection_resample.md): A transformation that resamples a dataset to achieve a target distribution.

[`sample_from_datasets(...)`](../../../../tf/compat/v1/data/experimental/sample_from_datasets.md): Samples elements at random from the datasets in `datasets`.

[`scan(...)`](../../../../tf/data/experimental/scan.md): A transformation that scans a function across an input dataset.

[`shuffle_and_repeat(...)`](../../../../tf/data/experimental/shuffle_and_repeat.md): Shuffles and repeats a Dataset, reshuffling with each repetition. (deprecated)

[`take_while(...)`](../../../../tf/data/experimental/take_while.md): A transformation that stops dataset iteration based on a `predicate`.

[`to_variant(...)`](../../../../tf/data/experimental/to_variant.md): Returns a variant representing the given dataset.

[`unbatch(...)`](../../../../tf/data/experimental/unbatch.md): Splits elements of a dataset into multiple elements on the batch dimension. (deprecated)

[`unique(...)`](../../../../tf/data/experimental/unique.md): Creates a `Dataset` from another `Dataset`, discarding duplicates.

## Other Members

* `AUTOTUNE = -1` <a id="AUTOTUNE"></a>
* `INFINITE_CARDINALITY = -1` <a id="INFINITE_CARDINALITY"></a>
* `UNKNOWN_CARDINALITY = -2` <a id="UNKNOWN_CARDINALITY"></a>
