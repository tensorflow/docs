page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distributions.quadrature_scheme_lognormal_quantiles


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/distributions/python/ops/poisson_lognormal.py#L97-L168">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Use LogNormal quantiles to form quadrature on positive-reals. (deprecated)

``` python
tf.contrib.distributions.quadrature_scheme_lognormal_quantiles(
    loc,
    scale,
    quadrature_size,
    validate_args=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2018-10-01.
Instructions for updating:
The TensorFlow Distributions library has moved to TensorFlow Probability (https://github.com/tensorflow/probability). You should update all references to use <a href="/probability/api_docs/python/tfp/distributions"><code>tfp.distributions</code></a> instead of <a href="../../../tf/contrib/distributions"><code>tf.contrib.distributions</code></a>.

#### Args:


* <b>`loc`</b>: `float`-like (batch of) scalar `Tensor`; the location parameter of
  the LogNormal prior.
* <b>`scale`</b>: `float`-like (batch of) scalar `Tensor`; the scale parameter of
  the LogNormal prior.
* <b>`quadrature_size`</b>: Python `int` scalar representing the number of quadrature
  points.
* <b>`validate_args`</b>: Python `bool`, default `False`. When `True` distribution
  parameters are checked for validity despite possibly degrading runtime
  performance. When `False` invalid inputs may silently render incorrect
  outputs.
* <b>`name`</b>: Python `str` name prefixed to Ops created by this class.


#### Returns:


* <b>`grid`</b>: (Batch of) length-`quadrature_size` vectors representing the
  `log_rate` parameters of a `Poisson`.
* <b>`probs`</b>: (Batch of) length-`quadrature_size` vectors representing the
  weight associate with each `grid` value.
