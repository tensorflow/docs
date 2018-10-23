

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.assign

``` python
tf.assign(
    ref,
    value,
    validate_shape=None,
    use_locking=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/state_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/ops/state_ops.py).

See the guide: [Variables > Variable helper functions](../../../api_guides/python/state_ops#Variable_helper_functions)

Update 'ref' by assigning 'value' to it.

This operation outputs a Tensor that holds the new value of 'ref' after
  the value has been assigned. This makes it easier to chain operations
  that need to use the reset value.

#### Args:

* <b>`ref`</b>: A mutable `Tensor`.
    Should be from a `Variable` node. May be uninitialized.
* <b>`value`</b>: A `Tensor`. Must have the same type as `ref`.
    The value to be assigned to the variable.
* <b>`validate_shape`</b>: An optional `bool`. Defaults to `True`.
    If true, the operation will validate that the shape
    of 'value' matches the shape of the Tensor being assigned to.  If false,
    'ref' will take on the shape of 'value'.
* <b>`use_locking`</b>: An optional `bool`. Defaults to `True`.
    If True, the assignment will be protected by a lock;
    otherwise the behavior is undefined, but may exhibit less contention.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` that will hold the new value of 'ref' after
  the assignment has completed.