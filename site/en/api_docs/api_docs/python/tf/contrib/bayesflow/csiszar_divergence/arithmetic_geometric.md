

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.csiszar_divergence.arithmetic_geometric

``` python
arithmetic_geometric(
    logu,
    self_normalized=False,
    name=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/csiszar_divergence_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/bayesflow/python/ops/csiszar_divergence_impl.py).

The Arithmetic-Geometric Csiszar-function in log-space.

A Csiszar-function is a member of,

```none
F = { f:R_+ to R : f convex }.
```

When `self_normalized = True` the Arithmetic-Geometric Csiszar-function is:

```none
f(u) = (1 + u) log( (1 + u) / sqrt(u) ) - (1 + u) log(2)
```

When `self_normalized = False` the `(1 + u) log(2)` term is omitted.

Observe that as an f-Divergence, this Csiszar-function implies:

```none
D_f[p, q] = KL[m, p] + KL[m, q]
m(x) = 0.5 p(x) + 0.5 q(x)
```

In a sense, this divergence is the "reverse" of the Jensen-Shannon
f-Divergence.

This Csiszar-function induces a symmetric f-Divergence, i.e.,
`D_f[p, q] = D_f[q, p]`.

Warning: this function makes non-log-space calculations and may therefore be
numerically unstable for `|logu| >> 0`.

#### Args:

* <b>`logu`</b>: Floating-type `Tensor` representing `log(u)` from above.
* <b>`self_normalized`</b>: Python `bool` indicating whether `f'(u=1)=0`. When
    `f'(u=1)=0` the implied Csiszar f-Divergence remains non-negative even
    when `p, q` are unnormalized measures.
* <b>`name`</b>: Python `str` name prefixed to Ops created by this function.


#### Returns:

* <b>`arithmetic_geometric_of_u`</b>: Floating-type `Tensor` of the
    Csiszar-function evaluated at `u = exp(logu)`.