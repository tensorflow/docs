

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.loss_functions.CategoricalLogitsNegativeLogProbLoss

## Class `CategoricalLogitsNegativeLogProbLoss`

Inherits From: [`DistributionNegativeLogProbLoss`](../../../../tf/contrib/kfac/loss_functions/DistributionNegativeLogProbLoss), [`NaturalParamsNegativeLogProbLoss`](../../../../tf/contrib/kfac/loss_functions/NaturalParamsNegativeLogProbLoss)



Defined in [`tensorflow/contrib/kfac/python/ops/loss_functions.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/kfac/python/ops/loss_functions.py).

Neg log prob loss for a categorical distribution parameterized by logits.


Note that the Fisher (for a single case) of a categorical distribution, with
respect to the natural parameters (i.e. the logits), is given by:

F = diag(p) - p*p^T

where p = softmax(logits).  F can be factorized as F = B * B^T where

B = diag(q) - p*q^T

where q is the entry-wise square root of p. This is easy to verify using the
fact that q^T*q = 1.

## Properties

<h3 id="dist"><code>dist</code></h3>



<h3 id="fisher_factor_inner_shape"><code>fisher_factor_inner_shape</code></h3>



<h3 id="fisher_factor_inner_static_shape"><code>fisher_factor_inner_static_shape</code></h3>



<h3 id="hessian_factor_inner_shape"><code>hessian_factor_inner_shape</code></h3>



<h3 id="hessian_factor_inner_static_shape"><code>hessian_factor_inner_static_shape</code></h3>



<h3 id="input_minibatches"><code>input_minibatches</code></h3>



<h3 id="inputs"><code>inputs</code></h3>



<h3 id="num_registered_minibatches"><code>num_registered_minibatches</code></h3>

Number of minibatches registered for this LossFunction.

Typically equal to the number of towers in a multi-tower setup.

#### Returns:

An `int` representing the number of registered minibatches.

<h3 id="params"><code>params</code></h3>



<h3 id="targets"><code>targets</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    logits,
    targets=None,
    seed=None
)
```

Instantiates a CategoricalLogitsNegativeLogProbLoss.

#### Args:

* <b>`logits`</b>: Tensor of shape [batch_size, output_size]. Parameters for
    underlying distribution.
* <b>`targets`</b>: None or Tensor of shape [output_size]. Each elements contains an
    index in [0, output_size).
* <b>`seed`</b>: int or None. Default random seed when sampling.

<h3 id="evaluate"><code>evaluate</code></h3>

``` python
evaluate()
```

Evaluate the loss function on the targets.

<h3 id="evaluate_on_sample"><code>evaluate_on_sample</code></h3>

``` python
evaluate_on_sample(seed=None)
```

Evaluates the log probability on a random sample.

#### Args:

* <b>`seed`</b>: int or None. Random seed for this draw from the distribution.


#### Returns:

Log probability of sampled targets, summed across examples.

<h3 id="multiply_fisher"><code>multiply_fisher</code></h3>

``` python
multiply_fisher(vector)
```



<h3 id="multiply_fisher_factor"><code>multiply_fisher_factor</code></h3>

``` python
multiply_fisher_factor(vector)
```



<h3 id="multiply_fisher_factor_replicated_one_hot"><code>multiply_fisher_factor_replicated_one_hot</code></h3>

``` python
multiply_fisher_factor_replicated_one_hot(index)
```



<h3 id="multiply_fisher_factor_transpose"><code>multiply_fisher_factor_transpose</code></h3>

``` python
multiply_fisher_factor_transpose(vector)
```



<h3 id="multiply_hessian"><code>multiply_hessian</code></h3>

``` python
multiply_hessian(vector)
```



<h3 id="multiply_hessian_factor"><code>multiply_hessian_factor</code></h3>

``` python
multiply_hessian_factor(vector)
```



<h3 id="multiply_hessian_factor_replicated_one_hot"><code>multiply_hessian_factor_replicated_one_hot</code></h3>

``` python
multiply_hessian_factor_replicated_one_hot(index)
```



<h3 id="multiply_hessian_factor_transpose"><code>multiply_hessian_factor_transpose</code></h3>

``` python
multiply_hessian_factor_transpose(vector)
```



<h3 id="register_additional_minibatch"><code>register_additional_minibatch</code></h3>

``` python
register_additional_minibatch(
    logits,
    targets=None
)
```

Register an additiona minibatch's worth of parameters.

#### Args:

* <b>`logits`</b>: Tensor of shape [batch_size, output_size]. Parameters for
    underlying distribution.
* <b>`targets`</b>: None or Tensor of shape [batch_size, output_size].  Each row must
    be a one-hot vector.

<h3 id="sample"><code>sample</code></h3>

``` python
sample(seed)
```





