page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v1.debugging


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Public API for tf.debugging namespace.

<!-- Placeholder for "Used in" -->


## Functions

[`Assert(...)`](../../../tf/debugging/Assert): Asserts that the given condition is true.

[`assert_all_finite(...)`](../../../tf/compat/v1/verify_tensor_all_finite): Assert that the tensor does not contain any NaN's or Inf's.

[`assert_equal(...)`](../../../tf/compat/v1/assert_equal): Assert the condition `x == y` holds element-wise.

[`assert_greater(...)`](../../../tf/compat/v1/assert_greater): Assert the condition `x > y` holds element-wise.

[`assert_greater_equal(...)`](../../../tf/compat/v1/assert_greater_equal): Assert the condition `x >= y` holds element-wise.

[`assert_integer(...)`](../../../tf/compat/v1/assert_integer): Assert that `x` is of integer dtype.

[`assert_less(...)`](../../../tf/compat/v1/assert_less): Assert the condition `x < y` holds element-wise.

[`assert_less_equal(...)`](../../../tf/compat/v1/assert_less_equal): Assert the condition `x <= y` holds element-wise.

[`assert_near(...)`](../../../tf/compat/v1/assert_near): Assert the condition `x` and `y` are close element-wise.

[`assert_negative(...)`](../../../tf/compat/v1/assert_negative): Assert the condition `x < 0` holds element-wise.

[`assert_non_negative(...)`](../../../tf/compat/v1/assert_non_negative): Assert the condition `x >= 0` holds element-wise.

[`assert_non_positive(...)`](../../../tf/compat/v1/assert_non_positive): Assert the condition `x <= 0` holds element-wise.

[`assert_none_equal(...)`](../../../tf/compat/v1/assert_none_equal): Assert the condition `x != y` holds for all elements.

[`assert_positive(...)`](../../../tf/compat/v1/assert_positive): Assert the condition `x > 0` holds element-wise.

[`assert_proper_iterable(...)`](../../../tf/debugging/assert_proper_iterable): Static assert that values is a "proper" iterable.

[`assert_rank(...)`](../../../tf/compat/v1/assert_rank): Assert `x` has rank equal to `rank`.

[`assert_rank_at_least(...)`](../../../tf/compat/v1/assert_rank_at_least): Assert `x` has rank equal to `rank` or higher.

[`assert_rank_in(...)`](../../../tf/compat/v1/assert_rank_in): Assert `x` has rank in `ranks`.

[`assert_same_float_dtype(...)`](../../../tf/debugging/assert_same_float_dtype): Validate and return float type based on `tensors` and `dtype`.

[`assert_scalar(...)`](../../../tf/compat/v1/assert_scalar): Asserts that the given `tensor` is a scalar (i.e. zero-dimensional).

[`assert_shapes(...)`](../../../tf/compat/v1/debugging/assert_shapes): Assert tensor shapes and dimension size relationships between tensors.

[`assert_type(...)`](../../../tf/compat/v1/assert_type): Statically asserts that the given `Tensor` is of the specified type.

[`check_numerics(...)`](../../../tf/debugging/check_numerics): Checks a tensor for NaN and Inf values.

[`get_log_device_placement(...)`](../../../tf/debugging/get_log_device_placement): Get if device placements are logged.

[`is_finite(...)`](../../../tf/math/is_finite): Returns which elements of x are finite.

[`is_inf(...)`](../../../tf/math/is_inf): Returns which elements of x are Inf.

[`is_nan(...)`](../../../tf/math/is_nan): Returns which elements of x are NaN.

[`is_non_decreasing(...)`](../../../tf/math/is_non_decreasing): Returns `True` if `x` is non-decreasing.

[`is_numeric_tensor(...)`](../../../tf/debugging/is_numeric_tensor): Returns `True` if the elements of `tensor` are numbers.

[`is_strictly_increasing(...)`](../../../tf/math/is_strictly_increasing): Returns `True` if `x` is strictly increasing.

[`set_log_device_placement(...)`](../../../tf/debugging/set_log_device_placement): Set if device placements should be logged.
