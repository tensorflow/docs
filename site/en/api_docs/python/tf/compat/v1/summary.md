description: Operations for writing summary data, for use in analysis and visualization.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.summary" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.summary

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Operations for writing summary data, for use in analysis and visualization.


See the [Summaries and
TensorBoard](https://www.tensorflow.org/guide/summaries_and_tensorboard) guide.

## Classes

[`class Event`](../../../tf/compat/v1/Event.md): A ProtocolMessage

[`class FileWriter`](../../../tf/compat/v1/summary/FileWriter.md): Writes `Summary` protocol buffers to event files.

[`class FileWriterCache`](../../../tf/compat/v1/summary/FileWriterCache.md): Cache for file writers.

[`class SessionLog`](../../../tf/compat/v1/SessionLog.md): A ProtocolMessage

[`class Summary`](../../../tf/compat/v1/Summary.md): A ProtocolMessage

[`class SummaryDescription`](../../../tf/compat/v1/summary/SummaryDescription.md): A ProtocolMessage

[`class TaggedRunMetadata`](../../../tf/compat/v1/summary/TaggedRunMetadata.md): A ProtocolMessage

## Functions

[`all_v2_summary_ops(...)`](../../../tf/compat/v1/summary/all_v2_summary_ops.md): Returns all V2-style summary ops defined in the current default graph.

[`audio(...)`](../../../tf/compat/v1/summary/audio.md): Outputs a `Summary` protocol buffer with audio.

[`get_summary_description(...)`](../../../tf/compat/v1/summary/get_summary_description.md): Given a TensorSummary node_def, retrieve its SummaryDescription.

[`histogram(...)`](../../../tf/compat/v1/summary/histogram.md): Outputs a `Summary` protocol buffer with a histogram.

[`image(...)`](../../../tf/compat/v1/summary/image.md): Outputs a `Summary` protocol buffer with images.

[`initialize(...)`](../../../tf/compat/v1/summary/initialize.md): Initializes summary writing for graph execution mode.

[`merge(...)`](../../../tf/compat/v1/summary/merge.md): Merges summaries.

[`merge_all(...)`](../../../tf/compat/v1/summary/merge_all.md): Merges all summaries collected in the default graph.

[`scalar(...)`](../../../tf/compat/v1/summary/scalar.md): Outputs a `Summary` protocol buffer containing a single scalar value.

[`tensor_summary(...)`](../../../tf/compat/v1/summary/tensor_summary.md): Outputs a `Summary` protocol buffer with a serialized tensor.proto.

[`text(...)`](../../../tf/compat/v1/summary/text.md): Summarizes textual data.

