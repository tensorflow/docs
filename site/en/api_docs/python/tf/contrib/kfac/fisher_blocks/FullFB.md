page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.fisher_blocks.FullFB

## Class `FullFB`

Inherits From: [`FisherBlock`](../../../../tf/contrib/kfac/fisher_blocks/FisherBlock)



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_blocks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/kfac/python/ops/fisher_blocks.py).

FisherBlock using a full matrix estimate (no approximations).

FullFB uses a full matrix estimate (no approximations), and should only ever
be used for very low dimensional parameters.

Note that this uses the naive "square the sum estimator", and so is applicable
to any type of parameter in principle, but has very high variance.

## Properties

<h3 id="num_registered_towers"><code>num_registered_towers</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    layer_collection,
    params
)
```

Creates a FullFB block.

#### Args:

* <b>`layer_collection`</b>: The collection of all layers in the K-FAC approximate
      Fisher information matrix to which this FisherBlock belongs.
* <b>`params`</b>: The parameters of this layer (Tensor or tuple of Tensors).

<h3 id="full_fisher_block"><code>full_fisher_block</code></h3>

``` python
full_fisher_block()
```

Explicitly constructs the full Fisher block.

<h3 id="instantiate_factors"><code>instantiate_factors</code></h3>

``` python
instantiate_factors(
    grads_list,
    damping
)
```



<h3 id="multiply"><code>multiply</code></h3>

``` python
multiply(vector)
```

Multiplies the vector by the (damped) block.

#### Args:

* <b>`vector`</b>: The vector (a Tensor or tuple of Tensors) to be multiplied.


#### Returns:

The vector left-multiplied by the (damped) block.

<h3 id="multiply_cholesky"><code>multiply_cholesky</code></h3>

``` python
multiply_cholesky(
    vector,
    transpose=False
)
```



<h3 id="multiply_cholesky_inverse"><code>multiply_cholesky_inverse</code></h3>

``` python
multiply_cholesky_inverse(
    vector,
    transpose=False
)
```



<h3 id="multiply_inverse"><code>multiply_inverse</code></h3>

``` python
multiply_inverse(vector)
```

Multiplies the vector by the (damped) inverse of the block.

#### Args:

* <b>`vector`</b>: The vector (a Tensor or tuple of Tensors) to be multiplied.


#### Returns:

The vector left-multiplied by the (damped) inverse of the block.

<h3 id="multiply_matpower"><code>multiply_matpower</code></h3>

``` python
multiply_matpower(
    vector,
    exp
)
```



<h3 id="register_additional_tower"><code>register_additional_tower</code></h3>

``` python
register_additional_tower(batch_size)
```

Register an additional tower.

#### Args:

* <b>`batch_size`</b>: The batch size, used in the covariance estimator.

<h3 id="register_cholesky"><code>register_cholesky</code></h3>

``` python
register_cholesky()
```



<h3 id="register_cholesky_inverse"><code>register_cholesky_inverse</code></h3>

``` python
register_cholesky_inverse()
```



<h3 id="register_inverse"><code>register_inverse</code></h3>

``` python
register_inverse()
```

Registers a matrix inverse to be computed by the block.

<h3 id="register_matpower"><code>register_matpower</code></h3>

``` python
register_matpower(exp)
```



<h3 id="tensors_to_compute_grads"><code>tensors_to_compute_grads</code></h3>

``` python
tensors_to_compute_grads()
```





