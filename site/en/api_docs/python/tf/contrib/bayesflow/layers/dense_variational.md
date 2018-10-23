

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.layers.dense_variational

``` python
dense_variational(
    inputs,
    units,
    activation=None,
    activity_regularizer=None,
    trainable=True,
    kernel_use_local_reparameterization=True,
    kernel_posterior_fn=default_mean_field_normal_fn(),
    kernel_posterior_tensor_fn=lambda d: d.sample(),
    kernel_prior_fn=lambda dtype, *args: normal_lib.Normal(loc=dtype.as_numpy_dtype(0.0), scale=dtype.as_numpy_dtype(1.0)),
    kernel_divergence_fn=lambda q, p, ignore: kl_lib.kl_divergence(q, p),
    bias_posterior_fn=default_mean_field_normal_fn(is_singular=True),
    bias_posterior_tensor_fn=lambda d: d.sample(),
    bias_prior_fn=None,
    bias_divergence_fn=lambda q, p, ignore: kl_lib.kl_divergence(q, p),
    name=None,
    reuse=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/layers_dense_variational_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/bayesflow/python/ops/layers_dense_variational_impl.py).

Densely-connected variational layer.

This layer implements the Bayesian variational inference analogue to:
`outputs = activation(matmul(inputs, kernel) + bias)`
by assuming the `kernel` and/or the `bias` are random variables.

The layer implements a stochastic dense calculation by making a Monte Carlo
approximation of a [variational Bayesian method based on KL divergence](
https://en.wikipedia.org/wiki/Variational_Bayesian_methods), i.e.,

```none
-log p(y|x) = -log int_{R**d} p(y|x,w) p(w) dw
            = -log int_{R**d} p(y,w|x) q(w|x) / q(w|x) dw
           <= E_q(W|x)[-log p(y,W|x) + log q(W|x)]       # Jensen's
            = E_q(W|x)[-log p(y|x,W)] + KL[q(W|x), p(W)]
           ~= m**-1 sum{ -log(y|x,w[j]) : w[j] ~ q(W|x), j=1..m }
               + KL[q(W|x), p(W)]
```

where `W` denotes the (independent) `kernel` and `bias` random variables, `w`
is a random variate or outcome of `W`, `y` is the label, `x` is the evidence`,
and `~=` denotes an approximation which becomes exact as `m->inf`. The above
bound is sometimes referred to as the negative Evidence Lower BOund or
negative [ELBO](https://arxiv.org/abs/1601.00670). In context of a DNN, this
layer is appropriate to use when the final loss is a negative log-likelihood.

The Monte-Carlo sum portion is used for the feed-forward calculation of the
DNN. The KL divergence portion can be added to the final loss via:
`loss += sum(tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES))`.

The arguments permit separate specification of the surrogate posterior
(`q(W|x)`), prior (`p(W)`), and divergence for both the `kernel` and `bias`
random variables (which together comprise `W`).

#### Args:

* <b>`inputs`</b>: Tensor input.
* <b>`units`</b>: Integer or Long, dimensionality of the output space.
* <b>`activation`</b>: Activation function (`callable`). Set it to None to maintain a
    linear activation.
* <b>`activity_regularizer`</b>: Regularizer function for the output.
* <b>`trainable`</b>: Boolean, if `True` also add variables to the graph collection
    `GraphKeys.TRAINABLE_VARIABLES` (see `tf.Variable`).
* <b>`kernel_use_local_reparameterization`</b>: Python `bool` indicating whether
    `kernel` calculation should employ the Local Reparameterization Trick.
    When `True`, `kernel_posterior_fn` must create an instance of
    `tf.distributions.Normal`.
* <b>`kernel_posterior_fn`</b>: Python `callable` which creates
    `tf.distributions.Distribution` instance representing the surrogate
    posterior of the `kernel` parameter. Default value:
    `default_mean_field_normal_fn()`.
* <b>`kernel_posterior_tensor_fn`</b>: Python `callable` which takes a
    `tf.distributions.Distribution` instance and returns a representative
    value. Default value: `lambda d: d.sample()`.
* <b>`kernel_prior_fn`</b>: Python `callable` which creates `tf.distributions`
    instance. See `default_mean_field_normal_fn` docstring for required
    parameter signature.
    Default value: `tf.distributions.Normal(loc=0., scale=1.)`.
* <b>`kernel_divergence_fn`</b>: Python `callable` which takes the surrogate posterior
    distribution, prior distribution and random variate sample(s) from the
    surrogate posterior and computes or approximates the KL divergence. The
    distributions are `tf.distributions.Distribution`-like instances and the
    sample is a `Tensor`.
* <b>`bias_posterior_fn`</b>: Python `callable` which creates
    `tf.distributions.Distribution` instance representing the surrogate
    posterior of the `bias` parameter. Default value:
    `default_mean_field_normal_fn(is_singular=True)` (which creates an
    instance of `tf.distributions.Deterministic`).
* <b>`bias_posterior_tensor_fn`</b>: Python `callable` which takes a
    `tf.distributions.Distribution` instance and returns a representative
    value. Default value: `lambda d: d.sample()`.
* <b>`bias_prior_fn`</b>: Python `callable` which creates `tf.distributions` instance.
    See `default_mean_field_normal_fn` docstring for required parameter
    signature. Default value: `None` (no prior, no variational inference)
* <b>`bias_divergence_fn`</b>: Python `callable` which takes the surrogate posterior
    distribution, prior distribution and random variate sample(s) from the
    surrogate posterior and computes or approximates the KL divergence. The
    distributions are `tf.distributions.Distribution`-like instances and the
    sample is a `Tensor`.
* <b>`name`</b>: Python `str`, the name of the layer. Layers with the same name will
    share `tf.Variable`s, but to avoid mistakes we require `reuse=True` in
    such cases.
* <b>`reuse`</b>: Python `bool`, whether to reuse the `tf.Variable`s of a previous
    layer by the same name.


#### Returns:

* <b>`output`</b>: `Tensor` representing a the affine transformed input under a random
    draw from the surrogate posterior distribution.