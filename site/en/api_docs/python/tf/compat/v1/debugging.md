page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v1.debugging


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/compat/v1/debugging">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Public API for tf.debugging namespace.

<!-- Placeholder for "Used in" -->


## Functions

[`Assert(...)`](../../../tf/debugging/Assert): Asserts that the given condition is true.

[`assert_all_finite(...)`](../../../tf/debugging/assert_all_finite): Assert that the tensor does not contain any NaN's or Inf's.

[`assert_equal(...)`](../../../tf/debugging/assert_equal): Assert the condition `x == y` holds element-wise.

[`assert_greater(...)`](../../../tf/debugging/assert_greater): Assert the condition `x > y` holds element-wise.

[`assert_greater_equal(...)`](../../../tf/debugging/assert_greater_equal): Assert the condition `x >= y` holds element-wise.

[`assert_integer(...)`](../../../tf/debugging/assert_integer): Assert that `x` is of integer dtype.

[`assert_less(...)`](../../../tf/debugging/assert_less): Assert the condition `x < y` holds element-wise.

[`assert_less_equal(...)`](../../../tf/debugging/assert_less_equal): Assert the condition `x <= y` holds element-wise.

[`assert_near(...)`](../../../tf/debugging/assert_near): Assert the condition `x` and `y` are close element-wise.

[`assert_negative(...)`](../../../tf/debugging/assert_negative): Assert the condition `x < 0` holds element-wise.

[`assert_non_negative(...)`](../../../tf/debugging/assert_non_negative): Assert the condition `x >= 0` holds element-wise.

[`assert_non_positive(...)`](../../../tf/debugging/assert_non_positive): Assert the condition `x <= 0` holds element-wise.

[`assert_none_equal(...)`](../../../tf/debugging/assert_none_equal): Assert the condition `x != y` holds element-wise.

[`assert_positive(...)`](../../../tf/debugging/assert_positive): Assert the condition `x > 0` holds element-wise.

[`assert_proper_iterable(...)`](../../../tf/debugging/assert_proper_iterable): Static assert that values is a "proper" iterable.

[`assert_rank(...)`](../../../tf/debugging/assert_rank): Assert `x` has rank equal to `rank`.

[`assert_rank_at_least(...)`](../../../tf/debugging/assert_rank_at_least): Assert `x` has rank equal to `rank` or higher.

[`assert_rank_in(...)`](../../../tf/debugging/assert_rank_in): Assert `x` has rank in `ranks`.

[`assert_same_float_dtype(...)`](../../../tf/debugging/assert_same_float_dtype): Validate and return float type based on `tensors` and `dtype`.

[`assert_scalar(...)`](../../../tf/debugging/assert_scalar): Asserts that the given `tensor` is a scalar (i.e. zero-dimensional).

[`assert_shapes(...)`](../../../tf/debugging/assert_shapes): Assert tensor shapes and dimension size relationships between tensors.

[`assert_type(...)`](../../../tf/debugging/assert_type): Statically asserts that the given `Tensor` is of the specified type.

[`check_numerics(...)`](../../../tf/debugging/check_numerics): Checks a tensor for NaN and Inf values.

[`get_log_device_placement(...)`](../../../tf/debugging/get_log_device_placement): Get if device placements are logged.

[`is_finite(...)`](../../../tf/math/is_finite): Returns which elements of x are finite.

[`is_inf(...)`](../../../tf/math/is_inf): Returns which elements of x are Inf.

[`is_nan(...)`](../../../tf/math/is_nan): Returns which elements of x are NaN.

[`is_non_decreasing(...)`](../../../tf/math/is_non_decreasing): Returns `True` if `x` is non-decreasing.

[`is_numeric_tensor(...)`](../../../tf/debugging/is_numeric_tensor): Returns `True` if the elements of `tensor` are numbers.

[`is_strictly_increasing(...)`](../../../tf/math/is_strictly_increasing): Returns `True` if `x` is strictly increasing.

[`set_log_device_placement(...)`](../../../tf/debugging/set_log_device_placement): Set if device placements should be logged.
