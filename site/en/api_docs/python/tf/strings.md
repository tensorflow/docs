page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.strings


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/strings">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Operations for working with string Tensors.

<!-- Placeholder for "Used in" -->


## Functions

[`as_string(...)`](../tf/strings/as_string): Converts each entry in the given tensor to strings.

[`bytes_split(...)`](../tf/strings/bytes_split): Split string elements of `input` into bytes.

[`format(...)`](../tf/strings/format): Formats a string template using a list of tensors.

[`join(...)`](../tf/strings/join): Joins the strings in the given list of string tensors into one tensor;

[`length(...)`](../tf/strings/length): String lengths of `input`.

[`lower(...)`](../tf/strings/lower): TODO: add doc.

[`ngrams(...)`](../tf/strings/ngrams): Create a tensor of n-grams based on `data`.

[`reduce_join(...)`](../tf/strings/reduce_join): Joins a string Tensor across the given dimensions.

[`regex_full_match(...)`](../tf/strings/regex_full_match): Check if the input matches the regex pattern.

[`regex_replace(...)`](../tf/strings/regex_replace): Replace elements of `input` matching regex `pattern` with `rewrite`.

[`split(...)`](../tf/strings/split): Split elements of `input` based on `sep`.

[`strip(...)`](../tf/strings/strip): Strip leading and trailing whitespaces from the Tensor.

[`substr(...)`](../tf/strings/substr): Return substrings from `Tensor` of strings.

[`to_hash_bucket(...)`](../tf/strings/to_hash_bucket): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`to_hash_bucket_fast(...)`](../tf/strings/to_hash_bucket_fast): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`to_hash_bucket_strong(...)`](../tf/strings/to_hash_bucket_strong): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`to_number(...)`](../tf/strings/to_number): Converts each string in the input Tensor to the specified numeric type.

[`unicode_decode(...)`](../tf/strings/unicode_decode): Decodes each string in `input` into a sequence of Unicode code points.

[`unicode_decode_with_offsets(...)`](../tf/strings/unicode_decode_with_offsets): Decodes each string into a sequence of code points with start offsets.

[`unicode_encode(...)`](../tf/strings/unicode_encode): Encodes each sequence of Unicode code points in `input` into a string.

[`unicode_script(...)`](../tf/strings/unicode_script): Determine the script codes of a given tensor of Unicode integer code points.

[`unicode_split(...)`](../tf/strings/unicode_split): Splits each string in `input` into a sequence of Unicode code points.

[`unicode_split_with_offsets(...)`](../tf/strings/unicode_split_with_offsets): Splits each string into a sequence of code points with start offsets.

[`unicode_transcode(...)`](../tf/strings/unicode_transcode): Transcode the input text from a source encoding to a destination encoding.

[`unsorted_segment_join(...)`](../tf/strings/unsorted_segment_join): Joins the elements of `inputs` based on `segment_ids`.

[`upper(...)`](../tf/strings/upper): TODO: add doc.
