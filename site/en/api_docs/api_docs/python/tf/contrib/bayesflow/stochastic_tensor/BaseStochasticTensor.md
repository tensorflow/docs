

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.stochastic_tensor.BaseStochasticTensor

## Class `BaseStochasticTensor`





Defined in [`tensorflow/contrib/bayesflow/python/ops/stochastic_tensor_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/bayesflow/python/ops/stochastic_tensor_impl.py).

See the guide: [BayesFlow Stochastic Tensors (contrib) > Stochastic Tensor Classes](../../../../../../api_guides/python/contrib.bayesflow.stochastic_tensor#Stochastic_Tensor_Classes)

Base Class for Tensor-like objects that emit stochastic values.

## Properties

<h3 id="dtype"><code>dtype</code></h3>



<h3 id="graph"><code>graph</code></h3>



<h3 id="name"><code>name</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__()
```



<h3 id="loss"><code>loss</code></h3>

``` python
loss(sample_loss)
```

Returns the term to add to the surrogate loss.

This method is called by `surrogate_loss`.  The input `sample_loss` should
have already had `stop_gradient` applied to it.  This is because the
surrogate_loss usually provides a Monte Carlo sample term of the form
`differentiable_surrogate * sample_loss` where `sample_loss` is considered
constant with respect to the input for purposes of the gradient.

#### Args:

* <b>`sample_loss`</b>: `Tensor`, sample loss downstream of this `StochasticTensor`.


#### Returns:

  Either `None` or a `Tensor`.

<h3 id="value"><code>value</code></h3>

``` python
value(name=None)
```





