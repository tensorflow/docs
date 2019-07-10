page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v2.ragged

Ragged Tensors.

<!-- Placeholder for "Used in" -->

This package defines ops for manipulating ragged tensors (<a href="../../../tf/RaggedTensor"><code>tf.RaggedTensor</code></a>),
which are tensors with non-uniform shapes.  In particular, each `RaggedTensor`
has one or more *ragged dimensions*, which are dimensions whose slices may have
different lengths.  For example, the inner (column) dimension of
`rt=[[3, 1, 4, 1], [], [5, 9, 2], [6], []]` is ragged, since the column slices
(`rt[0, :]`, ..., `rt[4, :]`) have different lengths.  For a more detailed
description of ragged tensors, see the <a href="../../../tf/RaggedTensor"><code>tf.RaggedTensor</code></a> class documentation
and the [Ragged Tensor Guide](/guide/ragged_tensors).


### Additional ops that support `RaggedTensor`

Arguments that accept `RaggedTensor`s are marked in **bold**.

* <a href="../../../tf/batch_gather"><code>tf.batch_gather</code></a>(**params**, **indices**, name=`None`)
* <a href="../../../tf/bitwise/bitwise_and"><code>tf.bitwise.bitwise_and</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/bitwise/bitwise_or"><code>tf.bitwise.bitwise_or</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/bitwise/bitwise_xor"><code>tf.bitwise.bitwise_xor</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/bitwise/invert"><code>tf.bitwise.invert</code></a>(**x**, name=`None`)
* <a href="../../../tf/bitwise/left_shift"><code>tf.bitwise.left_shift</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/bitwise/right_shift"><code>tf.bitwise.right_shift</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/clip_by_value"><code>tf.clip_by_value</code></a>(**t**, clip_value_min, clip_value_max, name=`None`)
* <a href="../../../tf/concat"><code>tf.concat</code></a>(**values**, axis, name=`'concat'`)
* <a href="../../../tf/debugging/check_numerics"><code>tf.debugging.check_numerics</code></a>(**tensor**, message, name=`None`)
* <a href="../../../tf/dtypes/cast"><code>tf.dtypes.cast</code></a>(**x**, dtype, name=`None`)
* <a href="../../../tf/dtypes/complex"><code>tf.dtypes.complex</code></a>(**real**, **imag**, name=`None`)
* <a href="../../../tf/dtypes/saturate_cast"><code>tf.dtypes.saturate_cast</code></a>(**value**, dtype, name=`None`)
* <a href="../../../tf/expand_dims"><code>tf.expand_dims</code></a>(**input**, axis=`None`, name=`None`, dim=`None`)
* <a href="../../../tf/gather_nd"><code>tf.gather_nd</code></a>(**params**, **indices**, name=`None`, batch_dims=`0`)
* <a href="../../../tf/gather"><code>tf.gather</code></a>(**params**, **indices**, validate_indices=`None`, name=`None`, axis=`None`, batch_dims=`0`)
* <a href="../../../tf/identity"><code>tf.identity</code></a>(**input**, name=`None`)
* <a href="../../../tf/io/decode_base64"><code>tf.io.decode_base64</code></a>(**input**, name=`None`)
* <a href="../../../tf/io/decode_compressed"><code>tf.io.decode_compressed</code></a>(**bytes**, compression_type=`''`, name=`None`)
* <a href="../../../tf/io/encode_base64"><code>tf.io.encode_base64</code></a>(**input**, pad=`False`, name=`None`)
* <a href="../../../tf/math/abs"><code>tf.math.abs</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/acos"><code>tf.math.acos</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/acosh"><code>tf.math.acosh</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/add_n"><code>tf.math.add_n</code></a>(**inputs**, name=`None`)
* <a href="../../../tf/math/add"><code>tf.math.add</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/angle"><code>tf.math.angle</code></a>(**input**, name=`None`)
* <a href="../../../tf/math/asin"><code>tf.math.asin</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/asinh"><code>tf.math.asinh</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/atan2"><code>tf.math.atan2</code></a>(**y**, **x**, name=`None`)
* <a href="../../../tf/math/atan"><code>tf.math.atan</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/atanh"><code>tf.math.atanh</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/ceil"><code>tf.math.ceil</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/conj"><code>tf.math.conj</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/cos"><code>tf.math.cos</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/cosh"><code>tf.math.cosh</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/digamma"><code>tf.math.digamma</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/divide_no_nan"><code>tf.math.divide_no_nan</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/divide"><code>tf.math.divide</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/equal"><code>tf.math.equal</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/erf"><code>tf.math.erf</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/erfc"><code>tf.math.erfc</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/exp"><code>tf.math.exp</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/expm1"><code>tf.math.expm1</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/floor"><code>tf.math.floor</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/floordiv"><code>tf.math.floordiv</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/floormod"><code>tf.math.floormod</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/greater_equal"><code>tf.math.greater_equal</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/greater"><code>tf.math.greater</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/imag"><code>tf.math.imag</code></a>(**input**, name=`None`)
* <a href="../../../tf/math/is_finite"><code>tf.math.is_finite</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/is_inf"><code>tf.math.is_inf</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/is_nan"><code>tf.math.is_nan</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/less_equal"><code>tf.math.less_equal</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/less"><code>tf.math.less</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/lgamma"><code>tf.math.lgamma</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/log1p"><code>tf.math.log1p</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/log_sigmoid"><code>tf.math.log_sigmoid</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/log"><code>tf.math.log</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/logical_and"><code>tf.math.logical_and</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/logical_not"><code>tf.math.logical_not</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/logical_or"><code>tf.math.logical_or</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/logical_xor"><code>tf.math.logical_xor</code></a>(**x**, **y**, name=`'LogicalXor'`)
* <a href="../../../tf/math/maximum"><code>tf.math.maximum</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/minimum"><code>tf.math.minimum</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/multiply"><code>tf.math.multiply</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/negative"><code>tf.math.negative</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/not_equal"><code>tf.math.not_equal</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/pow"><code>tf.math.pow</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/real"><code>tf.math.real</code></a>(**input**, name=`None`)
* <a href="../../../tf/math/reciprocal"><code>tf.math.reciprocal</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/reduce_any"><code>tf.math.reduce_any</code></a>(**input_tensor**, axis=`None`, keepdims=`False`, name=`None`)
* <a href="../../../tf/math/reduce_max"><code>tf.math.reduce_max</code></a>(**input_tensor**, axis=`None`, keepdims=`False`, name=`None`)
* <a href="../../../tf/math/reduce_mean"><code>tf.math.reduce_mean</code></a>(**input_tensor**, axis=`None`, keepdims=`False`, name=`None`)
* <a href="../../../tf/math/reduce_min"><code>tf.math.reduce_min</code></a>(**input_tensor**, axis=`None`, keepdims=`False`, name=`None`)
* <a href="../../../tf/math/reduce_prod"><code>tf.math.reduce_prod</code></a>(**input_tensor**, axis=`None`, keepdims=`False`, name=`None`)
* <a href="../../../tf/math/reduce_sum"><code>tf.math.reduce_sum</code></a>(**input_tensor**, axis=`None`, keepdims=`False`, name=`None`)
* <a href="../../../tf/math/rint"><code>tf.math.rint</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/round"><code>tf.math.round</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/rsqrt"><code>tf.math.rsqrt</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/sign"><code>tf.math.sign</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/sin"><code>tf.math.sin</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/sinh"><code>tf.math.sinh</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/sqrt"><code>tf.math.sqrt</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/square"><code>tf.math.square</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/squared_difference"><code>tf.math.squared_difference</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/subtract"><code>tf.math.subtract</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/tan"><code>tf.math.tan</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/truediv"><code>tf.math.truediv</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/unsorted_segment_max"><code>tf.math.unsorted_segment_max</code></a>(**data**, **segment_ids**, num_segments, name=`None`)
* <a href="../../../tf/math/unsorted_segment_mean"><code>tf.math.unsorted_segment_mean</code></a>(**data**, **segment_ids**, num_segments, name=`None`)
* <a href="../../../tf/math/unsorted_segment_min"><code>tf.math.unsorted_segment_min</code></a>(**data**, **segment_ids**, num_segments, name=`None`)
* <a href="../../../tf/math/unsorted_segment_prod"><code>tf.math.unsorted_segment_prod</code></a>(**data**, **segment_ids**, num_segments, name=`None`)
* <a href="../../../tf/math/unsorted_segment_sqrt_n"><code>tf.math.unsorted_segment_sqrt_n</code></a>(**data**, **segment_ids**, num_segments, name=`None`)
* <a href="../../../tf/math/unsorted_segment_sum"><code>tf.math.unsorted_segment_sum</code></a>(**data**, **segment_ids**, num_segments, name=`None`)
* <a href="../../../tf/ones_like"><code>tf.ones_like</code></a>(**tensor**, dtype=`None`, name=`None`, optimize=`True`)
* <a href="../../../tf/rank"><code>tf.rank</code></a>(**input**, name=`None`)
* <a href="../../../tf/realdiv"><code>tf.realdiv</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/reduce_all"><code>tf.reduce_all</code></a>(**input_tensor**, axis=`None`, keepdims=`False`, name=`None`)
* <a href="../../../tf/size"><code>tf.size</code></a>(**input**, name=`None`, out_type=<a href="../../../tf#int32"><code>tf.int32</code></a>)
* <a href="../../../tf/squeeze"><code>tf.squeeze</code></a>(**input**, axis=`None`, name=`None`, squeeze_dims=`None`)
* <a href="../../../tf/stack"><code>tf.stack</code></a>(**values**, axis=`0`, name=`'stack'`)
* <a href="../../../tf/strings/as_string"><code>tf.strings.as_string</code></a>(**input**, precision=`-1`, scientific=`False`, shortest=`False`, width=`-1`, fill=`''`, name=`None`)
* <a href="../../../tf/strings/join"><code>tf.strings.join</code></a>(**inputs**, separator=`''`, name=`None`)
* <a href="../../../tf/strings/length"><code>tf.strings.length</code></a>(**input**, name=`None`, unit=`'BYTE'`)
* <a href="../../../tf/strings/regex_full_match"><code>tf.strings.regex_full_match</code></a>(**input**, pattern, name=`None`)
* <a href="../../../tf/strings/regex_replace"><code>tf.strings.regex_replace</code></a>(**input**, pattern, rewrite, replace_global=`True`, name=`None`)
* <a href="../../../tf/strings/strip"><code>tf.strings.strip</code></a>(**input**, name=`None`)
* <a href="../../../tf/strings/substr"><code>tf.strings.substr</code></a>(**input**, pos, len, name=`None`, unit=`'BYTE'`)
* <a href="../../../tf/strings/to_hash_bucket_fast"><code>tf.strings.to_hash_bucket_fast</code></a>(**input**, num_buckets, name=`None`)
* <a href="../../../tf/strings/to_hash_bucket_strong"><code>tf.strings.to_hash_bucket_strong</code></a>(**input**, num_buckets, key, name=`None`)
* <a href="../../../tf/strings/unicode_script"><code>tf.strings.unicode_script</code></a>(**input**, name=`None`)
* <a href="../../../tf/tile"><code>tf.tile</code></a>(**input**, multiples, name=`None`)
* <a href="../../../tf/truncatediv"><code>tf.truncatediv</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/truncatemod"><code>tf.truncatemod</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/where"><code>tf.where</code></a>(**condition**, **x**=`None`, **y**=`None`, name=`None`)
* <a href="../../../tf/zeros_like"><code>tf.zeros_like</code></a>(**tensor**, dtype=`None`, name=`None`, optimize=`True`)n

## Functions

[`boolean_mask(...)`](../../../tf/ragged/boolean_mask): Applies a boolean mask to `data` without flattening the mask dimensions.

[`constant(...)`](../../../tf/ragged/constant): Constructs a constant RaggedTensor from a nested Python list.

[`map_flat_values(...)`](../../../tf/ragged/map_flat_values): Applies `op` to the values of one or more RaggedTensors.

[`range(...)`](../../../tf/ragged/range): Returns a `RaggedTensor` containing the specified sequences of numbers.

[`row_splits_to_segment_ids(...)`](../../../tf/ragged/row_splits_to_segment_ids): Generates the segmentation corresponding to a RaggedTensor `row_splits`.

[`segment_ids_to_row_splits(...)`](../../../tf/ragged/segment_ids_to_row_splits): Generates the RaggedTensor `row_splits` corresponding to a segmentation.

