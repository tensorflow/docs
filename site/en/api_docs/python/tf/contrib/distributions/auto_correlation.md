page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distributions.auto_correlation

``` python
tf.contrib.distributions.auto_correlation(
    x,
    axis=-1,
    max_lags=None,
    center=True,
    normalize=True,
    name='auto_correlation'
)
```



Defined in [`tensorflow/contrib/distributions/python/ops/sample_stats.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/distributions/python/ops/sample_stats.py).

Auto correlation along one axis.

Given a `1-D` wide sense stationary (WSS) sequence `X`, the auto correlation
`RXX` may be defined as  (with `E` expectation and `Conj` complex conjugate)

```
RXX[m] := E{ W[m] Conj(W[0]) } = E{ W[0] Conj(W[-m]) },
W[n]   := (X[n] - MU) / S,
MU     := E{ X[0] },
S**2   := E{ (X[0] - MU) Conj(X[0] - MU) }.
```

This function takes the viewpoint that `x` is (along one axis) a finite
sub-sequence of a realization of (WSS) `X`, and then uses `x` to produce an
estimate of `RXX[m]` as follows:

After extending `x` from length `L` to `inf` by zero padding, the auto
correlation estimate `rxx[m]` is computed for `m = 0, 1, ..., max_lags` as

```
rxx[m] := (L - m)**-1 sum_n w[n + m] Conj(w[n]),
w[n]   := (x[n] - mu) / s,
mu     := L**-1 sum_n x[n],
s**2   := L**-1 sum_n (x[n] - mu) Conj(x[n] - mu)
```

The error in this estimate is proportional to `1 / sqrt(len(x) - m)`, so users
often set `max_lags` small enough so that the entire output is meaningful.

Note that since `mu` is an imperfect estimate of `E{ X[0] }`, and we divide by
`len(x) - m` rather than `len(x) - m - 1`, our estimate of auto correlation
contains a slight bias, which goes to zero as `len(x) - m --> infinity`.

#### Args:

* <b>`x`</b>:  `float32` or `complex64` `Tensor`.
* <b>`axis`</b>:  Python `int`. The axis number along which to compute correlation.
    Other dimensions index different batch members.
* <b>`max_lags`</b>:  Positive `int` tensor.  The maximum value of `m` to consider
    (in equation above).  If `max_lags >= x.shape[axis]`, we effectively
    re-set `max_lags` to `x.shape[axis] - 1`.
* <b>`center`</b>:  Python `bool`.  If `False`, do not subtract the mean estimate `mu`
    from `x[n]` when forming `w[n]`.
* <b>`normalize`</b>:  Python `bool`.  If `False`, do not divide by the variance
    estimate `s**2` when forming `w[n]`.
* <b>`name`</b>:  `String` name to prepend to created ops.


#### Returns:

`rxx`: `Tensor` of same `dtype` as `x`.  `rxx.shape[i] = x.shape[i]` for
  `i != axis`, and `rxx.shape[axis] = max_lags + 1`.


#### Raises:

* <b>`TypeError`</b>:  If `x` is not a supported type.