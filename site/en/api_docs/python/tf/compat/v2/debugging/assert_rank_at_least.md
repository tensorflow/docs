page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.debugging.assert_rank_at_least

Assert that `x` has rank of at least `rank`.

``` python
tf.compat.v2.debugging.assert_rank_at_least(
    x,
    rank,
    message=None,
    name=None
)
```



Defined in [`python/ops/check_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/check_ops.py).

<!-- Placeholder for "Used in" -->

This Op checks that the rank of `x` is greater or equal to `rank`.

If `x` has a rank lower than `rank`, `message`, as well as the shape of `x`
are printed, and `InvalidArgumentError` is raised.

#### Args:


* <b>`x`</b>: `Tensor`.
* <b>`rank`</b>: Scalar integer `Tensor`.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>: A name for this operation (optional).  Defaults to
  "assert_rank_at_least".


#### Returns:

Op raising `InvalidArgumentError` unless `x` has specified rank or higher.
If static checks determine `x` has correct rank, a `no_op` is returned.
This can be used with <a href="../../../../tf/control_dependencies"><code>tf.control_dependencies</code></a> inside of <a href="../../../../tf/function"><code>tf.function</code></a>s
to block followup computation until the check has executed.




#### Raises:


* <b>`InvalidArgumentError`</b>: `x` does not have rank at least `rank`, but the rank
  cannot be statically determined.
* <b>`ValueError`</b>: If static checks determine `x` has mismatched rank.

#### Eager Compatibility
returns None

