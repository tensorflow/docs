page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v1.summary

Operations for writing summary data, for use in analysis and visualization.

<!-- Placeholder for "Used in" -->

See the [Summaries and
TensorBoard](https://www.tensorflow.org/guide/summaries_and_tensorboard) guide.

## Classes

[`class Event`](../../../tf/Event)

[`class FileWriter`](../../../tf/summary/FileWriter): Writes `Summary` protocol buffers to event files.

[`class FileWriterCache`](../../../tf/summary/FileWriterCache): Cache for file writers.

[`class SessionLog`](../../../tf/SessionLog)

[`class Summary`](../../../tf/Summary)

[`class SummaryDescription`](../../../tf/summary/SummaryDescription)

[`class TaggedRunMetadata`](../../../tf/summary/TaggedRunMetadata)

## Functions

[`all_v2_summary_ops(...)`](../../../tf/summary/all_v2_summary_ops): Returns all V2-style summary ops defined in the current default graph.

[`audio(...)`](../../../tf/summary/audio): Outputs a `Summary` protocol buffer with audio.

[`get_summary_description(...)`](../../../tf/summary/get_summary_description): Given a TensorSummary node_def, retrieve its SummaryDescription.

[`histogram(...)`](../../../tf/summary/histogram): Outputs a `Summary` protocol buffer with a histogram.

[`image(...)`](../../../tf/summary/image): Outputs a `Summary` protocol buffer with images.

[`initialize(...)`](../../../tf/summary/initialize): Initializes summary writing for graph execution mode.

[`merge(...)`](../../../tf/summary/merge): Merges summaries.

[`merge_all(...)`](../../../tf/summary/merge_all): Merges all summaries collected in the default graph.

[`scalar(...)`](../../../tf/summary/scalar): Outputs a `Summary` protocol buffer containing a single scalar value.

[`tensor_summary(...)`](../../../tf/summary/tensor_summary): Outputs a `Summary` protocol buffer with a serialized tensor.proto.

[`text(...)`](../../../tf/summary/text): Summarizes textual data.

