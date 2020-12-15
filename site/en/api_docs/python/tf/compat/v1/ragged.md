description: Ragged Tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.ragged" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.ragged

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Ragged Tensors.


This package defines ops for manipulating ragged tensors (<a href="../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>),
which are tensors with non-uniform shapes.  In particular, each `RaggedTensor`
has one or more *ragged dimensions*, which are dimensions whose slices may have
different lengths.  For example, the inner (column) dimension of
`rt=[[3, 1, 4, 1], [], [5, 9, 2], [6], []]` is ragged, since the column slices
(`rt[0, :]`, ..., `rt[4, :]`) have different lengths.  For a more detailed
description of ragged tensors, see the <a href="../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a> class documentation
and the [Ragged Tensor Guide](/guide/ragged_tensors).


### Additional ops that support `RaggedTensor`

Arguments that accept `RaggedTensor`s are marked in **bold**.

* `tf.batch_gather`(**params**, **indices**, name=`None`)
* <a href="../../../tf/bitwise/bitwise_and.md"><code>tf.bitwise.bitwise_and</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/bitwise/bitwise_or.md"><code>tf.bitwise.bitwise_or</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/bitwise/bitwise_xor.md"><code>tf.bitwise.bitwise_xor</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/bitwise/invert.md"><code>tf.bitwise.invert</code></a>(**x**, name=`None`)
* <a href="../../../tf/bitwise/left_shift.md"><code>tf.bitwise.left_shift</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/bitwise/right_shift.md"><code>tf.bitwise.right_shift</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/cast.md"><code>tf.cast</code></a>(**x**, dtype, name=`None`)
* <a href="../../../tf/clip_by_value.md"><code>tf.clip_by_value</code></a>(**t**, clip_value_min, clip_value_max, name=`None`)
* <a href="../../../tf/concat.md"><code>tf.concat</code></a>(**values**, axis, name=`'concat'`)
* <a href="../../../tf/debugging/check_numerics.md"><code>tf.debugging.check_numerics</code></a>(**tensor**, message, name=`None`)
* <a href="../../../tf/dtypes/complex.md"><code>tf.dtypes.complex</code></a>(**real**, **imag**, name=`None`)
* <a href="../../../tf/dtypes/saturate_cast.md"><code>tf.dtypes.saturate_cast</code></a>(**value**, dtype, name=`None`)
* <a href="../../../tf/dynamic_partition.md"><code>tf.dynamic_partition</code></a>(**data**, **partitions**, num_partitions, name=`None`)
* <a href="../../../tf/expand_dims.md"><code>tf.expand_dims</code></a>(**input**, axis=`None`, name=`None`, dim=`None`)
* <a href="../../../tf/gather_nd.md"><code>tf.gather_nd</code></a>(**params**, **indices**, name=`None`, batch_dims=`0`)
* <a href="../../../tf/gather.md"><code>tf.gather</code></a>(**params**, **indices**, validate_indices=`None`, name=`None`, axis=`None`, batch_dims=`0`)
* <a href="../../../tf/identity.md"><code>tf.identity</code></a>(**input**, name=`None`)
* <a href="../../../tf/io/decode_base64.md"><code>tf.io.decode_base64</code></a>(**input**, name=`None`)
* <a href="../../../tf/io/decode_compressed.md"><code>tf.io.decode_compressed</code></a>(**bytes**, compression_type=`''`, name=`None`)
* <a href="../../../tf/io/encode_base64.md"><code>tf.io.encode_base64</code></a>(**input**, pad=`False`, name=`None`)
* <a href="../../../tf/math/abs.md"><code>tf.math.abs</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/acos.md"><code>tf.math.acos</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/acosh.md"><code>tf.math.acosh</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/add_n.md"><code>tf.math.add_n</code></a>(**inputs**, name=`None`)
* <a href="../../../tf/math/add.md"><code>tf.math.add</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/angle.md"><code>tf.math.angle</code></a>(**input**, name=`None`)
* <a href="../../../tf/math/asin.md"><code>tf.math.asin</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/asinh.md"><code>tf.math.asinh</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/atan2.md"><code>tf.math.atan2</code></a>(**y**, **x**, name=`None`)
* <a href="../../../tf/math/atan.md"><code>tf.math.atan</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/atanh.md"><code>tf.math.atanh</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/ceil.md"><code>tf.math.ceil</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/conj.md"><code>tf.math.conj</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/cos.md"><code>tf.math.cos</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/cosh.md"><code>tf.math.cosh</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/digamma.md"><code>tf.math.digamma</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/divide_no_nan.md"><code>tf.math.divide_no_nan</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/divide.md"><code>tf.math.divide</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/equal.md"><code>tf.math.equal</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/erf.md"><code>tf.math.erf</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/erfc.md"><code>tf.math.erfc</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/erfinv.md"><code>tf.math.erfinv</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/exp.md"><code>tf.math.exp</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/expm1.md"><code>tf.math.expm1</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/floor.md"><code>tf.math.floor</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/floordiv.md"><code>tf.math.floordiv</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/floormod.md"><code>tf.math.floormod</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/greater_equal.md"><code>tf.math.greater_equal</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/greater.md"><code>tf.math.greater</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/imag.md"><code>tf.math.imag</code></a>(**input**, name=`None`)
* <a href="../../../tf/math/is_finite.md"><code>tf.math.is_finite</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/is_inf.md"><code>tf.math.is_inf</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/is_nan.md"><code>tf.math.is_nan</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/less_equal.md"><code>tf.math.less_equal</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/less.md"><code>tf.math.less</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/lgamma.md"><code>tf.math.lgamma</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/log1p.md"><code>tf.math.log1p</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/log_sigmoid.md"><code>tf.math.log_sigmoid</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/log.md"><code>tf.math.log</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/logical_and.md"><code>tf.math.logical_and</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/logical_not.md"><code>tf.math.logical_not</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/logical_or.md"><code>tf.math.logical_or</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/logical_xor.md"><code>tf.math.logical_xor</code></a>(**x**, **y**, name=`'LogicalXor'`)
* <a href="../../../tf/math/maximum.md"><code>tf.math.maximum</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/minimum.md"><code>tf.math.minimum</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/multiply.md"><code>tf.math.multiply</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/ndtri.md"><code>tf.math.ndtri</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/negative.md"><code>tf.math.negative</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/not_equal.md"><code>tf.math.not_equal</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/pow.md"><code>tf.math.pow</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/real.md"><code>tf.math.real</code></a>(**input**, name=`None`)
* <a href="../../../tf/math/reciprocal.md"><code>tf.math.reciprocal</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/reduce_all.md"><code>tf.math.reduce_all</code></a>(**input_tensor**, axis=`None`, keepdims=`False`, name=`None`)
* <a href="../../../tf/math/reduce_any.md"><code>tf.math.reduce_any</code></a>(**input_tensor**, axis=`None`, keepdims=`False`, name=`None`)
* <a href="../../../tf/math/reduce_max.md"><code>tf.math.reduce_max</code></a>(**input_tensor**, axis=`None`, keepdims=`False`, name=`None`)
* <a href="../../../tf/math/reduce_mean.md"><code>tf.math.reduce_mean</code></a>(**input_tensor**, axis=`None`, keepdims=`False`, name=`None`)
* <a href="../../../tf/math/reduce_min.md"><code>tf.math.reduce_min</code></a>(**input_tensor**, axis=`None`, keepdims=`False`, name=`None`)
* <a href="../../../tf/math/reduce_prod.md"><code>tf.math.reduce_prod</code></a>(**input_tensor**, axis=`None`, keepdims=`False`, name=`None`)
* <a href="../../../tf/math/reduce_sum.md"><code>tf.math.reduce_sum</code></a>(**input_tensor**, axis=`None`, keepdims=`False`, name=`None`)
* <a href="../../../tf/math/rint.md"><code>tf.math.rint</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/round.md"><code>tf.math.round</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/rsqrt.md"><code>tf.math.rsqrt</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/sign.md"><code>tf.math.sign</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/sin.md"><code>tf.math.sin</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/sinh.md"><code>tf.math.sinh</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/sqrt.md"><code>tf.math.sqrt</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/square.md"><code>tf.math.square</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/squared_difference.md"><code>tf.math.squared_difference</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/subtract.md"><code>tf.math.subtract</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/tan.md"><code>tf.math.tan</code></a>(**x**, name=`None`)
* <a href="../../../tf/math/truediv.md"><code>tf.math.truediv</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/math/unsorted_segment_max.md"><code>tf.math.unsorted_segment_max</code></a>(**data**, **segment_ids**, num_segments, name=`None`)
* <a href="../../../tf/math/unsorted_segment_mean.md"><code>tf.math.unsorted_segment_mean</code></a>(**data**, **segment_ids**, num_segments, name=`None`)
* <a href="../../../tf/math/unsorted_segment_min.md"><code>tf.math.unsorted_segment_min</code></a>(**data**, **segment_ids**, num_segments, name=`None`)
* <a href="../../../tf/math/unsorted_segment_prod.md"><code>tf.math.unsorted_segment_prod</code></a>(**data**, **segment_ids**, num_segments, name=`None`)
* <a href="../../../tf/math/unsorted_segment_sqrt_n.md"><code>tf.math.unsorted_segment_sqrt_n</code></a>(**data**, **segment_ids**, num_segments, name=`None`)
* <a href="../../../tf/math/unsorted_segment_sum.md"><code>tf.math.unsorted_segment_sum</code></a>(**data**, **segment_ids**, num_segments, name=`None`)
* <a href="../../../tf/nn/dropout.md"><code>tf.nn.dropout</code></a>(**x**, keep_prob=`None`, noise_shape=`None`, seed=`None`, name=`None`, rate=`None`)
* <a href="../../../tf/one_hot.md"><code>tf.one_hot</code></a>(**indices**, depth, on_value=`None`, off_value=`None`, axis=`None`, dtype=`None`, name=`None`)
* <a href="../../../tf/ones_like.md"><code>tf.ones_like</code></a>(**tensor**, dtype=`None`, name=`None`, optimize=`True`)
* <a href="../../../tf/print.md"><code>tf.print</code></a>(***inputs**, **kwargs)
* <a href="../../../tf/rank.md"><code>tf.rank</code></a>(**input**, name=`None`)
* <a href="../../../tf/realdiv.md"><code>tf.realdiv</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/reverse.md"><code>tf.reverse</code></a>(**tensor**, axis, name=`None`)
* <a href="../../../tf/size.md"><code>tf.size</code></a>(**input**, name=`None`, out_type=<a href="../../../tf.md#int32"><code>tf.int32</code></a>)
* <a href="../../../tf/squeeze.md"><code>tf.squeeze</code></a>(**input**, axis=`None`, name=`None`, squeeze_dims=`None`)
* <a href="../../../tf/stack.md"><code>tf.stack</code></a>(**values**, axis=`0`, name=`'stack'`)
* <a href="../../../tf/strings/as_string.md"><code>tf.strings.as_string</code></a>(**input**, precision=`-1`, scientific=`False`, shortest=`False`, width=`-1`, fill=`''`, name=`None`)
* <a href="../../../tf/strings/format.md"><code>tf.strings.format</code></a>(template, **inputs**, placeholder=`'{}'`, summarize=`3`, name=`None`)
* <a href="../../../tf/strings/join.md"><code>tf.strings.join</code></a>(**inputs**, separator=`''`, name=`None`)
* <a href="../../../tf/strings/length.md"><code>tf.strings.length</code></a>(**input**, name=`None`, unit=`'BYTE'`)
* <a href="../../../tf/strings/reduce_join.md"><code>tf.strings.reduce_join</code></a>(**inputs**, axis=`None`, keepdims=`False`, separator=`''`, name=`None`)
* <a href="../../../tf/strings/regex_full_match.md"><code>tf.strings.regex_full_match</code></a>(**input**, pattern, name=`None`)
* <a href="../../../tf/strings/regex_replace.md"><code>tf.strings.regex_replace</code></a>(**input**, pattern, rewrite, replace_global=`True`, name=`None`)
* <a href="../../../tf/strings/strip.md"><code>tf.strings.strip</code></a>(**input**, name=`None`)
* <a href="../../../tf/strings/substr.md"><code>tf.strings.substr</code></a>(**input**, pos, len, name=`None`, unit=`'BYTE'`)
* <a href="../../../tf/strings/to_hash_bucket_fast.md"><code>tf.strings.to_hash_bucket_fast</code></a>(**input**, num_buckets, name=`None`)
* <a href="../../../tf/strings/to_hash_bucket_strong.md"><code>tf.strings.to_hash_bucket_strong</code></a>(**input**, num_buckets, key, name=`None`)
* <a href="../../../tf/strings/to_hash_bucket.md"><code>tf.strings.to_hash_bucket</code></a>(**input**, num_buckets, name=`None`)
* <a href="../../../tf/strings/to_hash_bucket.md"><code>tf.strings.to_hash_bucket</code></a>(**input**, num_buckets, name=`None`)
* <a href="../../../tf/strings/to_number.md"><code>tf.strings.to_number</code></a>(**input**, out_type=<a href="../../../tf.md#float32"><code>tf.float32</code></a>, name=`None`)
* <a href="../../../tf/strings/unicode_script.md"><code>tf.strings.unicode_script</code></a>(**input**, name=`None`)
* <a href="../../../tf/tile.md"><code>tf.tile</code></a>(**input**, multiples, name=`None`)
* <a href="../../../tf/truncatediv.md"><code>tf.truncatediv</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/truncatemod.md"><code>tf.truncatemod</code></a>(**x**, **y**, name=`None`)
* <a href="../../../tf/where.md"><code>tf.where</code></a>(**condition**, **x**=`None`, **y**=`None`, name=`None`)
* <a href="../../../tf/where.md"><code>tf.where</code></a>(**condition**, **x**=`None`, **y**=`None`, name=`None`)
* <a href="../../../tf/zeros_like.md"><code>tf.zeros_like</code></a>(**tensor**, dtype=`None`, name=`None`, optimize=`True`)n

## Classes

[`class RaggedTensorValue`](../../../tf/compat/v1/ragged/RaggedTensorValue.md): Represents the value of a `RaggedTensor`.

## Functions

[`boolean_mask(...)`](../../../tf/ragged/boolean_mask.md): Applies a boolean mask to `data` without flattening the mask dimensions.

[`constant(...)`](../../../tf/ragged/constant.md): Constructs a constant RaggedTensor from a nested Python list.

[`constant_value(...)`](../../../tf/compat/v1/ragged/constant_value.md): Constructs a RaggedTensorValue from a nested Python list.

[`cross(...)`](../../../tf/ragged/cross.md): Generates feature cross from a list of tensors.

[`cross_hashed(...)`](../../../tf/ragged/cross_hashed.md): Generates hashed feature cross from a list of tensors.

[`map_flat_values(...)`](../../../tf/ragged/map_flat_values.md): Applies `op` to the values of one or more RaggedTensors.

[`placeholder(...)`](../../../tf/compat/v1/ragged/placeholder.md): Creates a placeholder for a <a href="../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a> that will always be fed.

[`range(...)`](../../../tf/ragged/range.md): Returns a `RaggedTensor` containing the specified sequences of numbers.

[`row_splits_to_segment_ids(...)`](../../../tf/ragged/row_splits_to_segment_ids.md): Generates the segmentation corresponding to a RaggedTensor `row_splits`.

[`segment_ids_to_row_splits(...)`](../../../tf/ragged/segment_ids_to_row_splits.md): Generates the RaggedTensor `row_splits` corresponding to a segmentation.

[`stack(...)`](../../../tf/ragged/stack.md): Stacks a list of rank-`R` tensors into one rank-`(R+1)` `RaggedTensor`.

[`stack_dynamic_partitions(...)`](../../../tf/ragged/stack_dynamic_partitions.md): Stacks dynamic partitions of a Tensor or RaggedTensor.

