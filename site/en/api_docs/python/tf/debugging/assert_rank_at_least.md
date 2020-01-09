page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_rank_at_least


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/check_ops.py#L1270-L1300">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Assert that `x` has rank of at least `rank`.

### Aliases:

* `tf.compat.v2.debugging.assert_rank_at_least`


``` python
tf.debugging.assert_rank_at_least(
    x,
    rank,
    message=None,
    name=None
)
```



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
This can be used with <a href="../../tf/control_dependencies"><code>tf.control_dependencies</code></a> inside of <a href="../../tf/function"><code>tf.function</code></a>s
to block followup computation until the check has executed.




#### Raises:


* <b>`InvalidArgumentError`</b>: `x` does not have rank at least `rank`, but the rank
  cannot be statically determined.
* <b>`ValueError`</b>: If static checks determine `x` has mismatched rank.

#### Eager Compatibility
returns None
