

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.layers.dense_local_reparameterization

``` python
tf.contrib.bayesflow.layers.dense_local_reparameterization(
    inputs,
    units,
    activation=None,
    activity_regularizer=None,
    trainable=True,
    kernel_posterior_fn=layers_util.default_mean_field_normal_fn(),
    kernel_posterior_tensor_fn=lambda d: d.sample(),
    kernel_prior_fn=lambda dtype, *args: normal_lib.Normal(loc=dtype.as_numpy_dtype(0.0), scale=dtype.as_numpy_dtype(1.0)),
    kernel_divergence_fn=lambda q, p, ignore: kl_lib.kl_divergence(q, p),
    bias_posterior_fn=layers_util.default_mean_field_normal_fn(is_singular=True),
    bias_posterior_tensor_fn=lambda d: d.sample(),
    bias_prior_fn=None,
    bias_divergence_fn=lambda q, p, ignore: kl_lib.kl_divergence(q, p),
    name=None,
    reuse=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/layers_dense_variational.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/bayesflow/python/ops/layers_dense_variational.py).

Densely-connected layer with local reparameterization estimator.

This layer implements the Bayesian variational inference analogue to
a dense layer by assuming the `kernel` and/or the `bias` are drawn
from distributions. By default, the layer implements a stochastic
forward pass via sampling from the kernel and bias posteriors,

```none
kernel, bias ~ posterior
outputs = activation(matmul(inputs, kernel) + bias)
```

It uses the local reparameterization estimator [1], which performs a
Monte Carlo approximation of the distribution on the hidden units
induced by the `kernel` and `bias`.

The arguments permit separate specification of the surrogate posterior
(`q(W|x)`), prior (`p(W)`), and divergence for both the `kernel` and `bias`
distributions.

#### Args:

* <b>`inputs`</b>: Tensor input.
* <b>`units`</b>: Integer or Long, dimensionality of the output space.
* <b>`activation`</b>: Activation function (`callable`). Set it to None to maintain a
    linear activation.
* <b>`activity_regularizer`</b>: Regularizer function for the output.
* <b>`trainable`</b>: Boolean, if `True` also add variables to the graph collection
    `GraphKeys.TRAINABLE_VARIABLES` (see `tf.Variable`).
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

#### Examples

We illustrate a Bayesian neural network with [variational inference](
https://en.wikipedia.org/wiki/Variational_Bayesian_methods),
assuming a dataset of `features` and `labels`.

```python
tfp = tf.contrib.bayesflow

net = tfp.layers.dense_local_reparameterization(
    features, 512, activation=tf.nn.relu)
logits = tfp.layers.dense_local_reparameterization(net, 10)
neg_log_likelihood = tf.nn.softmax_cross_entropy_with_logits(
    labels=labels, logits=logits)
kl = sum(tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES))
loss = neg_log_likelihood + kl
train_op = tf.train.AdamOptimizer().minimize(loss)
```

It uses local reparameterization gradients to minimize the
Kullback-Leibler divergence up to a constant, also known as the
negative Evidence Lower Bound. It consists of the sum of two terms:
the expected negative log-likelihood, which we approximate via
Monte Carlo; and the KL divergence, which is added via regularizer
terms which are arguments to the layer.

[1]: "Variational Dropout and the Local Reparameterization Trick."
      Diederik P. Kingma, Tim Salimans, Max Welling.
      Neural Information Processing Systems, 2015.