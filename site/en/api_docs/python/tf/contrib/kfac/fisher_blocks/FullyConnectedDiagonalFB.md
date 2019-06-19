

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.fisher_blocks.FullyConnectedDiagonalFB

## Class `FullyConnectedDiagonalFB`

Inherits From: [`FisherBlock`](../../../../tf/contrib/kfac/fisher_blocks/FisherBlock)



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_blocks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/kfac/python/ops/fisher_blocks.py).

FisherBlock for fully-connected (dense) layers using a diagonal approx.

Estimates the Fisher Information matrix's diagonal entries for a fully
connected layer. Unlike NaiveDiagonalFB this uses the low-variance "sum of
squares" estimator.

Let 'params' be a vector parameterizing a model and 'i' an arbitrary index
into it. We are interested in Fisher(params)[i, i]. This is,

<div>   $$Fisher(params)[i, i] = E[ v(x, y, params) v(x, y, params)^T ][i, i]
                       = E[ v(x, y, params)[i] ^ 2 ]$$</div>

Consider fully connected layer in this model with (unshared) weight matrix
'w'. For an example 'x' that produces layer inputs 'a' and output
preactivations 's',

<div>   $$v(x, y, w) = vec( a (d loss / d s)^T )$$ </div>

This FisherBlock tracks Fisher(params)[i, i] for all indices 'i' corresponding
to the layer's parameters 'w'.

## Properties

<h3 id="num_registered_towers"><code>num_registered_towers</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    layer_collection,
    has_bias=False
)
```

Creates a FullyConnectedDiagonalFB block.

#### Args:

* <b>`layer_collection`</b>: The collection of all layers in the K-FAC approximate
      Fisher information matrix to which this FisherBlock belongs.
* <b>`has_bias`</b>: Whether the component Kronecker factors have an additive bias.
      (Default: False)

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

Multiplies the vector by the (damped) matrix-power of the block.

#### Args:

* <b>`vector`</b>: Tensor or 2-tuple of Tensors. if self._has_bias, Tensor of shape
    [input_size, output_size] corresponding to layer's weights. If not, a
    2-tuple of the former and a Tensor of shape [output_size] corresponding
    to the layer's bias.
* <b>`exp`</b>: A scalar representing the power to raise the block before multiplying
       it by the vector.


#### Returns:

The vector left-multiplied by the (damped) matrix-power of the block.

<h3 id="register_additional_tower"><code>register_additional_tower</code></h3>

``` python
register_additional_tower(
    inputs,
    outputs
)
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

Tensors to compute derivative of loss with respect to.



