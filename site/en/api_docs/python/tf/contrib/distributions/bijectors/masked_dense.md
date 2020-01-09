page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distributions.bijectors.masked_dense


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/distributions/python/ops/bijectors/masked_autoregressive.py#L358-L437">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A autoregressively masked dense layer. (deprecated)

``` python
tf.contrib.distributions.bijectors.masked_dense(
    inputs,
    units,
    num_blocks=None,
    exclusive=False,
    kernel_initializer=None,
    reuse=None,
    name=None,
    *args,
    **kwargs
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2018-10-01.
Instructions for updating:
The TensorFlow Distributions library has moved to TensorFlow Probability (https://github.com/tensorflow/probability). You should update all references to use <a href="/probability/api_docs/python/tfp/distributions"><code>tfp.distributions</code></a> instead of <a href="../../../../tf/contrib/distributions"><code>tf.contrib.distributions</code></a>.

Analogous to <a href="../../../../tf/layers/dense"><code>tf.compat.v1.layers.dense</code></a>.

See [Germain et al. (2015)][1] for detailed explanation.

#### Arguments:


* <b>`inputs`</b>: Tensor input.
* <b>`units`</b>: Python `int` scalar representing the dimensionality of the output
  space.
* <b>`num_blocks`</b>: Python `int` scalar representing the number of blocks for the
  MADE masks.
* <b>`exclusive`</b>: Python `bool` scalar representing whether to zero the diagonal of
  the mask, used for the first layer of a MADE.
* <b>`kernel_initializer`</b>: Initializer function for the weight matrix. If `None`
  (default), weights are initialized using the
  `tf.glorot_random_initializer`.
* <b>`reuse`</b>: Python `bool` scalar representing whether to reuse the weights of a
  previous layer by the same name.
* <b>`name`</b>: Python `str` used to describe ops managed by this function.
* <b>`*args`</b>: <a href="../../../../tf/layers/dense"><code>tf.compat.v1.layers.dense</code></a> arguments.
* <b>`**kwargs`</b>: <a href="../../../../tf/layers/dense"><code>tf.compat.v1.layers.dense</code></a> keyword arguments.


#### Returns:

Output tensor.



#### Raises:


* <b>`NotImplementedError`</b>: if rightmost dimension of `inputs` is unknown prior to
  graph execution.

#### References

[1]: Mathieu Germain, Karol Gregor, Iain Murray, and Hugo Larochelle. MADE:
     Masked Autoencoder for Distribution Estimation. In _International
     Conference on Machine Learning_, 2015. https://arxiv.org/abs/1502.03509
