

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distributions.bijectors.real_nvp_default_template

``` python
tf.contrib.distributions.bijectors.real_nvp_default_template(
    hidden_layers,
    shift_only=False,
    activation=tf.nn.relu,
    name=None,
    *args,
    **kwargs
)
```



Defined in [`tensorflow/contrib/distributions/python/ops/bijectors/real_nvp.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/distributions/python/ops/bijectors/real_nvp.py).

Build a scale-and-shift function using a multi-layer neural network.

This will be wrapped in a make_template to ensure the variables are only
created once. It takes the `d`-dimensional input x[0:d] and returns the `D-d`
dimensional outputs `loc` ("mu") and `log_scale` ("alpha").

#### Arguments:

* <b>`hidden_layers`</b>: Python `list`-like of non-negative integer, scalars
    indicating the number of units in each hidden layer. Default: `[512, 512].
* <b>`shift_only`</b>: Python `bool` indicating if only the `shift` term shall be
    computed (i.e. NICE bijector). Default: `False`.
* <b>`activation`</b>: Activation function (callable). Explicitly setting to `None`
    implies a linear activation.
* <b>`name`</b>: A name for ops managed by this function. Default:
    "real_nvp_default_template".
* <b>`*args`</b>: <a href="../../../../tf/layers/dense"><code>tf.layers.dense</code></a> arguments.
* <b>`**kwargs`</b>: <a href="../../../../tf/layers/dense"><code>tf.layers.dense</code></a> keyword arguments.


#### Returns:

* <b>`shift`</b>: `Float`-like `Tensor` of shift terms ("mu" in
    [Papamakarios et al.  (2016)][1]).
* <b>`log_scale`</b>: `Float`-like `Tensor` of log(scale) terms ("alpha" in
    [Papamakarios et al. (2016)][1]).


#### Raises:

* <b>`NotImplementedError`</b>: if rightmost dimension of `inputs` is unknown prior to
    graph execution.

#### References

[1]: George Papamakarios, Theo Pavlakou, and Iain Murray. Masked
     Autoregressive Flow for Density Estimation. In _Neural Information
     Processing Systems_, 2017. https://arxiv.org/abs/1705.07057