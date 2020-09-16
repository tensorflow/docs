description: Public API for tf.debugging namespace.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.debugging" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.debugging

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf.debugging namespace.



## Modules

[`experimental`](../../../tf/compat/v1/debugging/experimental.md) module: Public API for tf.debugging.experimental namespace.

## Functions

[`Assert(...)`](../../../tf/debugging/Assert.md): Asserts that the given condition is true.

[`assert_all_finite(...)`](../../../tf/compat/v1/verify_tensor_all_finite.md): Assert that the tensor does not contain any NaN's or Inf's.

[`assert_equal(...)`](../../../tf/compat/v1/assert_equal.md): Assert the condition `x == y` holds element-wise.

[`assert_greater(...)`](../../../tf/compat/v1/assert_greater.md): Assert the condition `x > y` holds element-wise.

[`assert_greater_equal(...)`](../../../tf/compat/v1/assert_greater_equal.md): Assert the condition `x >= y` holds element-wise.

[`assert_integer(...)`](../../../tf/compat/v1/assert_integer.md): Assert that `x` is of integer dtype.

[`assert_less(...)`](../../../tf/compat/v1/assert_less.md): Assert the condition `x < y` holds element-wise.

[`assert_less_equal(...)`](../../../tf/compat/v1/assert_less_equal.md): Assert the condition `x <= y` holds element-wise.

[`assert_near(...)`](../../../tf/compat/v1/assert_near.md): Assert the condition `x` and `y` are close element-wise.

[`assert_negative(...)`](../../../tf/compat/v1/assert_negative.md): Assert the condition `x < 0` holds element-wise.

[`assert_non_negative(...)`](../../../tf/compat/v1/assert_non_negative.md): Assert the condition `x >= 0` holds element-wise.

[`assert_non_positive(...)`](../../../tf/compat/v1/assert_non_positive.md): Assert the condition `x <= 0` holds element-wise.

[`assert_none_equal(...)`](../../../tf/compat/v1/assert_none_equal.md): Assert the condition `x != y` holds element-wise.

[`assert_positive(...)`](../../../tf/compat/v1/assert_positive.md): Assert the condition `x > 0` holds element-wise.

[`assert_proper_iterable(...)`](../../../tf/debugging/assert_proper_iterable.md): Static assert that values is a "proper" iterable.

[`assert_rank(...)`](../../../tf/compat/v1/assert_rank.md): Assert `x` has rank equal to `rank`.

[`assert_rank_at_least(...)`](../../../tf/compat/v1/assert_rank_at_least.md): Assert `x` has rank equal to `rank` or higher.

[`assert_rank_in(...)`](../../../tf/compat/v1/assert_rank_in.md): Assert `x` has rank in `ranks`.

[`assert_same_float_dtype(...)`](../../../tf/debugging/assert_same_float_dtype.md): Validate and return float type based on `tensors` and `dtype`.

[`assert_scalar(...)`](../../../tf/compat/v1/assert_scalar.md): Asserts that the given `tensor` is a scalar (i.e. zero-dimensional).

[`assert_shapes(...)`](../../../tf/compat/v1/debugging/assert_shapes.md): Assert tensor shapes and dimension size relationships between tensors.

[`assert_type(...)`](../../../tf/compat/v1/assert_type.md): Statically asserts that the given `Tensor` is of the specified type.

[`check_numerics(...)`](../../../tf/debugging/check_numerics.md): Checks a tensor for NaN and Inf values.

[`disable_check_numerics(...)`](../../../tf/debugging/disable_check_numerics.md): Disable the eager/graph unified numerics checking mechanism.

[`enable_check_numerics(...)`](../../../tf/debugging/enable_check_numerics.md): Enable tensor numerics checking in an eager/graph unified fashion.

[`get_log_device_placement(...)`](../../../tf/debugging/get_log_device_placement.md): Get if device placements are logged.

[`is_finite(...)`](../../../tf/math/is_finite.md): Returns which elements of x are finite.

[`is_inf(...)`](../../../tf/math/is_inf.md): Returns which elements of x are Inf.

[`is_nan(...)`](../../../tf/math/is_nan.md): Returns which elements of x are NaN.

[`is_non_decreasing(...)`](../../../tf/math/is_non_decreasing.md): Returns `True` if `x` is non-decreasing.

[`is_numeric_tensor(...)`](../../../tf/debugging/is_numeric_tensor.md): Returns `True` if the elements of `tensor` are numbers.

[`is_strictly_increasing(...)`](../../../tf/math/is_strictly_increasing.md): Returns `True` if `x` is strictly increasing.

[`set_log_device_placement(...)`](../../../tf/debugging/set_log_device_placement.md): Set if device placements should be logged.

