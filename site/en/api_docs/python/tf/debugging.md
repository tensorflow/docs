description: Public API for tf.debugging namespace.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.debugging" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.debugging

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf.debugging namespace.



## Modules

[`experimental`](../tf/debugging/experimental.md) module: Public API for tf.debugging.experimental namespace.

## Functions

[`Assert(...)`](../tf/debugging/Assert.md): Asserts that the given condition is true.

[`assert_all_finite(...)`](../tf/debugging/assert_all_finite.md): Assert that the tensor does not contain any NaN's or Inf's.

[`assert_equal(...)`](../tf/debugging/assert_equal.md): Assert the condition `x == y` holds element-wise.

[`assert_greater(...)`](../tf/debugging/assert_greater.md): Assert the condition `x > y` holds element-wise.

[`assert_greater_equal(...)`](../tf/debugging/assert_greater_equal.md): Assert the condition `x >= y` holds element-wise.

[`assert_integer(...)`](../tf/debugging/assert_integer.md): Assert that `x` is of integer dtype.

[`assert_less(...)`](../tf/debugging/assert_less.md): Assert the condition `x < y` holds element-wise.

[`assert_less_equal(...)`](../tf/debugging/assert_less_equal.md): Assert the condition `x <= y` holds element-wise.

[`assert_near(...)`](../tf/debugging/assert_near.md): Assert the condition `x` and `y` are close element-wise.

[`assert_negative(...)`](../tf/debugging/assert_negative.md): Assert the condition `x < 0` holds element-wise.

[`assert_non_negative(...)`](../tf/debugging/assert_non_negative.md): Assert the condition `x >= 0` holds element-wise.

[`assert_non_positive(...)`](../tf/debugging/assert_non_positive.md): Assert the condition `x <= 0` holds element-wise.

[`assert_none_equal(...)`](../tf/debugging/assert_none_equal.md): Assert the condition `x != y` holds for all elements.

[`assert_positive(...)`](../tf/debugging/assert_positive.md): Assert the condition `x > 0` holds element-wise.

[`assert_proper_iterable(...)`](../tf/debugging/assert_proper_iterable.md): Static assert that values is a "proper" iterable.

[`assert_rank(...)`](../tf/debugging/assert_rank.md): Assert that `x` has rank equal to `rank`.

[`assert_rank_at_least(...)`](../tf/debugging/assert_rank_at_least.md): Assert that `x` has rank of at least `rank`.

[`assert_rank_in(...)`](../tf/debugging/assert_rank_in.md): Assert that `x` has a rank in `ranks`.

[`assert_same_float_dtype(...)`](../tf/debugging/assert_same_float_dtype.md): Validate and return float type based on `tensors` and `dtype`.

[`assert_scalar(...)`](../tf/debugging/assert_scalar.md): Asserts that the given `tensor` is a scalar.

[`assert_shapes(...)`](../tf/debugging/assert_shapes.md): Assert tensor shapes and dimension size relationships between tensors.

[`assert_type(...)`](../tf/debugging/assert_type.md): Asserts that the given `Tensor` is of the specified type.

[`check_numerics(...)`](../tf/debugging/check_numerics.md): Checks a tensor for NaN and Inf values.

[`disable_check_numerics(...)`](../tf/debugging/disable_check_numerics.md): Disable the eager/graph unified numerics checking mechanism.

[`enable_check_numerics(...)`](../tf/debugging/enable_check_numerics.md): Enable tensor numerics checking in an eager/graph unified fashion.

[`get_log_device_placement(...)`](../tf/debugging/get_log_device_placement.md): Get if device placements are logged.

[`is_numeric_tensor(...)`](../tf/debugging/is_numeric_tensor.md): Returns `True` if the elements of `tensor` are numbers.

[`set_log_device_placement(...)`](../tf/debugging/set_log_device_placement.md): Set if device placements should be logged.

