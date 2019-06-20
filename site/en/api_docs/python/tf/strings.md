page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.strings



Defined in [`tensorflow/strings/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/strings/__init__.py).

Operations for working with string Tensors.

See the <a href="../../../api_guides/python/string_ops">Strings</a> guide.

## Functions

[`join(...)`](../tf/string_join): Joins the strings in the given list of string tensors into one tensor;

[`regex_full_match(...)`](../tf/strings/regex_full_match): Check if the input matches the regex pattern.

[`regex_replace(...)`](../tf/regex_replace): Replaces the match of pattern in input with rewrite.

[`split(...)`](../tf/strings/split): Split elements of `source` based on `sep` into a `SparseTensor`.

[`strip(...)`](../tf/string_strip): Strip leading and trailing whitespaces from the Tensor.

[`substr(...)`](../tf/substr): Return substrings from `Tensor` of strings.

[`to_hash_bucket(...)`](../tf/string_to_hash_bucket): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`to_hash_bucket_fast(...)`](../tf/string_to_hash_bucket_fast): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`to_hash_bucket_strong(...)`](../tf/string_to_hash_bucket_strong): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`to_number(...)`](../tf/string_to_number): Converts each string in the input Tensor to the specified numeric type.

