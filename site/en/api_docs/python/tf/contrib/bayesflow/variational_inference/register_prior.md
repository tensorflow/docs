

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.bayesflow.variational_inference.register_prior

### `tf.contrib.bayesflow.variational_inference.register_prior`

``` python
register_prior(
    variational,
    prior
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/variational_inference_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/bayesflow/python/ops/variational_inference_impl.py).

See the guide: [BayesFlow Variational Inference (contrib) > Ops](../../../../../../api_guides/python/contrib.bayesflow.variational_inference#Ops)

Associate a variational `StochasticTensor` with a `Distribution` prior.

This is a helper function used in conjunction with `elbo` that allows users
to specify the mapping between variational distributions and their priors
without having to pass in `variational_with_prior` explicitly.

#### Args:

* <b>`variational`</b>: `StochasticTensor` q(Z). Approximating distribution.
* <b>`prior`</b>: `Distribution` p(Z). Prior distribution.


#### Returns:

  None


#### Raises:

* <b>`ValueError`</b>: if variational is not a `StochasticTensor` or `prior` is not
    a `Distribution`.