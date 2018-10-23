

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.loss_functions.MultiBernoulliNegativeLogProbLoss

## Class `MultiBernoulliNegativeLogProbLoss`

Inherits From: [`DistributionNegativeLogProbLoss`](../../../../tf/contrib/kfac/loss_functions/DistributionNegativeLogProbLoss), [`NaturalParamsNegativeLogProbLoss`](../../../../tf/contrib/kfac/loss_functions/NaturalParamsNegativeLogProbLoss)



Defined in [`tensorflow/contrib/kfac/python/ops/loss_functions.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/kfac/python/ops/loss_functions.py).

Neg log prob loss for multiple Bernoulli distributions param'd by logits.

Represents N independent Bernoulli distributions where N = len(logits). Its
Fisher Information matrix is given by,

F = diag(p * (1-p))
p = sigmoid(logits)

As F is diagonal with positive entries, its factor B is,

B = diag(sqrt(p * (1-p)))

## Properties

<h3 id="fisher_factor_inner_shape"><code>fisher_factor_inner_shape</code></h3>



<h3 id="fisher_factor_inner_static_shape"><code>fisher_factor_inner_static_shape</code></h3>



<h3 id="hessian_factor_inner_shape"><code>hessian_factor_inner_shape</code></h3>



<h3 id="hessian_factor_inner_static_shape"><code>hessian_factor_inner_static_shape</code></h3>



<h3 id="inputs"><code>inputs</code></h3>



<h3 id="params"><code>params</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    logits,
    targets=None,
    seed=None
)
```



<h3 id="evaluate"><code>evaluate</code></h3>

``` python
evaluate()
```

Evaluate the loss function.

<h3 id="evaluate_on_sample"><code>evaluate_on_sample</code></h3>

``` python
evaluate_on_sample(seed=None)
```



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



<h3 id="sample"><code>sample</code></h3>

``` python
sample(seed)
```





