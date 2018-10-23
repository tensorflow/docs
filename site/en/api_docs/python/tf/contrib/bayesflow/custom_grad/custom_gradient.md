

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.custom_grad.custom_gradient

``` python
tf.contrib.bayesflow.custom_grad.custom_gradient(
    fx,
    gx,
    x,
    axis=(),
    fx_gx_manually_stopped=False,
    name=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/custom_grad_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/bayesflow/python/ops/custom_grad_impl.py).

Enables specifying a custom gradient.

This function works by clever application of `stop_gradient`. I.e., observe
that:

```none
h(x) = x * stop_gradient(g(x)) + stop_gradient(f(x) - x * g(x))
```

is such that `h(x) = stop_gradient(f(x))` and `grad[h(x), x] =
stop_gradient(g(x)).`

In addition to scalar-domain/scalar-range functions, this function also
supports tensor-domain/scalar-range functions. However, in the latter case it
is necessary to reduce `x` to a scalar. This can be done by indicating the
`axis` over which `f` operates or by appropriately `reduce_sum`-ing `x`, prior
to calling this function.

Partial Custom Gradient:

Suppose `h(x) = htilde(x, y)`. Note that `dh/dx = stop(g(x))` but `dh/dy =
None`. This is because a `Tensor` cannot have only a portion of its gradient
stopped. To circumvent this issue, one must manually `stop_gradient` the
relevant portions of `f`, `g`. For example see the unit-test,
`test_works_correctly_fx_gx_manually_stopped`.

#### Args:

* <b>`fx`</b>: `Tensor`. Output of function evaluated at `x`.
* <b>`gx`</b>: `Tensor`. Gradient of function evaluated at `x`.
* <b>`x`</b>: `Tensor`. Point of evaluation for `f, g`.
* <b>`axis`</b>: 1D `int` `Tensor` representing dimensions of `x` which are the domain
    of `f`. If `()` (the default), `f` is assumed scalar-domain/scalar-range.
    If `None` `f` is assumed to render one scalar given all of `x`. Otherwise
    `f` is assumed to output one scalar for each of `axis` dimensions of `x`.
* <b>`fx_gx_manually_stopped`</b>: Python `bool` indicating that `fx`, `gx` manually
    have `stop_gradient` applied.
* <b>`name`</b>: Python `str` name prefixed to Ops created by this function.


#### Returns:

* <b>`fx`</b>: Floating-type `Tensor` equal to `f(x)` but which has gradient
    `stop_gradient(g(x))`.