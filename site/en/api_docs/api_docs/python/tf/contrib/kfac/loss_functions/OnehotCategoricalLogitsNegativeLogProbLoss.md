

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.loss_functions.OnehotCategoricalLogitsNegativeLogProbLoss

## Class `OnehotCategoricalLogitsNegativeLogProbLoss`

Inherits From: [`CategoricalLogitsNegativeLogProbLoss`](../../../../tf/contrib/kfac/loss_functions/CategoricalLogitsNegativeLogProbLoss)



Defined in [`tensorflow/contrib/kfac/python/ops/loss_functions.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/kfac/python/ops/loss_functions.py).

Neg log prob loss for a categorical distribution with onehot targets.

Identical to CategoricalLogitsNegativeLogProbLoss except that the underlying
distribution is OneHotCategorical as opposed to Categorical.

## Properties

<h3 id="dist"><code>dist</code></h3>



<h3 id="fisher_factor_inner_shape"><code>fisher_factor_inner_shape</code></h3>



<h3 id="fisher_factor_inner_static_shape"><code>fisher_factor_inner_static_shape</code></h3>



<h3 id="hessian_factor_inner_shape"><code>hessian_factor_inner_shape</code></h3>



<h3 id="hessian_factor_inner_static_shape"><code>hessian_factor_inner_static_shape</code></h3>



<h3 id="inputs"><code>inputs</code></h3>



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



<h3 id="sample"><code>sample</code></h3>

``` python
sample(seed)
```





