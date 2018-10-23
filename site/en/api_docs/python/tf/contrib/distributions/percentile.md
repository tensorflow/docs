

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.distributions.percentile

``` python
percentile(
    x,
    q,
    axis=None,
    interpolation=None,
    keep_dims=False,
    validate_args=False,
    name=None
)
```



Defined in [`tensorflow/contrib/distributions/python/ops/sample_stats.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/distributions/python/ops/sample_stats.py).

Compute the `q`-th percentile of `x`.

Given a vector `x`, the `q`-th percentile of `x` is the value `q / 100` of the
way from the minimum to the maximum in a sorted copy of `x`.

The values and distances of the two nearest neighbors as well as the
`interpolation` parameter will determine the percentile if the normalized
ranking does not match the location of `q` exactly.

This function is the same as the median if `q = 50`, the same as the minimum
if `q = 0` and the same as the maximum if `q = 100`.


```python
# Get 30th percentile with default ('nearest') interpolation.
x = [1., 2., 3., 4.]
percentile(x, q=30.)
==> 2.0

# Get 30th percentile with 'lower' interpolation
x = [1., 2., 3., 4.]
percentile(x, q=30., interpolation='lower')
==> 1.0

# Get 100th percentile (maximum).  By default, this is computed over every dim
x = [[1., 2.]
     [3., 4.]]
percentile(x, q=100.)
==> 4.0

# Treat the leading dim as indexing samples, and find the 100th quantile (max)
# over all such samples.
x = [[1., 2.]
     [3., 4.]]
percentile(x, q=100., axis=[0])
==> [3., 4.]
```

Compare to `numpy.percentile`.

#### Args:

* <b>`x`</b>:  Floating point `N-D` `Tensor` with `N > 0`.  If `axis` is not `None`,
    `x` must have statically known number of dimensions.
* <b>`q`</b>:  Scalar `Tensor` in `[0, 100]`. The percentile.
* <b>`axis`</b>:  Optional `0-D` or `1-D` integer `Tensor` with constant values.
    The axis that hold independent samples over which to return the desired
    percentile.  If `None` (the default), treat every dimension as a sample
    dimension, returning a scalar.
* <b>`interpolation `</b>: {"lower", "higher", "nearest"}.  Default: "nearest"
    This optional parameter specifies the interpolation method to
    use when the desired quantile lies between two data points `i < j`:
      * lower: `i`.
      * higher: `j`.
      * nearest: `i` or `j`, whichever is nearest.
* <b>`keep_dims`</b>:  Python `bool`. If `True`, the last dimension is kept with size 1
    If `False`, the last dimension is removed from the output shape.
* <b>`validate_args`</b>:  Whether to add runtime checks of argument validity.
    If False, and arguments are incorrect, correct behavior is not guaranteed.
* <b>`name`</b>:  A Python string name to give this `Op`.  Default is "percentile"


#### Returns:

A `(N - len(axis))` dimensional `Tensor` of same dtype as `x`, or, if
  `axis` is `None`, a scalar.


#### Raises:

* <b>`ValueError`</b>:  If argument 'interpolation' is not an allowed type.