

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.bayesflow.stochastic_tensor.StochasticTensor

### `class tf.contrib.bayesflow.stochastic_tensor.StochasticTensor`



Defined in [`tensorflow/contrib/bayesflow/python/ops/stochastic_tensor_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/bayesflow/python/ops/stochastic_tensor_impl.py).

See the guide: [BayesFlow Stochastic Tensors (contrib) > Stochastic Tensor Classes](../../../../../../api_guides/python/contrib.bayesflow.stochastic_tensor#Stochastic_Tensor_Classes)

StochasticTensor is a BaseStochasticTensor backed by a distribution.

## Properties

<h3 id="distribution"><code>distribution</code></h3>



<h3 id="dtype"><code>dtype</code></h3>



<h3 id="graph"><code>graph</code></h3>



<h3 id="name"><code>name</code></h3>



<h3 id="value_type"><code>value_type</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    dist,
    name='StochasticTensor',
    dist_value_type=None,
    loss_fn=sge.score_function
)
```

Construct a `StochasticTensor`.

`StochasticTensor` is backed by the `dist` distribution and its `value`
method will return the same value each time it is called. What `value` is
returned is controlled by the `dist_value_type` (defaults to
`SampleValue`).

Some distributions' sample functions are not differentiable (e.g. a sample
from a discrete distribution like a Bernoulli) and so to differentiate
wrt parameters upstream of the sample requires a gradient estimator like
the score function estimator. This is accomplished by passing a
differentiable `loss_fn` to the `StochasticTensor`, which
defaults to a function whose derivative is the score function estimator.
Calling `stochastic_graph.surrogate_loss(final_losses)` will call
`loss()` on every `StochasticTensor` upstream of final losses.

`loss()` will return None for `StochasticTensor`s backed by
reparameterized distributions; it will also return None if the value type is
`MeanValueType` or if `loss_fn=None`.

#### Args:

* <b>`dist`</b>: an instance of `Distribution`.
* <b>`name`</b>: a name for this `StochasticTensor` and its ops.
* <b>`dist_value_type`</b>: a `_StochasticValueType`, which will determine what the
      `value` of this `StochasticTensor` will be. If not provided, the
      value type set with the `value_type` context manager will be used.
* <b>`loss_fn`</b>: callable that takes
      `(st, st.value(), influenced_loss)`, where
      `st` is this `StochasticTensor`, and returns a `Tensor` loss. By
      default, `loss_fn` is the `score_function`, or more precisely, the
      integral of the score function, such that when the gradient is taken,
      the score function results. See the `stochastic_gradient_estimators`
      module for additional loss functions and baselines.


#### Raises:

* <b>`TypeError`</b>: if `dist` is not an instance of `Distribution`.
* <b>`TypeError`</b>: if `loss_fn` is not `callable`.

<h3 id="entropy"><code>entropy</code></h3>

``` python
entropy(name='entropy')
```



<h3 id="loss"><code>loss</code></h3>

``` python
loss(
    final_loss,
    name='Loss'
)
```



<h3 id="mean"><code>mean</code></h3>

``` python
mean(name='mean')
```



<h3 id="value"><code>value</code></h3>

``` python
value(name='value')
```





