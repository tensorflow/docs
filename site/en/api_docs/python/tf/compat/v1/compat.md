description: Compatibility functions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.compat" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="bytes_or_text_types"/>
<meta itemprop="property" content="complex_types"/>
<meta itemprop="property" content="integral_types"/>
<meta itemprop="property" content="real_types"/>
</div>

# Module: tf.compat.v1.compat

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Compatibility functions.


The <a href="../../../tf/compat.md"><code>tf.compat</code></a> module contains two sets of compatibility functions.

## Tensorflow 1.x and 2.x APIs

The <a href="../../../tf/compat/v1.md"><code>compat.v1</code></a> and `compat.v2` submodules provide a complete copy of both the
<a href="../../../tf/compat/v1.md"><code>v1</code></a> and `v2` APIs for backwards and forwards compatibility across TensorFlow
versions 1.x and 2.x. See the
[migration guide](https://www.tensorflow.org/guide/migrate) for details.

## Utilities for writing compatible code

Aside from the <a href="../../../tf/compat/v1.md"><code>compat.v1</code></a> and `compat.v2` submodules, <a href="../../../tf/compat.md"><code>tf.compat</code></a> also contains
a set of helper functions for writing code that works in both:

* TensorFlow 1.x and 2.x
* Python 2 and 3


## Type collections

The compatibility module also provides the following aliases for common
sets of python types:

* `bytes_or_text_types`
* `complex_types`
* `integral_types`
* `real_types`

## Functions

[`as_bytes(...)`](../../../tf/compat/as_bytes.md): Converts `bytearray`, `bytes`, or unicode python input types to `bytes`.

[`as_str(...)`](../../../tf/compat/as_str.md)

[`as_str_any(...)`](../../../tf/compat/as_str_any.md): Converts input to `str` type.

[`as_text(...)`](../../../tf/compat/as_text.md): Converts any string-like python input types to unicode.

[`dimension_at_index(...)`](../../../tf/compat/dimension_at_index.md): Compatibility utility required to allow for both V1 and V2 behavior in TF.

[`dimension_value(...)`](../../../tf/compat/dimension_value.md): Compatibility utility required to allow for both V1 and V2 behavior in TF.

[`forward_compatibility_horizon(...)`](../../../tf/compat/forward_compatibility_horizon.md): Context manager for testing forward compatibility of generated graphs.

[`forward_compatible(...)`](../../../tf/compat/forward_compatible.md): Return true if the forward compatibility window has expired.

[`path_to_str(...)`](../../../tf/compat/path_to_str.md): Converts input which is a `PathLike` object to `str` type.

## Other Members

* `bytes_or_text_types` <a id="bytes_or_text_types"></a>
* `complex_types` <a id="complex_types"></a>
* `integral_types` <a id="integral_types"></a>
* `real_types` <a id="real_types"></a>
