

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.layers.conv2d_flipout

### Aliases:

* `tf.contrib.bayesflow.layers.conv2d_flipout`
* `tf.contrib.bayesflow.layers.convolution2d_flipout`

``` python
tf.contrib.bayesflow.layers.conv2d_flipout(
    inputs,
    filters,
    kernel_size,
    strides=(1, 1),
    padding='valid',
    data_format='channels_last',
    dilation_rate=(1, 1),
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
    seed=None,
    name=None,
    reuse=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/layers_conv_variational.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/bayesflow/python/ops/layers_conv_variational.py).

Functional interface for the 2D convolution layer.

This layer creates a convolution kernel that is convolved
(actually cross-correlated) with the layer input to produce a tensor of
outputs. It may also include a bias addition and activation function
on the outputs. It assumes the `kernel` and/or `bias` are drawn from
distributions.

By default, the layer implements a stochastic forward pass via
sampling from the kernel and bias posteriors,

```none
outputs = f(inputs; kernel, bias), kernel, bias ~ posterior
```
where f denotes the layer's calculation. It uses the Flipout
estimator [1], which performs a Monte Carlo approximation of the
distribution integrating over the `kernel` and `bias`. Flipout uses
roughly twice as many floating point operations as the
reparameterization estimator but has the advantage of significantly
lower variance.

The arguments permit separate specification of the surrogate posterior
(`q(W|x)`), prior (`p(W)`), and divergence for both the `kernel` and `bias`
distributions.

#### Arguments:

* <b>`inputs`</b>: Tensor input.
* <b>`filters`</b>: Integer, the dimensionality of the output space (i.e. the number
    of filters in the convolution).
* <b>`kernel_size`</b>: An integer or tuple/list of 2 integers, specifying the
    height and width of the 2D convolution window.
    Can be a single integer to specify the same value for
    all spatial dimensions.
* <b>`strides`</b>: An integer or tuple/list of 2 integers,
    specifying the strides of the convolution along the height and width.
    Can be a single integer to specify the same value for
    all spatial dimensions.
    Specifying any stride value != 1 is incompatible with specifying
    any `dilation_rate` value != 1.
* <b>`padding`</b>: One of `"valid"` or `"same"` (case-insensitive).
* <b>`data_format`</b>: A string, one of `channels_last` (default) or `channels_first`.
    The ordering of the dimensions in the inputs.
    `channels_last` corresponds to inputs with shape
    `(batch, height, width, channels)` while `channels_first` corresponds to
    inputs with shape `(batch, channels, height, width)`.

* <b>`dilation_rate`</b>: An integer or tuple/list of 2 integers, specifying
    the dilation rate to use for dilated convolution.
    Can be a single integer to specify the same value for
    all spatial dimensions.
    Currently, specifying any `dilation_rate` value != 1 is
    incompatible with specifying any stride value != 1.
* <b>`activation`</b>: Activation function. Set it to None to maintain a
    linear activation.
* <b>`activity_regularizer`</b>: Optional regularizer function for the output.
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
* <b>`seed`</b>: Python scalar `int` which initializes the random number
    generator. Default value: `None` (i.e., use global seed).
* <b>`name`</b>: A string, the name of the layer.
* <b>`reuse`</b>: Boolean, whether to reuse the weights of a previous layer
    by the same name.


#### Returns:

Output tensor.


#### Raises:

* <b>`ValueError`</b>: if eager execution is enabled.

#### Examples

We illustrate a Bayesian neural network with [variational inference](
https://en.wikipedia.org/wiki/Variational_Bayesian_methods),
assuming a dataset of `features` and `labels`.

```python
tfp = tf.contrib.bayesflow

net = tf.reshape(features, [-1, 32, 32, 3])
net = tfp.layers.conv2d_flipout(net,
                                filters=64,
                                kernel_size=5,
                                padding="SAME",
                                activation=tf.nn.relu)
net = tf.layers.max_pooling2d(net,
                              pool_size=2,
                              strides=2,
                              padding="SAME")
net = tf.reshape(net, [-1, 8 * 8 * 64])
logits = tfp.layers.dense_flipout(net, 10)
neg_log_likelihood = tf.nn.softmax_cross_entropy_with_logits(
    labels=labels, logits=logits)
kl = sum(tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES))
loss = neg_log_likelihood + kl
train_op = tf.train.AdamOptimizer().minimize(loss)
```

It uses the Flipout gradient estimator to minimize the
Kullback-Leibler divergence up to a constant, also known as the
negative Evidence Lower Bound. It consists of the sum of two terms:
the expected negative log-likelihood, which we approximate via
Monte Carlo; and the KL divergence, which is added via regularizer
terms which are arguments to the layer.

[1]: "Flipout: Efficient Pseudo-Independent Weight Perturbations on
      Mini-Batches."
      Anonymous. OpenReview, 2017.
      https://openreview.net/forum?id=rJnpifWAb