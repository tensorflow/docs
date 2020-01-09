page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v1.summary


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Operations for writing summary data, for use in analysis and visualization.

<!-- Placeholder for "Used in" -->

See the [Summaries and
TensorBoard](https://www.tensorflow.org/guide/summaries_and_tensorboard) guide.

## Classes

[`class Event`](../../../tf/compat/v1/Event): A ProtocolMessage

[`class FileWriter`](../../../tf/compat/v1/summary/FileWriter): Writes `Summary` protocol buffers to event files.

[`class FileWriterCache`](../../../tf/compat/v1/summary/FileWriterCache): Cache for file writers.

[`class SessionLog`](../../../tf/compat/v1/SessionLog): A ProtocolMessage

[`class Summary`](../../../tf/compat/v1/Summary): A ProtocolMessage

[`class SummaryDescription`](../../../tf/compat/v1/summary/SummaryDescription): A ProtocolMessage

[`class TaggedRunMetadata`](../../../tf/compat/v1/summary/TaggedRunMetadata): A ProtocolMessage

## Functions

[`all_v2_summary_ops(...)`](../../../tf/compat/v1/summary/all_v2_summary_ops): Returns all V2-style summary ops defined in the current default graph.

[`audio(...)`](../../../tf/compat/v1/summary/audio): Outputs a `Summary` protocol buffer with audio.

[`get_summary_description(...)`](../../../tf/compat/v1/summary/get_summary_description): Given a TensorSummary node_def, retrieve its SummaryDescription.

[`histogram(...)`](../../../tf/compat/v1/summary/histogram): Outputs a `Summary` protocol buffer with a histogram.

[`image(...)`](../../../tf/compat/v1/summary/image): Outputs a `Summary` protocol buffer with images.

[`initialize(...)`](../../../tf/compat/v1/summary/initialize): Initializes summary writing for graph execution mode.

[`merge(...)`](../../../tf/compat/v1/summary/merge): Merges summaries.

[`merge_all(...)`](../../../tf/compat/v1/summary/merge_all): Merges all summaries collected in the default graph.

[`scalar(...)`](../../../tf/compat/v1/summary/scalar): Outputs a `Summary` protocol buffer containing a single scalar value.

[`tensor_summary(...)`](../../../tf/compat/v1/summary/tensor_summary): Outputs a `Summary` protocol buffer with a serialized tensor.proto.

[`text(...)`](../../../tf/compat/v1/summary/text): Summarizes textual data.
