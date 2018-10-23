

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.csiszar_divergence.dual_csiszar_function

``` python
dual_csiszar_function(
    logu,
    csiszar_function,
    name=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/csiszar_divergence_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/bayesflow/python/ops/csiszar_divergence_impl.py).

Calculates the dual Csiszar-function in log-space.

A Csiszar-function is a member of,

```none
F = { f:R_+ to R : f convex }.
```

The Csiszar-dual is defined as:

```none
f^*(u) = u f(1 / u)
```

where `f` is some other Csiszar-function.

For example, the dual of `kl_reverse` is `kl_forward`, i.e.,

```none
f(u) = -log(u)
f^*(u) = u f(1 / u) = -u log(1 / u) = u log(u)
```

The dual of the dual is the original function:

```none
f^**(u) = {u f(1/u)}^*(u) = u (1/u) f(1/(1/u)) = f(u)
```

Warning: this function makes non-log-space calculations and may therefore be
numerically unstable for `|logu| >> 0`.

#### Args:

* <b>`logu`</b>: `float`-like `Tensor` representing `log(u)` from above.
* <b>`csiszar_function`</b>: Python `callable` representing a Csiszar-function over
    log-domain.
* <b>`name`</b>: Python `str` name prefixed to Ops created by this function.


#### Returns:

* <b>`dual_f_of_u`</b>: `float`-like `Tensor` of the result of calculating the dual of
    `f` at `u = exp(logu)`.