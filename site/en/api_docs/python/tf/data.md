page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.data


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/data">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



<a href="../tf/data/Dataset"><code>tf.data.Dataset</code></a> API for input pipelines.

<!-- Placeholder for "Used in" -->

See [Importing Data](https://tensorflow.org/guide/datasets) for an overview.

## Modules

[`experimental`](../tf/data/experimental) module: Experimental API for building input pipelines.

## Classes

[`class Dataset`](../tf/data/Dataset): Represents a potentially large set of elements.

[`class DatasetSpec`](../tf/data/DatasetSpec): Type specification for <a href="../tf/data/Dataset"><code>tf.data.Dataset</code></a>.

[`class FixedLengthRecordDataset`](../tf/data/FixedLengthRecordDataset): A `Dataset` of fixed-length records from one or more binary files.

[`class Iterator`](../tf/data/Iterator): Represents the state of iterating through a `Dataset`.

[`class Options`](../tf/data/Options): Represents options for tf.data.Dataset.

[`class TFRecordDataset`](../tf/data/TFRecordDataset): A `Dataset` comprising records from one or more TFRecord files.

[`class TextLineDataset`](../tf/data/TextLineDataset): A `Dataset` comprising lines from one or more text files.

## Functions

[`get_output_classes(...)`](../tf/data/get_output_classes): Returns the output classes of a `Dataset` or `Iterator` elements.

[`get_output_shapes(...)`](../tf/data/get_output_shapes): Returns the output shapes of a `Dataset` or `Iterator` elements.

[`get_output_types(...)`](../tf/data/get_output_types): Returns the output shapes of a `Dataset` or `Iterator` elements.

[`make_initializable_iterator(...)`](../tf/data/make_initializable_iterator): Creates a <a href="../tf/data/Iterator"><code>tf.compat.v1.data.Iterator</code></a> for enumerating the elements of a dataset.

[`make_one_shot_iterator(...)`](../tf/data/make_one_shot_iterator): Creates a <a href="../tf/data/Iterator"><code>tf.compat.v1.data.Iterator</code></a> for enumerating the elements of a dataset.
