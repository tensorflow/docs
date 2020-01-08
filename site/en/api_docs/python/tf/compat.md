page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat





Functions for Python 2 vs. 3 compatibility.

## Conversion routines
In addition to the functions below, `as_str` converts an object to a `str`.


## Types
The compatibility module also provides the following types:

* `bytes_or_text_types`
* `complex_types`
* `integral_types`
* `real_types`

## Functions

[`as_bytes(...)`](../tf/compat/as_bytes): Converts either bytes or unicode to `bytes`, using utf-8 encoding for text.

[`as_str(...)`](../tf/compat/as_bytes): Converts either bytes or unicode to `bytes`, using utf-8 encoding for text.

[`as_str_any(...)`](../tf/compat/as_str_any): Converts to `str` as `str(value)`, but use `as_str` for `bytes`.

[`as_text(...)`](../tf/compat/as_text): Returns the given argument as a unicode string.

[`forward_compatibility_horizon(...)`](../tf/compat/forward_compatibility_horizon): Context manager for testing forward compatibility of generated graphs.

[`forward_compatible(...)`](../tf/compat/forward_compatible): Return true if the forward compatibility window has expired.

[`path_to_str(...)`](../tf/compat/path_to_str): Returns the file system path representation of a `PathLike` object, else as it is.

## Other Members

<h3 id="bytes_or_text_types"><code>bytes_or_text_types</code></h3>

<h3 id="complex_types"><code>complex_types</code></h3>

<h3 id="integral_types"><code>integral_types</code></h3>

<h3 id="real_types"><code>real_types</code></h3>

