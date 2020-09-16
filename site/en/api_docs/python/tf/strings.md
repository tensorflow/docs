description: Operations for working with string Tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strings" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.strings

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Operations for working with string Tensors.



## Functions

[`as_string(...)`](../tf/strings/as_string.md): Converts each entry in the given tensor to strings.

[`bytes_split(...)`](../tf/strings/bytes_split.md): Split string elements of `input` into bytes.

[`format(...)`](../tf/strings/format.md): Formats a string template using a list of tensors.

[`join(...)`](../tf/strings/join.md): Perform element-wise concatenation of a list of string tensors.

[`length(...)`](../tf/strings/length.md): String lengths of `input`.

[`lower(...)`](../tf/strings/lower.md): Converts all uppercase characters into their respective lowercase replacements.

[`ngrams(...)`](../tf/strings/ngrams.md): Create a tensor of n-grams based on `data`.

[`reduce_join(...)`](../tf/strings/reduce_join.md): Joins all strings into a single string, or joins along an axis.

[`regex_full_match(...)`](../tf/strings/regex_full_match.md): Check if the input matches the regex pattern.

[`regex_replace(...)`](../tf/strings/regex_replace.md): Replace elements of `input` matching regex `pattern` with `rewrite`.

[`split(...)`](../tf/strings/split.md): Split elements of `input` based on `sep` into a `RaggedTensor`.

[`strip(...)`](../tf/strings/strip.md): Strip leading and trailing whitespaces from the Tensor.

[`substr(...)`](../tf/strings/substr.md): Return substrings from `Tensor` of strings.

[`to_hash_bucket(...)`](../tf/strings/to_hash_bucket.md): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`to_hash_bucket_fast(...)`](../tf/strings/to_hash_bucket_fast.md): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`to_hash_bucket_strong(...)`](../tf/strings/to_hash_bucket_strong.md): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`to_number(...)`](../tf/strings/to_number.md): Converts each string in the input Tensor to the specified numeric type.

[`unicode_decode(...)`](../tf/strings/unicode_decode.md): Decodes each string in `input` into a sequence of Unicode code points.

[`unicode_decode_with_offsets(...)`](../tf/strings/unicode_decode_with_offsets.md): Decodes each string into a sequence of code points with start offsets.

[`unicode_encode(...)`](../tf/strings/unicode_encode.md): Encodes each sequence of Unicode code points in `input` into a string.

[`unicode_script(...)`](../tf/strings/unicode_script.md): Determine the script codes of a given tensor of Unicode integer code points.

[`unicode_split(...)`](../tf/strings/unicode_split.md): Splits each string in `input` into a sequence of Unicode code points.

[`unicode_split_with_offsets(...)`](../tf/strings/unicode_split_with_offsets.md): Splits each string into a sequence of code points with start offsets.

[`unicode_transcode(...)`](../tf/strings/unicode_transcode.md): Transcode the input text from a source encoding to a destination encoding.

[`unsorted_segment_join(...)`](../tf/strings/unsorted_segment_join.md): Joins the elements of `inputs` based on `segment_ids`.

[`upper(...)`](../tf/strings/upper.md): Converts all lowercase characters into their respective uppercase replacements.

