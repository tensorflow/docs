description: <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> API for input pipelines.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.data" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.data

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



<a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> API for input pipelines.


See [Importing Data](https://tensorflow.org/guide/data) for an overview.

## Modules

[`experimental`](../../../tf/compat/v1/data/experimental.md) module: Experimental API for building input pipelines.

## Classes

[`class Dataset`](../../../tf/compat/v1/data/Dataset.md): Represents a potentially large set of elements.

[`class DatasetSpec`](../../../tf/data/DatasetSpec.md): Type specification for <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.

[`class FixedLengthRecordDataset`](../../../tf/compat/v1/data/FixedLengthRecordDataset.md): A `Dataset` of fixed-length records from one or more binary files.

[`class Iterator`](../../../tf/compat/v1/data/Iterator.md): Represents the state of iterating through a `Dataset`.

[`class Options`](../../../tf/data/Options.md): Represents options for tf.data.Dataset.

[`class TFRecordDataset`](../../../tf/compat/v1/data/TFRecordDataset.md): A `Dataset` comprising records from one or more TFRecord files.

[`class TextLineDataset`](../../../tf/compat/v1/data/TextLineDataset.md): A `Dataset` comprising lines from one or more text files.

## Functions

[`get_output_classes(...)`](../../../tf/compat/v1/data/get_output_classes.md): Returns the output classes of a `Dataset` or `Iterator` elements.

[`get_output_shapes(...)`](../../../tf/compat/v1/data/get_output_shapes.md): Returns the output shapes of a `Dataset` or `Iterator` elements.

[`get_output_types(...)`](../../../tf/compat/v1/data/get_output_types.md): Returns the output shapes of a `Dataset` or `Iterator` elements.

[`make_initializable_iterator(...)`](../../../tf/compat/v1/data/make_initializable_iterator.md): Creates a <a href="../../../tf/compat/v1/data/Iterator.md"><code>tf.compat.v1.data.Iterator</code></a> for enumerating the elements of a dataset.

[`make_one_shot_iterator(...)`](../../../tf/compat/v1/data/make_one_shot_iterator.md): Creates a <a href="../../../tf/compat/v1/data/Iterator.md"><code>tf.compat.v1.data.Iterator</code></a> for enumerating dataset elements.

