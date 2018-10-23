

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.variational_inference.ELBOForms

## Class `ELBOForms`





Defined in [`tensorflow/contrib/bayesflow/python/ops/variational_inference_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/bayesflow/python/ops/variational_inference_impl.py).

See the guide: [BayesFlow Variational Inference (contrib) > Ops](../../../../../../api_guides/python/contrib.bayesflow.variational_inference#Ops)

Constants to control the `elbo` calculation.

`analytic_kl` uses the analytic KL divergence between the
variational distribution(s) and the prior(s).

`analytic_entropy` uses the analytic entropy of the variational
distribution(s).

`sample` uses the sample KL or the sample entropy is the joint is provided.

See `elbo` for what is used with `default`.

## Methods

<h3 id="check_form"><code>check_form</code></h3>

``` python
check_form(form)
```





## Class Members

<h3 id="analytic_entropy"><code>analytic_entropy</code></h3>

<h3 id="analytic_kl"><code>analytic_kl</code></h3>

<h3 id="default"><code>default</code></h3>

<h3 id="sample"><code>sample</code></h3>

